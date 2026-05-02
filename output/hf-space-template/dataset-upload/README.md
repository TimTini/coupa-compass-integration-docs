---
configs:
- config_name: default
  data_files:
  - split: train
    path: chunks.jsonl
---

# Coupa Docs Semantic Index

This dataset stores semantic-search artifacts for `TimTini/coupa-docs-semantic-index`.

- `chunks.jsonl`: chunk rows for dataset viewer/training pipelines
- `embeddings.npy`: dense vectors aligned by row index with `chunks.jsonl`
- `index-meta.json`: index metadata (model, dimensions, chunk params)

The viewer is configured to parse only `chunks.jsonl` to avoid schema conflicts with metadata files.
