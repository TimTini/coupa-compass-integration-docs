---
title: "Purchase Order Lines API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961"
status_code: 200
fetched_at: "2026-04-09T11:59:55+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Purchase Orders API (/purchase_orders)"
  - "Purchase Order Lines API"
---

# Purchase Order Lines API

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| DELETE | `/api/purchase_order_lines/:id` | destroy | Delete purchase order line |
| GET | `/api/purchase_order_lines` | index | Query purchase order lines |
| PUT | `/api/purchase_order_lines/:id/reopen_for_invoicing` | reopen_for_invoicing | Reopen for invoicing |
| PUT | `/api/purchase_order_lines/:id/reopen_for_receiving` | reopen_for_receiving | Reopen for receiving |
| GET | `/api/purchase_order_lines/:id` | show | Show purchase order line |
| PUT | `/api/purchase_order_lines/:id/soft_close_for_invoicing` | soft_close_for_invoicing | Soft close for invoicing |
| PUT | `/api/purchase_order_lines/:id/soft_close_for_receiving` | soft_close_for_receiving | Soft close for receiving |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account | The account associated with the Purchase Order line. Use this element if there is no split billing for a Purchase Order line; for example, if there is only one account associated with the Purchase Order line. If there is more than one account, use the `account-allocations` element. | yes | | | yes | yes | [Account](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)) |
| account-allocations | The account information associated with the Purchase Order line. Use this element to designate split billing for a Purchase Order line; for example, if there is more than one account associated with the Purchase Order line. If there is only one account, use the `account` element. | | | | yes | yes | [Order Line Allocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/order-line-allocations-api) |
| account-type | chart of accounts | | | | yes | | [AccountType](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| accounting-total | accounting_total | | | | yes | yes | decimal(32,4) |
| accounting-total-currency | accounting_total_currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| asset-tags | asset_tags | | | | yes | yes | [Asset Tag](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/asset-tags-api) |
| attachments | attachments | | | | yes | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| bulk-price | Bulk Price | | | | yes | yes | [Bulk Price](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/bulk-price-api) |
| commodity | commodity | | | | yes | yes | [Commodity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)) |
| contract | contract | | | | yes | yes | [Contract](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency of transaction | yes | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| department | department | | | | yes | yes | [Department](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/departments-api-(departments)) |
| description | description | yes | | | yes | yes | string(255) |
| extra-line-attribute | Extra line attribute | | | | | yes | [Extra Line Attributes:: Order Line Attribute](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/extralineattributesorderlineattribute-api-da-5838-da-5838) |
| form-response | form_response | | | | yes | yes | Form Response |
| id | Coupa unique identifier | | | | | yes | integer |
| invoice-stop | Invoice Stop flag | | | | | yes | boolean |
| invoiced | invoiced | | | | yes | yes | decimal(32,6) |
| item | item | | | | yes | yes | [Item](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)) |
| line-num | line_num | | yes | | yes | yes | string(255) |
| match-type | Match type | 3-way-fifo, 3-way, 2-way, direct_matching, none | yes | yes | string(255) | | |
| milestones | Milestones | | | | yes | yes | Procurement::Milestone |
| minimum-order-quantity | Minimum order quantity | | | | | yes | decimal(30,6) |
| need-by-date | need_by_date | | | | yes | yes | datetime |
| order-header-id | order_header_id | | | | yes | yes | integer |
| order-header-number | PO Number | | | | | yes | string |
| easy_form_response_id | ID of the Easy Form Response | | | | | yes | |
| period | period | | | | yes | yes | [Period](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api) |
| price | price | yes | | | yes | yes | decimal(30,6) |
| quantity | quantity | | | | yes | yes | decimal(30,6) |
| receipt-approval-required | Receipt approval required | | | | | yes | boolean |
| receipt-required | receipt_required | | | | yes | yes | boolean |
| received | Quantity/Amount received | | | | yes | yes | integer/decimal |
| receiving-warehouse | Receiving warehouse | | | | yes | yes | Warehouse |
| reporting-total | reporting_total | | | | yes | yes | decimal(32,4) |
| requester | requester | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| rfq-form-response | rfq_form_response | | | | | yes | [Form Response](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/form-api) |
| savings-pct | savings_pct | | | | yes | yes | decimal(8,2) |
| service-type | Specifies the type of service. Field only available when services procurement is enabled in the instance. For more information about service types, see [Introducing Services Maestro](https://compass.coupa.com/x298787.xml). | | | resource,<br>quantity_deliverable,<br>amount_deliverable, non_service | | yes | string |
| status | transaction status | | | | yes | yes | string(50) |
| sub-line-num | sub_line_num | | | | yes | yes | integer |
| supp-aux-part-num | supp_aux_part_num | | | | yes | yes | text |
| supplier | supplier | | | | yes | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| supplier-order-number | supplier_order_number | | | | yes | yes | string(255) |
| supplier-site-id | supplier site id | | | | | yes | integer |
| total | total | | | | yes | yes | decimal(32,4) |
| type | type | | | | yes | yes | string(100) |
| uom | unit of measure | | | | yes | yes | [Uom](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| version | version | | | | yes | yes | integer |
| manufacturer_name | Manufacturer Name | | | | yes | | string(255) |
| manufacturer_part_number | Manufacturer Part Number | | | | yes | | string(255) |
| external_reference_number | External Reference Number | yes | | | yes | yes | string(255) |
| external_reference_type | External Reference Type | | | | yes | yes | string(255) |
| third_party_supplier | | | | | yes | yes | |
| amount_components | | | | | yes | yes | [] |
| extra_line_attribute | | | | | yes | | |
| requisition_line_id | Requisition line ID | | | | | yes | RequisitionLine |
| recurring_rules | Recurring rules | | | | | yes | |
| line_owner | Line owner | | | | yes | yes | |
| order_line_tax_detail | Oder line tax detail | | | | yes | yes | |
