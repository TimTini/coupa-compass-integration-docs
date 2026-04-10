---
title: "Advance Ship Notice Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/advance-ship-notice-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/advance-ship-notice-import"
status_code: 200
fetched_at: "2026-04-09T12:00:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Advance Ship Notice Import"
---

# Advance Ship Notice Import

## Overview

The Advance Ship Notice import process read files from
`./Incoming/AdvanceShipNotice/` in the SFTP. These files will be moved to
the archive folder located at `./Incoming/Archive/AdvanceShipNotice/` before
being processed in alphanumeric order.

## Possible values

Carrier
fedex, usps, ups, dhl, ontrac, asendia, apc, firstmile, newgistics, globegistics,
rr_donnelley, purolator_ca

## Asn-Header

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| ASN Header* | Yes | No | | Record type - ASN Header | |
| ASN Number* | Yes | Yes | string(40) | ASN Header Number | |
| Supplier* | Yes | No | | Supplier Name | |
| Ship To Name | No | No | | Ship To Name | |
| Ship To Street 1 | No | No | | Ship To Street 1 | |
| Ship To Street 2 | No | No | | Ship To Street 2 | |
| Ship To Street 3 | No | No | | Ship To Street 3 | |
| Ship To Street 4 | No | No | | Ship To Street 4 | |
| Ship To City | No | No | | Ship To City | |
| Ship To State | No | No | | Ship To State | |
| Ship To Postal Code | No | No | | Ship To Postal Code | |
| Ship To Country Code | No | No | | Ship To Country Code | |
| Ship To Country Name | No | No | | Ship To Country Name | |
| Ship To Location Code | No | No | | Ship To Location Code | |
| Ship to Email | No | No | | Ship to Email | |
| Ship To Warehouse | No | No | | Ship To Warehouse | |
| Ship Date* | Yes | No | datetime | Date of Shipment | |
| Delivery Date | No | No | datetime | Expected Delivery Date | |
| Gross weight | No | No | decimal(30,6) | Gross weight | |
| UOM | No | No | string(255) | UOM of Gross weight | |
| Ship To Attention | No | No | | Ship To Attention | |
| Ship Method | No | No | string(255) | Ship Method | |
| Shipper Note | No | No | string(255) | Shipper Note | |
| Carrier | No | No | string(255) | Carrier for the shipment | |
| Tracking Number | No | No | string(255) | Tracking Number | |
| Standard Carrier Alpha Code | No | No | string(255) | Unique two-to-four-letter code used to identify transportation companies | |
| Container | No | No | string(255) | Container or LPN for the shipped material | |
| Trailer | No | No | string(255) | Trailer number for the shipment | |
| Bill Of Lading | No | No | string(255) | Document issued by a carrier to acknowledge receipt of cargo for shipment | |
| Packing Slip | No | No | string(255) | Delivery list | |
| ASN Line* | Yes | No | | Record type - ASN Line | |
| Line Number* | Yes | No | | ASN Line Number | |
| Status | No | No | string(50) | ASN Line Current Status | |
| Item Name | No | No | | ASN Line Item Name | |
| Quantity | No | No | | Quantity | |
| PO Number* | Yes | No | | Purchase Order Number | |
| PO Line Number* | Yes | No | | Purchase Order Line Number | |
| Invoice Line Number | No | No | | Invoice Line Number | |
| Invoice Number | No | No | | Invoice Number | |
| Match Reference | No | No | | Three-way match attribute to connect with Receipt and Invoice Header | |
| Comments | No | No | | ASN Line Comments | |
| Supplier Part Number | No | No | | Supplier Part Number | |
| Supplier Aux Part Number | No | No | | Supplier Aux Part Number | |
| Lot | No | No | | Lot | |
| Lot Number | No | No | | Lot Number | |
| Expiration Date | No | No | | Lot Expiration Date | |

## ASN Line Columns

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| ASN Line* | Describes the type of row | FALSE | FALSE | - | ASN Line |
| Line Number* | ASN Line Number | FALSE | FALSE | string(255) | any |
| Status | ASN Line Current Status | FALSE | FALSE | string(255) | any |
| Item Name | ASN Line Item Name | FALSE | FALSE | string(255) | any |
| Quantity* | ASN Line Shipped Quantity | FALSE | FALSE | decimal(30,6) | any |
| PO Number* | Purchase Order Number | FALSE | FALSE | string(20) | any |
| PO Line Number* | Purchase Order Line Number | FALSE | FALSE | string(255) | any |
| Invoice Line Number | Invoice Line Number | FALSE | FALSE | string(255) | any |
| Match Reference | Three-way match attribute to connect with Receipt and Invoice Header | FALSE | FALSE | string(255) | any |
| Invoice Number | Invoice Number | FALSE | FALSE | string(255) | any |
| Comments | ASN Line Comments | FALSE | FALSE | string(255) | any |
| Supplier Part Number | Supplier Part Number | FALSE | FALSE | string(255) | any |
| Supplier Aux Part Number | Supplier Aux Part Number | FALSE | FALSE | string(255) | any |
