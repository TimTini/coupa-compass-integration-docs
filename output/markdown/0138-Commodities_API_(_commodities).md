---
title: "Commodities API (/commodities)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)"
status_code: 200
fetched_at: "2026-04-09T11:59:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Commodities API (/commodities)"
---

# Commodities API (/commodities)

## Associations

This resources is associated with [Items API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)), [Order Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961),
[Suppliers API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api),
and [Supplier Information API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)-da-5810-da-5810).

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/commodities` | create | Create commodity |
| GET | `/api/commodities` | index | Query commodities |
| GET | `/api/commodities/:id` | show | Show commodity |
| PATCH | `/api/commodities/:id` | update | Update commodity |
| PUT | `/api/commodities/:id` | update | Update commodity |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | A false value will inactivate the account making it no longer available to users. A true value will make it active and available to users. | true, false | yes | yes | boolean | | |
| category | Category | | | goods, services, monetary, others | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | yes | datetime | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| deductibility | Deductibility | | | fully_deductible, partially_deductible, not_deductible | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| imported-from-taxonomy | A true value will tell that the commodity is imported from Coupa Taxonomy. A false value will tell that the value is created by a user or system | | | | | yes | boolean |
| name | name | yes | yes | | yes | yes | string(255) |
| parent | parent | | | | yes | yes | Commodity |
| preferred | A Yes/No value will mark/unmark commodity as preferred. Set to Automatic if you want the system to mark preferred. 'Automatic' option is available only if 'Automatic Guided Experiences configuration' is enabled on the Company Information page. | | | Yes, No, Automatic, Always, Never | yes | yes | string(255) |
| subcategory | Subcategory | | | raw_materials, investment_goods, services_exceptions | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | yes | datetime | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| translated_name | Translated name | | | | | yes | |
