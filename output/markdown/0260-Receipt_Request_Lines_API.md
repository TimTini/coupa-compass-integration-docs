---
title: "Receipt Request Lines API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipt-requests-api-(receipt_requests)/receipt-request-lines-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipt-requests-api-(receipt_requests)/receipt-request-lines-api"
status_code: 200
fetched_at: "2026-04-09T11:59:59+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Receipt Requests API (/receipt_requests)"
  - "Receipt Request Lines API"
---

# Receipt Request Lines API

## Associations

This resource is associated with [Receipt Requests API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipt-requests-api-(receipt_requests)).

## Receipt Request Line Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | | any | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| type | Type | | | any | | yes | string(255) |
| receipt_type | Receipt type | | | any | | yes | string |
| receipt_date | Receipt date | | | any | | yes | datetime |
| quantity | Quantity | | | any | | yes | decimal(30,6) |
| price | Price | | | any | | yes | decimal(30,6) |
| weight | Weight | | | any | | yes | decimal(30,6) |
| soft_close_for_receiving | Soft close PO after receiving | | | any | | yes | boolean |
| inventory_transaction_id | Inventory Transaction id | | | any | | yes | integer |
| warehouse | Warehouse | | | any | | yes | |
| warehouse_location | Warehouse Location | | | any | | yes | |
| order_line | Order line | | | any | | yes | |
| item | Item | | | any | | yes | |
| uom | Unit of Measure | | | any | | yes | |
| currency | Currency | | | any | | yes | |
| on_behalf_of | On behalf of user | | | any | | yes | |
| asn_line | Asn Line id | | | any | | yes | |
