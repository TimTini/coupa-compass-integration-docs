---
title: "Expense Reports Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/expense-reports-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/expense-reports-export"
status_code: 200
fetched_at: "2026-04-09T12:00:18+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Expense Reports Export"
---

# Expense Reports Export

## Overview

The expense report export process from Coupa queries for
all approved Expense Reports that have NOT been exported. The
frequency of the integration run is once every hour. The generated
files will be placed
into `./Outgoing/ExpenseReports`. Once the files
are successfully placed into the sFTP folder the expense reports
will be marked as exported.

Export of these records is included as a Standard CSV
Export.

## Expense Report

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| RecordType | Describes the type of row. Possible values are Header, Line, or Line Split. | | No/No | |
| ID | Coupa Generated Document ID | integer | No/No | |
| Created-At | When the expense report was created in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| Updated-At | When the expense report was last updated in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | datetime | No/No | |
| Title | The title of the expense report. | string(255) | No/No | |
| Status | The current status of the expense report. Possible values are: draft, working, pending_approval, pending_info, approved, accounting_review, approved_for_payment, scheduled_for_payment, paid | string(255) | No/No | |
| Submitted-at | When the expense report was submitted for approval in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ. | datetime | No/No | |
| auditor-note | Auditor comments on the expense report. | text | No/No | |
| Rejection-Reason | The reason why the expense report was rejected. | text | No/No | |
| Paid | Flag to indicate if the expense report has been paid. True or False. | boolean | No/No | |
| total | The total amount of the expense report in the transaction currency. | decimal(32,4) | No/No | |
| currency | The currency of the transaction. | | No/No | |
| audit-score | The audit-score Coupa assigns to the expense report. | integer | No/No | |
| Accounting-Total | The total amount of the expense report in the chart of accounts currency. | decimal | No/No | |
| Accounting-Total-Currency | The currency code of the chart of account for this expense report | | No/No | |
| Expensed-By_email | The email address of the user to be reimbursed. | | No/No | |
| Expensed-By_employee_number | The employee number of the user to be reimbursed. | | No/No | |
| Expensed-By_id | The Coupa User ID of the user to be reimbursed. | | No/No | |
| Expensed-By_login | The username of the user to be reimbursed. | | No/No | |
| Expensed-By_Fullname | The full name of the user to be reimbursed. | | No/No | |
| Created-By_email | The email address of the user who created the report. | | No/No | |
| Created-By_employee_number | The employee number of the user who created the report. | | No/No | |
| Created-By_id | The Coupa User ID of the user who created the report. | | No/No | |
| Created-By_login | The username of the user who created the report. | | No/No | |
| Created-By_Fullname,_Firstname | The full name of the user who created the report. | | No/No | |
| Updated-By_email | The email address of the user who last updated the report. | | No/No | |
| Updated-By_employee_number | The employee number of the user who last updated the report. | | No/No | |
| Updated-By_id | The Coupa User ID of the user who last updated the report. | | No/No | |
| Updated-By_login | The username of the user who last updated the report. | | No/No | |
| Updated-By_Fullname | The full name of the user who last updated the report. | | No/No | |
| Event_-_ID | The list of the event IDs. | | No/No | |
| Event_-_Status | The list of the event statuses | | No/No | |
| Event_-_Created_at | The list of event created dates in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | No/No | |
| Event_-_Updated_at | The list of event updated dates in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | No/No | |
| Event_-_Created-By_email | List of Email of user creating report event | | No/No | |
| Event_-_Created-By_employee_number | List of Employee Number of user creating event | | No/No | |
| Event_-_Created-By_id | List of Internal Coupa User ID creating event | | No/No | |
| Event_-_Created-By_login | List of Login of user creating event | | No/No | |
| Event_-_Created-By_Fullname | List of Employee Name of user creating event | | No/No | |
| Event_-_Updated-By_email | List of Email of user who last updated event | | No/No | |
| Event_-_Updated-By_employee_number | List of Employee Number of user who last updated event | | No/No | |
| Event_-_Updated-By_id | List of Internal Coupa User ID who last updated event | | No/No | |
| Event_-_Updated-By_login | List of Login of user who last updated event | | No/No | |
| Event_-By_Fullname | List of Employee Name of user who last updated event | | No/No | |
| Approval_Created-AT | List of Approval Created-At Dates in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | No/No | |
| Approval_Updated-At | List of Approval Updated-At Dates in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | No/No | |
| Position | Approval Order | | No/No | |
| approval-chain-id | Approval Chain ID | | No/No | |
| Approval_status | Approval Status | | No/No | |
| approval-date | Approval Date in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | No/No | |
| Approval_Notes | Approval Notes | | No/No | |
| Approval_Type | Type of Approval Hierarchy | | No/No | |
| Approvable_Type | Type of Approvable | | No/No | |
| Approvable_ID | ID of Approvable | | No/No | |
| Approver_-_Updated-By_email | List of Email of user who last updated event | | No/No | |
| Approver_-_Updated-By_employee_number | List of Employee Number of user who last updated event | | No/No | |
| Approver_-_Updated-By_id | List of Internal Coupa User ID who last updated event | | No/No | |
| Approver_-_Updated-By_login | List of Login of user who last updated event | | No/No | |
| Approver_Updated-By_Fullname | List of Employee Name of user who last updated event | | No/No | |
| Reimburse-to-Employee | Total amount reimbursable to the employee. | decimal | No/No | |
| Reimburse-to-Employee-Currency | The currency code of the reimbursable amount. | | No/No | |
| Payment Channel | The payment channel used to reimburse the employee. | string(255) | No/No | |
| ERP Document ID | Expense document id on ERP side. | string(255) | No/No | |
| ERP Document Status | Expense document status on ERP side. | string(255) | No/No | |

