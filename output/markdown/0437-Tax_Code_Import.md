---
title: "Tax Code Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/tax-code-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/tax-code-import"
status_code: 200
fetched_at: "2026-04-09T12:00:47+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Tax Code Import"
---

# Tax Code Import

## Overview

The Tax Code Import process reads files from the `./Incoming/TaxCodes/` from
SFTP.

These files are moved to the archive folder located at ./Archive/Incoming/TaxCodes/ before
being processed in alphanumeric order.

You can also load tax codes and rates using the UI CSV file loader on your instance at
`./tax_codes`.

The `Code` column is the key column, and must be unique.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: Compliance users must also specify standard fields. For example,
if specifying `Tax Rate Percentage`, you still have to specify the same
value in `Percentage`.

## Tax Code

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Country Code | Yes | Yes | string(255) | The country code where the tax code will be applied | |
| Tax Rate Percentage | Yes | No | float | Tax Rate Percentage | |
| Tax Rate Exempt? | No | No | | Used to map the tax code to a tax rate and tax rate type. This determines if a tax code is for an exempt tax rate | |
| Tax Rate Reverse Charge? | No | No | | Used to map the tax code to a tax rate and tax rate type. This determines if a tax code is for a reverse charge tax rate | |
| Tax Rate Customer Accounting? | No | No | | Used to map the tax code to a tax rate and tax rate type. This determines if a tax code is for a customer accounting tax rate | |
| Tax Rate Description | No | No | string(255) | Used to map the tax code to a tax rate and tax rate type. This corresponds with the tax rate type's description | |
| Tax Rate Out of Scope? | No | No | | Used to map the tax code to a tax rate and tax rate type. This determines if a tax code is for an out of scope tax rate | |
| Withholding Tax Type | No | No | | Withholding Tax Type | |
| Enterprise Name | No | No | | Name of the enterprise that this tax code belongs to | |
| Supplier Name | No | No | | Used to map withholding taxes to a supplier | |
| Code* | Yes | Yes | string(255) | Tax Code Identifier | |
| Percentage* | Yes | No | float | Tax Percentage Amount | |
| Description | No | No | string(255) | Tax Description | |
| Enforce VAT Rules | No | No | | If VAT rules are enforced | |
| Active | No | No | boolean | Determines if the tax code is enabled or disabled | |
| Effective Date | No | No | datetime | The date when the tax code will become active | |
| Is Withholding? | No | No | | Is Withholding? | |
| Subtract from Gross | No | No | | Withhold from Supplier? | |
| Is TCS? | No | No | | Is Tax Collected at Source? | |
| Withholding Tax Amount Overwritable | No | No | boolean | Withholding Tax Amount Overwritable | |
