---
name: coupa-compass-docs
description: Tra cứu tài liệu Coupa Compass (integration) từ kho local; bắt buộc dùng trước khi trả lời chi tiết API/auth/flow tích hợp.
---

# Coupa Compass — tra cứu tài liệu gốc

## Khi nào dùng

- Câu hỏi về **Coupa Compass**, API REST, OAuth/OIDC, Supplier Portal, invoice, integration technical docs.
- Bất kỳ chi tiết có thể **sai nếu đoán**: endpoint, bước cấu hình, thuật ngữ sản phẩm.

## Quy tắc trả lời

1. Chạy tra cứu (lệnh dưới đây) với câu hỏi đã tóm tắt.
2. Trả lời **dựa trên** các đoạn trong `results`; **không** bịa URL hoặc chi tiết không có trong kết quả.
3. Trích dẫn: **title + URL** của chunk dùng; trích ngắn `text` khi cần.

## Lệnh (JSON cho agent)

Đặt `REPO` = đường dẫn tuyệt đối tới clone `coupa-compass-integration-docs`.

```bash
python "%REPO%\scripts\coupa_doc_search.py" "your search query" --top-k 8
```

Windows PowerShell:

```powershell
python "E:\Documents\MyGitProject\coupa-compass-integration-docs\scripts\coupa_doc_search.py" "OAuth client Coupa" --top-k 8
```

Đầu ra là JSON: `results[].title`, `url`, `text`, `score`, `toc_path`.

- Index mặc định: `output/semantic-search`. Nếu rebuild index ở chỗ khác: thêm `--index-dir "..."`.
- Đọc người: `--format text`.

## Nếu lỗi `index_missing`

Chạy build index trong repo (xem `README.md` mục semantic search), rồi tìm lại.

---

## Cài trên từng công cụ (một skill, nhiều nơi)

**Nguyên tắc:** cùng một thư mục skill này; copy hoặc symlink vào đúng thư mục skill của từng tool.

### Cursor

- Copy hoặc symlink `skills/coupa-compass-docs` vào một trong:
  - `%USERPROFILE%\.cursor\skills-cursor\coupa-compass-docs`, hoặc
  - `.cursor/skills/coupa-compass-docs` trong workspace (nếu project cho phép).
- Trong chat: nhắc `coupa-compass-docs` hoặc “tra Coupa doc trước khi trả lời”.

### Claude Code (CLI)

- Copy/symlink vào `%USERPROFILE%\.claude\skills\coupa-compass-docs` (hoặc skills project-level nếu bạn dùng).
- Khi task liên quan Coupa integration: đọc skill này và chạy `coupa_doc_search.py` trước.

### Codex (OpenAI / VS tooling)

- **Không** dùng chung một “skill store” với Cursor: thêm đoạn ngắn vào rule project (vd. `AGENTS.md` hoặc `.codex/`) trỏ tới repo và lệnh trên, hoặc symlink skill vào path Codex đọc (nếu bạn đã cấu hình universal agent skills `%.agents\skills%`).
- Nội dung tối thiểu: “Với Coupa Compass integration: luôn chạy `coupa_doc_search.py` với query tiếng Anh/ngắn, parse JSON, trả lời kèm URL.”

### MCP (tuỳ chọn)

Nếu sau này bọc `coupa_doc_search.py` trong MCP server: một tool `search_coupa_docs` trả cùng schema JSON — Cursor/Claude có thể gọi thống nhất. Skill này vẫn giữ làm hợp đồng hành vi (khi nào phải search).
