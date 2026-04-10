from __future__ import annotations

import argparse
import concurrent.futures
import csv
import html
import io
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlunparse
import xml.etree.ElementTree as ET

import requests

import fetch_coupa_docs as base


DISCOVERY_MISC_PREFIX = "/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/"


def canonicalize_url(url: str) -> str:
    parsed = urlparse(url)
    path = re.sub(r"/+", "/", parsed.path or "/")
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    filtered_query = [
        (key, value)
        for key, value in parse_qsl(parsed.query, keep_blank_values=True)
        if key.lower() not in {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"}
    ]
    query = urlencode(filtered_query)
    return urlunparse((parsed.scheme.lower() or "https", parsed.netloc.lower(), path, "", query, ""))


def safe_slug_from_url(url: str) -> str:
    parsed = urlparse(url)
    leaf = Path(parsed.path).name or Path(parsed.path).parent.name or "resource"
    leaf = leaf or "resource"
    if "." in leaf:
        stem = leaf.rsplit(".", 1)[0]
    else:
        stem = leaf
    return base.safe_filename_segment(stem)[:64] or "resource"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def should_include_candidate(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.netloc.lower() != "compass.coupa.com":
        return False
    path = parsed.path or "/"
    lower_path = path.lower()

    if path.startswith("/Saml/") or "/sso/" in lower_path or "login" in lower_path:
        return False
    if path.startswith("/api/") or path.startswith("/fonts/") or path.startswith("/etc."):
        return False
    if lower_path.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".css", ".js", ".ico", ".woff", ".woff2", ".ttf", ".eot", ".pdf")):
        return False

    return (
        path.startswith("/en-us/")
        or re.match(r"^/x\d+\.xml$", path) is not None
        or path.startswith(DISCOVERY_MISC_PREFIX)
        or path.startswith("/Integrate/Technical_Documentation/")
    )


def extract_links_from_html(page_url: str, html_text: str) -> list[str]:
    links: list[str] = []
    for href in re.findall(r'<a\s+[^>]*href="([^"]+)"', html_text, flags=re.IGNORECASE):
        href = html.unescape(href).strip()
        if not href or href.startswith("#") or href.lower().startswith(("javascript:", "mailto:", "tel:")):
            continue
        links.append(canonicalize_url(urljoin(page_url, href)))
    return links


def load_base_manifest(base_output_dir: Path) -> dict[str, Any]:
    return json.loads((base_output_dir / "manifest.json").read_text(encoding="utf-8"))


def write_auth_gated_report(base_output_dir: Path, manifest: dict[str, Any]) -> None:
    report_dir = base_output_dir / "reports"
    auth_items = [item for item in manifest["results"] if item.get("capture_mode") == "auth_redirect"]
    auth_items.sort(key=lambda item: item["index"])

    write_json(report_dir / "auth-gated-existing.json", auth_items)

    with (report_dir / "auth-gated-existing.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["index", "title", "url", "final_url", "toc_path", "markdown_path", "raw_html_path"],
        )
        writer.writeheader()
        for item in auth_items:
            writer.writerow(
                {
                    "index": item["index"],
                    "title": item["title"],
                    "url": item["url"],
                    "final_url": item["final_url"],
                    "toc_path": " > ".join(item["toc_path"]),
                    "markdown_path": item["markdown_path"],
                    "raw_html_path": item["raw_html_path"],
                }
            )

    lines = [
        "# Existing auth-gated TOC items",
        "",
        f"- Generated at: {base.utc_now_iso()}",
        f"- Count: {len(auth_items)}",
        "",
    ]
    for item in auth_items:
        lines.extend(
            [
                f"## {item['index']:04d}. {item['title']}",
                "",
                f"- TOC Path: {' > '.join(item['toc_path'])}",
                f"- Requested URL: {item['url']}",
                f"- Redirect URL: {item['final_url']}",
                f"- Markdown placeholder: `{item['markdown_path']}`",
                f"- Raw HTML: `{item['raw_html_path']}`",
                "",
            ]
        )
    write_text(report_dir / "auth-gated-existing.md", "\n".join(lines).strip() + "\n")


