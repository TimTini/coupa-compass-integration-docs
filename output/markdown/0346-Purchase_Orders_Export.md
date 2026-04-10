---
title: "Purchase Orders Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/purchase-orders-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/purchase-orders-export"
status_code: 200
fetched_at: "2026-04-09T12:00:25+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Purchase Orders Export"
---

# Purchase Orders Export

## Overview

The Purchase Order Export process from Coupa uses the Coupa API to query for all Purchase Orders that are issued and have not been exported. The frequency of the integration run is once every hour. The generated files will be placed into `./Outgoing/PurchaseOrders`. Once the files are successfully placed into the sFTP folder the purchase orders will be marked as exported.

Purchase Order Revisions can also be exported and will be placed into `./Outgoing/PurchaseOrders/`. Export of these records is included as a Standard CSV Export.

Coupa generally recommends that customers send POs to suppliers from the Coupa system, rather than issuing POs to suppliers from their ERP system. PO exports from Coupa are therefore generally done for purposes of reporting and analytics.

## Purchase Order

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| acknowledged-at | Has PO been acknowledged by Supplier? | datetime | No/No | |
| created-at | Date record was created in Coupa. | datetime | No/No | |
| id | Coupa's internal ID | integer | No/No | |
| status | PO Status | string(50) | No/No | |
| transmission-status | Transmission Status | | No/No | |
| updated-at | Last Updated at Date | datetime | No/No | |
| version | PO Supplier Version Number - Increase each time a PO is changed and triggers a resend to the supplier. | integer | No/No | |
| internal-revision | Internal Revision Number - Increases each time a change is made to a PO whether that change is internal or causes the PO to be resent to the supplier. | | No/No | |
| exported | Has the PO successfully been sent to target system? | | No/No | |
| accounting-total | Amount of document in Chart Of Accounts Accounting Currency | decimal | No/No | |
| accounting-total-currency | Currency Code for Accounting Total | | No/No | |
| created-by-email | Email of User who created purchase order | | No/No | |
| created-by-employee-number | Employee Number of User who created purchase order | | No/No | |
| created-by-firstname | First name of User who created purchase order | | No/No | |
| created-by-id | Coupa ID of User who created purchase order | integer | No/No | |
| created-by-lastname | Last name of User who created purchase order | | No/No | |
| created-by-login | Login name of User who created purchase order | | No/No | |
| requisition-id | Coupa ID of originating requisition | integer | No/No | |
| requester-email | Requesting account's email address | | No/No | |
| requester-employee-number | Requesting account's employee number | | No/No | |
| requester-firstname | Requesting account's First Name | | No/No | |
| requester-id | Requesting Account's ID | | No/No | |
| requester-lastname | Requesting Account's Last Name | | No/No | |
| requester-login | Requesting Account's Login | | No/No | |
| ship-to-attention | Ship To Address Attention Line | | No/No | |
| ship-to-address-city | Ship To Address City | | No/No | |
| ship-to-address-id | Ship To Address Internal Coupa ID | integer | No/No | |
| ship-to-address-name | Ship To Address Name | | No/No | |
| ship-to-address-postal-code | Ship To Address Postal Code | | No/No | |
| ship-to-address-state | Ship To Address State/Province | | No/No | |
| ship-to-address-street1 | Ship To Address Street Address | | No/No | |
| ship-to-address-street2 | Ship To Address Street Address Line 2 | | No/No | |
| ship-to-address-country | Country Code | | No/No | |
| ship-to-user-email | Email of User Ship To User | | No/No | |
| ship-to-user-employee-number | Employee Number of Ship To User | | No/No | |
| ship-to-user-firstname | First name of Ship To User | | No/No | |
| ship-to-user-id | Coupa ID of Ship To User | integer | No/No | |
| ship-to-user-lastname | Last name of Ship To User | | No/No | |
| ship-to-user-login | Login name of Ship To User | | No/No | |
| supplier-id | Supplier Coupa internal ID number | integer | No/No | |
| supplier-name | Supplier Name | | No/No | |
| supplier-number | Supplier Number | | No/No | |
| updated-by-email | Email of User last updated by | | No/No | |
| updated-by-employee-number | Employee Number of User last updated by | | No/No | |
| updated-by-firstname | First name of user last updated by | | No/No | |
| updated-by-id | Coupa ID of User last updated by | integer | No/No | |
| updated-by-lastname | Last name of User last updated by | | No/No | |
| updated-by-login | Login name of User last updated by | | No/No | |
| payment-terms-code | Payment Terms | | No/No | |
| payment-terms-days-for-discount-payment | Number of days to pay to receive discount | | No/No | |
| payment-terms-days-for-net-payment | Net Days for Payment | | No/No | |
| payment-terms-discount-rate | Discount Rate for payment within Discount Terms | | No/No | |
| Shipping-terms-code | Shipping Terms Code | | No/No | |
| attachment-text-concat | Concatenation of Text Attachment Text (Header Level) | string | No/No | |

