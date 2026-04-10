---
title: "Order Amount Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/order-amount-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/order-amount-line-api"
status_code: 200
fetched_at: "2026-04-09T11:59:54+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Purchase Orders API (/purchase_orders)"
  - "Order Amount Line API"
---

# Order Amount Line API

## Association

This resource is associated with [Purchase Order Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961).

## Elements

The following elements are available for the Order Amount
Line API:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account | account | yes | | | yes | yes | Account |
| account-allocations | account_allocations | | | | yes | yes | [OrderLineAllocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/order-line-allocations-api) |
| account-type | chart of accounts | | | | yes | | [AccountType](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| accounting-total | accounting_total | | | | yes | yes | decimal(32,4) |
| accounting-total-currency | accounting_total_currency | | | | yes | yes | Currency |
| amount-components | Amount components | | | | yes | yes | [AmountComponent](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/account-group-api) |
| asset-tags | asset_tags | | | | yes | yes | [AssetTag](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/asset-tags-api) |
| attachments | attachments | | | | yes | yes | Attachment |
| bulk-price | Bulk price | | | | yes | | [BulkPrice](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/bulk-price-api) |
| commodity | commodity | | | | yes | yes | Commodity |
| contract | contract | | | | yes | yes | Contract |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | User |
| currency | Currency of transaction | yes | | | yes | yes | Currency |
| department | department | | | | yes | yes | Department |
| description | description | yes | | | yes | yes | string(255) |
| easy-form-response-id | Easy Form Response Id | | | | | yes | integer |
| external-reference-number | External Reference Number | yes | | | yes | yes | string(255) |
| external-reference-type | External Reference Type | | | staff_augmentation, sow_project | yes | yes | string(255) |
| extra-line-attribute | Extra line attribute | | | | yes | yes | [ExtraLineAttributes::OrderLineAttribute](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/extralineattributesorderlineattribute-api-da-5838-da-5838) |
| form-response | form_response | | | | yes | yes | [FormResponse](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/form-api) |
| id | Coupa unique identifier | | | | | yes | integer |
| invoiced | invoiced | | | | yes | yes | decimal(32,6) |
| item | item | | | | yes | yes | Item |
| line-num | line_num | | yes | | yes | yes | string(255) |
| manufacturer-name | Manufacturer Name | | | | yes | | string(255) |
| manufacturer-part-number | Manufacturer Part Number | | | | yes | | string(255) |
| match-type | Match type | | | direct_matching, 3-way-fifo, 3-way, 2-way, none | yes | yes | string(255) |
| milestones | Milestones | | | | yes | yes | Procurement::Milestone |
| need-by-date | need_by_date | | | | yes | yes | datetime |
| order-header-id | order_header_id | | | | yes | yes | integer |
| order-header-number | Order header number | | | | | yes | |
| period | period | | | | yes | yes | Period |
| price | price | yes | | | yes | yes | decimal(30,6) |
| quantity | quantity | | | | yes | yes | decimal(30,6) |
| receipt-approval-required | Receipt Approval Required | | | | | yes | boolean |
| receipt-required | receipt_required | | | | yes | yes | boolean |
| received | received | | | | yes | yes | decimal |
| receiving-warehouse | Receiving warehouse | | | | yes | | Warehouse |
| reporting-total | reporting_total | | | | yes | yes | decimal(32,4) |
| requester | requester | | | | | yes | |
| rfq-form-response | rfq_form_response | | | | | yes | [FormResponse](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/form-api) |
| savings-pct | savings_pct | | | | yes | yes | decimal(8,2) |
| service-type | Service type | | | | | yes | string |
| source-part-num | source_part_num | | | | yes | yes | string(255) |
| status | transaction status | | | | yes | yes | string(50) |
| sub-line-num | sub_line_num | | | | yes | yes | integer |
| supp-aux-part-num | supp_aux_part_num | | | | yes | yes | text |
| supplier | supplier | | | | yes | yes | Supplier |
| supplier-order-number | supplier_order_number | | | | yes | yes | string(255) |
| third-party-supplier | Third party supplier | | | | yes | yes | Supplier |
| total | total | | | | yes | yes | decimal(32,4) |
| type | type | | | | yes | yes | string(100) |
| uom | unit of measure | | | | yes | | [Uom](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | User |
| version | version | | | | yes | yes | integer |
| line_owner | Line owner | | | | yes | | |
| order_line_tax_detail | Oder line tax detail | yes | | | yes | yes | |
