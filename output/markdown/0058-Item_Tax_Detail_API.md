---
title: "Item Tax Detail API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)/item-tax-detail-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)/item-tax-detail-api"
status_code: 200
fetched_at: "2026-04-09T11:59:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Items API (/items)"
  - "Item Tax Detail API"
---

# Item Tax Detail API

## Associations

This API is associated with the [Items API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)).

## Elements

The following elements are available for the Item Tax
Detail API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cfop | Cfop | | | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| ncm | Ncm | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
