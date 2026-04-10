---
title: "Inventory Balance Lot Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/inventory-balance-lot-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/inventory-balance-lot-import"
status_code: 200
fetched_at: "2026-04-09T12:00:40+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Inventory Balance Lot Import"
---

# Inventory Balance Lot Import

## Overview

The Inventory Balance Lot import process reads files from
`./Incoming/InventoryBalanceLot/` SFTP folder. These files will be moved to
the archive folder located at `./Incoming/Archive/InventoryBalanceLot/`
before being processed in alpha-numeric order.

## Keys and Validations

`Item number` is the unique identifier.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Warning: The bulk loader doesn't support modifying the
on-hand balance with items that have a quantity of 0 and a price of $0.

## Inventory Balance Lot

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Balance | No | No | | Type of row - Balance | |
| Item Number | No | No | | Item Number | |
| Item Name | No | No | | Item Name | |
| Warehouse | No | No | | Warehouse Name | |
| Aisle | No | No | | Warehouse Location Aisle | |
| Bin | No | No | | Warehouse Location Bin | |
| Level | No | No | | Warehouse Location Level | |
| Quantity | Yes | No | decimal(32,4) | Quantity | |
| UOM | Yes | No | | Unit of Measure | |
| Price | No | No | | Price | |
| Currency | No | No | | Currency | |
| Lot | No | No | | Lot | |
| Lot Number | No | No | | Lot Number | |
| Expiration Date | No | No | | Lot Expiration Date | |

## Inventory lot columns

| **Column** | **Description** | **Hidden** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| Lot | Indicates the row type. Required if the item has lot tracking enabled. | false | true | false | - | Lot |
| Lot Number | Lot Number. Required if the item has lot tracking enabled. | false | true | false | string(255) | Any |
| Quantity | Lot quantity. Required if the item has lot tracking enabled. | false | true | false | decimal(32,4) | Any |
| Expiration Date | Lot Expiration Date | false | false | false | date | Any |
