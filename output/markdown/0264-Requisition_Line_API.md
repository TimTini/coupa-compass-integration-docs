---
title: "Requisition Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/requisition-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/requisition-line-api"
status_code: 200
fetched_at: "2026-04-09T11:59:59+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Requisitions API (/requisitions)"
  - "Requisition Line API"
---

# Requisition Line API

## Association

This resource is associated with [Requisitions API](https://compass.coupa.com/x286199.xml).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account | account | | | | yes | yes | [Account](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)) |
| account-allocations | account-allocations | | | | yes | yes | [Req Line Allocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/req-line-allocation-api) |
| asset-tags | asset-tags | | | | yes | yes | [Asset Tag](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/asset-tags-api) |
| attachments | attachments | | | | | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| commodity | commodity | | | | yes | yes | [Commodity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)) |
| contract | contract | | | | yes | yes | [Contract](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency of transaction | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| description | description | yes | | | yes | yes | string(255) |
| easy-form-response-id | Easy Form Response Id | | | | | yes | integer |
| extra-line-attribute | | | | | yes | | |
| form-response | form-response | | | | | yes | [Form Response](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/form-api) |
| id | Coupa unique identifier | | | | | yes | integer |
| item | item | yes | | | yes | yes | [Item](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)) |
| line-num | line-num | | | | yes | yes | integer |
| line-type | line type | | | RequisitionQuantityLine, RequisitionAmountLine | yes | yes | string |
| manufacturer-name | Manufacturer Name | | | | yes | yes | string(255) |
| manufacturer-part-number | Manufacturer Part Number | | | | yes | yes | string(255) |
| milestones | Milestones | | | | yes | yes | Procurement::Milestone |
| minimum-order-quantity | Minimum order quantity | | | | | yes | decimal(30,6) |
| need-by-date | need-by-date | | | | yes | yes | datetime |
| order-line-id | order-line-id | | | | | yes | integer |
| order-pad-line | Order pad line | | | | | yes | Order Pad Line |
| payment-term | payment-term | | | | yes | yes | [Payment Term](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/payment-terms-api-(payment_terms)) |
| period | Budget period | | | | | yes | Period |
| punchout-site | punchout-site | | | | yes | yes | Punchout Site |
| quantity | quantity | | | | yes | yes | decimal(30,6) |
| realtime-extension | Realtime extension | | | | | yes | |
| receipt-required | receipt-required | | | | yes | yes | boolean |
| recurring-rules | Recurring rules | | | | | | |
| shipping-term | shipping-term | | | | yes | yes | [Shipping Term](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/shipping-terms-api-(shipping_terms)) |
| source | Source | | | | yes | | string(255) |
| source-details | Source Details | | | | yes | | string(255) |
| source-part-num | source-part-num | | | | yes | yes | string(255) |
| source-type | source type | | | | | yes | Non-Catalog Request, Form |
| status | transaction status | | | | | yes | string(50) |
| sub-line-num | sub-line-num | | | | | yes | integer |
| supp-aux-part-num | supp-aux-part-num | | | | yes | yes | text |
| supplier | supplier | | | | yes | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| supplier-site | supplier site | | | | | yes | Supplier Site |
| supplier-site-id | Supplier site | | | | yes | yes | integer |
| tags | | | | | yes | yes | [] |
| taggings | | | | | yes | yes | [] |
| total | total | | | | | yes | decimal(32,4) |
| transmission-emails | Transmission emails | | | | yes | yes | text |
| transmission-method-override | Transmission method override | | | supplier_default, email, do_not_transmit | | yes | string(30) |
| unit-price | line item price | | | | yes | yes | decimal(30,6) |
| unspsc-code | UNSPSC code | | | | | yes | string(255) |
| uom | unit of measure | | | | yes | yes | [Uom](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| line_owner | Line owner | | | | yes | yes | |
| requisition_line_tax_detail | Tax Detail | yes | | | yes | yes | |
| order_confirmation_level | Order confirmation level | | | | yes | yes | integer |
| confirm_by_hrs | Confirm by hours | | | 0..87600 | yes | yes | decimal(10,0) |
