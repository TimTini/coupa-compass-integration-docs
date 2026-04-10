---
title: "Bulk Price API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/bulk-price-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/bulk-price-api"
status_code: 200
fetched_at: "2026-04-09T11:59:27+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Bulk Price API"
---

# Bulk Price API

This API is used to manage bulk pricing on orders and invoices.

## Associations

This API is associated with [Order Line API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961) and [Invoice Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-line-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | True | | | yes | integer |
| price | Bulk Price | | | any | yes | yes | decimal(30,6) |
| qty | Bulk Price Qty | | | any | yes | yes | decimal(30,6) |
| uom | Unit of Measure | True | | any | yes | yes | [UoM](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| conversion_numerator | UOM conversion numerator | False | False | any | yes | yes | decimal(30,6) |
| conversion_denominator | UOM conversion_denominator | False | False | any | yes | yes | decimal(30,6) |
