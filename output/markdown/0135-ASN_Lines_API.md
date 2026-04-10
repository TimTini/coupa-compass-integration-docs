---
title: "ASN Lines API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/advance-ship-notices-api-(asn)/asn-lines-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/advance-ship-notices-api-(asn)/asn-lines-api"
status_code: 200
fetched_at: "2026-04-09T11:59:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Advance Ship Notices API (/asn)"
  - "ASN Lines API"
---

# ASN Lines API

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| | | | |
| Verb | Path | Action | Description |
| PUT | /api/asn/lines/receive | receive | |
| PUT | /api/asn/lines/:id/receive | receive | |
| PUT | /api/asn/lines/void | void | |
| PUT | /api/asn/lines/:id/void | void | |

## Elements

| **Field Name** | **Field Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| comments | Free form based comments about the shipment (e.g. hazardous) | yes | yes | string(255) | | | |
| container | Shipping Container number for tracking purposes | yes | yes | string(255) | | | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | description | | | | | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| invoice-line | invoice line | | | | yes | yes | [Invoice Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-line-api) |
| item | item | | | | yes | yes | [Item](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)) |
| line-num | line_num | yes | yes | | yes | yes | string(255) |
| match-reference | Used for matching invoice against ASN line and receipts | yes | yes | string(255) | | | |
| order-line | order_line is a segment that contains multiple fields like "id" and "order-header-number" that are required to associate the ASN line with a PO and PO line. | yes | yes | [Order Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961) | | | |
| quantity | Shipped quantity | yes | | | yes | yes | decimal(30,6) |
| received-qty | Actual quantity received | yes | | | | yes | decimal(30,6) |
| review-reason | reasons - a free form text | | | | | yes | string(255) |
| status | Line status | draft, pending_receipt, partially_received, received, error, cancelled | yes | yes | string(255) | | |
| supplier-aux-part-num | Supplier auxiliary part number | | | | yes | yes | string(255) |
| supplier-part-num | Supplier part number | | | | yes | yes | string(255) |
| uom | unit of measure | | | | | yes | UoM |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