## Expense Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| RecordType | Describes the type of row. Possible values are Header, Line, or Line Split. | | No/No | |
| ID | Coupa's Expense Report ID | integer | No/No | |
| Line-ID | Coupa's Expense Report Line ID | integer | No/No | |
| Line-Number | Line Number | | No/No | |
| PO-Order-Line-ID | If pre approved, Coupa Order Line ID | integer | No/No | |
| Created-at | Time of Record Creation in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| Updated-At | Time Record was last updated in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| Description | Description of Expense Report Line Item | string(1550) | No/No | |
| Merchant | Merchant on line | string(255) | No/No | |
| Reason | Reason for Expense | string(255) | No/No | |
| Transaction-Amount | The amount paid when the transaction was made. | | No/No | |
| Transaction-Currency | The currency that the transaction was made in. | | No/No | |
| Amount | Amount in user's default currency | | No/No | |
| Currency | User's default currency | | No/No | |
| Account-Total | Total of Amount in Chart of Accounts Currency | | No/No | |
| Accounting-Currency | Currency Code | | No/No | |
| Expense-Date | Expense Report Date in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| Expense-Category-Name | Expense Category Name | | No/No | |
| Account-Code | Account Code | | No/No | |
| Account-Segment-1 | Account Segment 1 | | No/No | |
| Account-Segment-2 | Account Segment 2 | | No/No | |
| Account-Segment-3 | Account Segment 3 | | No/No | |
| Account-Segment-4 | Account Segment 4 | | No/No | |
| Account-Segment-5 | Account Segment 5 | | No/No | |
| Account-Segment-6 | Account Segment 6 | | No/No | |
| Account-Segment-7 | Account Segment 7 | | No/No | |
| Account-Segment-8 | Account Segment 8 | | No/No | |
| Account-Segment-9 | Account Segment 9 | | No/No | |
| Account-Segment-10 | Account Segment 10 | | No/No | |
| Account-Segment-11 | Account Segment 11 | | No/No | |
| Account-Segment-12 | Account Segment 12 | | No/No | |
| Account-Segment-13 | Account Segment 13 | | No/No | |
| Account-Segment-14 | Account Segment 14 | | No/No | |
| Account-Segment-15 | Account Segment 15 | | No/No | |
| Account-Segment-16 | Account Segment 16 | | No/No | |
| Account-Segment-17 | Account Segment 17 | | No/No | |
| Account-Segment-18 | Account Segment 18 | | No/No | |
| Account-Segment-19 | Account Segment 19 | | No/No | |
| Account-Segment-20 | Account Segment 20 | | No/No | |
| Account Type | Chart of Account | | No/No | |
| Period Name | Budget Period | | No/No | |
| External Source Name | The corp card template name like corporate_credit_card_amex etc. | string(255) | No/No | |
| External Source Data | The file name of the credit card file that we received from cc company. | string(255) | No/No | |
| External Source Ref | The unique transaction identifier for each credit card transaction | string(255) | No/Yes | |
| Parent External Source Name | The corp card template name like corporate_credit_card_amex etc. | | No/No | |
| Parent External Source Data | The file name of the credit card file that we received from cc company. | | No/No | |
| Parent External Source Ref | The unique transaction identifier for each credit card transaction | | No/No | |
| Imported-Amount | Imported Amount | | No/No | |
| Account Number | Credit Card Account number | | No/No | |
| Employee Number | Employee number | | No/No | |
| First Name | First Name | | No/No | |
| Last Name | Last Name. | | No/No | |
| Parent-Expense-Line-Id | ID of the expense line that was itemized | integer | No/No | |
| Supplier Reference Number | Supplier Reference Number | | No/No | |
| Company Tax Id | The merchant ABN number or Federal Tax ID | | No/No | |
| Corp Card Integration Name | The integration name that is used received the transaction | | No/No | |
| Applied Expense Preapproval Id | Applied Expense Preapproval Id | | No/No | |
| Applied Expense Preapproval Description | Applied Expense Preapproval Description | | No/No | |
| Applied Expense Preapproval Amount | Applied Expense Preapproval Amount | | No/No | |
| Applied Expense Preapproval Currency Code | Applied Expense Preapproval Currency Code | | No/No | |
| Applied Expense Line Cash Advance Amount | Applied Expense Line Cash Advance Amount | | No/No | |
| Applied Expense Line Cash Advance Currency Code | Applied Expense Line Cash Advance Currency Code | | No/No | |
| Reimburse to Employee | Is the Expense Line reimbursable to the employee? | boolean | No/No | |

