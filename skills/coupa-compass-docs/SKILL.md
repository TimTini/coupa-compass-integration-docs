---
name: coupa-compass-docs
description: "VI: Tra cứu Coupa Compass (local). EN: Ground answers in local Compass integration docs before API/auth/OIDC details."
---

# Coupa Compass — tra cứu tài liệu gốc

> **English / Tiếng Anh:** [SKILL.en.md](SKILL.en.md)

## Khi nào dùng

- Câu hỏi về **Coupa Compass**, API REST, OAuth/OIDC, Supplier Portal, invoice, integration technical docs.
- Bất kỳ chi tiết có thể **sai nếu đoán**: endpoint, bước cấu hình, thuật ngữ sản phẩm.

## Quy tắc trả lời

1. Chạy tra cứu (lệnh dưới đây) với câu hỏi đã tóm tắt.
2. Trả lời **dựa trên** các đoạn trong `results`; **không** bịa URL hoặc chi tiết không có trong kết quả.
3. Trích dẫn: **title + URL** của chunk dùng; trích ngắn `text` khi cần.

## Tiền đề

- Đã `pip install -r requirements.txt` (numpy, sentence-transformers, …).
- Đã build index semantic (`build_semantic_index.py` → `output/semantic-search/`). Xem `README.md` hoặc `README.en.md`, mục semantic search.

Gợi ý query: **tiếng Anh** hoặc đúng thuật ngữ tài liệu (OAuth, OIDC, Supplier Portal, …) thường cho điểm khớp tốt hơn.

## Đa ngôn ngữ (ngôn ngữ tài liệu vs ngôn ngữ câu hỏi)

- **Nội dung trả về** luôn là **tiếng Anh** (đúng text trong Compass đã crawl).
- **Câu hỏi / query** có thể viết **tiếng Việt hoặc tiếng Anh**.
- Index **mặc định** (`sentence-transformers/all-MiniLM-L6-v2`, xem `index-meta.json`) tối ưu cho query **Anh**. Query tiếng Việt vẫn có thể ra kết quả nhưng đôi khi **kém ổn định** (embedding chỉ một ngôn ngữ).
- Muốn **ưu tiên câu hỏi tiếng Việt**: build lại index với model đa ngôn ngữ, ví dụ `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (cùng `build_semantic_index.py`, đổi `--model` và `--output-dir` hoặc ghi đè có chủ đích). Sau đó trỏ `coupa_doc_search.py --index-dir` vào thư mục index mới.

## Lệnh (JSON)

Chạy từ **thư mục gốc repo** (thư mục có `scripts/` và `output/`):

```bash
python scripts/coupa_doc_search.py "your search query" --top-k 8
```

Đầu ra là JSON: `results[].title`, `url`, `text`, `score`, `toc_path`.

- Index mặc định: `output/semantic-search`. Nếu rebuild index ở chỗ khác: thêm `--index-dir "..."`.
- Đọc người: `--format text`.

## Nếu lỗi `index_missing`

Chạy build index trong repo (xem `README.md` / `README.en.md`, mục semantic search), rồi tìm lại.
