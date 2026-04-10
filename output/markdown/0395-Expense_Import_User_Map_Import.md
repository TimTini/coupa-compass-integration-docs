---
title: "Expense Import User Map Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/expense-import-user-map-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/expense-import-user-map-import"
status_code: 200
fetched_at: "2026-04-09T12:00:37+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Expense Import User Map Import"
---

# Expense Import User Map Import

## Overview

The Expense Import User Map Import process read files from
the `./Incoming/ExpenseImportUserMaps/` in the
SFTP. These files will be moved to the archive folder located
at `./Incoming/Archive/ExpenseImportUserMaps/` before
being processed in Alpha-Numeric order.

## Possible values

Corp Card Integration Name
Must match the name of the integration on the
Setup > Integrations
page.
Account Type
For Employee Id mapping, use EMPLOYEE_ID. When mapping with account number, use one of
AMEX, VISA, or MCC.
Reimbursement Type
Corporate Bill; Individual Bill

## Expense Import User Map

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Corp Card Integration Name | No | No | | Corporate Card Integration Name | |
| Account Type | No | No | | Account Type | |
| Account Number | No | No | | Account Number | |
| Email | No | No | | Email | |
| Reimbursement Type | No | No | | Reimbursement Type | |
