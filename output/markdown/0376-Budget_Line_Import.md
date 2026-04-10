---
title: "Budget Line Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/budget-line-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/budget-line-import"
status_code: 200
fetched_at: "2026-04-09T12:00:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Budget Line Import"
---

# Budget Line Import

## Overview

The Budget Line Import process read files from `./Incoming/BudgetLines/` in
the SFTP. These files will be moved to the archive folder located at
`./Incoming/Archive/BudgetLines/` before being processed in alphanumeric
order.

- The Chart of Accounts must already exist

- The Account must already exist for the Chart of Accounts

- Currency must be active.

## Keys

`Budgeting Segment` and `Period` are the keys to update an
existing budget line. Both keys are needed in order to perform an update.

When specified, the `Remaining Budget` field will cause the
`Amount` column to be ignored.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: When loading lines for the first time, always use the
`Amount` column and do not use the `Remaining Budget`
column.

## Notes

Coupa's integrations don't currently provide a way to directly capture outside spend. The
appropriate way to capture this change to the budget would be to update the budget to reduce
the budget's total amount by the amount of the outside spend. For example: a $5000 budget
exists for Account ABC for Fall 2012 with $2000 used for by PO 123 and PO 124. $1000 of
budget ABC is spent outside of Coupa. An update to Account ABC's Fall 2012 budget should be
made to change the total budget amount from $5000 to $4000 to reflect in Coupa that only
$2000 is remaining.

## Possible values

Owner Is Approver
1 or 2 (1=on all requisitions, 2=only when budget is exceeded)
Budget Overrun Calculation
1 or 2 (1=Approved, 2=approved and pending requisitions)

## Budget

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Budget Segment | Yes | No | | Budget Segment | |
| Chart of Accounts | Yes | No | | Chart of Accounts Name. Must Exist in Coupa. | |
| Owner (Login) | No | No | | Budget Owner Login. Must Exist in Coupa | |
| Description | No | No | | Budget Description | |
| Notes | No | No | | Budget Notes | |
| Owner Is Approver | No | No | | Have Budget Owner Approve things affecting budget | |
| Budget Hard Stop | No | No | | Prevent submission of requisitions that would exceed the budget | |
| Budget Overrun Calculation | No | No | | Use approved or approved and pending requisitions | |

## Budget Line

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Period | Yes | No | | Budget Period Name. Must exist in Coupa | |
| Budgeting Segment | No | No | | Budgeting Account Code | |
| Amount | No | No | decimal | Total Budget Amount | |
| Remaining | No | No | decimal | Budget Amount Remaining | |
| Pending Requisitions Amount | No | No | decimal | Amount consumed by pending Requisitions | |
| Description | No | No | string(255) | Budget Description | |
| Notes | No | No | text | Budget Notes | |
| Owner | No | No | | Budget Owner Login. Must Exist in Coupa | |
| Owner Is Approver | No | No | integer | Have budget owner approve things affecting budget. Once the box is checked, update with value of 0 to uncheck. Set to 1 for all requisitions, Set to 2 when budget is exceeded. | |
| Budget Hard Stop | No | No | boolean | Prevent submission of requisitions that would exceed the budget | |
| Budget Overrun Calculation | No | No | integer | Use this field to calculate budgets against approved requisitions or approved and pending requisitions. 1 for approved, 2 for approved and pending requisitions. | |
| Segment 1 | No | No | string(100) | Budgeting Account Segment 1 | |
| Segment 2 | No | No | string(100) | Budgeting Account Segment 2 | |
| Segment 3 | No | No | string(100) | Budgeting Account Segment 3 | |
| Segment 4 | No | No | string(100) | Budgeting Account Segment 4 | |
| Segment 5 | No | No | string(100) | Budgeting Account Segment 5 | |
| Segment 6 | No | No | string(100) | Budgeting Account Segment 6 | |
| Segment 7 | No | No | string(100) | Budgeting Account Segment 7 | |
| Segment 8 | No | No | string(100) | Budgeting Account Segment 8 | |
| Segment 9 | No | No | string(100) | Budgeting Account Segment 9 | |
| Segment 10 | No | No | string(100) | Budgeting Account Segment 10 | |
| Segment 11 | No | No | string(100) | Budgeting Account Segment 11 | |
| Segment 12 | No | No | string(100) | Budgeting Account Segment 12 | |
| Segment 13 | No | No | string(100) | Budgeting Account Segment 13 | |
| Segment 14 | No | No | string(100) | Budgeting Account Segment 14 | |
| Segment 15 | No | No | string(100) | Budgeting Account Segment 15 | |
| Segment 16 | No | No | string(100) | Budgeting Account Segment 16 | |
| Segment 17 | No | No | string(100) | Budgeting Account Segment 17 | |
| Segment 18 | No | No | string(100) | Budgeting Account Segment 18 | |
| Segment 19 | No | No | string(100) | Budgeting Account Segment 19 | |
| Segment 20 | No | No | string(100) | Budgeting Account Segment 20 | |
