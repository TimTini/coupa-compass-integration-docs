from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urljoin, urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DEFAULT_ROOT_URL = (
    "https://compass.coupa.com/en-us/products/product-documentation/"
    "integration-technical-documentation"
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def safe_filename_segment(segment: str) -> str:
    value = unquote(segment).strip()
    value = re.sub(r"[^A-Za-z0-9._()\-]+", "_", value)
    value = value.strip("._")
    return value or "_"


class TextExtractor(HTMLParser):
    """Extract readable text from HTML with minimal structure."""

    def __init__(self, preserve_whitespace: bool = False) -> None:
        super().__init__(convert_charrefs=True)
        self.preserve_whitespace = preserve_whitespace
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "br":
            self.parts.append("\n")
        elif tag in {"p", "div", "section", "article", "header", "footer", "aside"}:
            self.parts.append("\n\n")
        elif tag in {"li"}:
            self.parts.append("\n- ")
        elif tag in {"tr"}:
            self.parts.append("\n")
        elif tag in {"td", "th"}:
            self.parts.append("\t")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag in {"p", "div", "section", "article", "header", "footer", "aside", "ul", "ol"}:
            self.parts.append("\n")
        elif tag in {"table"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth or not data:
            return
        if self.preserve_whitespace:
            self.parts.append(data)
            return
        text = re.sub(r"\s+", " ", data)
        if text:
            self.parts.append(text)

    def get_text(self) -> str:
        text = "".join(self.parts)
        if self.preserve_whitespace:
            text = text.replace("\r\n", "\n").replace("\r", "\n")
            text = re.sub(r"\n{3,}", "\n\n", text)
            return text.strip()
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r" {2,}", " ", text)
        return text.strip()


def html_to_text(fragment: str, preserve_whitespace: bool = False) -> str:
    parser = TextExtractor(preserve_whitespace=preserve_whitespace)
    parser.feed(fragment)
    parser.close()
    return parser.get_text()


def strip_tags(fragment: str) -> str:
    return html_to_text(fragment, preserve_whitespace=False)


def html_table_to_markdown(table_html: str, base_url: str) -> str:
    rows = re.findall(r"<tr\b[^>]*>(.*?)</tr>", table_html, flags=re.IGNORECASE | re.DOTALL)
    parsed_rows: list[list[str]] = []
    header_row_index: int | None = None

    for row_index, row_html in enumerate(rows):
        cells = re.findall(r"<(th|td)\b[^>]*>(.*?)</(?:th|td)>", row_html, flags=re.IGNORECASE | re.DOTALL)
        if not cells:
            continue
        parsed_row: list[str] = []
        has_header = False
        for cell_tag, cell_html in cells:
            cell_text = inline_html_to_markdown(cell_html, base_url)
            cell_text = cell_text.replace("|", r"\|").replace("\n", "<br>")
            parsed_row.append(cell_text.strip())
            if cell_tag.lower() == "th":
                has_header = True
        if has_header and header_row_index is None:
            header_row_index = len(parsed_rows)
        parsed_rows.append(parsed_row)

    if not parsed_rows:
        return ""

    max_columns = max(len(row) for row in parsed_rows)
    for row in parsed_rows:
        while len(row) < max_columns:
            row.append("")

    if header_row_index is None:
        header = parsed_rows[0]
        body_rows = parsed_rows[1:]
    else:
        header = parsed_rows[header_row_index]
        body_rows = parsed_rows[:header_row_index] + parsed_rows[header_row_index + 1 :]

    table_lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * max_columns) + " |",
    ]
    for row in body_rows:
        table_lines.append("| " + " | ".join(row) + " |")
    return "\n".join(table_lines)


