---
title: "Payables :: Expense Preapproval Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/payables-expense-preapproval-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/payables-expense-preapproval-export"
status_code: 200
fetched_at: "2026-04-09T12:00:23+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Payables :: Expense Preapproval Export"
---

# Payables :: Expense Preapproval Export

## Payable Expense Preapproval

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible value is ExpensePreapproval | | No/No | |
| id | The ID of the payable expense preapproval | integer | No/No | |
| created-at | The date the payable Expense Preapproval was created on | datetime | No/No | |
| updated-at | The date the payable expense preapproval was last updated on | datetime | No/No | |
| status | The status of the payable expense preapproval | string(255) | No/No | |
| paid-date | The date the payable expense preapproval was marked as fully paid | datetime | No/No | |
| paid-total | The total amount paid | decimal | No/No | |
| remaining-total | The total amount remaining to be paid | decimal | No/No | |
| remittance-total | The total remittance amount required | decimal | No/No | |
| accounting-total | The total of the payable expense preapproval in the CoA currency | decimal | No/No | |
| exported | A flag indicating if the payable expense preapproval has been marked as exported | | No/No | |
| last-exported-at | The date that the payable expense preapproval was last marked as exported | datetime | No/No | |
| type | the type of payable | string(255) | Yes/No | |
| payment-channel | The payment channel on the payable expense preapproval | string(255) | No/No | |
| payable-type | The type of associated payable. Value can be ExpensePreapproval | | No/No | |
| payable-id | The ID of the associated ExpensePreapproval | | No/No | |
| user-fullname | The user fullname from the associated ExpensePreapproval | | No/No | |
| chart-of-account-code | The Chart of Accounts name | | No/No | |
