---
title: "Payables/Order Reconciliation Lines API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payablesorder-reconciliation-lines-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payablesorder-reconciliation-lines-api"
status_code: 200
fetched_at: "2026-04-09T11:59:53+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Payables API (/payables/)"
  - "Payables/Order Reconciliation Lines API"
---

# Payables/Order Reconciliation Lines API

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/payables/order/reconciliation_lines` | create | /api/payables/order/reconciliation_lines |
| GET | `/api/payables/order/reconciliation_lines` | index | /api/payables/order/reconciliation_lines |
| GET | `/api/payables/order/reconciliation_lines/:id` | show | /api/payables/order/reconciliation_lines/:id |

## Elements

Key: `id`

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| adjustment-date | Adjustment Date (Payment Date) | | | | yes | | datetime |
| amount | Amount | | | | yes | | decimal(30,6) |
| amount-paid | Amount | | | | | yes | decimal(30,6) |
| category | Category | | | | yes | | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| note | Payment Note | | | | yes | | string(255) |
| notes | Payment Note | | | | | yes | string(255) |
| payable-id | Milestone ID | | | | yes | yes | integer |
| payable-type | Payable Type | | | | | yes | string |
| payment-date | Adjustment Date (Payment Date) | | | | | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
