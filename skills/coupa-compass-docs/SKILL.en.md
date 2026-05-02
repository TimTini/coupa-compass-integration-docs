---
name: coupa-compass-docs
description: "Ground answers in local Coupa Compass integration docs (RAG) before API/auth/OIDC details. See SKILL.md for Vietnamese."
---

# Coupa Compass — source documentation lookup

> **Tiếng Việt:** [SKILL.md](SKILL.md)

## When to use

- Questions about **Coupa Compass**, REST API, OAuth/OIDC, Supplier Portal, invoices, integration technical documentation.
- Any detail that is **unsafe to guess**: endpoints, configuration steps, product terminology.

## Answer rules

1. Run the search command (below) with a concise paraphrase of the question.
2. Answer **only from** the `results` chunks; **do not** fabricate URLs or details not present in the results.
3. Cite **title + URL** of each chunk used; quote `text` briefly when needed.

## Prerequisites

- `pip install -r requirements.txt` (numpy, sentence-transformers, …).
- Built semantic index (`build_semantic_index.py` → `output/semantic-search/`). See `README.en.md` or `README.md` (semantic search section).

Query tips: **English** or exact doc terms (OAuth, OIDC, Supplier Portal, …) usually score better with the default English embedding model.

## Multilingual (document language vs query language)

- **Returned chunk text** is always **English** (as crawled from Compass).
- **Queries** may be **Vietnamese or English**.
- The **default** index (`sentence-transformers/all-MiniLM-L6-v2`, see `index-meta.json`) fits **English** queries best. Vietnamese queries can still return hits but may be **less consistent** (monolingual embeddings).
- For **reliable Vietnamese queries**, rebuild the index with a multilingual model, e.g. `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (same `build_semantic_index.py`, change `--model` and `--output-dir` or overwrite deliberately). Point `coupa_doc_search.py --index-dir` at the new index folder.

## Command (JSON)

Run from the **repository root** (the folder that contains `scripts/` and `output/`):

```bash
python scripts/coupa_doc_search.py "your search query" --top-k 8
```

Output is JSON: `results[].title`, `url`, `text`, `score`, `toc_path`.

- Default index: `output/semantic-search`. If the index lives elsewhere: add `--index-dir "..."`.
- Human-readable output: `--format text`.

## If you see `index_missing`

Build the index in this repo (see `README.en.md` / `README.md`, semantic search), then search again.