## Purchase order line columns

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| type | Indicates record type | FALSE | FALSE | string | Line |
| accounting-total | Accounting Total for Line | FALSE | FALSE | decimal(32,4) | any |
| accounting-total-currency | Currency used for Accounting Total | FALSE | FALSE | string(6) | any |
| created-at | Line Created At Date | FALSE | FALSE | datetime | any |
| description | Line Item Description | TRUE | FALSE | string(255) | any |
| id | Coupa Internal Line ID | FALSE | FALSE | integer | any |
| invoiced | Amount Invoiced | FALSE | FALSE | decimal(30,6) | any |
| active-invoiced-amount | Active Invoiced Amount which includes Pending Approval and Approved Invoices | FALSE | FALSE | decimal(32,4) | any |
| line-number | Line Number | FALSE | TRUE | string(255) | any |
| need-by-date | Line Need By Date | FALSE | FALSE | datetime | any |
| order-header-id | PO Number / Coupa Internal ID | FALSE | FALSE | integer | any |
| price | Unit Price<br>Note<br>For languages that use spaces as a currency delimiter, the CSV export interprets the space as: `“ ` | TRUE | FALSE | decimal(30,6) | any |
| quantity | Quantity Ordered | FALSE | FALSE | decimal(30,6) | any |
| received | Quantity/Amount Received | FALSE | FALSE | decimal(32,4) | any |
| source-part-num | Part Number - Determined by: For Catalog Items: Supplier Item Number For Catalog Item w/o Supplier Item Number: Item Number Non-Catalog Item: User Entered Item Number | FALSE | FALSE | string(255) | any |
| status | Line Status | FALSE | FALSE | string(50) | any |
| sub-line-num | <Reserved for future use> | FALSE | FALSE | integer | any |
| supp-aux-part-num | Supplier Auxiliary Part Number (Punch Out) | FALSE | FALSE | string(255) | any |
| total | Total Amount | FALSE | FALSE | decimal(32,4) | any |
| currency | Currency used for PO | FALSE | FALSE | string(6) | any |
| type | Line Type | FALSE | FALSE | string(100) | any |
| updated-at | Date Line Last Updated | FALSE | FALSE | datetime | any |
| version | Line Version/Revision # | FALSE | FALSE | int(11) | any |
| account-code | Account Code (combined segments) | FALSE | FALSE | string(1024) | any |
| segment-1 | Account Code Segment 1 | FALSE | FALSE | string(100) | any |
| segment-2 | Account Code Segment 2 | FALSE | FALSE | string(100) | any |
| segment-3 | Account Code Segment 3 | FALSE | FALSE | string(100) | any |
| segment-4 | Account Code Segment 4 | FALSE | FALSE | string(100) | any |
| segment-5 | Account Code Segment 5 | FALSE | FALSE | string(100) | any |
| segment-6 | Account Code Segment 6 | FALSE | FALSE | string(100) | any |
| segment-7 | Account Code Segment 7 | FALSE | FALSE | string(100) | any |
| segment-8 | Account Code Segment 8 | FALSE | FALSE | string(100) | any |
| segment-9 | Account Code Segment 9 | FALSE | FALSE | string(100) | any |
| segment-10 | Account Code Segment 10 | FALSE | FALSE | string(100) | any |
| segment-11 | Account Code Segment 11 | FALSE | FALSE | string(100) | any |
| segment-12 | Account Code Segment 12 | FALSE | FALSE | string(100) | any |
| segment-13 | Account Code Segment 13 | FALSE | FALSE | string(100) | any |
| segment-14 | Account Code Segment 14 | FALSE | FALSE | string(100) | any |
| segment-15 | Account Code Segment 15 | FALSE | FALSE | string(100) | any |
| segment-16 | Account Code Segment 16 | FALSE | FALSE | string(100) | any |
| segment-17 | Account Code Segment 17 | FALSE | FALSE | string(100) | any |
| segment-18 | Account Code Segment 18 | FALSE | FALSE | string(100) | any |
| segment-19 | Account Code Segment 19 | FALSE | FALSE | string(100) | any |
| segment-20 | Account Code Segment 20 | FALSE | FALSE | string(100) | any |
| account-name | Account Name | FALSE | FALSE | string(1024) | any |
| account-type | Chart of Accounts | FALSE | FALSE | string(50) | any |
| contract-id | Coupa Contract Internal ID | FALSE | FALSE | integer | any |
| contract-name | Contract Name | FALSE | FALSE | string(100) | any |
| department | Department Name | FALSE | FALSE | string(255) | any |
| created-by-email | Email of User who created PO | FALSE | FALSE | string(255) | any |
| created-by-employee-number | Employee Number of User who created PO | FALSE | FALSE | string(255) | any |
| created-by-firstname | First name of User who created PO | FALSE | FALSE | string(40) | any |
| created-by-id | Coupa ID of User who created PO | FALSE | FALSE | int(11) | any |
| created-by-lastname | Last name of User who created PO | FALSE | FALSE | string(40) | any |
| created-by-login | Login name of User who created PO | FALSE | FALSE | string(255) | any |
| supplier-id | Supplier Coupa internal ID number | FALSE | FALSE | integer | any |
| supplier-name | Supplier Name | FALSE | FALSE | string(100) | any |
| supplier-number | Supplier Number | FALSE | FALSE | string(255) | any |
| uom | Unit of Measure | FALSE | FALSE | string(6) | any |
| updated-by-email | Email of User last updated by | FALSE | FALSE | string(255) | any |
| updated-by-employee-number | Employee Number of User last updated by | FALSE | FALSE | string(255) | any |
| updated-by-firstname | First name of User last updated by | FALSE | FALSE | string(40) | any |
| updated-by-id | Coupa ID of User last updated by | FALSE | FALSE | Int(11) | any |
| updated-by-lastname | Last name of User last updated by | FALSE | FALSE | string(40) | any |
| updated-by-login | Login name of User last updated by | FALSE | FALSE | string(255) | any |
| commodity | commodity | FALSE | FALSE | string(255) | any |
| requisition-line | Requisition Line ID | FALSE | FALSE | RequisitionLine | any |
| custom-field-1 | Integration Custom Field 1 | FALSE | FALSE | string(255) | any |
| custom-field-2 | Integration Custom Field 2 | FALSE | FALSE | string(255) | any |
| custom-field-3 | Integration Custom Field 3 | FALSE | FALSE | string(255) | any |
| custom-field-4 | Integration Custom Field 4 | FALSE | FALSE | string(255) | any |
| custom-field-5 | Integration Custom Field 5 | FALSE | FALSE | string(255) | any |
| custom-field-6 | Integration Custom Field 6 | FALSE | FALSE | string(255) | any |
| custom-field-7 | Integration Custom Field 7 | FALSE | FALSE | string(255) | any |
| custom-field-8 | Integration Custom Field 8 | FALSE | FALSE | string(255) | any |
| custom-field-9 | Integration Custom Field 9 | FALSE | FALSE | string(255) | any |
| custom-field-10 | Integration Custom Field 10 | FALSE | FALSE | string(255) | any |

