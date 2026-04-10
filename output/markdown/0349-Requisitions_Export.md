---
title: "Requisitions Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/requisitions-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/requisitions-export"
status_code: 200
fetched_at: "2026-04-09T12:00:26+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Requisitions Export"
---

# Requisitions Export

## Overview

The requisition export process from Coupa queries for all
approved requisitions that have NOT been exported. The frequency of
the integration run is once every hour. The generated files will be
placed into `./Outgoing/Requisitions`. Once the
files are successfully placed into the sFTP folder the requisitions
will be marked as exported.

Export of these records is included as a Standard CSV
Export.

`For languages that use spaces as a currency delimiter, the CSV export interprets the space as: “ `

## Requisition

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Record Type | Indicates record type | | No/No | |
| Requisition Id | Coupa Internal Requisition ID | integer | No/No | |
| Submitted At Date | Date the Requisition was Submitted | datetime | No/No | |
| Status | Requisition Status | string(50) | Yes/No | |
| Buyer Note | Buyer Note | text | No/No | |
| Justification | Justification for requisition | text | No/No | |
| Reject Reason | rejection reason | | No/No | |
| Total | Total Amount for Request | decimal | No/No | |
| Currency Code | 3 digit Currency Code for Total | | No/No | |
| Requested By Employee Number | Employee Number of user who requisition is on behalf of cart/requisition | | No/No | |
| Requested by Login | Login of user who requisition is on behalf of cart/requisition | | No/No | |
| Requested by Email | Email of user who requisition is on behalf of cart/requisition | | No/No | |
| Department | Name of the Department for the requisition | | No/No | |
| Ship To Address Street 1 | Ship To Address Street Line 1 | | No/No | |
| Ship To Address Street 2 | Ship To Address Street Line 2 | | No/No | |
| Ship To Address City | Ship To Address City | | No/No | |
| Ship To Address State | Ship To Address State/Provience | | No/No | |
| Ship To Address Postal Code | Ship To Address Postal Code | | No/No | |
| Ship To Address Country Code | Ship To Address Country Code | | No/No | |
| Ship To Address Attention | Ship To Address Attention Field | | No/No | |
| Ship To Address Id | Ship To Address Internal Address ID | integer | No/No | |
| Ship To Address Name | Ship To Address Name | | No/No | |
| Ship To Address Location Code | Ship To Address Location Code | | No/No | |
| Department | Name of the Department for the requisition | | No/No | |
| Created At Date | Date the shopping cart/requisition was first created | datetime | No/No | |
| Updated At Date | Date the requisition was last updated | datetime | No/No | |
| Approved By Employee Number | Approved By Employee Numbers | | No/No | |
| Approved by Login | Approved by Logins | | No/No | |
| Approved by Email | Approved by Emails | | No/No | |
| Created By Employee Number | Employee Number of user who created cart/requisition | | No/No | |
| Created by Login | Login of user who created cart/requisition | | No/No | |
| Created by Email | Email of user who created cart/requisition | | No/No | |
| Updated By Employee Number | Employee Number of person who last updated the requisition | | No/No | |
| Updated by Login | Login of person who last updated the requisition | | No/No | |
| Updated by Email | Email of person who last updated the requisition | | No/No | |