def discover_candidates(base_output_dir: Path, manifest: dict[str, Any]) -> list[dict[str, Any]]:
    known_urls = {canonicalize_url(item["url"]) for item in manifest["results"]}
    candidates: dict[str, dict[str, Any]] = {}

    for item in manifest["results"]:
        raw_html_path = base_output_dir / item["raw_html_path"]
        raw_html = raw_html_path.read_text(encoding="utf-8", errors="ignore")
        for discovered_url in extract_links_from_html(item["url"], raw_html):
            if discovered_url in known_urls or not should_include_candidate(discovered_url):
                continue
            bucket = candidates.setdefault(
                discovered_url,
                {
                    "canonical_url": discovered_url,
                    "sources": [],
                },
            )
            if item["url"] not in bucket["sources"]:
                bucket["sources"].append(item["url"])

    result = []
    for index, discovered_url in enumerate(sorted(candidates), start=1):
        parsed = urlparse(discovered_url)
        ext = Path(parsed.path).suffix.lower()
        if re.match(r"^/x\d+\.xml$", parsed.path):
            kind_hint = "legacy_xml_alias"
        elif ext == ".json":
            kind_hint = "json"
        elif ext == ".xlsx":
            kind_hint = "xlsx"
        elif ext in {".csv", ".zip"}:
            kind_hint = ext.lstrip(".")
        elif ext:
            kind_hint = ext.lstrip(".")
        else:
            kind_hint = "page"
        result.append(
            {
                "index": index,
                "url": discovered_url,
                "kind_hint": kind_hint,
                "source_count": len(candidates[discovered_url]["sources"]),
                "sources_preview": candidates[discovered_url]["sources"][:8],
                "slug": f"{index:04d}-{safe_slug_from_url(discovered_url)}",
            }
        )
    return result


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def make_front_matter(metadata: dict[str, Any]) -> str:
    lines = [
        "---",
        f"title: {yaml_quote(str(metadata.get('title', '')))}",
        f"url: {yaml_quote(metadata['url'])}",
        f"final_url: {yaml_quote(metadata.get('final_url', metadata['url']))}",
        f"content_type: {yaml_quote(metadata.get('content_type', ''))}",
        f"classification: {yaml_quote(metadata.get('classification', ''))}",
        f"fetched_at: {yaml_quote(metadata.get('fetched_at', base.utc_now_iso()))}",
        "---",
    ]
    return "\n".join(lines)


def is_textual_content(content_type: str) -> bool:
    lower = (content_type or "").lower()
    return any(token in lower for token in ["text/", "json", "xml", "javascript"])


def column_to_index(ref: str) -> int:
    letters = "".join(ch for ch in ref if ch.isalpha()).upper()
    value = 0
    for ch in letters:
        value = value * 26 + (ord(ch) - ord("A") + 1)
    return max(value - 1, 0)


def extract_xlsx_text(binary_content: bytes) -> str:
    ns = {
        "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
        "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        "pkgrel": "http://schemas.openxmlformats.org/package/2006/relationships",
    }
    try:
        with zipfile.ZipFile(io.BytesIO(binary_content)) as archive:
            shared_strings: list[str] = []
            if "xl/sharedStrings.xml" in archive.namelist():
                root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
                for si in root.findall("main:si", ns):
                    text_parts = [node.text or "" for node in si.findall(".//main:t", ns)]
                    shared_strings.append("".join(text_parts))

            workbook_root = ET.fromstring(archive.read("xl/workbook.xml"))
            rel_root = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
            rel_map = {
                rel.attrib["Id"]: rel.attrib["Target"]
                for rel in rel_root.findall("pkgrel:Relationship", ns)
            }

            lines: list[str] = []
            for sheet in workbook_root.findall("main:sheets/main:sheet", ns):
                sheet_name = sheet.attrib.get("name", "Sheet")
                rel_id = sheet.attrib.get(f"{{{ns['rel']}}}id", "")
                target = rel_map.get(rel_id, "")
                if not target:
                    continue
                sheet_path = "xl/" + target.lstrip("/").replace("\\", "/")
                if not sheet_path.startswith("xl/"):
                    sheet_path = "xl/" + sheet_path
                sheet_root = ET.fromstring(archive.read(sheet_path))
                lines.append(f"# Sheet: {sheet_name}")
                for row in sheet_root.findall(".//main:sheetData/main:row", ns):
                    values: list[str] = []
                    for cell in row.findall("main:c", ns):
                        ref = cell.attrib.get("r", "")
                        cell_index = column_to_index(ref)
                        while len(values) < cell_index:
                            values.append("")
                        cell_type = cell.attrib.get("t", "")
                        value = ""
                        if cell_type == "inlineStr":
                            parts = [node.text or "" for node in cell.findall(".//main:t", ns)]
                            value = "".join(parts)
                        else:
                            v = cell.find("main:v", ns)
                            raw_value = v.text if v is not None and v.text is not None else ""
                            if cell_type == "s" and raw_value.isdigit():
                                idx = int(raw_value)
                                value = shared_strings[idx] if 0 <= idx < len(shared_strings) else raw_value
                            else:
                                value = raw_value
                        values.append(value)
                    lines.append("\t".join(values).rstrip())
                lines.append("")
            return "\n".join(lines).strip() + "\n"
    except Exception as exc:  # noqa: BLE001
        return f"[xlsx extraction failed] {type(exc).__name__}: {exc}\n"


