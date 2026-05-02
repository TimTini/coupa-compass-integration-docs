---
title: Coupa Docs Semantic Search
emoji: 📚
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 5.27.0
app_file: app.py
pinned: false
---

# Coupa Docs Semantic Search

Gradio template: load chunk and embedding artifacts from a local build of `output/semantic-search` (see the repository root `README.md`). The app downloads `chunks.jsonl`, `embeddings.npy`, and `index-meta.json` from a dataset whose id you supply via the `COUPA_DATASET_REPO` environment variable (see `app.py`).
