---
title: "Expense Line Cash Advance API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-cash-advance-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-cash-advance-api"
status_code: 200
fetched_at: "2026-04-09T11:59:43+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Line Cash Advance API"
---

# Expense Line Cash Advance API

## Association

This resource is associated with [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

## Expense Line Cash Advance Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | | any | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| amount | Original preapproved amount | | | any | | yes | decimal(32,4) |
| currency | Original preapproved currency | | | any | | yes | |
