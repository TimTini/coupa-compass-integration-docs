---
title: "Inventory Transaction Lot API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/inventory-transaction-lot-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/inventory-transaction-lot-api"
status_code: 200
fetched_at: "2026-04-09T11:59:58+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Receipts API"
  - "Inventory Transaction Lot API"
---

# Inventory Transaction Lot API

## Associations

This resource is associated with [Receipts API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| adjustment-code | Adjustment code | | | | | yes | AdjustmentCode |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| inventory-lot | Inventory lot | yes | yes | | yes | yes | InventoryLot |
| inventory-lot-id | Inventory lot | | | | yes | | integer |
| quantity | Quantity | yes | | | yes | yes | decimal(32,4) |
| uom | Unit of Measure | yes | | | | yes | Uom |
| uom-id | Uom | | | | yes | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
