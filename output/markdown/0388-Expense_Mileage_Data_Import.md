---
title: "Expense Mileage Data Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/expense-mileage-data-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/expense-mileage-data-import"
status_code: 200
fetched_at: "2026-04-09T12:00:36+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Expense Mileage Data Import"
---

# Expense Mileage Data Import

## Overview

The expense mileage data import process reads files from the
`./Incoming/ExpenseMileageData/` in the SFTP. These files will be moved to
the archive folder located at `./Incoming/Archive/ExpenseMileageData/` before
being processed in Alpha-Numeric order.

## Expense-Mileage-Data

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Country | No | No | | Country | |
| Region | No | No | | Region | |
| Vehicle Type | No | No | | Vehicle Type | |
| Effective Date | No | No | | Effective Date | |
| Currency | No | No | | Currency | |
| Base Rate | No | No | | Base Rate | |
| Rate 2 | No | No | | Rate 2 | |
| Rate 3 | No | No | | Rate 3 | |
| Rate 4 | No | No | | Rate 4 | |
| Rate 5 | No | No | | Rate 5 | |
| Passenger Rate | No | No | | Passenger Rate | |
| Expiry Date | No | No | | Expiry Date | |
