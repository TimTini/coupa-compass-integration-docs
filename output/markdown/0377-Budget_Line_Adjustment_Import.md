---
title: "Budget Line Adjustment Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/budget-line-adjustment-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/budget-line-adjustment-import"
status_code: 200
fetched_at: "2026-04-09T12:00:34+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Budget Line Adjustment Import"
---

# Budget Line Adjustment Import

## Overview

The Budget Line Adjustment Import process read files from
`./Incoming/BudgetLineAdjustments/` in the SFTP. These files will be moved
to the archive folder located at `./Incoming/Archive/BudgetLineAdjustment/`
before being processed in alphanumeric order.

- The Chart of Accounts must already exist

- The Account must already exist for the Chart of Accounts

- Currency must be active.

- Budget Segment Must exists

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: You must open an individual record in order to download the CSV
import template.

## Budget Line Adjustment

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Budget period* | Yes | No | | Name for Budget Period | |
| Chart of Accounts* | Yes | No | | Name for Chart of Accounts | |
| Budget segment* | Yes | No | | Budget Line code | |
| Adjustment amount* | Yes | No | decimal(32,4) | Budget Line Adjustment amount | |
| Currency* | Yes | No | | Currency code | |
| Description | No | No | string(255) | adjustment description | |
