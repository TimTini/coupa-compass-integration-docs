from __future__ import annotations

import json
import os
import time

import gradio as gr
import numpy as np
from huggingface_hub import InferenceClient, hf_hub_download
from sentence_transformers import SentenceTransformer

# Dataset id khi chạy trên hub: biến môi trường COUPA_DATASET_REPO = owner/name (cùng bộ file với output/semantic-search).
DATASET_REPO = os.environ.get("COUPA_DATASET_REPO", "").strip()
if not DATASET_REPO:
    raise RuntimeError(
        "Thiếu COUPA_DATASET_REPO: gán id dataset (owner/name) chứa chunks.jsonl, embeddings.npy, index-meta.json."
    )

# Tóm tắt (EN) rồi dịch sang VI — model nhỏ, phù hợp tier miễn phí (có giới hạn tốc độ).
SUMMARIZE_MODEL = "sshleifer/distilbart-cnn-12-6"
TRANSLATE_MODEL = "Helsinki-NLP/opus-mt-en-vi"
# Đoạn quá ngắn thì chỉ dịch, không gọi tóm tắt (tiết kiệm API + tránh tóm tắt vô nghĩa).
SUMMARIZE_MIN_CHARS = 320
TEXT_CLIP_CHARS = 1800
# Giảm 429 khi free tier: nghỉ nhẹ giữa các hàng (tùy chỉnh nếu cần).
DELAY_BETWEEN_ROWS_SEC = 0.35

_inference_client: InferenceClient | None = None


def get_inference_client() -> InferenceClient:
    global _inference_client
    if _inference_client is None:
        token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
        _inference_client = InferenceClient(token=token)
    return _inference_client


def _clean_one_line(text: str) -> str:
    return " ".join(text.replace("\n", " ").split())


def _clip_at_word_boundary(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars].rsplit(" ", 1)[0]
    return cut + "…"


def _pick_summary_text(out: object) -> str:
    if isinstance(out, dict):
        return str(out.get("summary_text") or out.get("summary") or out)
    return str(getattr(out, "summary_text", None) or out)


def _pick_translation_text(out: object) -> str:
    if isinstance(out, dict):
        return str(out.get("translation_text") or out)
    return str(getattr(out, "translation_text", None) or out)


def summarize_and_translate_vi(raw_text: str) -> str:
    """Tóm tắt (nếu đủ dài) rồi dịch EN→VI qua Inference API."""
    text = _clip_at_word_boundary(_clean_one_line(raw_text), TEXT_CLIP_CHARS)
    if not text.strip():
        return ""
    client = get_inference_client()
    try:
        if len(text) >= SUMMARIZE_MIN_CHARS:
            summary_out = client.summarization(text, model=SUMMARIZE_MODEL)
            en = _pick_summary_text(summary_out).strip()
            if not en:
                en = text
        else:
            en = text
        en = _clip_at_word_boundary(en, 1200)
        trans_out = client.translation(en, model=TRANSLATE_MODEL)
        return _pick_translation_text(trans_out).strip()
    except Exception as exc:
        return f"(Không xử lý được: {exc})"


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
    for idx, i in enumerate(top_indices):
        row = CHUNKS[int(i)]
        snippet = row["text"].replace("\n", " ")
        if len(snippet) > 350:
            snippet = snippet[:350] + "..."
        vi = summarize_and_translate_vi(row.get("text", ""))
        rows.append([f"{float(scores[i]):.4f}", row.get("title", ""), row.get("url", ""), snippet, vi])
        if idx < len(top_indices) - 1:
            time.sleep(DELAY_BETWEEN_ROWS_SEC)
    return rows


with gr.Blocks() as demo:
    gr.Markdown("# Coupa Docs Semantic Search")
    query = gr.Textbox(label="Query", placeholder="VD: invoice match exception flow")
    top_k = gr.Slider(minimum=1, maximum=20, value=5, step=1, label="Top K")
    btn = gr.Button("Search")
    table = gr.Dataframe(
        headers=["Score", "Title", "URL", "Snippet (EN)", "Tóm tắt / dịch (VI)"],
        wrap=True,
    )
    btn.click(fn=search, inputs=[query, top_k], outputs=[table])


if __name__ == "__main__":
    demo.launch()
