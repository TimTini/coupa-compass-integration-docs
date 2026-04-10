---
title: "Warehouse API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-api"
status_code: 200
fetched_at: "2026-04-09T11:59:53+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Pick Lists/Fulfillment Reservations API (/pick lists)"
  - "Warehouse API"
---

# Warehouse API

## Associations

This resource is associated with [Pick Lists/Fulfillment Reservations API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active-flag | active_flag | | | | yes | yes | boolean |
| address | address | yes | | | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency | yes | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| description | description | yes | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | name | yes | yes | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| warehouse-locations | Warehouse locations | | | | yes | yes | [Warehouse Location](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-location-api) |
| warehouse-type | warehouse_type | yes | | | yes | yes | [Warehouse Type](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-type-api) |
