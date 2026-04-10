---
title: "Item Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/item-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/item-import"
status_code: 200
fetched_at: "2026-04-09T12:00:40+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Item Import"
---

# Item Import

## Overview

The Items Import process read files from `./Incoming/Items/` in the SFTP. These files will be moved to the archive folder located at`./Incoming/Archive/Items/` before being processed in alphanumeric order.

## Unique Keys

- Item ID

- Item Number

- Item Name

Supplier Item uniqueness is based on a combination of `Supplier`, `Supplier Part Num`, and `Contract`.

## Validations

You can use the SFTP loader to update:

- `Item Name` using `Item Number`.

- `Item Number` using the `Item Name`.

- `Item Name` and `Item Number` by including both `Supplier` and `Supplier Part Num`.

For supplier items, depending on the Item loader you use, we do a lookup based on:

- `Item Number` or `Name` plus `Supplier` (Standard or Background loader through the UI) or `Item Number` (Standard loader).

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: You cannot update `Contract Number` or `Supplier Part Num` on a supplier item.

## Item finder logic

Catalog Items are found with the following query terms, in the following order. If a match is found, that item is returned and Coupa stops searching.

- `Item Number` can only match on one item.

- `Manufacturer Name` and `Manufacturer Part Number` return the first created matched item.

- `Supplier Part Number` and `Supplier Aux Part Number` (and `Contract` if present) return the last updated matched item.

- `Catalog Item Name` returns last updated matched item.

If `Supplier Part Number` and/or `Supplier Aux Part Number` are provided, Coupa first searches for an item with attached `Supplier Item` that matches the provided attributes. This is necessary in cases where the instance is configured with multiple Items with the same `Item Name`, but different associated `Supplier Item`. If no match is found with a joined query, a query with only item details are used as a fallback.

`Supplier Part Number` (and `Supplier Aux Part Number`) default to the requisition or order line if provided in CSV. If the `Supplier Item` exists, `Supplier Part Number` (and `Supplier Aux Part Number`) default from the Supplier Item. `Supplier Part Number` (and `Supplier Aux Part Number`) in CSV are used to try to find a supplier item.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: For `Supplier Item` custom fields, add the prefix `Supplier Item` before custom field name in the CSV file.

Example:

- Custom field name: `Warehouse`

- Field name in CSV file: `Supplier Item Warehouse`

