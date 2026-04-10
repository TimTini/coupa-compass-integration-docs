---
title: "Supplier Items API (/supplier_items)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/supplier-items-api-(supplier_items)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/supplier-items-api-(supplier_items)"
status_code: 200
fetched_at: "2026-04-09T11:59:19+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
  - "Supplier Items API (/supplier_items)"
---

# Supplier Items API (/supplier_items)

Use the supplier items API to create, update, or query goods
provided by suppliers that your employees will select from when
creating a requisition.

The URL to access supplier items is:

```text
https://<instance>/api/supplier items
```

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Supplier Items API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | /api/items/:item_id/supplier_items | create | Create supplier item |
| POST | /api/supplier_items | create | Create supplier item |
| GET | /api/items/:item_id/supplier_items | index | Query supplier items |
| GET | /api/supplier_items | index | Query supplier items |
| GET | /api/supplier_items/search | search | Advanced supplier item search |
| GET | /api/items/:item_id/supplier_items/:id | show | Show supplier item |
| GET | /api/supplier_items/:id | show | Show supplier item |
| PUT | /api/items/:item_id/supplier_items/:id | update | Update supplier item |
| PUT | /api/supplier_items/:id | update | Update supplier item |
| DELETE | /api/supplier_items/:id | delete | Delete supplier item |

## Elements

The following elements are available for the Supplier Items
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| availability | Availability | | | in_stock, out_of_stock, backordered | yes | | string(255) |
| availability-date | Availability Date | | | any | yes | | datetime |
| catalog | catalog | | | | yes | yes | |
| contract | contract | | | | yes | yes | [Contract](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)) |
| contract-term | contract_term | | | | yes | yes | [ContractTerm](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-terms-api) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency of transaction | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| id | Coupa unique identifier | | | | | yes | integer |
| item | item | | | | yes | yes | [Item](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)) |
| lead-time | lead_time | | | | yes | yes | integer |
| manufacturer | manufacturer | | | | yes | yes | string |
| minimum_order_quantity | minimum_order_quantity | No | No | any | yes | yes | decimal(30,6) |
| order_increment | order_increment | No | No | any | yes | yes | decimal(30,6) |
| preferred | Indicates preferred supplier for this item. Change to `preferred_flag` when using this element as a query parameter. Example: `/api/supplier_items?item[item_number]=&preferred_flag=false` | true, false | yes | yes | boolean | | |
| price | price | | | | yes | yes | decimal |
| price-change | price_change | | | | yes | yes | float |
| price-tier-1 | price_tier_1 | | | | yes | yes | decimal |
| price-tier-10 | price_tier_10 | | | | yes | yes | decimal |
| price-tier-11 | price_tier_11 | | | | yes | yes | decimal |
| price-tier-12 | price_tier_12 | | | | yes | yes | decimal |
| price-tier-13 | price_tier_13 | | | | yes | yes | decimal |
| price-tier-14 | price_tier_14 | | | | yes | yes | decimal |
| price-tier-15 | price_tier_15 | | | | yes | yes | decimal |
| price-tier-16 | price_tier_16 | | | | yes | yes | decimal |
| price-tier-17 | price_tier_17 | | | | yes | yes | decimal |
| price-tier-18 | price_tier_18 | | | | yes | yes | decimal |
| price-tier-19 | price_tier_19 | | | | yes | yes | decimal |
| price-tier-2 | price_tier_2 | | | | yes | yes | decimal |
| price-tier-20 | price_tier_20 | | | | yes | yes | decimal |
| price-tier-3 | price_tier_3 | | | | yes | yes | decimal |
| price-tier-4 | price_tier_4 | | | | yes | yes | decimal |
| price-tier-5 | price_tier_5 | | | | yes | yes | decimal |
| price-tier-6 | price_tier_6 | | | | yes | yes | decimal |
| price-tier-7 | price_tier_7 | | | | yes | yes | decimal |
| price-tier-8 | price_tier_8 | | | | yes | yes | decimal |
| price-tier-9 | price_tier_9 | | | | yes | yes | decimal |
| savings-pct | savings_pct | | | | yes | yes | decimal |
| supplier | supplier | yes | | | yes | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| supplier-aux-part-num | supplier_aux_part_num | | | | yes | yes | string |
| supplier-part-num | supplier_part_num | yes | | | yes | yes | string |
| unspsc-code | UNSPSC code | no | no | any | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

The supplier_number, contract_name, item_name, and currency_code must already exist in
the system.
