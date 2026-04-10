---
title: "Expense Line Imported Data API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-imported-data-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-imported-data-api"
status_code: 200
fetched_at: "2026-04-09T11:59:43+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Line Imported Data API"
---

# Expense Line Imported Data API

## Association

This resource is associated with [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | amount | | | | | yes | decimal(32,4) |
| description | description | | | | | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| local-amount-different | | | | | | yes | boolean |
| local-amount | | | | | | yes | decimal(32,4) |
| local-amount-currency | | | | | | yes | |