## Item

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name* | Yes | No | string(255) | Item Short Name | |
| Description* | Yes | No | text | Full Item Description | |
| UOM Code | No | No | | A valid UOM code that has already been configured in Coupa | |
| Purchasable | No | No | | If the item is currently purchasable or not | |
| Active* | Yes | No | boolean | Existing supplier items will be destroyed if set to No | |
| Purchasing Questionnaire | No | No | | Purchasing Questionnaire Name that has already been configured in Coupa | |
| RFQ Questionnaire | No | No | | Request for Quote Questionnaire Name that has already been configured in Coupa | |
| Receiving Questionnaire | No | No | | Receiving Questionnaire Name that has already been configured in Coupa | |
| Item Number | No | Yes | string(255) | Item Identification Number | |
| Item Classification | No | No | | Item Classification Name that has already been configured in Coupa | |
| Image Url | No | No | string | A valid and publically accessible URL where a product image can be downloaded from | |
| Image Filename | No | No | | relative path to image filename included in uploaded zipfile | |
| Commodity | No | No | | Commodity Name for the item | |
| Tags | No | No | | Item Tags. Separate tags with spaces. For tags with more than one word, surround the tag in double quotations. | |
| Supplier | No | No | | Supplier Name. Must Exist in Coupa | |
| Supplier Number | No | No | | Supplier Number. Must Exist in Coupa | |
| Preferred | No | No | | If the Supplier is a preferred supplier | |
| Contract Number | No | No | | Contract Number. Must exist in coupa | |
| Item Access Groups | No | No | | Comma separated Item Access Groups | |
| Pricing Type | No | No | | How the Inventory Valuation should be calculated (Fixed Price, Inventory) | |
| Price | No | No | | Item price for supplier | |
| Currency | No | No | | Item price currency. Must exist and be active in Coupa. | |
| Supplier Part Num | No | No | | Supplier Part Numer | |
| Supplier Aux Part Num | No | No | | Supplier Auxiliary Part Number | |
| Lead Time | No | No | | Items Lead Time in Days | |
| Manufacturer | No | No | | Manufacturer name | |
| Savings % | No | No | | Savings % | |
| Minimum Order Quantity | No | No | | Supplier Minimum Order Quantity | |
| Order Increment | No | No | | Supplier Order Increment | |
| Availability | No | No | | Availability | |
| Availability Date | No | No | | Availability Date | |
| Require Inspection | No | No | boolean | Does the item require inspection to be received? | |
| Require Asset Tag | No | No | boolean | Does the item require an Asset Tag to be received? | |
| Require RFID | No | No | | Does the item require an RFID? | |
| Storage Quantity | No | No | integer | Quantity in which to hold items in inventory | |
| Storage UOM | No | No | | UOM in which to hold items in inventory | |
| Consumption Quantity | No | No | integer | Quantity in which to consume items | |
| Consumption UOM | No | No | | UOM in which to consume items | |
| Use Pack Weight | No | No | boolean | Has the item calculate with the Pack Weight instead of item weight | |
| Pack Quantity | Yes | No | decimal(30,6) | Quanitity of items in a pack | |
| Pack Weight | Yes | No | decimal(30,6) | The weight of one pack | |
| Pack Weight UOM | No | No | | The UOM for a Pack | |
| Receive Catch Weight | No | No | boolean | Forces the item to be received as catch weight | |
| UNSPSC Code | No | No | | United Nations Standard Products and Services Code | |
| Contract Term | No | No | | The Contract Term by which the pricing tier is decided. Created beforehand in Coupa | |
| Allow Partial Qty | No | No | boolean | If this item allows for partial quantities | |
| Require Barcode | No | No | | Does the item require a barcode? | |
| Inventory Lot Tracking Enabled | No | No | boolean | Allow item to suport lot tracking information | |
| Inventory Lot Expiration Type | No | No | string | Set expiration type for item | |
| Supplier Item Purchasable | No | No | | If the supplier item is currently purchasable or not | |
| Manufacturer Name | Yes | No | string(255) | Manufacturer name for unique identification of item with manufacturer part number | |
| Manufacturer Part Number | No | Yes | string(255) | Manufacturer part number for unique identification of item with manufacturer name | |
| Coupa Internal Number | No | No | | Coupa Internal Number for unique identification of an item | |
| Coupa Supplier Internal Number | No | No | | Coupa Supplier Internal Number for unique identification of a supplier item | |
| Catalog | No | No | | Catalog name to look for supplier items with this catalog | |
| Sustainability | No | No | | Sustainability | |
| Sustainability URL | No | No | | Sustainability URL | |
| Link 0 Title | No | No | | If adding URL Links, This is the Title of the Link | |
| Link 0 URL | No | No | | If adding URL Links, This is the URL of the Link | |
| Link 1 Title | No | No | | If adding URL Links, This is the Title of the Link | |
| Link 1 URL | No | No | | If adding URL Links, This is the URL of the Link | |
| Link 2 Title | No | No | | If adding URL Links, This is the Title of the Link | |
| Link 2 URL | No | No | | If adding URL Links, This is the URL of the Link | |
| Link 3 Title | No | No | | If adding URL Links, This is the Title of the Link | |
| Link 3 URL | No | No | | If adding URL Links, This is the URL of the Link | |
| Link 4 Title | No | No | | If adding URL Links, This is the Title of the Link | |
| Link 4 URL | No | No | | If adding URL Links, This is the URL of the Link | |
| Link 5 Title | No | No | | If adding URL Links, This is the Title of the Link | |
| Link 5 URL | No | No | | If adding URL Links, This is the URL of the Link | |
| Image 0 Url | No | No | | If adding images, This is a valid and publically accessible URL for an image | |
| Image 1 Url | No | No | | If adding images, This is a valid and publically accessible URL for an image | |
| Image 2 Url | No | No | | If adding images, This is a valid and publically accessible URL for an image | |
| Image 3 Url | No | No | | If adding images, This is a valid and publically accessible URL for an image | |
| Image 4 Url | No | No | | If adding images, This is a valid and publically accessible URL for an image | |
| Image 5 Url | No | No | | If adding images, This is a valid and publically accessible URL for an image | |
| Price (Tier 1) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 2) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 3) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 4) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 5) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 6) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 7) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 8) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 9) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 10) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 11) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 12) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 13) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 14) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 15) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 16) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 17) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 18) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 19) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |
| Price (Tier 20) | No | No | | Price at different contract spend tiers. Typically goes down as more items are purchased | |

