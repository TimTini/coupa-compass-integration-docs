---
title: "Expense Category API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-category-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-category-api"
status_code: 200
fetched_at: "2026-04-09T11:59:43+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Category API"
---

# Expense Category API

## Association

This resource is associated with [Expense Reports API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-reports-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | A false value will inactivate the account making it no longer available to users. A true value will make it active and available to users. | true, false | yes | yes | boolean | | |
| attendee-tracking-enabled | Attendee tracking enabled | | | true, false | | yes | boolean |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | yes | datetime | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| dynamic-category-limit-enabled | Dynamic category limit enabled | | | | | yes | boolean |
| expense-attendee-types | Expense attendee types | | | | | yes | [Expense Attendee Type](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-attendee-type-api) |
| expense-mileage-config | Expense mileage config | yes | | | | yes | Expense::Mileage::Config |
| expense-per-diem-config | Expense per diem config | yes | | | | yes | Expense::PerDiem::Config |
| expense-policy | expense_policy | yes | | | | yes | Expense Policy |
| external_key | External expense category unique identifier | no | no | any | yes | yes | |
| group | Group | | | | | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| localized-group | | | | any | | yes | string(255) |
| name | name | yes | yes | | yes | yes | string(255) |
| scope | Scope | no | no | | | yes | string(255) |
| tax_currencies | | no | no | any | | yes | [] |
| tax-enabled | Tax enabled | | | | | yes | boolean |
| translated_name | Translation of the expense category name | no | no | any | | yes | |
| type | Type | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | yes | datetime | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
