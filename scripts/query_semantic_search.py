from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def normalize_l2(vectors: np.ndarray) -> np.ndarray:
    if vectors.ndim == 1:
        vectors = vectors.reshape(1, -1)
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1
    return vectors / norms


def search(
    query: str,
    top_k: int,
    model_name: str,
    chunks: list[dict[str, Any]],
    embeddings: np.ndarray,
) -> list[tuple[float, dict[str, Any]]]:
    model = SentenceTransformer(model_name)
    query_vector = model.encode([query], convert_to_numpy=True, normalize_embeddings=False).astype(np.float32)
    query_vector = normalize_l2(query_vector)
    scores = embeddings @ query_vector[0]
    indices = np.argsort(-scores)[:top_k]
    return [(float(scores[index]), chunks[int(index)]) for index in indices]


def main() -> int:
    parser = argparse.ArgumentParser(description="Query local semantic-search index")
    parser.add_argument("query", help="Natural-language search query")
    parser.add_argument(
        "--index-dir",
        default=str(Path(__file__).resolve().parents[1] / "output" / "semantic-search"),
        help="Directory containing chunks.jsonl, embeddings.npy, index-meta.json",
    )
    parser.add_argument("--top-k", type=int, default=5, help="Top K results")
    parser.add_argument("--model", default="", help="Override model name from index-meta.json")
    args = parser.parse_args()

    index_dir = Path(args.index_dir).resolve()
    chunks_path = index_dir / "chunks.jsonl"
    embeddings_path = index_dir / "embeddings.npy"
    meta_path = index_dir / "index-meta.json"
    if not chunks_path.exists() or not embeddings_path.exists() or not meta_path.exists():
        raise FileNotFoundError(f"Index artifacts missing in: {index_dir}")

    chunks = read_jsonl(chunks_path)
    embeddings = np.load(embeddings_path).astype(np.float32)
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    model_name = args.model.strip() or meta["model"]
    if len(chunks) != embeddings.shape[0]:
        raise RuntimeError("chunks.jsonl row count does not match embeddings.npy row count")

    results = search(
        query=args.query,
        top_k=max(1, args.top_k),
        model_name=model_name,
        chunks=chunks,
        embeddings=embeddings,
    )

    print(f"Query: {args.query}")
    print(f"Model: {model_name}")
    print(f"Top K: {args.top_k}")
    print("-" * 80)
    for rank, (score, row) in enumerate(results, start=1):
        text = row["text"].replace("\n", " ").strip()
        if len(text) > 320:
            text = text[:320] + "..."
        print(f"[{rank}] score={score:.4f}")
        print(f"title: {row.get('title', '')}")
        print(f"url: {row.get('url', '')}")
        print(f"toc_path: {' > '.join(row.get('toc_path', []))}")
        print(f"text: {text}")
        print("-" * 80)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
