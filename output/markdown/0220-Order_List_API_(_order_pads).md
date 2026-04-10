---
title: "Order List API (/order_pads)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/order-list-api-(order_pads)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/order-list-api-(order_pads)"
status_code: 200
fetched_at: "2026-04-09T11:59:51+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Order List API (/order_pads)"
---

# Order List API (/order_pads)

The Order Lists API lets you create a list, set, or
kit of frequently requested items within a supplier catalog for
easy ordering.

The URL to access Order Lists
is: `https:///api/order_pads`

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Use the API key from the API user (created from: /api_keys) to be able to retrieve expense
reports from all users. If you use individual API keys, you will get expense reports for
specified user.

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

**Order Pad**

Order Pad API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/order_pads` | create | Create order pad |
| GET | `/api/order_pads` | index | Query order pads |
| GET | `/api/order_pads/:id` | show | Show order pad |
| PUT | `/api/order_pads/:id` | update | Update order pad |

**Order Pad Lines**

Order Pad Lines allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/order_pads/:order_pad_id/order_pad_lines` | create | Create order pad line |
| GET | `/api/order_pads/:order_pad_id/order_pad_lines` | index | Query order pad lines |
| GET | `/api/order_pads/:order_pad_id/order_pad_lines/:id` | show | Show order pad line |
| PUT | `/api/order_pads/:order_pad_id/order_pad_lines/:id` | update | Update order pad line |

## Elements

**Order Pad**

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| add-all-items | Flag indicating to add all items | | | | yes | | boolean |
| any-supplier | any_supplier | | | | yes | yes | boolean |
| base-value | base_value | yes | | | yes | yes | decimal(10,0) |
| base-value-currency | base_value_currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| business-groups | business_groups | | | | yes | yes | [Period](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| locked | locked | | | | yes | yes | boolean |
| name | name | yes | yes | | yes | yes | string(255) |
| order-pad-lines | order_pad_lines | | | | yes | yes | Order Pad Line |
| order-pad-sections | order_pad_sections | | | | yes | yes | Order Pad Section |
| suppliers | suppliers | | | | yes | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| use-base-value | use_base_value | | | | yes | yes | boolean |

**Order Pad Lines**

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | amount | | | | yes | yes | decimal(30,6) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| item | item | yes | | | yes | yes | [Item](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)) |
| key-item | key_item | | | | yes | yes | boolean |
| order-amount-method | order_amount_method | yes | | amount, par | yes | yes | string(255) |
| order-pad-section | order_pad_section | | | | yes | yes | Order Pad Section |
| par-level | par_level | | | | yes | yes | decimal(10,2) |
| position | position | | | | yes | yes | integer |
| supplier-id | supplier_id | yes | | | yes | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

**Order Pad Section**

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| name | name | yes | | | yes | yes | string(255) |
| position | position | | | | yes | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
