---
title: "Order Line Confirmations API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/order-confirmations-api-(order_header_confirmations)/order-line-confirmations-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/order-confirmations-api-(order_header_confirmations)/order-line-confirmations-api"
status_code: 200
fetched_at: "2026-04-09T11:59:51+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Order Confirmations API (/order_header_confirmations)"
  - "Order Line Confirmations API"
---

# Order Line Confirmations API

Use the Order Confirmations API to access Order Line Confirmations.

## Elements

The Order Line Confirmations API contains the following elements:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| action | Action | | | | yes | | |
| can-fulfill | Can fulfill | | | | | yes | integer |
| confirm-by-hrs | Confirm by hrs | | | | | yes | decimal(10,0) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency | | | | | yes | OrderLineConfirmation |
| id | Coupa unique identifier | | | | | yes | integer |
| item-change | Item change | | | | | yes | boolean |
| item_record_match_found | Item record match found | | | | | yes | |
| line-num | Line num | | | | | yes | |
| order-line | order line | | | | | yes | OrderLineConfirmation |
| price | Price | yes | | | | yes | decimal(30,6) |
| promised-date | Promised date | | | | | yes | datetime |
| promised-deliveries | Promised deliveries | | | | | yes | integer |
| quantity | Quantity | yes | | | | yes | decimal(30,6) |
| reason-insight-events | Reason insight events | | | | yes | yes | ReasonInsightEvent |
| schedule-lines | Schedule lines | | | | | yes | OrderLineConfirmation |
| status | Status | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
