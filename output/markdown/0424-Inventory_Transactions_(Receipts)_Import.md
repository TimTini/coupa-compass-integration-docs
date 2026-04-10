---
title: "Inventory Transactions (Receipts) Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/inventory-transactions-(receipts)-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/inventory-transactions-(receipts)-import"
status_code: 200
fetched_at: "2026-04-09T12:00:44+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Inventory Transactions (Receipts) Import"
---

# Inventory Transactions (Receipts) Import

## Overview

The inventory transactions (receipts) import process read files from the
`./Incoming/Receipts/` SFTP folder. These files will be moved to the
archive folder located at `./Incoming/Archive/Receipts/` before being
processed in alphanumeric order.

## Unique Keys/Validations

One of the following five sets of columns are required:

- ID

- Order Line ID and Order Line PO Number

- Order Line Number and Order Line PO ID

- Order Line ID

- Order Line PO Number and Order Line Number

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| ID | This is the unique identifier (database ID) Coupa assigns when a new record is created. It can’t be modified, but can be used to update the record. | TRUE* | TRUE | int(11) | any |
| Barcode | Barcode | FALSE | FALSE | string(255) | any |
| Currency | Transaction Currency Code | FALSE | FALSE | string(100) | any |
| Price | Transaction Price | FALSE | FALSE | decimal(30,6) | any |
| Quantity | Quantity Received in UOM | FALSE | FALSE | decimal(30,6) | any |
| RFID Tag | RFID Tag | FALSE | TRUE | string(255) | any |
| Type | Transaction Type | TRUE | FALSE | string(255) | InventoryReceipt, ReceivingConsumption, ReceivingAmountConsumption, ReceivingQuantityConsumption ReceivingReturnToSupplier, ReceivingAmountReturnToSupplier, ReceivingQuantityReturnToSupplier, ReceivingDisposal, ReceivingAmountDisposal, ReceivingQuantityDisposal |
| Order Line Id | Order Line Coupa Id Number | TRUE* | FALSE | int(11) | any |
| Order Line Number | Order Line Number | TRUE* | FALSE | string(255) | any |
| Order Line PO Id | Order Line PO Coupa Id Number | TRUE* | FALSE | int(11) | any |
| ASN Line Id | ASN Line Coupa Id | FALSE | FALSE | int(11) | any |
| ASN Line Number | ASN Line Coupa Number | FALSE | FALSE | string(255) | any |
| ASN Header Id | ASN Header Coupa Id | FALSE | FALSE | int(11) | any |
| ASN Header Number | ASN Header Coupa Number | FALSE | FALSE | string(40) | any |
| UOM Code | Unit of Measure Code | FALSE | FALSE | string(6) | any |
| Status | The status of the transaction. Default is created. | FALSE | FALSE | string(255) | any |
| Match Reference | Three-way match attribute to connect with Receipt and Invoice Header | FALSE | FALSE | string(255) | any |
| External Id | This is a custom field that Coupa creates to accommodate the ERP Id. See note below. | FALSE | FALSE | string(255) | any |
| Transaction Reference | ID of original transaction | FALSE | FALSE | integer | any |
| Reason Insight | Reason Insight Code | FALSE | FALSE | | any |

*One of the following five sets of columns are required:

- `ID`

- `Order Line ID`

- `Order Line ID` and `Order Line PO Number`

- `Order Line Number` and `Order Line PO ID`

- `Order Line Number` and `Order Line PO Number`

- `Order Line PO Number` and `Order Line Number`

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: For Receipts created through ERP, the
`External_ID` (the unique ERP number per transaction) should be populated
in Coupa, If the same receipt is required to be voided using integration, the same
`External_ID` field should be passed to Coupa for voiding the externally
integrated transaction.