## Requisition Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Record Type | Indicates record type | | No/No | |
| Requisition Header Id | Requisition Header Id | | No/No | |
| Line Number | Line Number | integer | No/No | |
| Description | Line Description | string(255) | Yes/No | |
| Item Name | Item Name | | No/No | |
| Item Number | Item Number | | No/No | |
| Supplier Auxiliary Part Number | Supplier Auxiliary Part Number | text | No/No | |
| Source Part Number | Source Part Number | string(255) | No/No | |
| Need By Date | Need By Date | datetime | No/No | |
| Price | Unit Price of Item | decimal | No/No | |
| Total Quantity | Total Quantity Ordered | decimal(30,6) | No/No | |
| Line Total | Line Total Amount | decimal(32,4) | No/No | |
| Request Type | Request Type | string | No/No | |
| Currency Code | Currency Code | | No/No | |
| Supplier Number | Supplier Number | | No/No | |
| Supplier Name | Supplier Name | | No/No | |
| Payment Terms | Payment Term Code | | No/No | |
| Shipping Terms | Shipping Term Code | | No/No | |
| Unit of Measure | Unit of Measure | | No/No | |
| Assets Tags | Assets Tags | string | No/No | |
| Commodity Name | Commodity Name | | No/No | |
| Chart of Account Name | Chart of Account Name | | No/No | |
| Account Code | Account Code | | No/No | |
| Account Name | Account Name | | No/No | |
| Segment 1 | Account Segment 1 | | No/No | |
| Segment 2 | Account Segment 2 | | No/No | |
| Segment 3 | Account Segment 3 | | No/No | |
| Segment 4 | Account Segment 4 | | No/No | |
| Segment 5 | Account Segment 5 | | No/No | |
| Segment 6 | Account Segment 6 | | No/No | |
| Segment 7 | Account Segment 7 | | No/No | |
| Segment 8 | Account Segment 8 | | No/No | |
| Segment 9 | Account Segment 9 | | No/No | |
| Segment 10 | Account Segment 10 | | No/No | |
| Segment 11 | Account Segment 11 | | No/No | |
| Segment 12 | Account Segment 12 | | No/No | |
| Segment 13 | Account Segment 13 | | No/No | |
| Segment 14 | Account Segment 14 | | No/No | |
| Segment 15 | Account Segment 15 | | No/No | |
| Segment 16 | Account Segment 16 | | No/No | |
| Segment 17 | Account Segment 17 | | No/No | |
| Segment 18 | Account Segment 18 | | No/No | |
| Segment 19 | Account Segment 19 | | No/No | |
| Segment 20 | Account Segment 20 | | No/No | |
| Created At | Date line was created | datetime | No/No | |
| Updated At | Date line was last updated | datetime | No/No | |
| Created By Employee Number | Employee Number of user who created line | | No/No | |
| Created by Login | Login of user who created line | | No/No | |
| Created by Email | Email of user who created line | | No/No | |
| Updated By Employee Number | Employee Number of user who last updated line | | No/No | |
| Updated by Login | Login of user who last updated line | | No/No | |
| Updated by Email | email of user who last updated line | | No/No | |

## Req Line Allocation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| RecordType | Describes the type of row. Possible values are Header, Line, or Line Split. | | No/No | |
| Requisition Header ID | Coupa's Requisition Report ID | integer | No/No | |
| Requsition Line ID | Coupa's Requisition Report Line ID | integer | No/No | |
| Requisition Line Number | Requisition Line Number | | No/No | |
| Purchase Order Header Number | If a PO was created, Coupa's Order Header Number | | No/No | |
| Purchase Order Line ID | If a PO was created, Coupa's Order Line ID | | No/No | |
| Purchase Order Line Number | If a PO was created, Coupa's Order Line Number | | No/No | |
| Account Allocation ID | Account Allocation ID | integer | No/No | |
| Allocation Number | Position in the Account Allocation Sequence | | No/No | |
| Allocation Amount | Amount allocated to the account | | No/No | |
| Allocation Percent | Percentage allocated to the account | | No/No | |
| Account Code | The whole account code of the account | | No/No | |
| Account Active | Flag indicating if the account is active. True or False. | | No/No | |
| Account Segment 1 | Account Segment 1 | | No/No | |
| Account Segment 2 | Account Segment 2 | | No/No | |
| Account Segment 3 | Account Segment 3 | | No/No | |
| Account Segment 4 | Account Segment 4 | | No/No | |
| Account Segment 5 | Account Segment 5 | | No/No | |
| Account Segment 6 | Account Segment 6 | | No/No | |
| Account Segment 7 | Account Segment 7 | | No/No | |
| Account Segment 8 | Account Segment 8 | | No/No | |
| Account Segment 9 | Account Segment 9 | | No/No | |
| Account Segment 10 | Account Segment 10 | | No/No | |
| Account Segment 11 | Account Segment 11 | | No/No | |
| Account Segment 12 | Account Segment 12 | | No/No | |
| Account Segment 13 | Account Segment 13 | | No/No | |
| Account Segment 14 | Account Segment 14 | | No/No | |
| Account Segment 15 | Account Segment 15 | | No/No | |
| Account Segment 16 | Account Segment 16 | | No/No | |
| Account Segment 17 | Account Segment 17 | | No/No | |
| Account Segment 18 | Account Segment 18 | | No/No | |
| Account Segment 19 | Account Segment 19 | | No/No | |
| Account Segment 20 | Account Segment 20 | | No/No | |
| Account Name | Nickname for the account | | No/No | |
| Currency Code | Currency Code | | No/No | |

## Requisition Event History

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
