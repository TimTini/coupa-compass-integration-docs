---
title: "Procurement Milestone Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/procurement-milestone-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/procurement-milestone-export"
status_code: 200
fetched_at: "2026-04-09T12:00:25+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Procurement Milestone Export"
---

# Procurement Milestone Export

Export of these records is included as a Standard CSV
Export.

## Payment Agreement

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| record type | Milestone | | No/No | |
| type | Type | string(255) | No/No | |
| status | Status | string(255) | No/No | |
| percent | Percent | decimal(30,6) | No/No | |
| amount | Amount | decimal(30,6) | No/No | |
| description | Description | text | No/No | |
| due-date | Due date | date | No/No | |
| external-reference-code | External reference code | string(255) | No/No | |
| payment-terms-code | Payment Terms | | No/No | |
| payment-terms-days-for-discount-payment | Number of days to pay to receive discount | | No/No | |
| payment-terms-days-for-net-payment | Net Days for Payment | | No/No | |
| payment-terms-discount-rate | Discount Rate for payment within Discount Terms | | No/No | |
