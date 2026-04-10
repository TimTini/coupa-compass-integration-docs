---
title: "Schedule Line Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/schedule-line-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/schedule-line-export"
status_code: 200
fetched_at: "2026-04-09T12:00:26+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Schedule Line Export"
---

# Schedule Line Export

## Schedule Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| id | Coupa's internal ID | integer | No/No | |
| schedulable-type | Schedulable Type | string(255) | No/No | |
| schedulable-id | Schedulable Id | integer | No/No | |
| quantity | Quantity | decimal(30,6) | Yes/No | |
| delivery-date | Delivery Date | datetime | No/No | |
| system-generated | System Generated | boolean | No/No | |
| created-by-id | Coupa ID of User who created purchase order | integer | No/No | |
| updated-by-id | Coupa ID of User last updated by | integer | No/No | |
| created-at | Date record was created in Coupa. | datetime | No/No | |
| updated-at | Last Updated at Date | datetime | No/No | |
| initiated-by | Initiated By | integer | No/No | |
