# Coupa Compass Integration Technical Documentation Archive

**English / Tiếng Anh:** [README.en.md](README.en.md)

Nguồn gốc:

- Đây là bản lưu kỹ thuật của mục **Integration Technical Documentation** trên Coupa Compass; URL và metadata đầy đủ nằm trong `output/manifest.json`, `output/toc.md`, và front matter từng trang.
- Thời điểm tạo: 2026-04-09

## Kết quả

- Tổng link duy nhất trong TOC: **548**
- Tải được nội dung trực tiếp dạng article: **508**
- Link bị chuyển sang trang đăng nhập Okta nên chỉ tạo placeholder + lưu raw HTML redirect/login: **40**
- Lỗi tải: **0**

## Discovery mở rộng ngoài TOC gốc

Mình đã quét tiếp toàn bộ internal link liên quan xuất hiện trong archive đã tải và lấy thêm:

- Candidate ngoài TOC gốc: **338**
- Public / lưu được artifact: **183**
- Auth-gated / redirect sang Okta: **155**
- Lỗi còn lại: **0**

Trong phần mở rộng này có:

- **107** JSON/OpenAPI schema assets
- **38** XLSX assets
- **37** trang/alias public nhưng chỉ lấy được placeholder hoặc landing content
- **1** trang article public bổ sung

## Cấu trúc thư mục

(Từ thư mục gốc của repo.)

- `scripts/fetch_coupa_docs.py` — script tải lại toàn bộ TOC và sinh dữ liệu AI-ready.
- `output/raw-html/` — HTML đầy đủ của từng URL.
- `output/article-html/` — HTML phần nội dung chính đã tách riêng.
- `output/markdown/` — Markdown từng trang, có front matter metadata.
- `output/text/` — plain text từng trang.
- `output/toc.json` — TOC chuẩn hóa để máy xử lý.
- `output/toc.md` — TOC ở dạng Markdown.
- `output/manifest.json` — manifest đầy đủ: URL, file map, mode, hash, kích thước.
- `output/documents.jsonl` — một dòng JSON cho mỗi tài liệu, kèm markdown/text để ingest cho AI/RAG.
- `output/all-docs.md` — bản ghép toàn bộ tài liệu thành một corpus Markdown lớn.
- `output/reports/auth-gated-existing.md` — danh sách 40 mục trong TOC gốc bị auth-gated.

### Kết quả discovery mở rộng

- `output/discovery/manifest.json` — manifest toàn bộ tài nguyên phát hiện thêm ngoài TOC.
- `output/discovery/summary.md` — tóm tắt số lượng theo loại.
- `output/discovery/corpus.md` — corpus Markdown lớn cho phần discovery.
- `output/discovery/pages/` — các page HTML/Markdown/Text phát hiện thêm.
- `output/discovery/assets/` — JSON/XLSX và bản text/markdown phục vụ AI.
- `output/discovery/reports/auth-gated-discovery.md` — danh sách 155 link discovery bị auth-gated.
- `output/discovery/reports/public-discovery.json` — danh sách public artifacts đã lấy được trong discovery.

## Ghi chú

- Với các link yêu cầu auth, file Markdown tương ứng sẽ ghi rõ URL gốc, URL redirect, và lý do không thể tải nội dung gốc ẩn danh.
- Tên file được rút gọn theo `NNNN-Title` để tránh lỗi path quá dài trên Windows.
- Một phần các JSON schema đời cũ/đời mới dưới `_dita_/.../misc/` là public; một phần khác chỉ truy cập được khi đăng nhập nên được ghi nhận là auth-gated.

## Chạy lại

```powershell
python scripts/fetch_coupa_docs.py `
  --output-dir output `
  --workers 8
```

```powershell
python scripts/extend_coupa_discovery.py `
  --base-output-dir output `
  --workers 8
```

(Chạy từ thư mục gốc repo.)

## Semantic search (local)

### 1) Cài dependencies

```powershell
pip install -r requirements.txt
```

### 2) Build semantic index từ corpus docs

```powershell
python scripts/build_semantic_index.py `
  --documents-jsonl output/documents.jsonl `
  --output-dir output/semantic-search `
  --model "sentence-transformers/all-MiniLM-L6-v2"
```

Artifacts sinh ra:

- `output/semantic-search/chunks.jsonl`
- `output/semantic-search/embeddings.npy`
- `output/semantic-search/index-meta.json`

### 3) Query semantic search local

```powershell
python scripts/query_semantic_search.py `
  "invoice match exception flow" `
  --index-dir output/semantic-search `
  --top-k 5
```

### 3b) Tra cứu JSON (agent / script)

- Script: `scripts/coupa_doc_search.py` — in **JSON** (mặc định) để parse; `--format text` cho người đọc.
- Quy tắc trích dẫn: `skills/coupa-compass-docs/` (`SKILL.md` = tiếng Việt, `SKILL.en.md` = tiếng Anh).
- Cần đã build index (mục 2) và cài dependency (mục 1). Gợi ý query: tiếng Anh hoặc đúng thuật ngữ Compass (invoice, OAuth, Supplier Portal, …).
- **Đa ngôn ngữ:** tài liệu trích ra là **tiếng Anh**. Query có thể **VI hoặc EN**; index mặc định (`all-MiniLM-L6-v2`) hợp query Anh hơn. Nếu thường hỏi bằng **tiếng Việt**, build lại index với model đa ngôn ngữ, ví dụ `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (mục 2, đổi `--model`); trỏ `coupa_doc_search.py --index-dir` tới thư mục index mới.

```powershell
python scripts/coupa_doc_search.py `
  "invoice match exception" `
  --index-dir output/semantic-search `
  --top-k 8
```

### 4) Script xuất bản (tuỳ chọn)

Các file `scripts/publish_semantic_to_hf.py`, `scripts/publish_hf_space.py` và thư mục `output/hf-space-template/` phục vụ đóng gói index/app ra môi trường bên ngoài repo; tham số repo và xác thực cấu hình tại chỗ khi bạn dùng — không mô tả ở đây.
