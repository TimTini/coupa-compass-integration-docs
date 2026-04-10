---
title: "Expense Lines API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api"
status_code: 200
fetched_at: "2026-04-09T11:59:43+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Lines API"
---

# Expense Lines API

## Actions

The Expense Lines API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/expense_lines/:id/assign_attendee/:expense_attendee_id` | assign_attendee | Assign attendee to expense line |
| POST | `/api/expense_lines/:id/calculate_mileage` | calculate_mileage | Calculate line total based on mileage data |
| POST | `/api/expense_lines/:id/calculate_per_diem` | calculate_per_diem | Calculate line total based on trip data |
| POST | `/api/expense_reports/:expense_report_id/expense_lines` | create | Create expense line |
| POST | `/api/expense_lines` | create | Create expense line |
| DELETE | `/api/expense_reports/:expense_report_id/expense_lines/:id` | destroy | Delete expense line |
| DELETE | `/api/expense_lines/:id` | destroy | Delete expense line |
| GET | `/api/expense_reports/:expense_report_id/expense_lines` | index | Query expense lines |
| GET | `/api/expense_lines` | index | Query expense lines |
| GET | `/api/expense_reports/:expense_report_id/expense_lines/:id` | show | Show expense line |
| GET | `/api/expense_lines/:id` | show | Show expense line |
| DELETE | `/api/expense_lines/:id/unassign_attendee/:expense_attendee_id` | unassign_attendee | Unassign attendee from expense line |
| PATCH | `/api/expense_reports/:expense_report_id/expense_lines/:id` | update | Update expense line |
| PUT | `/api/expense_reports/:expense_report_id/expense_lines/:id` | update | Update expense line |
| PATCH | `/api/expense_lines/:id` | update | Update expense line |
| PUT | `/api/expense_lines/:id` | update | Update expense line |

## Elements

The following elements are available for the Expense
Lines API:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account | Account | | | | yes | yes | [Account](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)) |
| account-allocations | Account allocations | | | | yes | yes | [Expense Line Allocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-allocation-api) |
| accounting-total | Accounting total | | | | | yes | decimal(32,4) |
| accounting-total-currency | Accounting total currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| allow-attach-preapproval | Can preapproval be allowed to attach to Expense Line? | | | | | yes | boolean |
| amount | Amount | | | | yes | yes | decimal(32,4) |
| approved-amount | Approved amount | | | | yes | yes | decimal(32,4) |
| attach-preapproval | Attach passed preapproval to line | | | | yes | | boolean |
| audit-status | Audit status | Verified Receipt Online, Verified Unattached Receipt, Waiting for Receipt, No Receipt Required, Approved Without Receipt | yes | yes | [Audit Status](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/audit-status-api) | | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency of transaction | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| custom-field-1 | Custom field 1 | | | | yes | yes | text |
| custom-field-10 | Custom field 10 | | | | yes | yes | text |
| custom-field-11 | Custom field 11 | | | | yes | yes | string(255) |
| custom-field-12 | Custom field 12 | | | | yes | yes | string(255) |
| custom-field-13 | Custom field 13 | | | | yes | yes | string(255) |
| custom-field-14 | Custom field 14 | | | | yes | yes | string(255) |
| custom-field-15 | Custom field 15 | | | | yes | yes | string(255) |
| custom-field-16 | Custom field 16 | | | | yes | yes | string(255) |
| custom-field-17 | Custom field 17 | | | | yes | yes | string(255) |
| custom-field-18 | Custom field 18 | | | | yes | yes | string(255) |
| custom-field-19 | Custom field 19 | | | | yes | yes | string(255) |
| custom-field-2 | Custom field 2 | | | | yes | yes | text |
| custom-field-20 | Custom field 20 | | | | yes | yes | string(255) |
| custom-field-3 | Custom field 3 | | | | yes | yes | text |
| custom-field-4 | Custom field 4 | | | | yes | yes | text |
| custom-field-5 | Custom field 5 | | | | yes | yes | text |
| custom-field-6 | Custom field 6 | | | | yes | yes | text |
| custom-field-7 | Custom field 7 | | | | yes | yes | text |
| custom-field-8 | Custom field 8 | | | | yes | yes | text |
| custom-field-9 | Custom field 9 | | | | yes | yes | text |
| description | Description | | | | yes | yes | string(1550) |
| divisor | Divisor unit | | | | yes | yes | decimal(30,2) |
| end-date | Divisor end date | | | | yes | yes | datetime |
| exchange-rate | Exchange rate | | | | yes | yes | decimal(30,9) |
| expense-artifacts | Expense artifacts | | | | | yes | Expense Artifact |
| expense-attendee | Expense attendee | | | | | yes | [Expense Attendee](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-attendee-api) |
| expense-category | Expense category | yes | | | yes | yes | [Expense Category](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-category-api) |
| expense-category-custom-field-1 | Expense category custom field 1 | | | | yes | yes | text |
| expense-category-custom-field-10 | Expense category custom field 10 | | | | yes | yes | text |
| expense-category-custom-field-2 | Expense category custom field 2 | | | | yes | yes | text |
| expense-category-custom-field-3 | Expense category custom field 3 | | | | yes | yes | text |
| expense-category-custom-field-4 | Expense category custom field 4 | | | | yes | yes | text |
| expense-category-custom-field-5 | Expense category custom field 5 | | | | yes | yes | text |
| expense-category-custom-field-6 | Expense category custom field 6 | | | | yes | yes | text |
| expense-category-custom-field-7 | Expense category custom field 7 | | | | yes | yes | text |
| expense-category-custom-field-8 | Expense category custom field 8 | | | | yes | yes | text |
| expense-category-custom-field-9 | Expense category custom field 9 | | | | yes | yes | text |
| employee-reimbursable | Is the line reimbursable to the employee? | | | | | yes | boolean |
| expense-date | Expense date | | | | yes | yes | datetime |
| expense-line-cash-advance | Expense Line Cash Advance | | | | | yes | expense-line-cash-advance |
| expense-line-daily-per-diems | Daily per diems with amount information for each day | no | no | any | | yes | Expense Line Daily Per Diem |
| expense-line-imported-data | Expense line imported data | | | | | yes | [Expense Line Imported Data](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-imported-data-api) |
| expense-line-mileage | Expense line mileage | | | | | yes | [Expense Line Mileage](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-mileage-api) |
| expense-line-per-diem | Expense per diem data | | | | | yes | [Expense Line Per Diem](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-per-diem-api) |
| expense-line-preapproval | Applied expense preapproval | | | | | yes | [Expense Preapproval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-preapproval-api) |
| expense-line-taxes | Expense line taxes | | | | | yes | [Expense Line Tax](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-tax-api) |
| expense-line-virtual-card | Expense Line Virtual Card | | | | | yes | expense-line-virtual-card |
| expense-report-id | Expense report id | | | | | yes | integer |
| expense-trip | Expense trip | no | no | any | | yes | ExpenseTrip |
| expensed-by | Expensed by user | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| external-src-data | External source data | | | | | yes | string(255) |
| external-src-name | External source name | | | | yes | yes | string(255) |
| external-src-ref | External source reference | | yes | | yes | yes | string(255) |
| foreign-currency | Foreign currency | yes | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| foreign-currency-amount | Foreign currency amount | | | | yes | yes | decimal(32,4) |
| foreign-currency-id | Foreign currency id | | | | yes | | integer |
| frugality | Frugality rating | | | shame, praise | | yes | string |
| has-preapproval | Does Expense Line has preapproval attached? | | | | | yes | boolean |
| id | Coupa unique identifier | | | | yes | yes | integer |
| integration | Corp card integration name | | | | | yes | [Integration](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)) |
| itemized-expense-lines | Itemized expense line | | | | yes | | [Itemized Expense Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/itemized-expense-line-api) |
| last-send-back-comment | Last comment why line was sent back | no | no | any | | yes | comment |
| last-send-back-reason | Last reason why line was sent back | no | no | any | | yes | reason-insight-event |
| line-number | Expense line number | | | | | yes | integer |
| merchant | Merchant | | | | yes | yes | string(255) |
| order-line-id | Order line id | | | | yes | yes | integer |
| over-limit | Over limit flag | | | | | yes | boolean |
| parent-expense-line-id | Parent expense line id | | | | | yes | integer |
| parent-external-src-data | Parent External Source Data | | | | | yes | string(255) |
| parent-external-src-name | Parent External Source Name | | | | | yes | string(255) |
| parent-external-src-ref | Parent External Source Ref | | | | | yes | string(255) |
| per-diem-trip | Expense Per-diem Trip Information | | | | | yes | [Expense Trip](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-trip-api) |
| period | Period | | | | yes | yes | [Period](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api) |
| reason | Reason | | | | yes | yes | string(255) |
| receipt-total-amount | Receipt total amount | | | | yes | yes | decimal(32,4) |
| receipt-total-currency-id | Receipt total currency id | | | | yes | yes | integer |
| reporting-total | Reporting total | | | | | yes | decimal(32,4) |
| requires-receipt | Requires receipt flag | | | | | yes | boolean |
| start-date | Divisor start date | yes | | | yes | yes | datetime |
| status | Transaction status | | | | | yes | string(255) |
| suggested-exchange-rate | Suggested exchange rate | | | | | yes | [Exchange Rate](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/exchange-rates-api-(exchange_rates)) |
| type | Type | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| employee-reimbursable-overridden | Has the expense user changed the default reimbursable state of an expense line? | | | | | yes | boolean |
| employee-reimbursable-editable | Can expense user change the default reimbursable state of an expense line? | | | | | yes | boolean |
| travel-trip-booking | Travel trip booking | | | | | yes | |
