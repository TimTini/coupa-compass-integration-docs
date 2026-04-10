---
title: "Advance Ship Notices API (/asn)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/advance-ship-notices-api-(asn)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/advance-ship-notices-api-(asn)"
status_code: 200
fetched_at: "2026-04-09T11:59:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Advance Ship Notices API (/asn)"
---

# Advance Ship Notices API (/asn)

## Overview

You can access ASN headers at `/api/asn/headers`
and ASN lines at `/api/asn/lines`.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | /api/asn/headers | create | Create advance ship notice header |
| GET | /api/asn/headers | index | Query advance ship notice header |
| PUT | /api/asn/headers/receive | receive | Add query parameter fully_consume=true to receive. |
| PUT | /api/asn/headers/:id/receive | receive | |
| GET | /api/asn/headers/:id | show | Show advance ship notice header |
| PUT | /api/asn/headers/:id | update | Update advance ship notice header |
| PUT | /api/asn/headers/void | void | |
| PUT | /api/asn/headers/:id/void | void | |

## Elements

| **Field Name** | **Field Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| asn-number | Advanced Ship Notice Number | yes | yes | | yes | yes | string(40) |
| bill-of-lading | Detailed list of a shipment of goods used to clear customs | | | | yes | | string(255) |
| carrier | Shipper | | | fedex, usps, ups, dhl, ontrac, asendia, apc, firstmile, newgistics, globegistics, rr_donnelley, purolator_ca | yes | | string(255) |
| container | Shipping Container number for tracking purposes | | | | yes | | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | User |
| delivery-date | Expected Delivery date when goods arrives | | | | yes | yes | datetime |
| export-flag | Indicates if transaction has been exported | | | | yes | yes | boolean |
| gross-weight | Gross weight of package | | | | yes | | decimal(30,6) |
| id | Coupa unique identifier | | | | | yes | integer |
| lines | Lines | yes | | | yes | yes | Asn/Line |
| packing-slip | shipping list/manifest of goods usually inside the box | | | | yes | | string(255) |
| ship-date | Shipment Date | yes | | | yes | yes | datetime |
| ship-method | Method of shipment | | | | yes | | string(255) |
| ship-note | Note to shipper | | | | yes | | string(255) |
| ship-to-address | Ship to address | yes | | | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| ship-to-user | Ship to user | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| ship-to-warehouse | Ship to warehouse | | | | yes | yes | Warehouse |
| standard-carrier-alpha-code | SCAC code to identify road transport companies | | | | yes | | string(255) |
| status | transaction status | | | | | yes | string(50) |
| supplier | supplier | yes | | | yes | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| tracking-number | Tracking number of shipment | | | | yes | | string(255) |
| trailer | Trailer number your product will be shipping on | | | | yes | | string(255) |
| uom | UOM Code | | | | yes | | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
