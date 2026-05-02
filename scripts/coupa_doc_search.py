from __future__ import annotations

"""
Tra cứu tài liệu Coupa Compass (semantic index local). Mặc định in JSON ra stdout
để Cursor / Claude / Codex (hoặc MCP) dễ parse.

Cần build index trước: scripts/build_semantic_index.py
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

# Cùng thư mục với query_semantic_search.py
sys.path.insert(0, str(Path(__file__).resolve().parent))
from query_semantic_search import read_jsonl, search  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search Coupa docs (JSON for agents, or --format text for humans)"
    )
    parser.add_argument("query", help="Câu hỏi / từ khóa tìm kiếm")
    parser.add_argument(
        "--index-dir",
        default=str(Path(__file__).resolve().parents[1] / "output" / "semantic-search"),
        help="Thư mục có chunks.jsonl, embeddings.npy, index-meta.json",
    )
    parser.add_argument("--top-k", type=int, default=5, help="Số kết quả (>=1)")
    parser.add_argument("--model", default="", help="Ghi đè model trong index-meta.json (hiếm khi cần)")
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="json: một mảng JSON (mặc định); text: dạng đọc cho người",
    )
    args = parser.parse_args()

    index_dir = Path(args.index_dir).resolve()
    chunks_path = index_dir / "chunks.jsonl"
    embeddings_path = index_dir / "embeddings.npy"
    meta_path = index_dir / "index-meta.json"
    if not chunks_path.exists() or not embeddings_path.exists() or not meta_path.exists():
        err = {
            "error": "index_missing",
            "message": f"Thiếu index trong: {index_dir}. Chạy build_semantic_index.py trước.",
        }
        print(json.dumps(err, ensure_ascii=False), file=sys.stderr)
        return 2

    chunks = read_jsonl(chunks_path)
    embeddings = np.load(embeddings_path).astype(np.float32)
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    model_name = args.model.strip() or meta["model"]
    if len(chunks) != embeddings.shape[0]:
        err = {"error": "index_corrupt", "message": "chunks.jsonl và embeddings.npy không khớp số dòng."}
        print(json.dumps(err, ensure_ascii=False), file=sys.stderr)
        return 3

    top_k = max(1, args.top_k)
    results = search(
        query=args.query,
        top_k=top_k,
        model_name=model_name,
        chunks=chunks,
        embeddings=embeddings,
    )

    if args.format == "text":
        print(f"Query: {args.query}")
        print(f"Model: {model_name}")
        print(f"Top K: {top_k}")
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

    out: list[dict[str, Any]] = []
    for score, row in results:
        out.append(
            {
                "score": round(score, 6),
                "title": row.get("title", ""),
                "url": row.get("url", ""),
                "toc_path": row.get("toc_path", []),
                "text": row.get("text", "").strip(),
            }
        )
    payload = {
        "query": args.query,
        "model": model_name,
        "top_k": top_k,
        "index_dir": str(index_dir),
        "results": out,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
