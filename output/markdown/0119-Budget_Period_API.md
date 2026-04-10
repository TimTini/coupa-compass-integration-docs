---
title: "Budget Period API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api"
status_code: 200
fetched_at: "2026-04-09T11:59:29+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Budget Period API"
---

# Budget Period API

Use this API to specify the budget period on some transactional objects.

## Associations

This API is associated with [Budget Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/budget-lines-api-(budget-lines)), [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api), [Purchase Order Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961), and [Invoice Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-line-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account-type | account_type | | | | yes | yes | [AccountType](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | yes | yes | datetime | | | |
| created-by | User who created | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| end-date | end_date | yes | | | yes | yes | datetime |
| id | Coupa unique identifier | | | | yes | yes | integer |
| is-open | is_open | | | | yes | yes | boolean |
| name | name | yes | yes | | yes | yes | string(100) |
| segment-1 | segment_1 | | | | yes | yes | boolean |
| segment-10 | segment_10 | | | | yes | yes | boolean |
| segment-11 | segment_11 | | | | yes | yes | boolean |
| segment-12 | segment_12 | | | | yes | yes | boolean |
| segment-13 | segment_13 | | | | yes | yes | boolean |
| segment-14 | segment_14 | | | | yes | yes | boolean |
| segment-15 | segment_15 | | | | yes | yes | boolean |
| segment-16 | segment_16 | | | | yes | yes | boolean |
| segment-17 | segment_17 | | | | yes | yes | boolean |
| segment-18 | segment_18 | | | | yes | yes | boolean |
| segment-19 | segment_19 | | | | yes | yes | boolean |
| segment-2 | segment_2 | | | | yes | yes | boolean |
| segment-20 | segment_20 | | | | yes | yes | boolean |
| segment-3 | segment_3 | | | | yes | yes | boolean |
| segment-4 | segment_4 | | | | yes | yes | boolean |
| segment-5 | segment_5 | | | | yes | yes | boolean |
| segment-6 | segment_6 | | | | yes | yes | boolean |
| segment-7 | segment_7 | | | | yes | yes | boolean |
| segment-8 | segment_8 | | | | yes | yes | boolean |
| segment-9 | segment_9 | | | | yes | yes | boolean |
| start-date | start_date | yes | | | yes | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | yes | yes | datetime | | | |
| updated-by | User who updated | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
