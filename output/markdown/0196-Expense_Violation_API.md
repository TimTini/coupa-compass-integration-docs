---
title: "Expense Violation API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-violation-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-violation-api"
status_code: 200
fetched_at: "2026-04-09T11:59:46+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Violation API"
---

# Expense Violation API

## Elements

| **Element** | **Description** | **Type** | **API In** | **API Out** | **Required** | **Length** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | datetime | | yes | | | |
| created-by | User who created | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) | | yes | | | |
| id | Coupa unique identifier | integer | | yes | | | |
| limit-exceeded | Limit exceeded | decimal(32,4) | | yes | | | |
| receipt-missing | Receipt missing | boolean | | yes | | | |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | datetime | | yes | | | |
| updated-by | User who updated | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) | | yes | | | |
| violable | Violable | | | yes | | | |
| violator | Violator | ExpenseLine | | yes | | | |
