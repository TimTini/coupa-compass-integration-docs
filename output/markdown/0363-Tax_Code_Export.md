---
title: "Tax Code Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/tax-code-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/tax-code-export"
status_code: 200
fetched_at: "2026-04-09T12:00:30+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Tax Code Export"
---

# Tax Code Export

Export of these records is included as a Standard CSV
Export.

## Tax Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | | No/No | |
| invoice-number | The user-created invoice number. | | No/No | |
| invoice-line-id | The unique identifier Coupa assigns to the invoice line. | | No/No | |
| invoice-line-number | The line number of the corresponding invoice line. | | No/No | |
| invoice-charge-id | The unique identifier Coupa assigns to the invoice charge | | No/No | |
| invoice-charge-number | The line number of the invoice charge | | No/No | |
| tax-line-number | The line number of the corresponding of the tax line. | integer | No/No | |
| tax-line-id | The unique identifier Coupa assigns to the tax line. | integer | No/No | |
| amount | The amount of tax calculated on the line. | decimal(32,4) | No/No | |
| rate | The tax rate indicated on the invoice line. | float | No/No | |
| tax-rate-type | The tax rate type description on the line | | No/No | |
| code | The tax rate code for the invoice line tax rate. Must match an existing tax rate code within Coupa. | | No/No | |
| amount-engine | Amount calculated by either Coupa Native or External Tax Engine based on configuration | decimal(32,4) | No/No | |
| code-engine | Code returned by External Tax Engine based on configuration | string(255) | No/No | |
| rate-engine | Rate returned by External Tax Engine based on configuration | decimal(30,6) | No/No | |
| description | The tax line description. | string(255) | No/No | |
| location | The taxable location for this tax line. | string(255) | No/No | |
| date | The tax line date in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| kind-of-factor | Kind of Factor indicates the specific type of Withholding which applies to the line item | string(255) | No/No | |
| basis | Basis indicates the CFDI base amount of the invoice or line item to which withholding tax was applied | decimal(30,6) | No/No | |
| Base Amount | Base indicates the base amount of the invoice or line item to which tax was applied | decimal(30,4) | No/No | |
| Supplier Withholding Rate | CFDI Withholding Rate | decimal(30,4) | No/No | |
| Supplier Withholding Amount | CFDI Withholding Amount | decimal(30,4) | No/No | |
| nature-of-tax | Nature of Tax indicates the specific type of tax which applies to the line item e.g. VAT or Withholding | string(255) | No/No | |
| Withholding Amount | Withholding Amount | decimal(30,4) | No/No | |
| Direct/Withholding Tax/TCS Tax | WithholdingTaxLine, TcsTaxLine or TaxLine | string(255) | No/No | |
| product-tax-classification | Product Tax Classification | string(255) | No/No | |

## Withholding Tax Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | | No/No | |
| invoice-number | The user-created invoice number. | | No/No | |
| invoice-line-id | The unique identifier Coupa assigns to the invoice line. | | No/No | |
| invoice-line-number | The line number of the corresponding purchase order line (if any). | | No/No | |
| tax-line-number | The line number of the corresponding of the tax line. | integer | No/No | |
| tax-line-id | The unique identifier Coupa assigns to the tax line. | integer | No/No | |
| amount | The amount of tax calculated on the line. | decimal(32,4) | No/No | |
| rate | The tax rate indicated on the invoice line. | float | No/No | |
| code | The tax rate code for the invoice line tax rate. Must match an existing tax rate code within Coupa. | | No/No | |
| description | The tax line description. | string(255) | No/No | |
| location | The taxable location for this tax line. | string(255) | No/No | |
| date | The tax line date in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| kind-of-factor | Kind of Factor indicates the specific type of Withholding which applies to the line item | string(255) | No/No | |
| basis | Basis indicates the CFDI base amount of the invoice or line item to which withholding tax was applied | decimal(30,6) | No/No | |
| Withholding Base | Base indicates the base amount of the invoice or line item to which withholding tax was applied | decimal(30,4) | No/No | |
| Supplier Withholding Rate | CFDI Withholding Rate | decimal(30,4) | No/No | |
| Supplier Withholding Amount | CFDI Withholding Amount | decimal(30,4) | No/No | |
| nature-of-tax | Nature of Tax indicates the specific type of tax which applies to the line item e.g. VAT or Withholding | string(255) | No/No | |
| Withholding Amount | Withholding Amount | decimal(30,4) | No/No | |
| Direct/Withholding Tax | WithholdingTaxLine or TaxLine | string(255) | No/No | |
