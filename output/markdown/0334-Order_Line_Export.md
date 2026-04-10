---
title: "Order Line Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/order-line-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/order-line-export"
status_code: 200
fetched_at: "2026-04-09T12:00:21+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Order Line Export"
---

# Order Line Export

Export of these records is included as a Standard CSV
Export.

## Order Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| accounting-total | Accounting Total for Line | decimal(32,4) | No/No | |
| accounting-total-currency | Currency used for Accounting Total | | No/No | |
| created-at | Line Created At Date | datetime | No/No | |
| description | Line Item Description | string(255) | Yes/No | |
| id | Coupa Internal Line ID | integer | No/No | |
| invoiced | Amount Invoiced | decimal(32,6) | No/No | |
| active-invoiced-amount | Active Invoiced Amount which includes Pending Approval and Approved Invoices | | No/No | |
| line-number | Line Number | string(255) | No/Yes | |
| need-by-date | Line Need By Date | string | No/No | |
| order-header-id | PO Number / Coupa Internal ID | integer | No/No | |
| price | Unit Price | decimal(30,6) | Yes/No | |
| quantity | Quantity Ordered | decimal(30,6) | No/No | |
| received | Quantity/Amount Received | integer | No/No | |
| source-part-num | Part Number - Determined by: For Catalog Items: Supplier Item Number For Catalog Item w/o Supplier Item Number: Item Number Non-Catalog Item: User Entered Item Number | string(255) | No/No | |
| status | Line Status | string(50) | No/No | |
| sub-line-num | <Reserved for future use> | integer | No/No | |
| supp-aux-part-num | Supplier Auxiliary Part Number (Punch Out) | text | No/No | |
| total | Total Amount | decimal(32,4) | No/No | |
| currency | Currency used for PO | | No/No | |
| line-type | Line Type | string(100) | No/No | |
| updated-at | Date Line Last Updated | datetime | No/No | |
| version | Line Version/Revision # | integer | No/No | |
| account-code | Account Code (combined segments) | | No/No | |
| segment-1 | Account Code Segment 1 | | No/No | |
| segment-2 | Account Code Segment 2 | | No/No | |
| segment-3 | Account Code Segment 3 | | No/No | |
| segment-4 | Account Code Segment 4 | | No/No | |
| segment-5 | Account Code Segment 5 | | No/No | |
| segment-6 | Account Code Segment 6 | | No/No | |
| segment-7 | Account Code Segment 7 | | No/No | |
| segment-8 | Account Code Segment 8 | | No/No | |
| segment-9 | Account Code Segment 9 | | No/No | |
| segment-10 | Account Code Segment 10 | | No/No | |
| segment-11 | Account Code Segment 11 | | No/No | |
| segment-12 | Account Code Segment 12 | | No/No | |
| segment-13 | Account Code Segment 13 | | No/No | |
| segment-14 | Account Code Segment 14 | | No/No | |
| segment-15 | Account Code Segment 15 | | No/No | |
| segment-16 | Account Code Segment 16 | | No/No | |
| segment-17 | Account Code Segment 17 | | No/No | |
| segment-18 | Account Code Segment 18 | | No/No | |
| segment-19 | Account Code Segment 19 | | No/No | |
| segment-20 | Account Code Segment 20 | | No/No | |
| account-name | Account Name | | No/No | |
| account-type | Chart of Accounts | | No/No | |
| contract-id | Coupa Contract Internal ID | integer | No/No | |
| contract-name | Contract Name | | No/No | |
| department | Department Name | | No/No | |
| created-by-email | Email of User who created order line | | No/No | |
| created-by-employee-number | Employee Number of User who created order line | | No/No | |
| created-by-firstname | First name of User who created order line | | No/No | |
| created-by-id | Coupa ID of User who created order line | integer | No/No | |
| created-by-lastname | Last name of User who created order line | | No/No | |
| created-by-login | Login name of User who created order line | | No/No | |
| supplier-id | Supplier Coupa internal ID number | integer | No/No | |
| supplier-name | Supplier Name | | No/No | |
| supplier-number | Supplier Number | | No/No | |
| uom | Unit of Measure | | No/No | |
| updated-by-email | Email of User last updated by | | No/No | |
| updated-by-employee-number | Employee Number of User last updated by | | No/No | |
| updated-by-firstname | First name of User last updated by | | No/No | |
| updated-by-id | Coupa ID of User last updated by | integer | No/No | |
| updated-by-lastname | Last name of User last updated by | | No/No | |
| updated-by-login | Login name of User last updated by | | No/No | |
| commodity | commodity | | No/No | |
| asn-quantity | ASN Quantity | decimal(30,6) | No/No | |

