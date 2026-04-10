---
title: "Expense Preapproval API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-preapproval-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-preapproval-api"
status_code: 200
fetched_at: "2026-04-09T11:59:44+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Preapproval API"
---

# Expense Preapproval API

## Association

This resource is associated with [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

## Elements

| **Field Name** | **Field Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api-In Field?** | **Api-Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | Original preapproved amount | yes | | | | yes | decimal(32,4) |
| available | A flag to show the availability & validity of this preapproval | | | | | yes | boolean |
| available-amount | Remaining preapproved amount | | | | | yes | decimal(32,4) |
| available-amount-currency | Remaining preapproved currency | | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created preapproval request | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Original preapproved currency | | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| description | Additional information for preapproval request | yes | | | | yes | string(255) |
| easy-form-widget-responses | Easy form widget responses | | | | | yes | |
| end-date | End date | | | | | yes | datetime |
| expense-cash-advance | Expense Cash Advance | | | | | yes | |
| expense-cash-advance | Expense Cash Advance | | | | | yes | |
| expense-preapproval-lines | Expense preapproval lines | | | | | yes | |
| expense-virtual-card | Expense Virtual Card | | | | | yes | |
| for-user | User who requested expense preapproval | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| start-date | Start date | | | | | yes | datetime |
| type | Type of preapproval request (trip, cash advance, gifts, entertainment) | no | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who last updated preapproval request | | | | | yes | integer |
