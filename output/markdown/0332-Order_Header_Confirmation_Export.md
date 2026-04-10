---
title: "Order Header Confirmation Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/order-header-confirmation-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/order-header-confirmation-export"
status_code: 200
fetched_at: "2026-04-09T12:00:21+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Order Header Confirmation Export"
---

# Order Header Confirmation Export

Export of these records is included as a Standard CSV
Export.

## Order Confirmation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| id | Coupa's internal ID | integer | No/No | |
| status | PO Confirmation Status | string(255) | No/No | |
| order-header-id | Coupa's internal ID | integer | No/No | |
| order-header-version-id | Coupa's internal ID | integer | No/No | |
| external-reference-number | External Reference Number | string(255) | No/No | |
| integration-message | Integration Message | text | Yes/No | |
| created-at | Created Date | datetime | No/No | |
| updated-at | Last Updated at Date | datetime | No/No | |
| tags | Tags | Tag | No/No | |
