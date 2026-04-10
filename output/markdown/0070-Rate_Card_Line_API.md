---
title: "Rate Card Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/rate-card-api/rate-card-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/rate-card-api/rate-card-line-api"
status_code: 200
fetched_at: "2026-04-09T11:59:17+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Rate Card API"
  - "Rate Card Line API"
---

# Rate Card Line API

Use the Rate Card Line API to create, update, or query rate card
lines.

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Associated APIs

- [Rate Card API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/rate-card-api)

## Elements

The following elements are available for the Rate Card Line
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| name | Name | true | true | any | yes | yes | string(255) |
| code | Code | false | false | any | yes | yes | string(255) |
| price | Price | true | false | any | yes | yes | decimal(30,6) |
| rate-card-line-type | Rate card line type | true | false | any | yes | yes | integer |
| rate-card-type | Rate card type | true | false | any | yes | yes | integer |
| uom | UOM | false | false | any | yes | yes | UoM |
| currency | Currency | false | false | any | yes | yes | Currency |
| active | Active | false | false | any | yes | yes | boolean |
| id | Coupa unique identifier | false | false | any | yes | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| rate-card-id | Rate card ID | false | false | any | yes | yes | integer |
| created-by | User who created | false | false | any | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| updated-by | User who updated | false | false | any | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| commodity | Commodity | false | false | any | | yes | Commodity |
