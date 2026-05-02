# Coupa Compass Integration Technical Documentation Archive

Nguồn gốc:

- TOC gốc: <https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation>
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

- `E:\Documents\MyGitProject\coupa-compass-integration-docs\scripts\fetch_coupa_docs.py`
  - Script tải lại toàn bộ TOC và sinh dữ liệu AI-ready.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\raw-html\`
  - HTML đầy đủ của từng URL.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\article-html\`
  - HTML phần nội dung chính đã tách riêng.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\markdown\`
  - Markdown từng trang, có front matter metadata.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\text\`
  - Plain text từng trang.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\toc.json`
  - TOC chuẩn hóa để máy xử lý.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\toc.md`
  - TOC ở dạng Markdown.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\manifest.json`
  - Manifest đầy đủ: URL, file map, mode, hash, kích thước.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\documents.jsonl`
  - Một dòng JSON cho mỗi tài liệu, kèm markdown/text để ingest cho AI/RAG.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\all-docs.md`
  - Bản ghép toàn bộ tài liệu thành một corpus Markdown lớn.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\reports\auth-gated-existing.md`
  - Danh sách 40 mục trong TOC gốc bị auth-gated.

### Kết quả discovery mở rộng

- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\discovery\manifest.json`
  - Manifest toàn bộ tài nguyên phát hiện thêm ngoài TOC.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\discovery\summary.md`
  - Tóm tắt số lượng theo loại.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\discovery\corpus.md`
  - Corpus Markdown lớn cho phần discovery.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\discovery\pages\`
  - Các page HTML/Markdown/Text phát hiện thêm.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\discovery\assets\`
  - JSON/XLSX và bản text/markdown phục vụ AI.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\discovery\reports\auth-gated-discovery.md`
  - Danh sách 155 link discovery bị auth-gated.
- `E:\Documents\MyGitProject\coupa-compass-integration-docs\output\discovery\reports\public-discovery.json`
  - Danh sách public artifacts đã lấy được trong discovery.

## Ghi chú

- Với các link yêu cầu auth, file Markdown tương ứng sẽ ghi rõ URL gốc, URL redirect, và lý do không thể tải nội dung gốc ẩn danh.
- Tên file được rút gọn theo `NNNN-Title` để tránh lỗi path quá dài trên Windows.
- Một phần các JSON schema đời cũ/đời mới dưới `_dita_/.../misc/` là public; một phần khác chỉ truy cập được khi đăng nhập nên được ghi nhận là auth-gated.

## Chạy lại

```powershell
python "E:\Documents\MyGitProject\coupa-compass-integration-docs\scripts\fetch_coupa_docs.py" `
  --output-dir "E:\Documents\MyGitProject\coupa-compass-integration-docs\output" `
  --workers 8
```

```powershell
python "E:\Documents\MyGitProject\coupa-compass-integration-docs\scripts\extend_coupa_discovery.py" `
  --base-output-dir "E:\Documents\MyGitProject\coupa-compass-integration-docs\output" `
  --workers 8
```