## Purchase order line allocation columns

| **Column Name** | **Description** | **Req** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| type | Indicates record type | FALSE | FALSE | | any |
| order-header-id | PO Number / Coupa Internal ID | FALSE | FALSE | integer(11) | any |
| order-line-id | Coupa Purchase Order Line ID | FALSE | FALSE | integer(11) | any |
| order-line-num | Coupa Purchase Order Line Number | FALSE | FALSE | string(255) | any |
| account-allocation-id | Unique allocation id (only used if split line accounting is in use for the given Line record) | FALSE | FALSE | integer(11) | any |
| account-allocation-sequence | Unique allocation sequential counter (only used if split line accounting is in use for the given Line record) | FALSE | FALSE | integer(11) | any |
| account-allocation-amount | Dollar amount for this allocation (only used if split line accounting is in use for the given Line record) | FALSE | FALSE | decimal(32,4) | any |
| account-allocation-percent | Amount allocation percent (only used if split line accounting is in use for the given Line record) | TRUE | FALSE | decimal(16,10) | any |
| account-code | Account code from Coupa (only used if split line accounting is in use for the given Line record) | FALSE | FALSE | string(1024) | any |
| account-active | Account active flag | FALSE | FALSE | integer(1) | any |
| segment-1 | Account Segment-1 | FALSE | FALSE | string(100) | any |
| segment-2 | Account Segment-2 | FALSE | FALSE | string(100) | any |
| segment-3 | Account Segment-3 | FALSE | FALSE | string(100) | any |
| segment-4 | Account Segment-4 | FALSE | FALSE | string(100) | any |
| segment-5 | Account Segment-5 | FALSE | FALSE | string(100) | any |
| segment-6 | Account Segment-6 | FALSE | FALSE | string(100) | any |
| segment-7 | Account Segment-7 | FALSE | FALSE | string(100) | any |
| segment-8 | Account Ssegment-8 | FALSE | FALSE | string(100) | any |
| segment-9 | Account Segment-9 | FALSE | FALSE | string(100) | any |
| segment-10 | Account Segment-10 | FALSE | FALSE | string(100) | any |
| segment-11 | Account Segment-11 | FALSE | FALSE | string(100) | any |
| segment-12 | Account Segment-12 | FALSE | FALSE | string(100) | any |
| segment-13 | Account Segment-13 | FALSE | FALSE | string(100) | any |
| segment-14 | Account Segment-14 | FALSE | FALSE | string(100) | any |
| segment-15 | Account Ssegment-15 | FALSE | FALSE | string(100) | any |
| segment-16 | Account Segment-16 | FALSE | FALSE | string(100) | any |
| segment-17 | Account Segment-17 | FALSE | FALSE | string(100) | any |
| segment-18 | Account Segment-18 | FALSE | FALSE | string(100) | any |
| segment-19 | Account Segment-19 | FALSE | FALSE | string(100) | any |
| segment-20 | Account Segment-20 | FALSE | FALSE | string(100) | any |
| account-name | Account name from Coupa | FALSE | FALSE | string(1024) | any |
| account-type | Chart of Accounts Name from Coupa | FALSE | FALSE | string(50) | any |
| custom-field-1 | Integration Custom Field 1 | FALSE | FALSE | string(255) | any |
| custom-field-2 | Integration Custom Field 2 | FALSE | FALSE | string(255) | any |
| custom-field-3 | Integration Custom Field 3 | FALSE | FALSE | string(255) | any |
| custom-field-4 | Integration Custom Field 4 | FALSE | FALSE | string(255) | any |
| custom-field-5 | Integration Custom Field 5 | FALSE | FALSE | string(255) | any |
| custom-field-6 | Integration Custom Field 6 | FALSE | FALSE | string(255) | any |
| custom-field-7 | Integration Custom Field 7 | FALSE | FALSE | string(255) | any |
| custom-field-8 | Integration Custom Field 8 | FALSE | FALSE | string(255) | any |
| custom-field-9 | Integration Custom Field 9 | FALSE | FALSE | string(255) | any |
| custom-field-10 | Integration Custom Field 10 | FALSE | FALSE | string(255) | any |

