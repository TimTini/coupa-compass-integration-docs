---
title: "Forecast Collaboration Line"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/forecast-collaboration-line"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/forecast-collaboration-line"
status_code: 200
fetched_at: "2026-04-09T12:00:18+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Forecast Collaboration Line"
---

# Forecast Collaboration Line

Export of these records is included as a Standard CSV Export.

## Forecast Collaboration Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| id | Coupa's Internal ID | integer | No/No | |
| external-reference | External Reference of Forecast Line | string(255) | Yes/Yes | |
| name | Name | string(255) | No/No | |
| description | Description | string(255) | Yes/No | |
| price | Price | decimal(30,6) | No/No | |
| uom-id | Coupa's Internal ID | integer | No/No | |
| forecast-collaboration-header-id | Coupa's Internal ID | integer | No/No | |
| supplier-id | Coupa's Internal ID | integer | No/No | |
| item-id | Coupa's Internal ID | integer | No/No | |
| lead-time | Lead Time | integer | No/No | |
| currency-id | Coupa's Internal ID | integer | No/No | |
| supplier-item-id | Coupa's Internal ID | integer | No/No | |
| receiving-warehouse-id | Coupa's Internal ID | integer | No/No | |
| fence | Fence | integer | No/No | |
| supplier-last-updated-at | Supplier Last Updated at Date | datetime | No/No | |
| created-by-id | Coupa's Internal ID | integer | No/No | |
| updated-by-id | Coupa's Internal ID | integer | No/No | |
| created-at | Created Date | datetime | No/No | |
| updated_at | Last Updated at Date | datetime | No/No | |
