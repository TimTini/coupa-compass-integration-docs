---
title: "Data File Sources API (/data_file_sources)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/data-file-sources-api-(data_file_sources)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/data-file-sources-api-(data_file_sources)"
status_code: 200
fetched_at: "2026-04-09T11:59:12+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Data File Sources API (/data_file_sources)"
---

# Data File Sources API (/data_file_sources)

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Data File Sources API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/data_file_sources` | create | Creating data file source is not supported |
| GET | `/api/data_file_sources` | index | Query data file sources |
| POST | `/api/data_file_sources/load_from_coupa_file_service` | load_from_coupa_file_service | Load from Coupa file service |
| POST | `/api/data_file_sources/load_from_sftp` | load_from_sftp | Upload flat file and process via data file source |
| GET | `/api/data_file_sources/:id` | show | Show data file source |
| PUT | `/api/data_file_sources/:id` | update | Updating data file source is not supported |
| GET | `/api/data_file_sources/validate_api_key` | validate_api_key | Validate API key |

## Elements

The following elements are available for the Data File Sources
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| end-time | end_time | | | | | yes | datetime |
| file-content-type | file_content_type | | | | | yes | string |
| file-file-name | file_file_name | | | | | yes | string |
| file-file-size | file_file_size | | | | | yes | string |
| id | Coupa unique identifier | | | | | yes | integer |
| progress | progress | | | | | yes | integer |
| result-text | result_text | | | | | yes | text |
| source-for | source_for | yes | | | | yes | string |
| start-time | start_time | | | | | yes | datetime |
| status | transaction status | | | | | yes | string |
| type | type | | | | | yes | string |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| upload-errors | upload_errors | | | | | yes | |