def extract_zip_listing(binary_content: bytes) -> str:
    try:
        with zipfile.ZipFile(io.BytesIO(binary_content)) as archive:
            lines = ["ZIP entries:"]
            for name in archive.namelist():
                info = archive.getinfo(name)
                lines.append(f"- {name} ({info.file_size} bytes)")
            return "\n".join(lines) + "\n"
    except Exception as exc:  # noqa: BLE001
        return f"[zip listing failed] {type(exc).__name__}: {exc}\n"


def save_text_resource(
    discovery_dir: Path,
    slug: str,
    extension: str,
    text_content: str,
    markdown_title: str,
    metadata: dict[str, Any],
) -> dict[str, str]:
    raw_path = discovery_dir / "assets" / "raw" / f"{slug}{extension}"
    text_path = discovery_dir / "assets" / "text" / f"{slug}.txt"
    markdown_path = discovery_dir / "assets" / "markdown" / f"{slug}.md"

    write_text(raw_path, text_content)
    write_text(text_path, text_content if text_content.endswith("\n") else text_content + "\n")

    front_matter = make_front_matter({**metadata, "title": markdown_title})
    markdown = front_matter + "\n\n" + f"# {markdown_title}\n\n```{extension.lstrip('.') or 'text'}\n{text_content}\n```\n"
    write_text(markdown_path, markdown)

    return {
        "raw_path": str(raw_path.relative_to(discovery_dir)),
        "text_path": str(text_path.relative_to(discovery_dir)),
        "markdown_path": str(markdown_path.relative_to(discovery_dir)),
    }


def save_binary_resource(
    discovery_dir: Path,
    slug: str,
    extension: str,
    binary_content: bytes,
    extracted_text: str,
    markdown_title: str,
    metadata: dict[str, Any],
) -> dict[str, str]:
    raw_path = discovery_dir / "assets" / "raw" / f"{slug}{extension}"
    text_path = discovery_dir / "assets" / "text" / f"{slug}.txt"
    markdown_path = discovery_dir / "assets" / "markdown" / f"{slug}.md"

    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_bytes(binary_content)
    write_text(text_path, extracted_text if extracted_text.endswith("\n") else extracted_text + "\n")

    front_matter = make_front_matter({**metadata, "title": markdown_title})
    markdown = (
        front_matter
        + "\n\n"
        + f"# {markdown_title}\n\n"
        + f"- Raw file: `{raw_path.relative_to(discovery_dir)}`\n"
        + f"- Extracted text: `{text_path.relative_to(discovery_dir)}`\n\n"
        + "## Extracted content\n\n"
        + "```text\n"
        + extracted_text.strip("\n")
        + "\n```\n"
    )
    write_text(markdown_path, markdown)

    return {
        "raw_path": str(raw_path.relative_to(discovery_dir)),
        "text_path": str(text_path.relative_to(discovery_dir)),
        "markdown_path": str(markdown_path.relative_to(discovery_dir)),
    }


