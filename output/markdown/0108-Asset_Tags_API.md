---
title: "Asset Tags API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/asset-tags-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/asset-tags-api"
status_code: 200
fetched_at: "2026-04-09T11:59:27+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Asset Tags API"
---

# Asset Tags API

Use this API to specify asset tags on some transactional and reference objects.

## Associations

This API is associated with [Purchase Order Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961), and [Receiving Transactions API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/receiving-transactions-api-(receiving_transactions)).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| inventory-balance-id | inventory_balance_id | | | | yes | yes | integer |
| note | note | | | | yes | yes | text |
| order-line-id | order_line_id | | | | yes | yes | integer |
| owner | owner | | | | yes | yes | string(255) |
| received | received | | | | yes | yes | boolean |
| requisition-line-id | requisition_line_id | | | | yes | yes | integer |
| serial-number | serial number | | | | yes | yes | string(255) |
| tag | tag | | yes | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