def inline_html_to_markdown(fragment: str, base_url: str) -> str:
    text = fragment
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(
        r"<img\b([^>]*?)src=\"([^\"]+)\"([^>]*?)>",
        lambda m: _image_to_markdown(m.group(0), m.group(2), base_url),
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(
        r"<a\b([^>]*?)href=\"([^\"]+)\"([^>]*)>(.*?)</a>",
        lambda m: _link_to_markdown(m.group(4), m.group(2), base_url),
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(
        r"<code\b[^>]*>(.*?)</code>",
        lambda m: f"`{strip_tags(m.group(1)).replace('`', '\\`')}`",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(r"</?(strong|b)\b[^>]*>", "**", text, flags=re.IGNORECASE)
    text = re.sub(r"</?(em|i)\b[^>]*>", "*", text, flags=re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</?span\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?sup\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?sub\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = strip_tags(text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    return text.strip()


def article_html_to_markdown(article_html: str, base_url: str) -> str:
    text = article_html.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    placeholders: dict[str, str] = {}

    def stash(value: str) -> str:
        key = f"@@BLOCK_{len(placeholders)}@@"
        placeholders[key] = value.strip("\n")
        return f"\n\n{key}\n\n"

    def replace_pre(match: re.Match[str]) -> str:
        inner = re.sub(r"</?code\b[^>]*>", "", match.group(1), flags=re.IGNORECASE)
        code_text = html_to_text(inner, preserve_whitespace=True)
        fenced = "```text\n" + code_text.strip("\n") + "\n```"
        return stash(fenced)

    def replace_table(match: re.Match[str]) -> str:
        markdown = html_table_to_markdown(match.group(1), base_url)
        return stash(markdown or "")

    text = re.sub(r"<pre\b[^>]*>(.*?)</pre>", replace_pre, text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<table\b[^>]*>(.*?)</table>", replace_table, text, flags=re.IGNORECASE | re.DOTALL)

    text = re.sub(
        r"<img\b([^>]*?)src=\"([^\"]+)\"([^>]*?)>",
        lambda m: _image_to_markdown(m.group(0), m.group(2), base_url),
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(
        r"<a\b([^>]*?)href=\"([^\"]+)\"([^>]*)>(.*?)</a>",
        lambda m: _link_to_markdown(m.group(4), m.group(2), base_url),
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    for level in range(6, 0, -1):
        pattern = rf"<h{level}\b[^>]*>(.*?)</h{level}>"
        text = re.sub(
            pattern,
            lambda m, lvl=level: "\n\n" + ("#" * lvl) + " " + inline_html_to_markdown(m.group(1), base_url) + "\n\n",
            text,
            flags=re.IGNORECASE | re.DOTALL,
        )

    text = re.sub(r"<blockquote\b[^>]*>(.*?)</blockquote>", lambda m: "\n\n> " + strip_tags(m.group(1)).replace("\n", "\n> ") + "\n\n", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<li\b[^>]*>", "\n- ", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</?(ul|ol)\b[^>]*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</?(p|div|section|article|header|footer|aside|nav)\b[^>]*>", "\n\n", text, flags=re.IGNORECASE)
    text = re.sub(
        r"<code\b[^>]*>(.*?)</code>",
        lambda m: f"`{strip_tags(m.group(1)).replace('`', '\\`')}`",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(r"</?(strong|b)\b[^>]*>", "**", text, flags=re.IGNORECASE)
    text = re.sub(r"</?(em|i)\b[^>]*>", "*", text, flags=re.IGNORECASE)
    text = re.sub(r"<hr\b[^>]*>", "\n\n---\n\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</?(tbody|thead|tfoot|tr|td|th)\b[^>]*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)

    for key, value in placeholders.items():
        text = text.replace(key, value)

    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"(?m)^-\s*\n\s*", "- ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" {2,}", " ", text)
    return text.strip() + "\n"


def _link_to_markdown(label_html: str, href: str, base_url: str) -> str:
    label = inline_html_to_markdown(label_html, base_url)
    url = urljoin(base_url, html.unescape(href))
    if not label:
        return url
    return f"[{label}]({url})"


def _image_to_markdown(tag_html: str, src: str, base_url: str) -> str:
    alt_match = re.search(r'alt="([^"]*)"', tag_html, flags=re.IGNORECASE)
    alt = html.unescape(alt_match.group(1)) if alt_match else ""
    url = urljoin(base_url, html.unescape(src))
    return f"![{alt}]({url})"


class ArticleExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.capture_title = False
        self.title_parts: list[str] = []
        self.title_tag_capture = False
        self.page_title_parts: list[str] = []
        self.in_article = False
        self.article_depth = 0
        self.article_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self.title_tag_capture = True
        if tag == "h1" and self.in_article:
            self.capture_title = True

        if self.in_article:
            self.article_parts.append(self.get_starttag_text())
            if tag == "article":
                self.article_depth += 1
            return

        if tag == "article":
            self.in_article = True
            self.article_depth = 1
            self.article_parts.append(self.get_starttag_text())

    def handle_endtag(self, tag: str) -> None:
        if self.title_tag_capture and tag == "title":
            self.title_tag_capture = False
        if self.capture_title and tag == "h1":
            self.capture_title = False

        if self.in_article:
            self.article_parts.append(f"</{tag}>")
            if tag == "article":
                self.article_depth -= 1
                if self.article_depth == 0:
                    self.in_article = False

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.in_article:
            self.article_parts.append(self.get_starttag_text())

    def handle_data(self, data: str) -> None:
        if self.title_tag_capture:
            self.page_title_parts.append(data)
        if self.capture_title:
            self.title_parts.append(data)
        if self.in_article:
            self.article_parts.append(data)

    def handle_entityref(self, name: str) -> None:
        value = f"&{name};"
        if self.in_article:
            self.article_parts.append(value)
        if self.capture_title:
            self.title_parts.append(html.unescape(value))
        if self.title_tag_capture:
            self.page_title_parts.append(html.unescape(value))

    def handle_charref(self, name: str) -> None:
        value = f"&#{name};"
        if self.in_article:
            self.article_parts.append(value)
        if self.capture_title:
            self.title_parts.append(html.unescape(value))
        if self.title_tag_capture:
            self.page_title_parts.append(html.unescape(value))

    def article_html(self) -> str:
        return "".join(self.article_parts).strip()

    def title(self) -> str:
        title = normalize_whitespace("".join(self.title_parts))
        if title:
            return title
        return normalize_whitespace("".join(self.page_title_parts))


def is_auth_redirect(final_url: str, page_title: str, page_html: str) -> bool:
    host = urlparse(final_url).netloc.lower()
    title = page_title.lower()
    html_lower = page_html.lower()
    return (
        "okta.com" in host
        or ("sign in" in title and "okta" in html_lower)
        or ("login" in title and "okta" in html_lower)
    )


def build_placeholder_article(
    title: str,
    source_url: str,
    final_url: str,
    reason: str,
    details: list[str] | None = None,
) -> str:
    safe_title = html.escape(title)
    lines = [
        '<article id="placeholder-generated-by-codex">',
        f"<h1>{safe_title}</h1>",
        f"<p>{html.escape(reason)}</p>",
        f'<p><strong>Requested URL:</strong> <a href="{html.escape(source_url)}">{html.escape(source_url)}</a></p>',
    ]
    if final_url != source_url:
        lines.append(
            f'<p><strong>Final URL:</strong> <a href="{html.escape(final_url)}">{html.escape(final_url)}</a></p>'
        )
    for detail in details or []:
        lines.append(f"<p>{html.escape(detail)}</p>")
    lines.append("</article>")
    return "\n".join(lines)


class TocParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.sidebar_depth = 0
        self.li_stack: list[dict[str, Any]] = []
        self.root_nodes: list[dict[str, Any]] = []
        self.capture_anchor = False
        self.anchor_text_parts: list[str] = []
        self.anchor_href: str | None = None

    @property
    def in_sidebar(self) -> bool:
        return self.sidebar_depth > 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value for key, value in attrs}
        if tag == "div":
            if self.in_sidebar:
                self.sidebar_depth += 1
            elif attr_map.get("id") == "sidebar-tabs":
                self.sidebar_depth = 1
            return

        if not self.in_sidebar:
            return

        if tag == "li":
            self.li_stack.append(
                {
                    "classes": (attr_map.get("class") or "").split(),
                    "title": "",
                    "href": "",
                    "children": [],
                }
            )
            return

        if tag == "a" and self.li_stack:
            classes = (attr_map.get("class") or "").split()
            href = attr_map.get("href") or ""
            if "toggle" in classes or href == "#":
                return
            self.capture_anchor = True
            self.anchor_href = href
            self.anchor_text_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "div" and self.in_sidebar:
            self.sidebar_depth -= 1
            return

        if not self.in_sidebar:
            return

        if tag == "a" and self.capture_anchor:
            self.capture_anchor = False
            if self.li_stack:
                self.li_stack[-1]["href"] = self.anchor_href or ""
                self.li_stack[-1]["title"] = normalize_whitespace("".join(self.anchor_text_parts))
            self.anchor_href = None
            self.anchor_text_parts = []
            return

        if tag == "li" and self.li_stack:
            node = self.li_stack.pop()
            if "heading" in node["classes"]:
                return
            node_has_link = bool(node["href"] and node["title"])
            if node_has_link:
                target = self.li_stack[-1]["children"] if self.li_stack else self.root_nodes
                target.append(node)
            elif node["children"]:
                target = self.li_stack[-1]["children"] if self.li_stack else self.root_nodes
                target.extend(node["children"])

    def handle_data(self, data: str) -> None:
        if self.capture_anchor:
            self.anchor_text_parts.append(data)

    def flatten(self, base_url: str) -> list[dict[str, Any]]:
        flattened: list[dict[str, Any]] = []

        def visit(node: dict[str, Any], trail: list[str]) -> None:
            title = normalize_whitespace(node["title"])
            current_trail = trail + ([title] if title else [])
            href = node["href"]
            if title and href:
                flattened.append(
                    {
                        "title": title,
                        "url": urljoin(base_url, href),
                        "toc_path": current_trail,
                        "depth": len(current_trail) - 1,
                    }
                )
            for child in node["children"]:
                visit(child, current_trail)

        for root in self.root_nodes:
            visit(root, [])

        unique: list[dict[str, Any]] = []
        seen: set[str] = set()
        for item in flattened:
            if item["url"] in seen:
                continue
            seen.add(item["url"])
            unique.append(item)
        return unique


@dataclass
class FetchResult:
    index: int
    url: str
    title: str
    toc_path: list[str]
    relative_stem: str
    status_code: int
    final_url: str
    fetched_at: str
    raw_html_path: str
    article_html_path: str
    markdown_path: str
    text_path: str
    content_sha1: str
    article_sha1: str
    markdown_chars: int
    text_chars: int
    capture_mode: str
    error: str | None = None


def build_session() -> requests.Session:
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("HEAD", "GET", "OPTIONS"),
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=16, pool_maxsize=16)
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (compatible; CoupaDocsMirror/1.0; +https://compass.coupa.com/)",
            "Accept-Language": "en-US,en;q=0.9",
        }
    )
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def relative_stem_for_url(url: str, collisions: dict[str, str]) -> str:
    parsed = urlparse(url)
    segments = [safe_filename_segment(segment) for segment in parsed.path.split("/") if segment]
    if not segments:
        segments = ["root"]
    stem = str(Path(*segments, "index"))
    existing = collisions.get(stem)
    if existing and existing != url:
        suffix = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
        stem = str(Path(*segments[:-1], f"{segments[-1]}__{suffix}", "index"))
    collisions[stem] = url
    return stem


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def make_front_matter(item: dict[str, Any], fetched_at: str, status_code: int) -> str:
    lines = [
        "---",
        f"title: {yaml_quote(item['title'])}",
        f"url: {yaml_quote(item['url'])}",
        f"final_url: {yaml_quote(item.get('final_url', item['url']))}",
        f"status_code: {status_code}",
        f"fetched_at: {yaml_quote(fetched_at)}",
        "toc_path:",
    ]
    for part in item["toc_path"]:
        lines.append(f"  - {yaml_quote(part)}")
    lines.append("---")
    return "\n".join(lines)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def fetch_one(
    item: dict[str, Any],
    output_dir: Path,
    root_url: str,
    index: int,
    session: requests.Session,
) -> FetchResult:
    fetched_at = utc_now_iso()
    response = session.get(item["url"], timeout=60)
    response.raise_for_status()
    response.encoding = response.encoding or "utf-8"

    extractor = ArticleExtractor()
    extractor.feed(response.text)
    extractor.close()

    article_html = extractor.article_html()
    extracted_title = extractor.title() or item["title"]
    final_url = response.url
    capture_mode = "article"
    auth_redirect = False
    if not article_html:
        auth_redirect = is_auth_redirect(final_url, extracted_title, response.text)
        if auth_redirect:
            capture_mode = "auth_redirect"
            title = item["title"]
            article_html = build_placeholder_article(
                title=title,
                source_url=item["url"],
                final_url=final_url,
                reason="This TOC entry redirected to an authentication page, so the original documentation body could not be downloaded anonymously.",
                details=[
                    f"Observed redirect page title: {extracted_title}",
                    "Raw HTML for the redirect/login page is still preserved in the raw-html archive.",
                ],
            )
        else:
            capture_mode = "placeholder"
            title = extracted_title or item["title"]
            body_preview = html_to_text(response.text, preserve_whitespace=False)[:1000]
            details = []
            if body_preview:
                details.append(f"Page text preview: {body_preview}")
            article_html = build_placeholder_article(
                title=title or item["title"],
                source_url=item["url"],
                final_url=final_url,
                reason="The page did not expose a standard <article> block, so a generated placeholder was created instead.",
                details=details,
            )
    else:
        title = extracted_title

    markdown_body = article_html_to_markdown(article_html, final_url)
    text_body = html_to_text(article_html, preserve_whitespace=False) + "\n"

    front_matter = make_front_matter({**item, "title": title, "final_url": final_url}, fetched_at, response.status_code)
    markdown_document = front_matter + "\n\n" + markdown_body

    relative = Path(item["relative_stem"])
    raw_html_path = output_dir / "raw-html" / relative.with_suffix(".html")
    article_html_path = output_dir / "article-html" / relative.with_suffix(".html")
    markdown_path = output_dir / "markdown" / relative.with_suffix(".md")
    text_path = output_dir / "text" / relative.with_suffix(".txt")

    write_text(raw_html_path, response.text)
    write_text(article_html_path, article_html)
    write_text(markdown_path, markdown_document)
    write_text(text_path, text_body)

    return FetchResult(
        index=index,
        url=item["url"],
        title=title,
        toc_path=item["toc_path"],
        relative_stem=item["relative_stem"],
        status_code=response.status_code,
        final_url=final_url,
        fetched_at=fetched_at,
        raw_html_path=str(raw_html_path.relative_to(output_dir)),
        article_html_path=str(article_html_path.relative_to(output_dir)),
        markdown_path=str(markdown_path.relative_to(output_dir)),
        text_path=str(text_path.relative_to(output_dir)),
        content_sha1=hashlib.sha1(response.text.encode("utf-8")).hexdigest(),
        article_sha1=hashlib.sha1(article_html.encode("utf-8")).hexdigest(),
        markdown_chars=len(markdown_document),
        text_chars=len(text_body),
        capture_mode=capture_mode,
    )


def build_toc(root_html: str, root_url: str, collisions: dict[str, str]) -> list[dict[str, Any]]:
    parser = TocParser()
    parser.feed(root_html)
    parser.close()
    return parser.flatten(root_url)


def build_toc_markdown(toc_items: list[dict[str, Any]]) -> str:
    lines = ["# Coupa Integration Technical Documentation TOC", ""]
    for item in toc_items:
        indent = "  " * item["depth"]
        lines.append(f"{indent}- [{item['title']}]({item['url']})")
    lines.append("")
    return "\n".join(lines)


def build_combined_corpus(results: list[FetchResult], output_dir: Path) -> str:
    lines = [
        "# Coupa Integration Technical Documentation Corpus",
        "",
        f"- Generated at: {utc_now_iso()}",
        f"- Document count: {len(results)}",
        "",
    ]
    for result in results:
        markdown_path = output_dir / result.markdown_path
        markdown_text = markdown_path.read_text(encoding="utf-8")
        body = re.sub(r"^---\n.*?\n---\n+", "", markdown_text, flags=re.DOTALL)
        lines.extend(
            [
                "---",
                "",
                f"## {result.index:04d}. {result.title}",
                "",
                f"- URL: {result.url}",
                f"- Final URL: {result.final_url}",
                f"- Capture mode: {result.capture_mode}",
                f"- TOC Path: {' > '.join(result.toc_path)}",
                f"- Markdown file: `{result.markdown_path}`",
                "",
                body.strip(),
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Mirror Coupa Compass docs from the legacy TOC page.")
    parser.add_argument("--root-url", default=DEFAULT_ROOT_URL, help="Root documentation URL containing the TOC.")
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parents[1] / "output"),
        help="Directory to write downloaded artifacts to.",
    )
    parser.add_argument("--workers", type=int, default=8, help="Concurrent download workers.")
    parser.add_argument("--delay", type=float, default=0.0, help="Optional delay in seconds between worker submissions.")
    parser.add_argument("--limit", type=int, default=0, help="Optional limit for the number of TOC pages to fetch.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    root_session = build_session()
    root_response = root_session.get(args.root_url, timeout=60)
    root_response.raise_for_status()
    root_response.encoding = root_response.encoding or "utf-8"

    collisions: dict[str, str] = {}
    toc_items = build_toc(root_response.text, args.root_url, collisions)
    if args.limit and args.limit > 0:
        toc_items = toc_items[: args.limit]

    if not toc_items:
        raise RuntimeError("No TOC links were discovered.")

    for index, item in enumerate(toc_items, start=1):
        item["index"] = index
        slug = safe_filename_segment(item["toc_path"][-1])[:48] or f"doc-{index:04d}"
        item["relative_stem"] = f"{index:04d}-{slug}"

    write_text(output_dir / "root-page.html", root_response.text)
    write_json(
        output_dir / "toc.json",
        {
            "generated_at": utc_now_iso(),
            "root_url": args.root_url,
            "count": len(toc_items),
            "items": toc_items,
        },
    )
    write_text(output_dir / "toc.md", build_toc_markdown(toc_items))

    results: list[FetchResult] = []
    errors: list[dict[str, Any]] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        future_map: dict[concurrent.futures.Future[FetchResult], tuple[int, dict[str, Any], requests.Session]] = {}
        for index, item in enumerate(toc_items, start=1):
            session = build_session()
            future = executor.submit(fetch_one, item, output_dir, args.root_url, index, session)
            future_map[future] = (index, item, session)
            if args.delay:
                time.sleep(args.delay)

        for future in concurrent.futures.as_completed(future_map):
            index, item, session = future_map[future]
            try:
                result = future.result()
                results.append(result)
                print(f"[{result.index:04d}/{len(toc_items):04d}] OK {result.url}")
            except Exception as exc:  # noqa: BLE001
                errors.append(
                    {
                        "index": index,
                        "url": item["url"],
                        "title": item["title"],
                        "toc_path": item["toc_path"],
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                )
                print(f"[{index:04d}/{len(toc_items):04d}] ERR {item['url']} :: {exc}")
            finally:
                session.close()

    results.sort(key=lambda item: item.index)

    documents_jsonl_path = output_dir / "documents.jsonl"
    with documents_jsonl_path.open("w", encoding="utf-8") as handle:
        for result in results:
            markdown_text = (output_dir / result.markdown_path).read_text(encoding="utf-8")
            text_body = (output_dir / result.text_path).read_text(encoding="utf-8")
            handle.write(
                json.dumps(
                    {
                        "index": result.index,
                        "title": result.title,
                        "url": result.url,
                        "final_url": result.final_url,
                        "toc_path": result.toc_path,
                        "status_code": result.status_code,
                        "fetched_at": result.fetched_at,
                        "capture_mode": result.capture_mode,
                        "markdown_path": result.markdown_path,
                        "text_path": result.text_path,
                        "article_html_path": result.article_html_path,
                        "raw_html_path": result.raw_html_path,
                        "markdown": markdown_text,
                        "text": text_body,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    combined_corpus = build_combined_corpus(results, output_dir)
    write_text(output_dir / "all-docs.md", combined_corpus)

    manifest = {
        "generated_at": utc_now_iso(),
        "root_url": args.root_url,
        "requested_count": len(toc_items),
        "success_count": len(results),
        "failure_count": len(errors),
        "documents_jsonl": str(documents_jsonl_path.relative_to(output_dir)),
        "combined_markdown": "all-docs.md",
        "results": [result.__dict__ for result in results],
        "errors": errors,
    }
    write_json(output_dir / "manifest.json", manifest)
    write_json(output_dir / "fetch-report.json", manifest)

    print(f"Done. Success={len(results)} Failure={len(errors)} Output={output_dir}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