## Purchase Order Change

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |

## Job Role Association

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| JobRoleAssociation | Specifies the header format for the row. | | No/No | |
| PO Number / Coupa Internal ID | The PO Number or Coupa Internal ID associated with the order header. | | No/No | |
| Coupa Purchase Order Line ID | The Coupa Purchase Order Line ID. | | No/No | |
| Coupa Purchase Order Line Number | The Coupa Purchase Order Line Number. | | No/No | |
| Job Role ID | The Coupa Job Role ID. | integer | No/No | |
| Job Role Name | The name of the job role. | | No/No | |
| Job Role Code | The code representing the job role. | | No/No | |
| Job Title ID | The Coupa Job Title ID. | integer | No/No | |
| Job Title | The name of the job title. | | No/No | |
| Category | The category of the job role. | | No/No | |
| Level | The level of the job role. | | No/No | |
| Source | The source of the job role information. | | No/No | |
| Work Location ID | The ID of the work location associated with the job role. | integer | No/No | |
| Work Location | The work location associated with the job role. | | No/No | |
| Work Arrangement | The work arrangement for the job role. | | No/No | |
| Working Hours | The working hours for the job role. | | No/No | |
| Created At | The timestamp when the record was created. | datetime | No/No | |
| Updated At | The timestamp when the record was last updated. | datetime | No/No | |

## Rate Cards

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| RateCardLine | Specifies the header format for the row. | | No/No | |
| PO Number / Coupa Internal ID | The PO Number or Coupa Internal ID associated with the order header. | | No/No | |
| Coupa Purchase Order Line ID | The Coupa Purchase Order Line ID. | | No/No | |
| Coupa Purchase Order Line Number | The Coupa Purchase Order Line Number. | | No/No | |
| Active | Indicates whether the rate card line is active. | boolean | No/No | |
| Name | The name of the rate card line. | string(255) | Yes/No | |
| Code | The code of the rate card line. | string(255) | No/No | |
| Type | The type of the rate card line. | | No/No | |
| Price | The price associated with the rate card line. | decimal(30,6) | Yes/No | |
| Unit of Measure | The unit of measure for the rate card line. | | No/No | |
| Currency | The currency of the rate card line. | | Yes/No | |
| Source | The source of the rate card line. | | No/No | |
| Created At | The timestamp when the rate card line was created. | datetime | No/No | |
| Updated At | The timestamp when the rate card line was last updated. | datetime | No/No | |
