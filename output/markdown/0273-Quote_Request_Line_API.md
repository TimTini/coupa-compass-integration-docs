---
title: "Quote Request Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-line-api"
status_code: 200
fetched_at: "2026-04-09T12:00:02+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Request Line API"
---

# Quote Request Line API

The quote request line resource lets you work with the lines on a sourcing event.

## Associations

This resource is associated with the [Quote Request API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| commodity | Line commodity | | | | yes | yes | [Commodity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| creatable-from-id | Creatable from | | | | | yes | integer |
| creatable-from-type | Creatable from type | | | | | yes | string(255) |
| created-by | User who created | | | | | yes | integer |
| description | Line description | | | | yes | yes | string(255) |
| extra-line-attribute | Extra Line Attribute | | | | yes | yes | ExtraLineAttributes/QuoteRequestLineAttribute |
| id | Coupa unique identifier | | | | | yes | integer |
| need-by-date | Date by which the line item is required | no | no | any | yes | | datetime |
| price-amount | Price | | | | yes | yes | decimal(30,6) |
| price-currency | Line currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| quantity | Quantity | | | | yes | yes | decimal(30,6) |
| reporting-price-amount | Line reporting price | | | | yes | yes | decimal(30,6) |
| type | Type of line | yes | | | yes | yes | string(255) |
| uom | Unit of measurement | | | | yes | yes | [Uom](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | integer |
| weight | Weight | | | | yes | yes | decimal |
| manufacturer_name | | | | | yes | yes | string(255) |
| manufacturer_part_number | | | | | yes | yes | string(255) |
| manually_entered_base_price | | | | | yes | yes | boolean |
| extended_description | | | | | yes | yes | text |
| fiscal_code | Fiscal code | | | | yes | yes | string(255) |
| classification_of_goods | Classification of goods | | | | yes | yes | string(255) |
| shipping_term | Shipping term | | | | yes | yes | |
| ship-to-address | Line Ship to address | | | | yes | | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| cost-formula | Cost Formula to calculate the total cost per unit of line | | | | yes | | [CostFormula](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-cost-formula-api) |
