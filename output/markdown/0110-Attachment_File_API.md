---
title: "Attachment File API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachment-file-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachment-file-api"
status_code: 200
fetched_at: "2026-04-09T11:59:27+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Attachment File API"
---

# Attachment File API

Use the Attachments API to manage attachments on Coupa Reference and Transactional
objects.

## Elements

The following elements are available for the
Attachment File API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| file | file | | | | | yes | string(255) |
| file-file-size | File file size | | | | | yes | string(255) |
| file-url | file url | | | | yes | yes | |
| id | Coupa unique identifier | | | | | yes | integer |
| intent | intent | | | | yes | yes | string(40) |
| linked-to | link to specific feature | | | | yes | | string(255) |
| text | text | | | | yes | | text |
| type | type | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| url | url | | | | yes | | string(255) |
