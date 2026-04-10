---
title: "Inventory Valuation API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/inventory-valuation-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/inventory-valuation-api"
status_code: 200
fetched_at: "2026-04-09T11:59:53+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Pick Lists/Fulfillment Reservations API (/pick lists)"
  - "Inventory Valuation API"
---

# Inventory Valuation API

## Associations

This resource is associated with [Pick Lists/Fulfillment Reservations API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| currency | Currency | yes | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| id | Coupa unique identifier | | | | | yes | integer |
| total | Total | | | | | yes | |
| unit-price | Unit price | | | | | yes | decimal |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