def fetch_candidate(
    candidate: dict[str, Any],
    discovery_dir: Path,
    known_urls: set[str],
    session: requests.Session,
) -> dict[str, Any]:
    response = session.get(candidate["url"], timeout=90)
    response.raise_for_status()
    content_type = (response.headers.get("content-type") or "").split(";")[0].strip().lower()
    fetched_at = base.utc_now_iso()
    final_url = response.url
    final_canonical_url = canonicalize_url(final_url)
    slug = candidate["slug"]

    result: dict[str, Any] = {
        "index": candidate["index"],
        "url": candidate["url"],
        "final_url": final_url,
        "final_canonical_url": final_canonical_url,
        "kind_hint": candidate["kind_hint"],
        "source_count": candidate["source_count"],
        "sources_preview": candidate["sources_preview"],
        "status_code": response.status_code,
        "content_type": content_type,
        "fetched_at": fetched_at,
        "slug": slug,
        "classification": "",
        "title": candidate["url"],
    }

    if final_canonical_url in known_urls and final_canonical_url != candidate["url"]:
        result["classification"] = "redirect_to_existing_archive"
        return result

    path = urlparse(candidate["url"]).path
    extension = Path(path).suffix.lower()

    if content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or extension == ".xlsx":
        extracted = extract_xlsx_text(response.content)
        title = Path(path).name or slug
        metadata = {
            "url": candidate["url"],
            "final_url": final_url,
            "content_type": content_type,
            "classification": "xlsx_asset",
            "fetched_at": fetched_at,
        }
        paths = save_binary_resource(discovery_dir, slug, ".xlsx", response.content, extracted, title, metadata)
        result.update(paths)
        result["classification"] = "xlsx_asset"
        result["title"] = title
        return result

    if content_type == "text/csv" or extension == ".csv":
        response.encoding = response.encoding or "utf-8"
        title = Path(path).name or slug
        metadata = {
            "url": candidate["url"],
            "final_url": final_url,
            "content_type": content_type,
            "classification": "csv_asset",
            "fetched_at": fetched_at,
        }
        paths = save_text_resource(discovery_dir, slug, ".csv", response.text, title, metadata)
        result.update(paths)
        result["classification"] = "csv_asset"
        result["title"] = title
        return result

    if content_type == "application/zip" or extension == ".zip":
        extracted = extract_zip_listing(response.content)
        title = Path(path).name or slug
        metadata = {
            "url": candidate["url"],
            "final_url": final_url,
            "content_type": content_type,
            "classification": "zip_asset",
            "fetched_at": fetched_at,
        }
        paths = save_binary_resource(discovery_dir, slug, ".zip", response.content, extracted, title, metadata)
        result.update(paths)
        result["classification"] = "zip_asset"
        result["title"] = title
        return result

    body_starts_like_json = False
    if extension == ".json" or "json" in content_type:
        try:
            preview = response.content[:256].lstrip()
            body_starts_like_json = preview.startswith(b"{") or preview.startswith(b"[")
        except Exception:  # noqa: BLE001
            body_starts_like_json = False

    if content_type == "application/json" or body_starts_like_json:
        try:
            payload = response.json()
            pretty = json.dumps(payload, ensure_ascii=False, indent=2)
        except Exception:  # noqa: BLE001
            response.encoding = response.encoding or "utf-8"
            pretty = response.text
        title = Path(path).name or slug
        metadata = {
            "url": candidate["url"],
            "final_url": final_url,
            "content_type": content_type,
            "classification": "json_asset",
            "fetched_at": fetched_at,
        }
        paths = save_text_resource(discovery_dir, slug, ".json", pretty, title, metadata)
        result.update(paths)
        result["classification"] = "json_asset"
        result["title"] = title
        return result

    if is_textual_content(content_type) or extension in {"", ".xml"}:
        response.encoding = response.encoding or "utf-8"
        extractor = base.ArticleExtractor()
        extractor.feed(response.text)
        extractor.close()

        article_html = extractor.article_html()
        extracted_title = extractor.title() or Path(path).name or candidate["url"]

        if article_html:
            capture_mode = "article"
            title = extracted_title
        elif base.is_auth_redirect(final_url, extracted_title, response.text):
            capture_mode = "auth_redirect"
            title = Path(path).name or extracted_title or candidate["url"]
            article_html = base.build_placeholder_article(
                title=title,
                source_url=candidate["url"],
                final_url=final_url,
                reason="This discovered internal link redirected to an authentication page, so the original documentation body could not be downloaded anonymously.",
                details=[f"Observed redirect page title: {extracted_title}"],
            )
        else:
            capture_mode = "placeholder"
            title = extracted_title
            preview = base.html_to_text(response.text, preserve_whitespace=False)[:1200]
            details = [f"Page text preview: {preview}"] if preview else None
            article_html = base.build_placeholder_article(
                title=title,
                source_url=candidate["url"],
                final_url=final_url,
                reason="The discovered page did not expose a standard <article> block, so a placeholder was generated.",
                details=details,
            )

        markdown = base.article_html_to_markdown(article_html, final_url)
        text_body = base.html_to_text(article_html, preserve_whitespace=False) + "\n"
        metadata = {
            "title": title,
            "url": candidate["url"],
            "final_url": final_url,
            "content_type": content_type,
            "classification": capture_mode,
            "fetched_at": fetched_at,
        }
        front_matter = make_front_matter(metadata)

        raw_path = discovery_dir / "pages" / "raw-html" / f"{slug}.html"
        article_path = discovery_dir / "pages" / "article-html" / f"{slug}.html"
        markdown_path = discovery_dir / "pages" / "markdown" / f"{slug}.md"
        text_path = discovery_dir / "pages" / "text" / f"{slug}.txt"
        write_text(raw_path, response.text)
        write_text(article_path, article_html)
        write_text(markdown_path, front_matter + "\n\n" + markdown)
        write_text(text_path, text_body)

        result.update(
            {
                "raw_path": str(raw_path.relative_to(discovery_dir)),
                "article_path": str(article_path.relative_to(discovery_dir)),
                "markdown_path": str(markdown_path.relative_to(discovery_dir)),
                "text_path": str(text_path.relative_to(discovery_dir)),
                "classification": capture_mode,
                "title": title,
            }
        )
        return result

    # Fallback for anything else.
    binary_title = Path(path).name or slug
    extracted = f"Unparsed binary resource.\nContent-Type: {content_type}\nSize: {len(response.content)} bytes\n"
    metadata = {
        "url": candidate["url"],
        "final_url": final_url,
        "content_type": content_type,
        "classification": "binary_asset",
        "fetched_at": fetched_at,
    }
    chosen_extension = extension or ".bin"
    paths = save_binary_resource(discovery_dir, slug, chosen_extension, response.content, extracted, binary_title, metadata)
    result.update(paths)
    result["classification"] = "binary_asset"
    result["title"] = binary_title
    return result


