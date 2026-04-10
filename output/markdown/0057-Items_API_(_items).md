---
title: "Items API (/items)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)"
status_code: 200
fetched_at: "2026-04-09T11:59:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Items API (/items)"
---

# Items API (/items)

Use the catalog items API to create, update, or query goods not
provided by suppliers that your employees will select from when
creating a requisition.

The URL to access
items is: `https:///api/items`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Items API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/items` | create | Create item |
| GET | `/api/items/:id/image` | image | Get item image |
| GET | `/api/items` | index | Query items |
| GET | `/api/items/:id` | show | Show item |
| PATCH | `/api/items/:id` | update | Update item |
| PUT | `/api/items/:id` | update | Update item |

## Elements

The following elements are available for the Items API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Is the item given for this supplier & contract active? and if NOT then DELETE | | | | yes | yes | boolean |
| allow-partial-quantity | Allow partial quantity in cycle counts | | | | | yes | boolean |
| commodity | Commodity | | | | yes | yes | [Commodity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)) |
| connect-item-id | connect_item_id | | | | yes | | integer |
| consumption-quantity | consumption_quantity | | | | yes | yes | integer |
| consumption-uom | consumption_uom | | | | yes | yes | [UoM](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | Item desciption | yes | | | yes | yes | text |
| external-image-url | External image URL for item image | | | | | yes | string |
| id | Coupa unique identifier | | | | | yes | integer |
| image-url | URL for item image (will be copied into Coupa on item create/update) | | | | yes | | string |
| inventory-lot-expiration-type | Lot expiration type | | | | | yes | string |
| inventory-lot-tracking-enabled | Enable lot tracking | | | | | yes | boolean |
| item-number | Unique item number | | yes | | yes | yes | string |
| item-type | Item Type | no | no | any | yes | yes | Item |
| manufacturer-name | Manufacturer name | yes | | | yes | yes | string(255) |
| manufacturer-part-number | Manufacturer part number | | yes | | yes | yes | string(255) |
| name | Item name | yes | | | yes | yes | string |
| net-weight | net_weight | yes | | | yes | | decimal |
| net-weight-uom | net_weight_uom | | | | yes | | [UoM](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| pack-qty | pack_qty | yes | | | yes | | decimal |
| pack-uom | pack_uom | | | | yes | | [UoM](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| pack-weight | pack_weight | yes | | | yes | | decimal |
| receive-catch-weight | receive_catch_weight | | | | yes | | boolean |
| receiving-form | receiving_form | | | | yes | yes | |
| reorder-alerts | reorder_alerts | | | | | yes | |
| reorder-point | reorder_point | | | | yes | | float |
| require-asset-tag | Require asset tag | | | | | yes | boolean |
| require-inspection | Require inspection | | | | | yes | boolean |
| storage-quantity | storage_quantity | | | | yes | yes | integer |
| storage-uom | storage_uom | | | | yes | yes | [UoM](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| sustainability-detail | Sustainability detail | | | | yes | yes | [SustainabilityDetail](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)/sustainability-detail-api) |
| tax_detail | Tax detail | | | | yes | yes | |
| uom | Unit of Measure | | | | yes | yes | [UoM](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| use-pack-weight | use_pack_weight | | | | yes | | boolean |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

The Commodity and UOM must already exist in the system.
