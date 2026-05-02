from __future__ import annotations

import argparse
import json
import re
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


def clean_markdown(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n+", "", text, flags=re.DOTALL)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_into_chunks(text: str, chunk_size: int, chunk_overlap: int) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be >= 0 and < chunk_size")

    words = text.split()
    if not words:
        return []

    chunks: list[str] = []
    step = chunk_size - chunk_overlap
    for start in range(0, len(words), step):
        end = min(start + chunk_size, len(words))
        chunk_words = words[start:end]
        if not chunk_words:
            continue
        chunks.append(" ".join(chunk_words))
        if end >= len(words):
            break
    return chunks


def build_chunks(
    documents_jsonl: Path,
    output_dir: Path,
    chunk_size: int,
    chunk_overlap: int,
) -> Path:
    docs = read_jsonl(documents_jsonl)
    chunk_rows: list[dict[str, Any]] = []
    chunk_id = 0
    for doc in docs:
        markdown = clean_markdown(doc.get("markdown", ""))
        if not markdown:
            continue
        chunks = split_into_chunks(markdown, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        for index, chunk_text in enumerate(chunks):
            chunk_rows.append(
                {
                    "chunk_id": chunk_id,
                    "doc_index": doc.get("index"),
                    "title": doc.get("title"),
                    "url": doc.get("url"),
                    "toc_path": doc.get("toc_path", []),
                    "chunk_index": index,
                    "text": chunk_text,
                }
            )
            chunk_id += 1

    output_dir.mkdir(parents=True, exist_ok=True)
    chunk_path = output_dir / "chunks.jsonl"
    with chunk_path.open("w", encoding="utf-8") as handle:
        for row in chunk_rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    return chunk_path


def load_chunks(path: Path) -> list[dict[str, Any]]:
    return read_jsonl(path)


def normalize_l2(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1
    return matrix / norms


def build_embeddings(chunks: list[dict[str, Any]], model_name: str, batch_size: int) -> np.ndarray:
    model = SentenceTransformer(model_name)
    texts = [row["text"] for row in chunks]
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        convert_to_numpy=True,
        normalize_embeddings=False,
        show_progress_bar=True,
    )
    return normalize_l2(embeddings.astype(np.float32))


def write_metadata(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build semantic-search chunks + embeddings from output/documents.jsonl")
    parser.add_argument(
        "--documents-jsonl",
        default=str(Path(__file__).resolve().parents[1] / "output" / "documents.jsonl"),
        help="Input documents.jsonl path",
    )
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parents[1] / "output" / "semantic-search"),
        help="Output directory for chunks + embeddings",
    )
    parser.add_argument(
        "--model",
        default="sentence-transformers/all-MiniLM-L6-v2",
        help="Hugging Face model id for sentence-transformers",
    )
    parser.add_argument("--chunk-size", type=int, default=220, help="Chunk size in words")
    parser.add_argument("--chunk-overlap", type=int, default=40, help="Chunk overlap in words")
    parser.add_argument("--batch-size", type=int, default=64, help="Embedding batch size")
    args = parser.parse_args()

    documents_jsonl = Path(args.documents_jsonl).resolve()
    output_dir = Path(args.output_dir).resolve()
    if not documents_jsonl.exists():
        raise FileNotFoundError(f"Input file not found: {documents_jsonl}")

    chunk_path = build_chunks(
        documents_jsonl=documents_jsonl,
        output_dir=output_dir,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
    )
    chunks = load_chunks(chunk_path)
    if not chunks:
        raise RuntimeError("No chunks generated. Check documents.jsonl content.")

    embeddings = build_embeddings(chunks=chunks, model_name=args.model, batch_size=args.batch_size)
    np.save(output_dir / "embeddings.npy", embeddings)

    metadata = {
        "model": args.model,
        "chunk_count": len(chunks),
        "embedding_dim": int(embeddings.shape[1]),
        "chunk_size_words": args.chunk_size,
        "chunk_overlap_words": args.chunk_overlap,
        "documents_jsonl": str(documents_jsonl),
        "chunks_file": "chunks.jsonl",
        "embeddings_file": "embeddings.npy",
    }
    write_metadata(output_dir / "index-meta.json", metadata)

    print(f"Built semantic index at: {output_dir}")
    print(f"Chunks: {len(chunks)} | Embedding dim: {embeddings.shape[1]} | Model: {args.model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
