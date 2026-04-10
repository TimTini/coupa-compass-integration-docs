---
title: "Inventory Adjustments API (/inventory_adjustments)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/inventory-adjustments-api-(inventory_adjustments)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/inventory-adjustments-api-(inventory_adjustments)"
status_code: 200
fetched_at: "2026-04-09T11:59:57+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Receipts API"
  - "Inventory Adjustments API (/inventory_adjustments)"
---

# Inventory Adjustments API (/inventory_adjustments)

The URL to access inventory adjustments
is: `https:///api/inventory_adjustments`

## Associations

This resource is associated with [Receipts API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api).

## Actions

Inventory Adjustments allow you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/inventory_adjustments` | create | Create inventory adjustment |
| GET | `/api/inventory_adjustments` | index | Query inventory adjustment |
| GET | `/api/inventory_adjustments/:id` | show | Show inventory adjustment |
| PATCH | `/api/inventory_adjustments/:id` | update | Update inventory adjustment export flag only |
| PUT | `/api/inventory_adjustments/:id` | update | Update inventory adjustment export flag only |

The **Type** payload for `/api/inventory_adjustments` includes:

```text
"InventoryAdjustment"
```

For more information about the Inventory Adjustments API payload, see [Receipts API Example Calls](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/receipts-api-example-calls).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account | Receipt Account Code | | | | yes | yes | [Account](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)) |
| account-allocations | account_allocations | | | | yes | yes | Inventory Transaction Allocation |
| adjustment-code | Adjustment code | no | no | any | yes | yes | Adjustment Code |
| asn-header | ASN Header | | | | | yes | [Asn/Header](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/advance-ship-notices-api-(asn)) |
| asn-line | ASN Line | | | | yes | yes | [Asn/Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/advance-ship-notices-api-(asn)/asn-lines-api) |
| asset-tags | Semi Colon seperated list of Asset Tag Identifiers | | | | | yes | [Asset Tag](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/asset-tags-api) |
| attachments | attachments | | | | | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| barcode | Barcode Value | | | | yes | yes | string(255) |
| comments | Comments for voiding transaction | no | no | any | | yes | text |
| created-at | Time of Inventory Transaction Creation | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | currency code | no | no | any | yes | | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| current-integration-history-records | Current integration history records | | | | | yes | [Integration History Record](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-history-record-api) |
| exported | Indicates if transaction has been exported | | | | yes | yes | boolean |
| from-warehouse | Warehouse ID | | | | yes | | Warehouse |
| from-warehouse-location | Coupa's Internal From-Warehouse-Location ID | | | | yes | yes | Warehouse Location |
| id | Coupa's Internal Inventory Transaction ID | | | | | yes | integer |
| inspection-code | Inspection Code | | | | yes | yes | Inspection Code |
| inventory-transaction-valuations | Inventory Transaction Valuations | | | | | yes | Inventory Transaction Valuation |
| item | item | | | | yes | yes | [Item](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)) |
| last-exported-at | Date and time transaction was last exported in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| match-reference | Three-way match attribute to connect with Receipt and ASN Line | | | | yes | yes | string(255) |
| order-line | Item Number | | | | yes | yes | [Order Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961) |
| original_transaction | Displays any custom fields associated with the original receipt when creating a return or void. | | | | | yes | |
| original_transaction_id | ID of the original transaction, when the transaction is partially voided | no | no | any | | yes | integer |
| price | Item Price | | | | yes | yes | decimal(30,6) |
| quantity | Receipt Quantity | | | | yes | yes | decimal(30,6) |
| reason_insight | Voiding reason | no | no | any | | yes | |
| receipt | receipt | | | | yes | | Receipt |
| receipts-batch-id | Receipts Batch ID | | | | | yes | integer |
| received-weight | Inventory Transaction Received Weight | | | | yes | yes | decimal(30,6) |
| receiving-form-response | receiving_form_response | | | | yes | | [Form Response](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/form-api) |
| rfid-tag | RFID Tag Value | yes | | | yes | yes | string(255) |
| soft-close-for-receiving | Soft close PO line for Receiving | | | | yes | | boolean |
| status | Inventory Transaction Status | | | | | yes | string(255) |
| to-warehouse | Warehouse ID | | | | yes | | Warehouse |
| to-warehouse-location | Coupa's Internal To-Warehouse-Location ID | | | | yes | yes | Warehouse Location |
| total | Receipt Total | | | | yes | yes | decimal(30,6) |
| transaction-date | Actual date of transaction | | | | yes | yes | datetime |
| type | Inventory Transaction Type | yes | | | yes | yes | string(255) |
| uom | Unit of Measure Code | | | | yes | yes | [Uom](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| updated-at | Time of Inventory Transaction Updation | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| voided_value | Total quantity/amount that was voided | no | no | any | | yes | decimal(30,6) |
| inventory_transaction_lots | | | | any | yes | | [] |
| notes | Notes for Inventory Adjustments | | | any | yes | | string(255) |