## Expense Line Allocation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| RecordType | Describes the type of row. Possible values are Header, Line, or Line Split. | | No/No | |
| expense-id | Coupa's Expense Report ID | integer | No/No | |
| expense-line-id | Coupa's Expense Report Line ID | integer | No/No | |
| line-num | Line Number | | No/No | |
| order-header-num | If pre approved, Coupa's Order Header Number | | No/No | |
| order-line-id | If pre approved, Coupa's Order Line ID | | No/No | |
| order-line-num | If pre approved, Coupa's Order Line Number | | No/No | |
| account-allocation-id | Account Allocation ID | integer | No/No | |
| account-allocation-sequence | Position in the Account Allocation Sequence | | No/No | |
| account-allocation-amount | Amount allocated to the account | | No/No | |
| account-allocation-percent | Percentage allocated to the account | | No/No | |
| account-code | The whole account code of the account | | No/No | |
| account-active | Flag indicating if the account is active. True or False. | | No/No | |
| segment-1 | Account Segment 1 | | No/No | |
| segment-2 | Account Segment 2 | | No/No | |
| segment-3 | Account Segment 3 | | No/No | |
| segment-4 | Account Segment 4 | | No/No | |
| segment-5 | Account Segment 5 | | No/No | |
| segment-6 | Account Segment 6 | | No/No | |
| segment-7 | Account Segment 7 | | No/No | |
| segment-8 | Account Segment 8 | | No/No | |
| segment-9 | Account Segment 9 | | No/No | |
| segment-10 | Account Segment 10 | | No/No | |
| segment-11 | Account Segment 11 | | No/No | |
| segment-12 | Account Segment 12 | | No/No | |
| segment-13 | Account Segment 13 | | No/No | |
| segment-14 | Account Segment 14 | | No/No | |
| segment-15 | Account Segment 15 | | No/No | |
| segment-16 | Account Segment 16 | | No/No | |
| segment-17 | Account Segment 17 | | No/No | |
| segment-18 | Account Segment 18 | | No/No | |
| segment-19 | Account Segment 19 | | No/No | |
| segment-20 | Account Segment 20 | | No/No | |
| account-name | Nickname for the account | | No/No | |
| currency_code | Currency Code | | No/No | |
| accounting-total | Total of Amount in Chart of Accounts Currency | decimal(32,4) | No/No | |
| accounting_currency | Currency Code | | No/No | |