## Item History

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Action | No | No | | Action For History | |
| Created By | No | No | | Created By | |
| Created At | No | No | | Created At | |
| Item | No | No | | Item | |
| Item Name | No | No | | Item Name | |
| Item Uom | No | No | | Item Uom | |
| Item Image | No | No | | Item Image | |
| Item Item Number | No | No | | Item Item Number | |
| Item Reorder Point | No | No | | Item Reorder Point | |
| Item Require Inspection | No | No | | Item Require Inspection | |
| Item Require Asset Tag | No | No | | Item Require Asset Tag | |
| Item Require Rfid | No | No | | Item Require Rfid | |
| Item Require Barcode | No | No | | Item Require Barcode | |
| Item Allow Partial Quantity | No | No | | Item Allow Partial Quantity | |
| Item Receiving form | No | No | | Item Receiving form | |
| Item Commodity | No | No | | Item Commodity | |
| Item Product Reviews Count | No | No | | Item Product Reviews Count | |
| Item Avg rating | No | No | | Item Avg rating | |
| Item Created By | No | No | | Item Created By | |
| Item Created At | No | No | | Item Created At | |
| Item Updated By | No | No | | Item Updated By | |
| Item Updated At | No | No | | Item Updated At | |
| Item Description | No | No | | Item Description | |
| Item Active | No | No | | Item Active | |
| Item Image File Name | No | No | | Item Image File Name | |
| Item Image Content Type | No | No | | Item Image Content Type | |
| Item Image File Size | No | No | | Item Image File Size | |
| Item Custom Field 1 | No | No | | Item Custom Field 1 | |
| Item Custom Field 2 | No | No | | Item Custom Field 2 | |
| Item Custom Field 3 | No | No | | Item Custom Field 3 | |
| Item Custom Field 4 | No | No | | Item Custom Field 4 | |
| Item Custom Field 5 | No | No | | Item Custom Field 5 | |
| Item Custom Field 6 | No | No | | Item Custom Field 6 | |
| Item Custom Field 7 | No | No | | Item Custom Field 7 | |
| Item Custom Field 8 | No | No | | Item Custom Field 8 | |
| Item Custom Field 9 | No | No | | Item Custom Field 9 | |
| Item Custom Field 10 | No | No | | Item Custom Field 10 | |
| Item Connect Item | No | No | | Item Connect Item | |
| Item Imported From Connect | No | No | | Item Imported From Connect | |
| Item Custom Field 11 | No | No | | Item Custom Field 11 | |
| Item Custom Field 12 | No | No | | Item Custom Field 12 | |
| Item Custom Field 13 | No | No | | Item Custom Field 13 | |
| Item Custom Field 14 | No | No | | Item Custom Field 14 | |
| Item Custom Field 15 | No | No | | Item Custom Field 15 | |
| Item Custom Field 16 | No | No | | Item Custom Field 16 | |
| Item Custom Field 17 | No | No | | Item Custom Field 17 | |
| Item Custom Field 18 | No | No | | Item Custom Field 18 | |
| Item Custom Field 19 | No | No | | Item Custom Field 19 | |
| Item Custom Field 20 | No | No | | Item Custom Field 20 | |
| Item Catalog | No | No | | Item Catalog | |
| Item Type | No | No | | Item Type | |
| Item Original Item | No | No | | Item Original Item | |
| Item Form | No | No | | Item Form | |
| Item Other Fields Changed Count | No | No | | Item Other Fields Changed Count | |
| Supplier Item | No | No | | Supplier Item | |
| Supplier Item Supplier | No | No | | Supplier Item Supplier | |
| Supplier Item Contract | No | No | | Supplier Item Contract | |
| Supplier Item Price | No | No | | Supplier Item Price | |
| Supplier Item Currency | No | No | | Supplier Item Currency | |
| Supplier Item Part Num | No | No | | Supplier Item Part Num | |
| Supplier Item Supplier Aux Part Num | No | No | | Supplier Item Supplier Aux Part Num | |
| Supplier Item Lead time | No | No | | Supplier Item Lead time | |
| Supplier Item Preferred Flag | No | No | | Supplier Item Preferred Flag | |
| Supplier Item Manufacturer | No | No | | Supplier Item Manufacturer | |
| Supplier Item Created By | No | No | | Supplier Item Created By | |
| Supplier Item Created At | No | No | | Supplier Item Created At | |
| Supplier Item Updated By | No | No | | Supplier Item Updated By | |
| Supplier Item Updated At | No | No | | Supplier Item Updated At | |
| Supplier Item Reporting Price | No | No | | Supplier Item Reporting Price | |
| Supplier Item Connect Supplier Item | No | No | | Supplier Item Connect Supplier Item | |
| Supplier Item Catalog | No | No | | Supplier Item Catalog | |
| Supplier Item Price Change | No | No | | Supplier Item Price Change | |
| Supplier Item Savings Pct | No | No | | Supplier Item Savings Pct | |
| Supplier Item Contract Term | No | No | | Supplier Item Contract Term | |
| Supplier Item Price Tier 1 | No | No | | Supplier Item Price Tier 1 | |
| Supplier Item Price Tier 2 | No | No | | Supplier Item Price Tier 2 | |
| Supplier Item Price Tier 3 | No | No | | Supplier Item Price Tier 3 | |
| Supplier Item Price Tier 4 | No | No | | Supplier Item Price Tier 4 | |
| Supplier Item Price Tier 5 | No | No | | Supplier Item Price Tier 5 | |
| Supplier Item Price Tier 6 | No | No | | Supplier Item Price Tier 6 | |
| Supplier Item Price Tier 7 | No | No | | Supplier Item Price Tier 7 | |
| Supplier Item Price Tier 8 | No | No | | Supplier Item Price Tier 8 | |
| Supplier Item Price Tier 9 | No | No | | Supplier Item Price Tier 9 | |
| Supplier Item Price Tier 10 | No | No | | Supplier Item Price Tier 10 | |
| Supplier Item Price Tier 11 | No | No | | Supplier Item Price Tier 11 | |
| Supplier Item Price Tier 12 | No | No | | Supplier Item Price Tier 12 | |
| Supplier Item Price Tier 13 | No | No | | Supplier Item Price Tier 13 | |
| Supplier Item Price Tier 14 | No | No | | Supplier Item Price Tier 14 | |
| Supplier Item Price Tier 15 | No | No | | Supplier Item Price Tier 15 | |
| Supplier Item Price Tier 16 | No | No | | Supplier Item Price Tier 16 | |
| Supplier Item Price Tier 17 | No | No | | Supplier Item Price Tier 17 | |
| Supplier Item Price Tier 18 | No | No | | Supplier Item Price Tier 18 | |
| Supplier Item Price Tier 19 | No | No | | Supplier Item Price Tier 19 | |
| Supplier Item Price Tier 20 | No | No | | Supplier Item Price Tier 20 | |
| Supplier Item Item Update | No | No | | Supplier Item Item Update | |
| Rich Body Text | No | No | | Rich Body Text | |

## Item Translation

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Item Number | Yes | No | | Item number of the item for this translation | |
| Locale | Yes | Yes | string(255) | Locale for this translation | |
| Name | No | No | string(255) | Translated Item name | |
| Description | No | No | text | Translated Item description | |