def build_discovery_corpus(discovery_dir: Path, results: list[dict[str, Any]]) -> str:
    lines = [
        "# Coupa discovery corpus",
        "",
        f"- Generated at: {base.utc_now_iso()}",
        f"- Resource count: {len(results)}",
        "",
    ]
    for item in results:
        markdown_path = item.get("markdown_path")
        if not markdown_path:
            continue
        markdown_text = (discovery_dir / markdown_path).read_text(encoding="utf-8")
        body = re.sub(r"^---\n.*?\n---\n+", "", markdown_text, flags=re.DOTALL)
        lines.extend(
            [
                "---",
                "",
                f"## {item['index']:04d}. {item['title']}",
                "",
                f"- URL: {item['url']}",
                f"- Final URL: {item['final_url']}",
                f"- Classification: {item['classification']}",
                f"- Sources seen: {item['source_count']}",
                "",
                body.strip(),
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def write_discovery_reports(discovery_dir: Path, results: list[dict[str, Any]]) -> None:
    report_dir = discovery_dir / "reports"
    auth_items = [item for item in results if item["classification"] == "auth_redirect"]
    public_items = [item for item in results if item["classification"] != "auth_redirect"]

    write_json(report_dir / "auth-gated-discovery.json", auth_items)
    write_json(report_dir / "public-discovery.json", public_items)

    with (report_dir / "auth-gated-discovery.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["index", "title", "url", "final_url", "kind_hint", "source_count", "classification"],
        )
        writer.writeheader()
        for item in auth_items:
            writer.writerow(
                {
                    "index": item["index"],
                    "title": item["title"],
                    "url": item["url"],
                    "final_url": item["final_url"],
                    "kind_hint": item["kind_hint"],
                    "source_count": item["source_count"],
                    "classification": item["classification"],
                }
            )

    lines = [
        "# Discovery auth-gated resources",
        "",
        f"- Generated at: {base.utc_now_iso()}",
        f"- Count: {len(auth_items)}",
        "",
    ]
    for item in auth_items:
        lines.extend(
            [
                f"## {item['index']:04d}. {item['title']}",
                "",
                f"- URL: {item['url']}",
                f"- Final URL: {item['final_url']}",
                f"- Kind hint: {item['kind_hint']}",
                f"- Seen from {item['source_count']} source page(s)",
                "",
            ]
        )
    write_text(report_dir / "auth-gated-discovery.md", "\n".join(lines).strip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover additional Coupa/Compass docs and assets beyond the original TOC.")
    parser.add_argument(
        "--base-output-dir",
        default=str(Path(__file__).resolve().parents[1] / "output"),
        help="Existing output directory from fetch_coupa_docs.py",
    )
    parser.add_argument("--workers", type=int, default=8, help="Concurrent workers for discovery fetches.")
    parser.add_argument("--limit", type=int, default=0, help="Optional cap on the number of discovery candidates.")
    args = parser.parse_args()

    base_output_dir = Path(args.base_output_dir).resolve()
    discovery_dir = base_output_dir / "discovery"
    discovery_dir.mkdir(parents=True, exist_ok=True)

    manifest = load_base_manifest(base_output_dir)
    write_auth_gated_report(base_output_dir, manifest)

    candidates = discover_candidates(base_output_dir, manifest)
    if args.limit and args.limit > 0:
        candidates = candidates[: args.limit]
    write_json(discovery_dir / "candidates.json", candidates)

    known_urls = {canonicalize_url(item["url"]) for item in manifest["results"]}
    results: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        future_map: dict[concurrent.futures.Future[dict[str, Any]], tuple[dict[str, Any], requests.Session]] = {}
        for candidate in candidates:
            session = base.build_session()
            future = executor.submit(fetch_candidate, candidate, discovery_dir, known_urls, session)
            future_map[future] = (candidate, session)

        for future in concurrent.futures.as_completed(future_map):
            candidate, session = future_map[future]
            try:
                result = future.result()
                results.append(result)
                print(f"[{result['index']:04d}/{len(candidates):04d}] OK {candidate['url']} :: {result['classification']}")
            except Exception as exc:  # noqa: BLE001
                errors.append(
                    {
                        "index": candidate["index"],
                        "url": candidate["url"],
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                )
                print(f"[{candidate['index']:04d}/{len(candidates):04d}] ERR {candidate['url']} :: {exc}")
            finally:
                session.close()

    results.sort(key=lambda item: item["index"])

    write_json(discovery_dir / "manifest.json", {"generated_at": base.utc_now_iso(), "count": len(results), "errors": errors, "results": results})
    write_json(discovery_dir / "errors.json", errors)

    summary_counter = Counter(item["classification"] for item in results)
    summary = {
        "generated_at": base.utc_now_iso(),
        "candidate_count": len(candidates),
        "success_count": len(results),
        "error_count": len(errors),
        "classification_counts": dict(summary_counter),
    }
    write_json(discovery_dir / "summary.json", summary)
    write_text(discovery_dir / "corpus.md", build_discovery_corpus(discovery_dir, results))
    write_discovery_reports(discovery_dir, results)

    lines = [
        "# Coupa discovery summary",
        "",
        f"- Generated at: {summary['generated_at']}",
        f"- Candidates fetched: {summary['candidate_count']}",
        f"- Successes: {summary['success_count']}",
        f"- Errors: {summary['error_count']}",
        "",
        "## Classification counts",
        "",
    ]
    for key, value in sorted(summary_counter.items()):
        lines.append(f"- {key}: {value}")
    lines.append("")
    write_text(discovery_dir / "summary.md", "\n".join(lines))

    print(f"Done. Discovery success={len(results)} errors={len(errors)} output={discovery_dir}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
