---
title: "Itemized Expense Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/itemized-expense-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/itemized-expense-line-api"
status_code: 200
fetched_at: "2026-04-09T11:59:46+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Itemized Expense Line API"
---

# Itemized Expense Line API

## Associations

This API resource is associated with [Expense Line Api](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

## Elements

The following elements are available for the Itemized Expense
Line API:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account | Account | | | | yes | yes | [Account](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)) |
| account-allocations | Account allocations | | | | yes | yes | [Expense Line Allocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-allocation-api) |
| accounting-total | Accounting total | | | | | yes | decimal(32,4) |
| accounting-total-currency | Accounting total currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| amount | Amount | | | | yes | yes | decimal(32,4) |
| approved-amount | Approved amount | | | | yes | yes | decimal(32,4) |
| audit-status | Audit status | | | | yes | yes | [Audit Status](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/audit-status-api) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [Users](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency of transaction | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| custom-field-1 | Custom field 1 | | | | yes | yes | string(255) |
| custom-field-10 | Custom field 10 | | | | yes | yes | string(255) |
| custom-field-11 | Custom field 11 | | | | yes | yes | string(255) |
| custom-field-12 | Custom field 12 | | | | yes | yes | string(255) |
| custom-field-13 | Custom field 13 | | | | yes | yes | string(255) |
| custom-field-14 | Custom field 14 | | | | yes | yes | string(255) |
| custom-field-15 | Custom field 15 | | | | yes | yes | string(255) |
| custom-field-16 | Custom field 16 | | | | yes | yes | string(255) |
| custom-field-17 | Custom field 17 | | | | yes | yes | string(255) |
| custom-field-18 | Custom field 18 | | | | yes | yes | string(255) |
| custom-field-19 | Custom field 19 | | | | yes | yes | string(255) |
| custom-field-2 | Custom field 2 | | | | yes | yes | string(255) |
| custom-field-20 | Custom field 20 | | | | yes | yes | string(255) |
| custom-field-3 | Custom field 3 | | | | yes | yes | string(255) |
| custom-field-4 | Custom field 4 | | | | yes | yes | string(255) |
| custom-field-5 | Custom field 5 | | | | yes | yes | string(255) |
| custom-field-6 | Custom field 6 | | | | yes | yes | string(255) |
| custom-field-7 | Custom field 7 | | | | yes | yes | string(255) |
| custom-field-8 | Custom field 8 | | | | yes | yes | string(255) |
| custom-field-9 | Custom field 9 | | | | yes | yes | string(255) |
| description | Description | | | | yes | yes | string(1550) |
| divisor | Divisor unit | | | | yes | yes | decimal(30,2) |
| end-date | Divisor end date | | | | yes | yes | datetime |
| exchange-rate | Exchange rate | | | | yes | yes | decimal(30,9) |
| expense-artifacts | Expense artifacts | | | | | yes | Expense Artifact |
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
| expense-date | Expense date | | | | yes | yes | datetime |
| expense-line-imported-data | Expense line imported data | | | | | yes | [ExpenseLineImportedData](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-imported-data-api) |
| expense-line-taxes | Expense line taxes | | | | | yes | [ExpenseLineTax](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-tax-api) |
| expense-report-id | Expense report id | | | | | yes | integer |
| expensed-by | Expensed by user | | | | yes | yes | [Users](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| external-src-data | External source data | | | | | yes | string(255) |
| external-src-name | External source name | | | | yes | yes | string(255) |
| external-src-ref | External source reference | | yes | | yes | yes | string(255) |
| foreign-currency | Foreign currency | yes | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| foreign-currency-amount | Foreign currency amount | | | | yes | yes | decimal(32,4) |
| foreign-currency-id | Foreign currency id | | | | yes | | integer |
| frugality | Frugality | | | | | yes | |
| id | Coupa unique identifier | | | | yes | yes | integer |
| integration | Corp card integration name | | | | | yes | [Integration](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)) |
| line-number | Expense line number | | | | | yes | |
| merchant | Merchant | | | | yes | yes | string(255) |
| order-line-id | Order line id | | | | yes | yes | integer |
| over-limit | Over limit flag | | | | | yes | boolean |
| parent-expense-line-id | Parent expense line id | | | | | yes | integer |
| parent-external-src-data | Parent External Source Data | | | | | yes | string |
| parent-external-src-name | Parent External Source Name | | | | | yes | string |
| parent-external-src-ref | Parent External Source Ref | | | | | yes | string |
| period | Period | | | | yes | yes | [Period](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api) |
| reason | Reason | | | | yes | yes | string(255) |
| receipt-total-amount | Receipt total amount | | | | yes | yes | decimal(32,4) |
| receipt-total-currency-id | Receipt total currency id | | | | yes | yes | integer |
| reporting-total | Reporting total | | | | | yes | decimal(32,4) |
| start-date | Divisor start date | yes | | | yes | yes | datetime |
| status | Transaction status | | | | | yes | string(255) |
| suggested-exchange-rate | Suggested exchange rate | | | | | yes | [Exchange Rate](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/exchange-rates-api-(exchange_rates)/exchange-rates-api-example-calls) |
| type | Type | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [Users](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| expense-attendees | Expense attendees | | | | yes | yes | [ExpenseAttendee](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-attendee-api) |
| per_diem_trip | Expense Per-diem Trip Information | | | | | yes | string |
| expense_trip | Expense trip | | | | yes | yes | [ExpenseTrip](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-trip-api) |
| expense_line_daily_per_diems | Daily per diems with amount information for each day | | | | | yes | ExpenseLineDailyPerDiem |
