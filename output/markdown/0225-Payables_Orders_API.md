---
title: "Payables/Orders API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payablesorders-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payablesorders-api"
status_code: 200
fetched_at: "2026-04-09T11:59:52+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Payables API (/payables/)"
  - "Payables/Orders API"
---

# Payables/Orders API

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/payables/orders` | index | Query Orders |
| PATCH | `/api/payables/orders/:id/pay_externally` | pay_externally | Mark Order as Paid Externally |
| PATCH | `/api/payables/orders/:id/ready_to_pay` | ready_to_pay | Mark Order as Ready to Pay |
| GET | `/api/payables/orders/:id` | show | Show Order |

## Elements

Keys: `id`

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| accounting-total | Order Total in the accounting currency | | | | | yes | decimal |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency | | | | | yes | Currency |
| exported | Has the Order been exported | | | | | yes | boolean |
| id | Coupa unique identifier | | | | | yes | integer |
| last-exported-at | Date the order was marked exported | | | | | yes | datetime |
| milestone-id | ID of associated milestone | | | | | yes | integer |
| paid-date | OrderPaid Date | | | | | yes | datetime |
| paid-total | Order Paid Total | | | | | yes | decimal |
| reconciliation-lines | Reconciliation lines | | | | | yes | Payables/Order/ReconciliationLine |
| remaining-total | Total Remaining amount | | | | | yes | decimal |
| remittance-total | Total Remittance amount | | | | | yes | decimal |
| status | Order Status | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
