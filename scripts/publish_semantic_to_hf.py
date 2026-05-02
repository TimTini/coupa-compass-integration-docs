from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from huggingface_hub import HfApi


def ensure_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_dataset_readme(dataset_repo_id: str) -> str:
    return f"""---
configs:
- config_name: default
  data_files:
  - split: train
    path: chunks.jsonl
---

# Coupa Docs Semantic Index

This dataset stores semantic-search artifacts for `{dataset_repo_id}`.

- `chunks.jsonl`: chunk rows for dataset viewer/training pipelines
- `embeddings.npy`: dense vectors aligned by row index with `chunks.jsonl`
- `index-meta.json`: index metadata (model, dimensions, chunk params)

The viewer is configured to parse only `chunks.jsonl` to avoid schema conflicts with metadata files.
"""


def build_space_template(space_dir: Path, dataset_repo_id: str) -> None:
    app_py = f"""from __future__ import annotations

import json

import gradio as gr
import numpy as np
from huggingface_hub import hf_hub_download
from sentence_transformers import SentenceTransformer

DATASET_REPO = "{dataset_repo_id}"


def normalize(vectors: np.ndarray) -> np.ndarray:
    if vectors.ndim == 1:
        vectors = vectors.reshape(1, -1)
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1
    return vectors / norms


def load_data():
    chunks_file = hf_hub_download(repo_id=DATASET_REPO, repo_type="dataset", filename="chunks.jsonl")
    embeddings_file = hf_hub_download(repo_id=DATASET_REPO, repo_type="dataset", filename="embeddings.npy")
    meta_file = hf_hub_download(repo_id=DATASET_REPO, repo_type="dataset", filename="index-meta.json")

    chunks = []
    with open(chunks_file, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))
    embeddings = np.load(embeddings_file).astype(np.float32)
    meta = json.loads(open(meta_file, "r", encoding="utf-8").read())
    return chunks, embeddings, meta


CHUNKS, EMBEDDINGS, META = load_data()
MODEL = SentenceTransformer(META["model"])


def search(query: str, top_k: int):
    if not query.strip():
        return []
    query_vec = MODEL.encode([query], convert_to_numpy=True, normalize_embeddings=False).astype(np.float32)
    query_vec = normalize(query_vec)[0]
    scores = EMBEDDINGS @ query_vec
    top_indices = np.argsort(-scores)[:top_k]
    rows = []
    for i in top_indices:
        row = CHUNKS[int(i)]
        snippet = row["text"].replace("\\n", " ")
        if len(snippet) > 350:
            snippet = snippet[:350] + "..."
        rows.append([f"{{float(scores[i]):.4f}}", row.get("title", ""), row.get("url", ""), snippet])
    return rows


with gr.Blocks() as demo:
    gr.Markdown("# Coupa Docs Semantic Search")
    query = gr.Textbox(label="Query", placeholder="VD: invoice match exception flow")
    top_k = gr.Slider(minimum=1, maximum=20, value=5, step=1, label="Top K")
    btn = gr.Button("Search")
    table = gr.Dataframe(headers=["Score", "Title", "URL", "Snippet"], wrap=True)
    btn.click(fn=search, inputs=[query, top_k], outputs=[table])


if __name__ == "__main__":
    demo.launch()
"""
    requirements_txt = """numpy
sentence-transformers
huggingface_hub
gradio
"""
    readme = f"""---
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

This Space loads chunk + embedding artifacts from dataset `{dataset_repo_id}` and provides semantic search.
"""
    write_text(space_dir / "app.py", app_py)
    write_text(space_dir / "requirements.txt", requirements_txt)
    write_text(space_dir / "README.md", readme)


def main() -> int:
    parser = argparse.ArgumentParser(description="Upload semantic-search artifacts to Hugging Face dataset and prepare Space template")
    parser.add_argument("--dataset-repo", required=True, help="Dataset repo id, e.g. username/coupa-docs-semantic-index")
    parser.add_argument("--space-repo", default="", help="Optional Space repo id to auto-create and upload app template")
    parser.add_argument(
        "--index-dir",
        default=str(Path(__file__).resolve().parents[1] / "output" / "semantic-search"),
        help="Directory with chunks.jsonl, embeddings.npy, index-meta.json",
    )
    parser.add_argument(
        "--work-dir",
        default=str(Path(__file__).resolve().parents[1] / "output" / "hf-space-template"),
        help="Local temp directory for Space files",
    )
    parser.add_argument("--private", action="store_true", help="Create private dataset/space repos")
    args = parser.parse_args()

    index_dir = Path(args.index_dir).resolve()
    work_dir = Path(args.work_dir).resolve()
    ensure_file(index_dir / "chunks.jsonl")
    ensure_file(index_dir / "embeddings.npy")
    ensure_file(index_dir / "index-meta.json")

    api = HfApi()

    publish_dir = work_dir / "dataset-upload"
    if publish_dir.exists():
        shutil.rmtree(publish_dir)
    publish_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(index_dir / "chunks.jsonl", publish_dir / "chunks.jsonl")
    shutil.copy2(index_dir / "embeddings.npy", publish_dir / "embeddings.npy")
    shutil.copy2(index_dir / "index-meta.json", publish_dir / "index-meta.json")
    write_text(publish_dir / "README.md", build_dataset_readme(args.dataset_repo))

    api.create_repo(repo_id=args.dataset_repo, repo_type="dataset", private=args.private, exist_ok=True)
    api.upload_folder(
        repo_id=args.dataset_repo,
        repo_type="dataset",
        folder_path=str(publish_dir),
        commit_message="Upload semantic-search index artifacts",
    )
    print(f"Uploaded dataset: https://huggingface.co/datasets/{args.dataset_repo}")

    if args.space_repo.strip():
        if work_dir.exists():
            shutil.rmtree(work_dir)
        work_dir.mkdir(parents=True, exist_ok=True)
        build_space_template(work_dir, args.dataset_repo)
        api.create_repo(
            repo_id=args.space_repo,
            repo_type="space",
            space_sdk="gradio",
            private=args.private,
            exist_ok=True,
        )
        api.upload_folder(
            repo_id=args.space_repo,
            repo_type="space",
            folder_path=str(work_dir),
            commit_message="Add semantic-search Space app",
        )
        print(f"Uploaded Space: https://huggingface.co/spaces/{args.space_repo}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
