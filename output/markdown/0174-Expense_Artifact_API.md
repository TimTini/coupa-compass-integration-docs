---
title: "Expense Artifact API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-artifact-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-artifact-api"
status_code: 200
fetched_at: "2026-04-09T11:59:41+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Artifact API"
---

# **Expense Artifact API**

Use this API to attach files to expense reports and expense lines.

## Overview

Artifact is Coupa-speak for attachments. This API endpoint lets you attach files to [expense reports](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-reports-api) and [expense lines](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

For attachments classified as a supported image type, the API supports downloading a preview (640x640) and thumbnail (128x128) version.

For attachments classified as a non-image file, the API supports downloading the original file (e.g pdf)

:style can have value of 'preview' or 'thumb' .. it allows a smaller size of image to be downloaded (only applies to artifacts of supported image types)

## Actions

The Expense Artifacts API lets you:

| Verb | Path | Action | Description |
| --- | --- | --- | --- |
| POST | @@BLOCK_0@@ | create | Create expense artifact |
| POST | `/api/expense_lines/:expense_line_id/expense_artifacts` | create | Create expense artifact |
| GET | @@BLOCK_1@@ | image | Query expense artifact image. `:style` is optional and can be `preview`' or `thumb` in order to fetch a smaller version of the image. |
| GET | @@BLOCK_2@@ | image | Query expense artifact image. `:style` is optional and can be `preview`' or `thumb` in order to fetch a smaller version of the image. |
| GET | @@BLOCK_3@@ | index | Query expense artifacts |
| GET | `/api/expense_lines/expense_artifacts` | index | Query expense artifacts |
| GET | `/api/expense_lines/:expense_line_id/expense_artifacts` | index | Query expense artifacts |
| GET | @@BLOCK_4@@ | show | Show expense artifact |
| GET | `/api/expense_lines/expense_artifacts/:id` | show | Show expense artifact |
| GET | @@BLOCK_5@@ | show | Show expense artifact |
| PUT | @@BLOCK_6@@ | update | Update expense artifact |
| PUT | `/api/expense_lines/expense_artifacts/:id` | update | Update expense artifact |
| PUT | @@BLOCK_7@@ | update | Update expense artifact |
| PUT | @@BLOCK_8@@ | update_with_ocr_response | Update expense artifact with OCR response. |
| GET | `/api/expense_reports/:expense_report_id/download` | retrieves expense report attachments | Response payload is a zip archive with folders for each expense line that has receipt attachments. When images have been converted to PDFs or when PDFs are digitally signed, then only those final receipt attachment files are included in the downloaded zip archive. Available with R29 and more recent. |

## Elements

| Element | Description | Req'd | Unique | Allowable Value | In | Out | Data Type |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | Userhttps://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users) |
| external-src-ref | External system's unique identifier for transaction | | | | | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| image-content-type | image_content_type | | | | | yes | string(255) |
| image-file-name | image_file_name | | | | | yes | string(255) |
| image-file-size | image_file_size | | | | | yes | string(255) |
| image-rotation | Image rotation angle | | | | yes | yes | integer |
| ocr-status | OCR Status | | | | yes | yes | string(50) |
| source-content-type | source_content_type | | | | | yes | string(255) |
| source-file-name | source_file_name | | | | | yes | string(255) |
| source-file-size | source_file_size | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | Userhttps://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users) |
| url | External link to artifact | | | | | yes | string |
| digitization-status | Digitization status | | | | | yes | string(25) |
| digitization-error | Digitization error | | | | | yes | string |
| digitized-receipt-file-name | Digitized receipt file name | | | | | yes | string(255) |
| digitized-receipt-content-type | Digitized receipt content type | | | | | yes | string(255) |
| digitized-receipt-file-size | Digitized receipt file size | | | | | yes | integer |