## Order Line Allocation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| order-header-id | PO Number / Coupa Internal ID | integer | No/No | |
| order-line-id | Coupa Purchase Order Line ID | integer | No/No | |
| order-line-num | Coupa Purchase Order Line Number | | No/No | |
| account-allocation-id | Unique allocation id (only used if split line accounting is in use for the given Line record) | integer | No/No | |
| account-allocation-sequence | Unique allocation sequential counter (only used if split line accounting is in use for the given Line record) | | No/No | |
| account-allocation-amount | Dollar amount for this allocation (only used if split line accounting is in use for the given Line record) | decimal(32,4) | No/No | |
| account-allocation-percent | Amount allocation percent (only used if split line accounting is in use for the given Line record) | decimal(16,10) | Yes/No | |
| account-code | Account code from Coupa (only used if split line accounting is in use for the given Line record) | | No/No | |
| account-active | Account active flag | | No/No | |
| segment-1 | Account Segment-1 | | No/No | |
| segment-2 | Account Segment-2 | | No/No | |
| segment-3 | Account Segment-3 | | No/No | |
| segment-4 | Account Segment-4 | | No/No | |
| segment-5 | Account Segment-5 | | No/No | |
| segment-6 | Account Segment-6 | | No/No | |
| segment-7 | Account Segment-7 | | No/No | |
| segment-8 | Account Ssegment-8 | | No/No | |
| segment-9 | Account Segment-9 | | No/No | |
| segment-10 | Account Segment-10 | | No/No | |
| segment-11 | Account Segment-11 | | No/No | |
| segment-12 | Account Segment-12 | | No/No | |
| segment-13 | Account Segment-13 | | No/No | |
| segment-14 | Account Segment-14 | | No/No | |
| segment-15 | Account Ssegment-15 | | No/No | |
| segment-16 | Account Segment-16 | | No/No | |
| segment-17 | Account Segment-17 | | No/No | |
| segment-18 | Account Segment-18 | | No/No | |
| segment-19 | Account Segment-19 | | No/No | |
| segment-20 | Account Segment-20 | | No/No | |
| account-name | Account name from Coupa | | No/No | |
| account-type | Chart of Accounts Name from Coupa | | No/No | |

## Order Line Confirmation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| id | Coupa's internal ID | integer | No/No | |
| status | PO Line Confirmation Status | string(255) | No/No | |
| confirm-by-hrs | Confirm By Hours | decimal(10,0) | No/No | |
| quantity | Quantity | | No/No | |
| price | Price | | No/No | |
| currency-id | Currency | | No/No | |
| order-line-id | Coupa's internal ID | integer | No/No | |
| order-line-version-id | Coupa's internal ID | integer | No/No | |
| Promised Date | Promised Date | | No/No | |
| order_header_confirmation_id | Coupa's internal ID | integer | No/No | |
| can-fulfill | Is supplier can fulfill the order? | integer | No/No | |
| proposed_by | Proposed by | string(255) | No/No | |
| created-at | Created Date | datetime | No/No | |
| updated-at | Last Updated at Date | datetime | No/No | |
| description | Line Item Description | | No/No | |
| uom | Unit of Measure | | No/No | |
| supplier-part-number | Supplier Part Number | | No/No | |
| supplier-auxiliary-part-number | Supplier Auxiliary Part Number | | No/No | |
| manufacturer-name | Manufacturer Name | | No/No | |
| manufacturer-part-number | Manufacturer Part Number | | No/No | |
| item-record-match-found | Item Record Match Found | | No/No | |
| item-change | Item Change | | No/No | |
| acted-on-behalf-of-supplier | Acted On Behalf Of Supplier | | No/No | |
| tags | Tags | Tag | No/No | |
| locked-for-integration-at | Locked For Integration At | datetime | No/No | |
| integration-version | Integration Version | integer | No/No | |
| custom-field-1 | Custom Field 1 | | No/No | |
| custom-field-2 | Custom Field 2 | | No/No | |
| custom-field-3 | Custom Field 3 | | No/No | |
| custom-field-4 | Custom Field 4 | | No/No | |
| custom-field-5 | Custom Field 5 | | No/No | |
| custom-field-6 | Custom Field 6 | | No/No | |
| custom-field-7 | Custom Field 7 | | No/No | |
| custom-field-8 | Custom Field 8 | | No/No | |
| custom-field-9 | Custom Field 9 | | No/No | |
| custom-field-10 | Custom Field 10 | | No/No | |
| custom-field-11 | Custom Field 11 | | No/No | |
| custom-field-12 | Custom Field 12 | | No/No | |
| custom-field-13 | Custom Field 13 | | No/No | |
| custom-field-14 | Custom Field 14 | | No/No | |
| custom-field-15 | Custom Field 15 | | No/No | |
| custom-field-16 | Custom Field 16 | | No/No | |
| custom-field-17 | Custom Field 17 | | No/No | |
| custom-field-18 | Custom Field 18 | | No/No | |
| custom-field-19 | Custom Field 19 | | No/No | |
| custom-field-20 | Custom Field 20 | | No/No | |
