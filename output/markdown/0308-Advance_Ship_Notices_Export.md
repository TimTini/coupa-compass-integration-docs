---
title: "Advance Ship Notices Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/advance-ship-notices-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/advance-ship-notices-export"
status_code: 200
fetched_at: "2026-04-09T12:00:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Advance Ship Notices Export"
---

# Advance Ship Notices Export

Export of these records is included as a Standard CSV Export.

## Asn-Header

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Record Type | Indicates record type | | No/No | |
| Id | Coupa's internal ID | integer | No/No | |
| ASN Number | ASN Number | string(40) | Yes/Yes | |
| Status | ASN Header Status | string(50) | No/No | |
| Ship to date | Ship to date | datetime | Yes/No | |
| Delivery date | Delivery date | datetime | No/No | |
| Supplier id | Supplier Coupa internal ID number | integer | No/No | |
| Supplier name | Supplier Name | | No/No | |
| Supplier number | Supplier Number | | No/No | |
| Created by employee number | Employee Number of User who created ASN | | No/No | |
| Created by id | Coupa ID of User who created ASN | integer | No/No | |
| Created by login | Login name of User who created ASN | | No/No | |
| Created at | Date record was created in Coupa. | datetime | No/No | |
| Updated by employee number | Employee Number of User last updated by | | No/No | |
| Updated by id | Coupa ID of User last updated by | integer | No/No | |
| Updated by login | Login name of User last updated by | | No/No | |
| Updated at | Last Updated at Date | datetime | No/No | |
| Ship to user employee number | Employee Number of Ship To User | | No/No | |
| Ship to user id | Coupa ID of Ship To User | integer | No/No | |
| Ship to user login | Login name of Ship To User | | No/No | |
| ASN Lines Count | ASN Lines Count | integer | No/No | |
| Gross weight | Gross weight | decimal(30,6) | No/No | |
| Carrier | Carrier for the shipment | string(255) | No/No | |
| Tracking Number | Tracking Number | string(255) | No/No | |
| Standard carrier alpha code | Unique two-to-four-letter code used to identify transportation companies | string(255) | No/No | |
| Container | Container or LPN for the shipped material | string(255) | No/No | |
| Version | Version | integer | No/No | |
| Channel | Channel | string(255) | No/No | |
| Trailer | Trailer number for the shipment | string(255) | No/No | |
| Bill of lading | Document issued by a carrier to acknowledge receipt of cargo for shipment | string(255) | No/No | |
| Packing slip | Delivery list | string(255) | No/No | |
| Ship to attention | Ship to attention | string(255) | No/No | |
| Ship method | Ship method | string(255) | No/No | |
| Ship note | Ship note | string(255) | No/No | |
| Uom code | Uom code | | No/No | |

## Asn-Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Record Type | Indicates record type | | No/No | |
| Id | Coupa's internal ID | integer | No/No | |
| Line num | Line num | string(255) | Yes/Yes | |
| Status | ASN Line Status | string(255) | No/No | |
| Description | Description | string(255) | No/No | |
| Quantity | Quantity | decimal(30,6) | Yes/No | |
| Uom code | Uom code | | No/No | |
| Asn Header Id | Asn Header Id | integer | No/No | |
| Asn Header Number | Asn Header Number | | No/No | |
| Order Line Id | Order Line Id | integer | No/No | |
| Description | Description | string(255) | No/No | |
| Created by Employee Number | Employee Number of User who created ASN | | No/No | |
| Created By Id | Coupa ID of User who created ASN | integer | No/No | |
| Created By Login | Login name of User who created ASN | | No/No | |
| Created At | Date record was created in Coupa. | datetime | No/No | |
| Updated_by Employee Number | Employee Number of User last updated by | | No/No | |
| Updated By Id | Coupa ID of User last updated by | integer | No/No | |
| Updated By Login | Login name of User last updated by | | No/No | |
| Updated At | Last Updated at Date | datetime | No/No | |
| Received Qty | Received Qty | decimal(30,6) | Yes/No | |
| Item Id | Item Id | integer | No/No | |
| Item Name | Item Name | | No/No | |
| Item Number | Item Number | | No/No | |
| Invoice Header Id | Invoice Header Id | integer | No/No | |
| Invoice Line Id | Invoice Line Id | integer | No/No | |
| Invoice Line Num | Invoice Line Num | string(255) | No/No | |
| Invoice Number | Invoice Number | string(255) | No/No | |
| Version | ASN Version Number | integer | No/No | |
| Container | Container or LPN for the shipped material | string(255) | No/No | |
| Supplier Part Num | Supplier Part Num | string(255) | No/No | |
| Supplier Aux Part Num | Supplier Aux Part Num | text | No/No | |
| Comments | Comments | string(255) | No/No | |
| Order Quantity | Order Quantity | decimal(30,6) | No/No | |
| Match Reference | Three-way match attribute to connect with Receipt and Invoice Header | string(255) | No/No | |
