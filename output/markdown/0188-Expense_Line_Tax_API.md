---
title: "Expense Line Tax API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-tax-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-tax-api"
status_code: 200
fetched_at: "2026-04-09T11:59:44+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Line Tax API"
---

# Expense Line Tax API

## Association

This resource is associated with [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | Amount | | | | | yes | decimal(32,4) |
| country | Country | | | | | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | integer |
| currency-id | Currency | | | | | yes | integer |
| entry_type | Entry type | no | no | any | | yes | integer |
| id | Coupa unique identifier | | | | | yes | integer |
| std-amount | Std amount | | | | | yes | decimal(32,4) |
| tax-code | tax code | | | | | yes | Tax Code |
| tax-rate | Tax rate | | | | | yes | [Tax Rate](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-api) |
| tax-rate-type | Tax rate type | | | | | yes | [Tax Rate Type](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-type-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | integer |
