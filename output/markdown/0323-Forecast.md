---
title: "Forecast"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/forecast"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/forecast"
status_code: 200
fetched_at: "2026-04-09T12:00:18+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Forecast"
---

# Forecast

Export of these records is included as a Standard CSV Export.

## Forecast

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| id | Coupa's Internal ID | integer | No/No | |
| external-reference | External Reference of Forecast Header | string(255) | Yes/Yes | |
| name | Name | string(255) | No/No | |
| description | Description | string(255) | No/No | |
| default-lead-time | Default Lead Time | integer | No/No | |
| default-fence | Default Fence | integer | No/No | |
| owner-id | Coupa's Internal ID | integer | No/No | |
| owner-type | Coupa's Internal Type | string(255) | No/No | |
| location-id | Coupa's Internal ID | integer | No/No | |
| interval | Possible Interval Values: day, week, month, year | string(255) | No/No | day, week, month, year |
| active | Active | boolean | No/No | |
| created-by-id | Coupa's Internal ID | integer | No/No | |
| updated-by-id | Coupa's Internal ID | integer | No/No | |
| created-at | Created Date | datetime | No/No | |
| updated-at | Last Updated at Date | datetime | No/No | |
