---
title: "Schedule Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/schedule-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/schedule-line-api"
status_code: 200
fetched_at: "2026-04-09T11:59:32+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Schedule Line API"
---

# Schedule Line API

The Schedule Line API is a shared object associated with the Purchase Order Lines API.

This API is associated with:

- [Purchase Order Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961)

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | no | no | any | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| delivery_date | Delivery date | no | no | any | | yes | datetime |
| quantity | Quantity | yes | no | any | | yes | decimal(30,6) |
| created_by | User who created | no | no | any | | yes | |
| updated_by | User who updated | no | no | any | | yes | |