## Expense Line Tax

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| RecordType | Expense Line Tax | | No/No | |
| tax-line-id | Coupa's Expense Line Tax ID | integer | No/No | |
| expense-line-id | Coupa's Expense Line ID | integer | No/No | |
| expense-line-number | Expense Line Number | | No/No | |
| expense-report-id | Coupa's Expense Report ID | | No/No | |
| tax-code | The Tax Code for the invoice line tax rate. Must match an existing tax rate code within Coupa. | | No/No | |
| tax-type-description | The Tax Rate Type description on the line. | | No/No | |
| tax-rate-description | The Tax Rate description on the line. | | No/No | |
| tax-line-currency | Tax Line Currency | | No/No | |
| country-code | Country Code | | No/No | |
| tax-rate | Tax Rate | decimal(8,3) | No/No | |
| tax-amount | Tax Amount | decimal(32,4) | No/No | |
| estimated-tax-amount | Estimated Tax Amount | decimal(32,4) | No/No | |

## Expense Report Event History

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |

## Expense Reconciliation Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Type | Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or ReconciliationLine. | | No/No | |
| Adjustment Date | The date the payment was made | datetime | Yes/No | |
| Type of document | The type of document that was paid | string | No/No | |
| Expense Report ID | The document ID that is being paid | | No/No | |
| Amount | The total amount paid | decimal(46,20) | No/No | |
| Currency | User's default currency | | No/No | |
| Created By ID | The user ID that created the payment | integer | No/No | |
| Created By Login | The user login that created the invoice payment | | No/No | |
| Created Date | The date the payment initially drafted | datetime | No/No | |
| Updated By ID | The user ID that most recently updated the payment | integer | No/No | |
| Updated By Login | Ther user login that most recently updated the invoice payment | | No/No | |
| Updated Date | The date the payment was most recently updated | datetime | No/No | |
| Note | Note associated with the payment | string(255) | No/No | |

## Expense To Pay

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible value is Expense | | No/No | |
| id | The ID of the expense | integer | No/No | |
| created-at | The date the expense was created on | datetime | No/No | |
| updated-at | The date the expense was last updated on | datetime | No/No | |
| status | The status of the expense | string(255) | No/No | |
| paid-date | The date the expense was marked as fully paid | datetime | No/No | |
| paid-total | The total amount paid | decimal | No/No | |
| remaining-total | The total amount remaining to be paid | decimal | No/No | |
| remittance-total | The total remittance amount required | decimal | No/No | |
| accounting-total | The total of the expense in the CoA currency | decimal | No/No | |
| exported | A flag indicating if the expense has been marked as exported | | No/No | |
| last-exported-at | The date that the expense was last marked as exported | datetime | No/No | |
| expense-type | The type of expense | string(255) | No/No | |
| payment-channel | The payment channel on the associated ExpenseReport | string(255) | No/No | |
| payable-type | The type of associated payable. Value is ExpenseReport | | No/No | |
| payable-id | The ID of the associated ExpenseReport | | No/No | |
| chart-of-account-code | The Chart of Accounts name | | No/No | |
| legal-entity-name | The Chart of Accounts Legal Entity name | | No/No | |
