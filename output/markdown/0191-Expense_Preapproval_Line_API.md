---
title: "Expense Preapproval Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-preapproval-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-preapproval-line-api"
status_code: 200
fetched_at: "2026-04-09T11:59:44+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Preapproval Line API"
---

# Expense Preapproval Line API

## Association

This resource is associated with [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Values** | **Api_In Field?** | **Api_Out Field?** | **Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | | | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| type | Type | | | | | yes | string(255) |
| estimated_amount | Estimated amount | | | | | yes | decimal(32,4) |
| requested_amount | Requested amount | | | | | yes | decimal(32,4) |
| accounting_total | Accounting total | | | | | yes | decimal(32,4) |
| estimated_reporting_total | Estimated reporting total | | | | | yes | decimal(32,4) |
| requested_reporting_total | Requested reporting total | | | | | yes | decimal(32,4) |
| notes | Notes | | | | | yes | text |
| estimated_amount_currency | Estimated amount currency | | | | | yes | |
| requested_amount_currency | Requested amount currency | | | | | yes | |
| accounting_total_currency | Accounting total currency | | | | | yes | |
| account_type | Account type | | | | | yes | |
| account | Account | | | | | yes | |
