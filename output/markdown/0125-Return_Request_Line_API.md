---
title: "Return Request Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/return-request-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/return-request-line-api"
status_code: 200
fetched_at: "2026-04-09T11:59:31+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Return Request Line API"
---

# Return Request Line API

Use the Return Request Line API to work with return request line items. This is a shared
object and does not have an endpoint.

This API is associated with:

- [Return Request API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/return-requests-api-(return_requests))

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | No | No | | | Yes | datetime |
| id | Coupa unique identifier | No | No | | | Yes | integer |
| inventory-transaction-id | Inventory transaction | No | No | | | Yes | integer |
| price | Price | Yes | No | | Yes | Yes | decimal(30,6) |
| quantity | Quantity | Yes | No | | Yes | Yes | decimal(30,6) |
| reason-insight | Reason Insight | No | No | | Yes | Yes | [ReasonInsight](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/reason-insights-api) |
| source-transaction-id | Source transaction | No | No | | Yes | Yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | No | No | | | Yes | datetime |
| warehouse | Warehouse | No | No | | Yes | Yes | [Warehouse](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-api) |
| warehouse-location | Warehouse location | No | No | | Yes | Yes | [WarehouseLocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-location-api) |
| weight | Weight | Yes | No | | Yes | Yes | decimal(30,6) |
