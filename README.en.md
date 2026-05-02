# Coupa Compass Integration Technical Documentation Archive

* [Tiếng Việt / Vietnamese](README.md)

## Provenance

- Source TOC: <https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation>
- Generated: 2026-04-09

## Results

- Unique links in the base TOC: **548**
- Article content fetched directly: **508**
- Links redirected to Okta login (placeholder + saved redirect/login HTML): **40**
- Fetch errors: **0**

## Extended discovery (beyond base TOC)

Additional internal links found in the archived pages were crawled:

- Candidates outside base TOC: **338**
- Public / stored artifacts: **183**
- Auth-gated / Okta redirect: **155**
- Remaining errors: **0**

Breakdown of the extension set:

- **107** JSON/OpenAPI schema assets
- **38** XLSX assets
- **37** public pages/aliases with only placeholder or landing content
- **1** additional public article page

## Directory layout

(From the repository root, or replace paths with your clone location.)

- `scripts/fetch_coupa_docs.py` — re-download the full TOC and generate AI-ready data.
- `output/raw-html/` — full HTML per URL.
- `output/article-html/` — main content HTML extracted.
- `output/markdown/` — per-page Markdown with front matter.
- `output/text/` — plain text per page.
- `output/toc.json` — machine-oriented TOC.
- `output/toc.md` — Markdown TOC.
- `output/manifest.json` — full manifest: URL, file map, mode, hash, size.
- `output/documents.jsonl` — one JSON line per document (markdown/text for RAG).
- `output/all-docs.md` — single large Markdown corpus.
- `output/reports/auth-gated-existing.md` — 40 base-TOC items that are auth-gated.

### Extended discovery outputs

- `output/discovery/manifest.json` — all extra resources found outside the base TOC.
- `output/discovery/summary.md` — counts by type.
- `output/discovery/corpus.md` — large Markdown corpus for discovery.
- `output/discovery/pages/` — extra HTML/Markdown/Text pages.
- `output/discovery/assets/` — JSON/XLSX and text/markdown for AI.
- `output/discovery/reports/auth-gated-discovery.md` — 155 auth-gated discovery links.
- `output/discovery/reports/public-discovery.json` — list of public artifacts recovered in discovery.

## Notes

- Auth-required links: the corresponding Markdown records the original URL, redirect URL, and why anonymous fetch failed.
- Filenames use shortened `NNNN-Title` to avoid overly long Windows paths.
- Some JSON schemas under `_dita_/.../misc/` are public; others require login and are marked auth-gated.

## Re-run fetch

```powershell
python "scripts/fetch_coupa_docs.py" `
  --output-dir "output" `
  --workers 8
```

```powershell
python "scripts/extend_coupa_discovery.py" `
  --base-output-dir "output" `
  --workers 8
```

(Run from the repository root, or use absolute paths.)

## Semantic search (local + Hugging Face)

### 1) Install dependencies

```powershell
pip install -r "requirements.txt"
```

### 2) Build semantic index from the document corpus

```powershell
python "scripts/build_semantic_index.py" `
  --documents-jsonl "output/documents.jsonl" `
  --output-dir "output/semantic-search" `
  --model "sentence-transformers/all-MiniLM-L6-v2"
```

Artifacts:

- `output/semantic-search/chunks.jsonl`
- `output/semantic-search/embeddings.npy`
- `output/semantic-search/index-meta.json`

### 3) Query semantic search locally

```powershell
python "scripts/query_semantic_search.py" `
  "invoice match exception flow" `
  --index-dir "output/semantic-search" `
  --top-k 5
```

### 3b) Agent lookup (Cursor / Claude / Codex) — JSON

- Script: `scripts/coupa_doc_search.py` — prints **JSON** by default for agents; `--format text` for humans.
- Skill + citation rules: `skills/coupa-compass-docs/` (`SKILL.md` = Vietnamese, `SKILL.en.md` = English).
- Requires index built (step 2) and dependencies (step 1). Prefer English queries or exact Compass terms (invoice, OAuth, Supplier Portal, …).
- **Languages:** retrieved snippets are **English**. Queries may be **VI or EN**; the default index (`all-MiniLM-L6-v2`) favors **English** queries. For **Vietnamese** queries more often, rebuild with a multilingual model, e.g. `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (step 2, change `--model`); point `coupa_doc_search.py --index-dir` at the new folder.

```powershell
python "scripts/coupa_doc_search.py" `
  "invoice match exception" `
  --index-dir "output/semantic-search" `
  --top-k 8
```

### 4) Upload index to Hugging Face Dataset (free tier)

Log in first:

```powershell
hf auth login
```

Upload dataset:

```powershell
python "scripts/publish_semantic_to_hf.py" `
  --dataset-repo "YOUR_HF_USERNAME/coupa-docs-semantic-index" `
  --index-dir "output/semantic-search"
```

### 5) Deploy Hugging Face Space (Gradio) — from `output/hf-space-template`

The script uploads only `app.py`, `requirements.txt`, `README.md` (skips `dataset-upload/`).

```powershell
python "scripts/publish_hf_space.py" `
  --space-repo "YOUR_HF_USERNAME/coupa-docs-semantic-search"
```

After build: `https://huggingface.co/spaces/YOUR_HF_USERNAME/coupa-docs-semantic-search`.  
For Inference API (summarize/translate after search): **Space → Settings → Repository secrets** → add `HF_TOKEN` (read).

### 5b) (Legacy) Create Space via `publish_semantic_to_hf.py`

`--space-repo` **deletes and regenerates** the old Space template folder (no summarize/translate). Only if you want a single command that also uploads the dataset:

```powershell
python "scripts/publish_semantic_to_hf.py" `
  --dataset-repo "YOUR_HF_USERNAME/coupa-docs-semantic-index" `
  --space-repo "YOUR_HF_USERNAME/coupa-docs-semantic-search"
```
