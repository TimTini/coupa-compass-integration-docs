---
title: "Expense Category Translation API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-category-translation-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-category-translation-api"
status_code: 200
fetched_at: "2026-04-09T11:59:43+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Category Translation API"
---

# Expense Category Translation API

## Association

This resource is associated with [Expense Category Translations](https://compass.coupa.com/x304265.xml).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Values** | **In** | **Out** | **Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| locale | Locale of this translation | true | false | any | yes | yes | string(255) |
| name | Translation of the expense category name | true | true | any | yes | yes | string(255) |
| expense_category_id | Coupa unique identifier of expense category which is associated with the translation | true | true | any | yes | yes | integer |
| id | Coupa unique identifier | false | false | any | yes | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| created_by | User who created | false | false | any | yes | yes | |
| updated_by | User who updated | false | false | any | yes | yes | |
