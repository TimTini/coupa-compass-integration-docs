---
title: "ExtraLineAttributes::OrderLineAttribute API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/extralineattributesorderlineattribute-api-da-5838-da-5838"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/extralineattributesorderlineattribute-api-da-5838-da-5838"
status_code: 200
fetched_at: "2026-04-09T11:59:27+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "ExtraLineAttributes::OrderLineAttribute API"
---

# ExtraLineAttributes::OrderLineAttribute API

ExtraLineAttributes::OrderLineAttribute is a shared object. It does not include an
endpoint.

## Associations

This API is associated with the [Purchase Order Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | No | No | No | | Yes | datetime |
| created-by | User who created | No | No | No | | Yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| end-date | End date | No | No | No | Yes | Yes | datetime |
| id | Coupa unique identifier | No | No | No | | Yes | integer |
| manager | Manager | No | No | No | Yes | Yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| rate-card | Rate card | No | No | No | Yes | Yes | RateCard |
| start-date | Start date | No | No | No | Yes | Yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | No | No | No | | Yes | datetime |
| updated-by | User who updated | No | No | No | | Yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| work-confirmer-email | Work confirmer email | No | No | No | Yes | Yes | string(255) |
