---
title: "TCS Tax Line Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/tcs-tax-line-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/tcs-tax-line-export"
status_code: 200
fetched_at: "2026-04-09T12:00:31+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "TCS Tax Line Export"
---

# TCS Tax Line Export

## Tcs Tax Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | | No/No | |
| invoice-number | The user-created invoice number. | | No/No | |
| tax-line-number | The line number of the corresponding of the tax line. | integer | No/No | |
| tax-line-id | The unique identifier Coupa assigns to the tax line. | integer | No/No | |
| amount | The amount of tax calculated on the line. | decimal(32,4) | No/No | |
| rate | The tax rate indicated on the invoice line. | float | No/No | |
| code | The tax rate code for the invoice line tax rate. Must match an existing tax rate code within Coupa. | | No/No | |
| base | Base indicates the base amount of the invoice or line item to which tax was applied | decimal(30,4) | No/No | |
| type | TcsTaxLine | string(255) | No/No | |
