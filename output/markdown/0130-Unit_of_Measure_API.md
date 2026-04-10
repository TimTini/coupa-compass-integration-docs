---
title: "Unit of Measure API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api"
status_code: 200
fetched_at: "2026-04-09T11:59:32+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Unit of Measure API"
---

# Unit of Measure API

Use this API to specify the unit of measure on orders, invoices, items, and more.

## Associations

This API is associated with [Items API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)), [Purchase Order Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961), [Invoice Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-line-api), [ASN Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/advance-ship-notices-api-(asn)/asn-lines-api), and [Receiving Transactions API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/receiving-transactions-api-(receiving_transactions)).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | A false value will inactivate the account making it no longer available to users. A true value will make it active and available to users. | yes | yes | boolean | | | |
| allowable-precision | allowable_precision | yes | | | yes | yes | integer |
| code | code | yes | yes | | yes | yes | string(6) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | name | yes | yes | | yes | yes | string(100) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
