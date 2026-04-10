---
title: "Cycle Count Line Lot API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/cycle-count-line-lot-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/cycle-count-line-lot-api"
status_code: 200
fetched_at: "2026-04-09T11:59:27+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Cycle Count Line Lot API"
---

# Cycle Count Line Lot API

## Associations

This resource is available through the [Cycle Count Line API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/cycle-count-lines-api-(cycle_count_lines)).

## Elements

| **Name** | **Description** | **Req'd** | **Unique** | **Allowable Values** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| balance-quantity | Balance Quantity | | | | | yes | decimal(32,4) |
| consumption-quantity | Quantity in consumption uom | | | | yes | yes | decimal(32,4) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| cycle-count-line-id | Cycle count line identifier | | | | | yes | integer |
| id | Coupa unique identifier | | | | | yes | integer |
| inventory-lot | Inventory Lot | yes | yes | | | yes | InventoryLot |
| inventory-lot-id | Inventory lot | | | | yes | yes | integer |
| inventory-lot-number | Inventory lot number | | | | yes | | |
| order-quantity | Quantity in order uom | | | | yes | yes | decimal(32,4) |
| quantity | Quantity | yes | | | yes | yes | decimal(32,4) |
| uom | Uom | yes | | | | yes | [Uom](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| uom-id | Uom Identifier | | | | yes | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
