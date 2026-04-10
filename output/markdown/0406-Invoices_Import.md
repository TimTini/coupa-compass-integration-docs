---
title: "Invoices Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/invoices-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/invoices-import"
status_code: 200
fetched_at: "2026-04-09T12:00:40+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Invoices Import"
---

# Invoices Import

## Overview

The Invoice Import process read files from the `./Incoming/Invoices/` SFTP folder. The files are moved to the archive folder located at `./Incoming/Archive/Invoices/` before being processed in alphanumeric order.

When including image scan attachments or file attachments, the invoice CSV and any relevant attachment files must be compressed together into a ZIP file. That ZIP file is what should be deposited on the SFTP folder. For more information, see [Coupa Scan One Integration](https://compass.coupa.com/en-us/products/total-spend-management-platform/integration-playbooks-and-resources/other-integration-playbooks/coupa-scan-one-integration).

You can load invoice files of any size as long as each ZIP file is less than 8MB. For Fast Invoice Entry, the limit is 2MB.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: If you need to load multiple invoices, combine the invoices into a single file. As every instance has a limited number of resources, loading multiple files can cause performance degradation.

For example, your Supplier needs to load invoices 1A, 1B, and 1C. Instead of loading each invoice as an individual file, combine the invoices into a single file in order to ensure optimal speed and results while processing.

## Unique Keys

Uniquely identifying an invoice requires the `Invoice Number` and one of `Supplier Name` or `Supplier Number`.

## Validations

The loader looks up supplier based first on number, then based on name. It then uses supplier and invoice number to look up the invoice.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: Depending on which invoicing configuration you have, some fields on this loader won't be applicable to you. For more information about what is applicable for your particular instance, see [Instance Specific Integration Documentation](https://compass.coupa.com/en-us/products/product-documentation/total-spend-management-platform/instance-specific-integration-documentation).

## Attachment Notes

When including file attachments, you need to compress the invoice CSV and the associated attachment files together in a ZIP file. The invoice CSV needs to be at the top level of the ZIP. You load that ZIP file through the integration.

- The attachment files are specified in the CSV. Each `Attachment`field can specify one file for your invoice file attachments. Use the syntax: `file://` (for example, `file://sample.pdf`). Do not enclose the file name in quotation marks. If your ZIP file structure uses sub-directories for your files, then specify the path to the file using syntax like: `file://FolderA/FolderB/sample.pdf`.

- For URL attachments, use `http://` or `https://` (for example, `http://www.coupa.com/resource/x12345.pdf`).

- Any other format is loaded as a TEXT attachment.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: For invoice_date and original_invoice_date, please provide the date only. Avoid adding the timestamp to avoid issues related to credit note linking.

## Invoice

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Invoice | No | No | | Type of header row. | |
| Invoice Number* | Yes | No | string(40) | Invoice Number this allocation belongs to | |
| Supplier Name | No | No | | Supplier Name | |
| Supplier Number | No | No | | Supplier Number | |
| Status | No | No | string(50) | Status | new, ap_hold, draft, on_hold, pending_receipt, rejected, abandoned, disputed, pending_approval, booking_hold, pending_action, approved, voided, processing, invalid, pending_action, payable_adjustment |
| Invoice Date* | Yes | No | datetime | Invoice Date | |
| Submit For Approval? | No | No | | Submit For Approval? | |
| Handling Amount | No | No | decimal(32,4) | Handling Amount | |
| Misc Amount | No | No | decimal(32,4) | Misc Amount | |
| Shipping Amount | No | No | decimal(32,4) | Shipping Amount | |
| Line Level Taxation* | Yes | No | boolean | Line Level Taxation | |
| Tax Amount | No | No | decimal | Tax Amount | |
| Tax Rate | No | No | float | Tax Rate | |
| Tax Code | No | No | string(255) | Tax Code | |
| Tax Rate Type | No | No | | Tax Rate Type | |
| Supplier Note | No | No | text | Supplier Note | |
| Payment Terms | No | No | | Payment Terms | |
| Shipping Terms | No | No | | Shipping Terms | |
| Requester Email | No | No | string | Requester Email | |
| Requester Name | No | No | string | Requester Name | |
| Requester Lookup Name | No | No | string | Requester Lookup Name | |
| Chart of Accounts* | Yes | No | | Chart of Accounts | |
| Currency | No | No | | Currency. Required when submit_for_approval is true. | |
| Contract Number | No | No | | Contract Number | |
| Image Scan Filename | No | No | | Image Scan Filename | |
| Image Scan URL | No | No | string(255) | Image Scan URL | |
| Local Currency Net | Yes | No | decimal(32,4) | Net Amount in local currency | |
| Taxes In Origin Country Currency | Yes | No | decimal(32,4) | Tax Amount in local currency | |
| Local Currency Gross | Yes | No | decimal(32,4) | Gross Amount in local currency | |
| Delivery Number | No | No | string(255) | Delivery Number | |
| Delivery Date | No | No | datetime | Delivery Date | |
| Margin Scheme | No | No | string(255) | Margin Scheme Description | margin_scheme_catalog_codes |
| Invoice Issuance Time | No | No | string(255) | Invoice Issuance Time | |
| Cash Register Operator | No | No | string(255) | Cash Register Operator | |
| Means Of Payment | No | No | string(255) | Means Of Payment | |
| Unique Identification Code Of Cash Receipt | No | Yes | string(255) | Identification Code Of Cash Receipt | |
| Security Code Of Issuer | No | No | string(255) | Security Code Of Issuer | |
| Cash Accounting Scheme Reference | No | No | string(255) | Non-blank Value Indicates Cash Accounting Scheme | |
| Exchange Rate | No | No | decimal(30,9) | Exchange Rate | |
| Gross Total | No | No | decimal | Gross Total. This field is for future use. Any value included in the field is not used, as this field is currently automatically calculated. | |
| Invoice Control Total | No | No | decimal | 'Invoice Control Total' should be equal to 'Invoicing Total With Taxes' (i.e Total + [Invoice Taxes + Linex Taxes + Charge Taxes]) | |
| Late Payment Penalties | No | No | string(255) | Late Payment Penalties | |
| Credit Reason | No | No | string(255) | The reason of creating the credit | credit_reason_catalog_codes |
| Early Payment Provisions | No | No | string(255) | Early Payment Provisions | |
| Pre-Payment Date | No | No | datetime | Pre-Payment Date | |
| Self Billing Reference | No | No | string(191) | Self Billing Reference - Used as billing reference in compliant countries like The Netherlands | |
| Discount Amount | No | No | decimal(32,4) | Discount Amount that supplier can provide - Used in compliant countries like The Netherlands | |
| Reverse Charge Reference | No | No | string(255) | Reverse Charge Reference | |
| Discount % | No | No | float | Discount % | |
| Credit Note differences with Original Invoice | No | No | decimal(30,4) | The difference between invoice total & VAT total with credit note while creating a credit note for compliant countries | |
| Original Value of Supply | No | No | decimal(46,20) | Original Value of Supply | |
| Correct Value of Supply | No | No | decimal(46,20) | Correct Value of Supply | |
| Customs Declaration Number | No | No | string(60) | Customs Declaration Number | |
| Customs Office | No | No | text | Customs Office | |
| Customs Declaration Date | No | No | datetime | Customs Declaration Date | |
| Payment Order Reference | No | No | string(255) | A code given by banks to use it instead of a bank account transfer. | |
| Payment Order Number | No | No | string(255) | Payment Order Number | |
| Resolution Number | No | No | string(255) | Resolution Number | |
| Amount of advance payment received | No | No | decimal(30,4) | Amount of advance payment received | |
| Type of Relationship | No | No | string(10) | MX only - Relationship (Credit Memo, Debit Note, etc) of this document to the associated invoice. Selected from CFDI catalog c_TipoRelacion | |
| Invoice Reference Number (IRN) | No | No | string(255) | The IRN is a unique ID generated using SHA256 algorithm and based on the parameters GST reg number, document number, financial year, and document type | |
| Series | No | No | string(30) | Series | |
| Folio Number | No | No | string(255) | Folio Number | |
| Buyer Representative Name | No | No | string(255) | Buyer Representative Name | |
| Supplier Representative Name | No | No | string(255) | Supplier Representative Name | |
| Payment Schedule Terms | No | No | string(255) | Payment Schedule Terms | |
| Transaction UUID | No | No | string(50) | Unique identifier created by the tax authority's system for a specific document | |
| Transaction Notification Date | No | No | datetime | Date on which the invoice is received from the tax authority's system | |
| VAT Chargeability System | No | No | string(255) | VAT Chargeability System | vat_chargeability_system_codes |
| Customer Account Number | No | No | string(255) | Customer Account Number | |
| Ship To Name | No | No | | Ship To Name | |
| Ship To Id | No | No | | Ship To Id | |
| Ship To Attention | No | No | | Ship To Attention | |
| Ship To Street1 | No | No | | Ship To Street1 | |
| Ship To Street2 | No | No | | Ship To Street2 | |
| Ship To City | No | No | | Ship To City | |
| Ship To State | No | No | | Ship To State | |
| Ship To Postal Code | No | No | | Ship To Postal Code | |
| Ship to Country Code | No | No | | Ship to Country Code | |
| Ship to Country Name | No | No | | Ship to Country Name | |
| Ship to Location Code | No | No | | Ship to Location Code | |
| Ship to VAT ID | No | No | | Ship to VAT ID | |
| Ship to Local Tax Number | No | No | | Ship to Local Tax Number | |
| Bill To Address Id | No | No | | Bill To Address Id | |
| Bill To Address Legal Entity Name | No | No | | Bill To Address Legal Entity Name | |
| Bill To Address Street | No | No | | Bill To Address Street | |
| Bill To Address City | No | No | | Bill To Address City | |
| Bill To Address Postal Code | No | No | | Bill To Address Postal Code | |
| Bill To Address Country Code | No | No | | Bill To Address Country Code | |
| Bill To Address Location Code | No | No | | Bill To Address Location Code | |
| Bill To Address VAT ID | No | No | | Bill To Address VAT ID | |
| Bill To Address Local Tax Number | No | No | | Bill To Address Local Tax Number | |
| Override Tax Country Code | No | No | | Override Tax Country Code | |
| Remit To Address Street1 | No | No | | Remit To Address Street1 | |
| Remit To Address Street2 | No | No | | Remit To Address Street2 | |
| Remit To Address City | No | No | | Remit To Address City | |
| Remit To Address State | No | No | | Remit To Address State | |
| Remit To Address Postal Code | No | No | | Remit To Address Postal Code | |
| Remit To Address Country Code | No | No | | Remit To Address Country Code | |
| Remit To Code | No | No | | Remit To Code | |
| Remit To Tax Prefix | No | No | | Remit To Tax Prefix | |
| Remit To Tax Number | No | No | | Remit To Tax Number | |
| Remit To Tax Country Code | No | No | | Remit To Tax Country Code | |
| Remit To VAT ID | No | No | | Remit To VAT ID | |
| Remit To Local Tax Number | No | No | | Remit To Local Tax Number | |
| Invoice From Address Street1 | No | No | | Invoice From Address Street1 | |
| Invoice From Address Street2 | No | No | | Invoice From Address Street2 | |
| Invoice From Address City | No | No | | Invoice From Address City | |
| Invoice From Address State | No | No | | Invoice From Address State | |
| Invoice From Address Postal Code | No | No | | Invoice From Address Postal Code | |
| Invoice From Address Country Code | No | No | | Invoice From Address Country Code | |
| Invoice From Code | No | No | | Invoice From Code | |
| Ship From Address Street1 | No | No | | Ship From Address Street1 | |
| Ship From Address Street2 | No | No | | Ship From Address Street2 | |
| Ship From Address City | No | No | | Ship From Address City | |
| Ship From Address State | No | No | | Ship From Address State | |
| Ship From Address Postal Code | No | No | | Ship From Address Postal Code | |
| Ship From Address Country Code | No | No | | Ship From Address Country Code | |
| Ship From Code | No | No | | Ship From Code | |
| Original invoice number | Yes | No | string(40) | Original invoice number. Available for credit notes only. This field is required when the presentation requires it. | |
| Original invoice date | Yes | No | datetime | Original invoice date. Available for credit notes only. This field is required when the presentation requires it. | |
| Is Credit Note | No | No | boolean | If any value is put in this column, Coupa will make the document a Credit Note. | |
| Disputed Invoice Number | No | No | | Disputed Invoice Number | |
| Dispute Resolution Credit Note Number | No | No | | This is the reference to a full adjustment credit note which has been processed to balance disputed invoice identified by Disputed Invoice Number field. | |
| Supplier Tax Number | No | No | | Supplier Tax Number | |
| Buyer Tax Number | No | No | | Buyer Tax Number | |
| Date of Discovery of Facts Decisive for Correction | No | No | datetime | Date of Discovery of Facts Decisive for Correction | |
| Place Of Supply | No | No | string(255) | Place Of Supply | |
| Split Payment Mechanism | No | No | boolean | Split Payment Mechanism | |
| Endorsement On Invoices | No | No | string(255) | Endorsement On Invoices | |
| New Means Of Transport | No | No | string(255) | New Means Of Transport | |
| Place Of Issuance | No | No | string(255) | Place Of Issuance | |
| Amount Of Advance Payment | No | No | decimal(46,20) | Amount Of Advance Payment | |
| Supplier Invoice Issuer Name | No | No | string(255) | Supplier Invoice Issuer Name | |
| Supplier Invoice Reviewer Name | No | No | string(255) | Supplier Invoice Reviewer Name | |
| Supplier Payment Collector Name | No | No | string(255) | Supplier Payment Collector Name | |
| Signed QR Code | No | No | text | Signed QR Code | |
| State Tax ID Number | No | No | string(255) | State Tax ID Number | |
| State Tax ID Number for Substitute Taxpayer | No | No | string(255) | State Tax ID Number for Substitute Taxpayer | |
| Municipality Tax ID Number | No | No | string(255) | Municipality Tax ID Number | |
| Serial Code of Fiscal Invoice | No | No | string(255) | Serial Code of Fiscal Invoice | |
| Verification Code | No | No | string(255) | Verification Code | |
| Type of Document | No | No | string(255) | Type of Document | type_of_document_catalog_codes |
| Protocol Number | No | No | string(255) | Protocol Number | |
| Nature of Operation | No | No | string(255) | Nature of Operation | |
| Type of Operation | No | No | string(255) | Type of Operation | |
| Freight Type | No | No | string(255) | Freight Type | |
| Vehicle License Plate | No | No | string(255) | Vehicle's License Plate | |
| National Enrollment of Conveyor | No | No | string(255) | National Enrollment of Conveyor | |
| Volume Amount | No | No | string(255) | Volume Amount | |
| Volume Gross Weight | No | No | string(255) | Volume Gross Weight | |
| Volume Liquid Weight | No | Yes | string(255) | Volume Liquid Weight | |
| Volume Brand | No | No | string(255) | Volume Brand | |
| Volume Type | No | No | string(255) | Volume Type | |
| Volume Numbering | No | No | string(255) | Volume Numbering | |
| Payment Agreement Notes | No | No | ReasonInsight | Payment Agreement Notes | |
| Attachment 1 | No | No | | Attachment 1 | |
| Attachment 2 | No | No | | Attachment 2 | |
| Attachment 3 | No | No | | Attachment 3 | |
| Attachment 4 | No | No | | Attachment 4 | |
| Attachment 5 | No | No | | Attachment 5 | |
| Attachment 6 | No | No | | Attachment 6 | |
| Attachment 7 | No | No | | Attachment 7 | |
| Attachment 8 | No | No | | Attachment 8 | |
| Attachment 9 | No | No | | Attachment 9 | |
| Attachment 10 | No | No | | Attachment 10 | |
| Ship To Street3 | No | No | | Ship To Street3 | |
| Ship To Street4 | No | No | | Ship To Street4 | |
| Remit To Address Street3 | No | No | | Remit To Address Street3 | |
| Remit To Address Street4 | No | No | | Remit To Address Street4 | |
| Invoice From Address Street3 | No | No | | Invoice From Address Street3 | |
| Invoice From Address Street4 | No | No | | Invoice From Address Street4 | |
| Ship From Address Street3 | No | No | | Ship From Address Street3 | |
| Ship From Address Street4 | No | No | | Ship From Address Street4 | |
| Invoice Charge | No | No | | Invoice Charge | |
| Line Number | No | No | | The child object's Line Number, used to add a tagging on a line | |
| Type* | Yes | No | | Type | |
| Description | No | No | | The Tagging's description | |
| Total* | Yes | No | | Invoice Charge Total | |
| Percent | No | No | | Percent | |
| Account Name | No | No | | Name of Account for this Allocation | |
| Account Code | No | No | | Account Code for this Allocation | |
| Billing Notes | No | No | | Account Billing Notes | |
| Account Segment 1 | No | No | | Account Segment 1 | |
| Account Segment 2 | No | No | | Account Segment 2 | |
| Account Segment 3 | No | No | | Account Segment 3 | |
| Account Segment 4 | No | No | | Account Segment 4 | |
| Account Segment 5 | No | No | | Account Segment 5 | |
| Account Segment 6 | No | No | | Account Segment 6 | |
| Account Segment 7 | No | No | | Account Segment 7 | |
| Account Segment 8 | No | No | | Account Segment 8 | |
| Account Segment 9 | No | No | | Account Segment 9 | |
| Account Segment 10 | No | No | | Account Segment 10 | |
| Account Segment 11 | No | No | | Account Segment 11 | |
| Account Segment 12 | No | No | | Account Segment 12 | |
| Account Segment 13 | No | No | | Account Segment 13 | |
| Account Segment 14 | No | No | | Account Segment 14 | |
| Account Segment 15 | No | No | | Account Segment 15 | |
| Account Segment 16 | No | No | | Account Segment 16 | |
| Account Segment 17 | No | No | | Account Segment 17 | |
| Account Segment 18 | No | No | | Account Segment 18 | |
| Account Segment 19 | No | No | | Account Segment 19 | |
| Account Segment 20 | No | No | | Account Segment 20 | |
| Budget Period Name | No | No | | Name of the existing budget period this falls under | |
| Line Tax Amount | No | No | | Line Tax Amount | |
| Line Tax Rate | No | No | | Line Tax Rate | |
| Line Tax Code | No | No | | Line Tax Code | |
| Line Tax Rate Type | No | No | | Line Tax Rate Type | |
| Exempt from Tax? | No | No | | Used for compliant invoicing to specify line is exempt from taxes | |
| Reverse Charge? | No | No | | Used for compliant invoicing to specify tax is a reverse charge | |
| Out of Scope? | No | No | | Used for compliant invoicing to specify tax is an out of scope | |
| Line Tax Location | No | No | | Line Tax Location | |
| Line Tax Description | No | No | | Line Tax Description | |
| Line Tax Supply Date | No | No | | Line Tax Supply Date | |
| Line Nature of Tax | No | No | | Line Nature of Tax | |
| Line Product Tax Classification | No | No | | Line Product Tax Classification | |
| Invoice Line | No | No | | Invoice Line | |
| Supplier Part Number | No | No | | Supplier Part Number | |
| Auxiliary Part Number | No | No | | Auxiliary Part Number | |
| Price* | Yes | No | | Price | |
| Quantity | No | No | | Quantity | |
| Bulk Price | No | No | | Price of the bulk material | |
| Bulk Price Qty | No | No | | Quantity of the bulk material | |
| Bulk Price UOM | No | No | | UOM of the bulk material | |
| Bulk Price Conversion Numerator | No | No | | Conversion Numerator of the Bulk Price UOM | |
| Bulk Price Conversion Denominator | No | No | | Conversion Denominator of the Bulk Price UOM | |
| Unit of Measure* | Yes | No | | Unit of Measure | |
| Category | No | No | | Category | |
| Subcategory | No | No | | Subcategory | |
| Deductibility | No | No | | Deductibility | |
| PO Number | No | No | | PO Number | |
| PO Line Number | No | No | | PO Line Number | |
| Net Weight | No | No | | Net Weight | |
| Weight UOM | No | No | | Weight UOM | |
| Price per Weight | No | No | | Price per Weight | |
| Match Reference | No | No | | Three-way match attribute to connect with Receipt and Invoice Header | |
| Delivery Note Number | No | No | | Delivery Note Number | |
| Original Date Of Supply | No | No | | Original Date Of Supply | |
| Commodity Name | No | No | | Name of the commodity | |
| HSN/SAC | No | No | | HSN/SAC | |
| UNSPSC | No | No | | UNSPSC | |
| Adjustment Type | No | No | | Adjustment Type | |
| Fiscal Code | No | No | | Fiscal Code | |
| Classification of Goods | No | No | | Classification of Goods | |
| Municipality Taxation Code | No | No | | Municipality Taxation Code | |
| Item Barcode | No | No | | Item Barcode | |
| Customer Accounting? | No | No | | Used to specify if tax is customer accounting | |
| Contract Name | No | No | | Contract Name | |
| Account Allocation | No | No | | Indication its an Invoice Line Allocation Record | |
| Amount | No | No | | Numerical Amount of the allocation in Invoice Line's currency | |
| Percent | No | No | | Allocation's Percentage of Invoice Line | |
| Tag | No | No | | Tag | |
| Object Number* | Yes | No | | The parent object's number, used to add a tagging to a header level object | |
| Name* | Yes | No | | The Tag's name | |
| System Tag | No | No | | System Tag, defaults to false if not specified | |

## Invoice Charge Columns

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Invoice Charge | Indicates the type of header row | No | No | - | Invoice Charge |
| Invoice Number* | Invoice Number | Yes | No | string(40) | any |
| Supplier Name | Supplier Name | No | No | string(100) | Must exist in Coupa |
| Supplier Number | Supplier Number | No | No | string(255) | Must exist in Coupa |
| Line Number | Invoice Line Number this allocation belongs to | No | No | integer(11) | any |
| Type* | Type | Yes | No | string(255) | InvoiceShippingCharge, InvoiceHandlingCharge, InvoiceMiscCharge |
| Description | Description | No | No | string(1550) | any |
| Total* | Invoice Charge Total | Yes | No | decimal(30,4) | any |
| Percent | Percent | No | No | decimal(16,10) | any |
| Line Tax Amount | Line Tax Amount | No | No | decimal(32,4) | any |
| Tax Rate | Tax Rate | No | No | decimal(16,10) | any |
| Tax Code | Tax Code | No | No | string(255) | Must exist in Coupa |
| Tax Rate Type | Tax Rate Type | No | No | string(255) | Must exist in Coupa |
| Line Tax Location | Line Tax Location | No | No | string(255) | any |
| Line Tax Description | Line Tax Description | No | No | string(255) | any |
| Line Tax Supply Date | Line Tax Supply Date | No | No | datetime | any |
| Account Name | Name of Account for this Allocation | No | No | string(1024) | any |
| Account Code | Account Code for this Allocation | No | No | string(1024) | any |
| Billing Notes | Account Billing Notes | No | No | text | any |
| Account Segment 1 | Account Segment 1 | No | No | string(100) | any |
| Account Segment 2 | Account Segment 2 | No | No | string(100) | any |
| Account Segment 3 | Account Segment 3 | No | No | string(100) | any |
| Account Segment 4 | Account Segment 4 | No | No | string(100) | any |
| Account Segment 5 | Account Segment 5 | No | No | string(100) | any |
| Account Segment 6 | Account Segment 6 | No | No | string(100) | any |
| Account Segment 7 | Account Segment 7 | No | No | string(100) | any |
| Account Segment 8 | Account Segment 8 | No | No | string(100) | any |
| Account Segment 9 | Account Segment 9 | No | No | string(100) | any |
| Account Segment 10 | Account Segment 10 | No | No | string(100) | any |
| Account Segment 11 | Account Segment 11 | No | No | string(100) | any |
| Account Segment 12 | Account Segment 12 | No | No | string(100) | any |
| Account Segment 13 | Account Segment 13 | No | No | string(100) | any |
| Account Segment 14 | Account Segment 14 | No | No | string(100) | any |
| Account Segment 15 | Account Segment 15 | No | No | string(100) | any |
| Account Segment 16 | Account Segment 16 | No | No | string(100) | any |
| Account Segment 17 | Account Segment 17 | No | No | string(100) | any |
| Account Segment 18 | Account Segment 18 | No | No | string(100) | any |
| Account Segment 19 | Account Segment 19 | No | No | string(100) | any |
| Account Segment 20 | Account Segment 20 | No | No | string(100) | any |
| Budget Period Name | Name of the existing budget period this falls under | No | No | string(100) | any |

## Invoice Line Columns

For invoice lines where the `PO Number` is specified, you must also provide `PO Line Number` or `Supplier Part Number` .

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Invoice Line | Indicates the type of header row | No | No | - | Invoice Line |
| Invoice Number* | Invoice Number* | Yes | No | string(40) | any |
| Supplier Name | Supplier Name | No | No | string(100) | Must exist in Coupa |
| Supplier Number | Supplier Number | No | No | string(255) | Must exist in Coupa |
| Line Number | Line Number | No | Yes | integer(11) | any |
| Description | The invoice line description, usually taken from the description of the item. | Yes | No | string(1550) | |
| Supplier Part Number | Supplier Part Number | No | No | string(255) | |
| Auxiliary Part Number | Auxiliary Part Number | FALSE | FALSE | string(255) | any |
| Price* | The price of the order line item. | Yes | No | decimal(46,20) | |
| Quantity | The quantity of the order line item. | No | No | decimal(30,6) | |
| Bulk Price | Bulk Price | No | No | decimal(30,6) | any |
| Bulk Price Qty | Bulk Price Qty | No | No | decimal(30,6) | any |
| Bulk Price UOM | Bulk Price UOM | No | No | int(11) | any |
| Bulk Price Conversion Numerator | Conversion Numerator of the Bulk Price UOM | No | No | | any |
| Bulk Price Conversion Denominator | Conversion Denominator of the Bulk Price UOM | No | No | | any |
| Line Tax Amount | Only has a value if the header item line level taxation is set to True. | No | No | decimal(32, 4) | |
| Line Tax Rate | The tax rate indicated on the invoice line. Only has a value if the header item line level taxation is set to True. | No | No | decimal(16,10) | any |
| Line Tax Code | The tax rate code for the line tax rate. Must match an existing tax rate code within Coupa. Only has a value if the header item line level taxation is set to True. | No | No | string(255) | Must exist in Coupa |
| Line Tax Rate Type | Line Tax Rate Type | No | No | string(255) | Must exist in Coupa |
| Exempt from Tax? | Used for compliant invoicing to specify line is exempt from taxes | No | No | boolean | |
| Reverse Charge? | Used for compliant invoicing to specify tax is a reverse charge | No | No | boolean | |
| Line Tax Location | Only has a value if the header item line level taxation is set to True. | No | No | string(255) | |
| Line Tax Description | The line level tax description. | No | No | string(255) | |
| Line Tax Supply Date | The line level tax supply date in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | No | No | datetime | YYYY-MM-DDTHH:MM:SS+HH:MM |
| Line Nature of Tax | Line Nature of Tax | No | No | | |
| Unit of Measure* | The unit of measure code. it must already exist in Coupa. | Yes | No | string(6) | |
| Category | Categroy | No | No | string(255) | any |
| Subcategory | Subcategory | No | No | string(255) | any |
| Deductibility | Deductibility | No | No | string(255) | any |
| PO Number | The number given to the corresponding purchase order within Coupa (if any). | No | No | string(20) | |
| PO Line Number | The line number of the corresponding purchase order line (if any). | No | No | string(255) | |
| Account Name | The account name from Coupa. | No | No | string(1024) | any |
| Account Code | The account code from Coupa. All segments are concatenated with a hyphen ( - ). | No | No | string(1024) | any |
| Billing Notes | A text field for adding notes to a billing line. | No | No | text(65,535) | any |
| Account Segment 1 | Account Segment 1 | No | No | string(100) | any |
| Account Segment 2 | Account Segment 2 | No | No | string(100) | any |
| Account Segment 3 | Account Segment 3 | No | No | string(100) | any |
| Account Segment 4 | Account Segment 4 | No | No | string(100) | any |
| Account Segment 5 | Account Segment 5 | No | No | string(100) | any |
| Account Segment 6 | Account Segment 6 | No | No | string(100) | any |
| Account Segment 7 | Account Segment 7 | No | No | string(100) | any |
| Account Segment 8 | Account Segment 8 | No | No | string(100) | any |
| Account Segment 9 | Account Segment 9 | No | No | string(100) | any |
| Account Segment 10 | Account Segment 10 | No | No | string(100) | any |
| Account Segment 11 | Account Segment 11 | No | No | string(100) | any |
| Account Segment 12 | Account Segment 12 | No | No | string(100) | any |
| Account Segment 13 | Account Segment 13 | No | No | string(100) | any |
| Account Segment 14 | Account Segment 14 | No | No | string(100) | any |
| Account Segment 15 | Account Segment 15 | No | No | string(100) | any |
| Account Segment 16 | Account Segment 16 | No | No | string(100) | any |
| Account Segment 17 | Account Segment 17 | No | No | string(100) | any |
| Account Segment 18 | Account Segment 18 | No | No | string(100) | any |
| Account Segment 19 | Account Segment 19 | No | No | string(100) | any |
| Account Segment 20 | Account Segment 20 | No | No | string(100) | any |
| Budget Period Name | Name of the existing budget period this falls under | No | No | string(100) | any |
| Net Weight | The net weight of the order line item. | No | No | decimal(30,6) | |
| Weight UOM | The unit of measure code of weight. It must already exist in Coupa. | No | No | string(6) | |
| Price per Weight | The price per weight of the order line item. | No | No | decimal(30,6) | |
| Match Reference | Three-way match attribute to connect with Receipt and Invoice Header | No | No | string(255) | |
| Delivery Note Number | Delivery Note Number | No | No | string(255) | |
| Commodity Name | Name of the commodity | No | No | string(255) | |
| HSN/SAC | HSN/SAC | No | No | string(255) | |
| UNSPSC | UNSPSC | No | No | string(255) | |
| Adjustment Type | Adjustment Type | No | No | string(255) | |
| Customer Accounting? | Used to specify if tax is customer accounting | No | No | boolean | |
| Original Date Of Supply | Original Date Of Supply | No | No | datetime | YYYY-MM-DDTHH:MM:SS+HH:MM |

## Invoice Account Allocation Columns

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Account Allocation | Indication its an Invoice Line Allocation Record | No | No | - | Account Allocation |
| Invoice Number* | Invoice Number* | Yes | No | string(40) | any |
| Invoice Line Number* | Invoice Line Number | No | No | integer(11) | any |
| Amount | Numerical Amount of the allocation in Invoice Line's currency | No | No | decimal(32,4) | any |
| Percent | Allocation's Percentage of Invoice Line | No | No | decimal(16,10) | any |
| Budget Period Name | Name of the existing budget period this falls under | No | No | string(100) | any |
| Account Name | Account Name | No | No | string(1024) | any |
| Account Code | Account Code | No | No | string(1024) | any |
| Account Segment 1 | Account Segment 1 | No | No | string(100) | any |
| Account Segment 2 | Account Segment 2 | No | No | string(100) | any |
| Account Segment 3 | Account Segment 3 | No | No | string(100) | any |
| Account Segment 4 | Account Segment 4 | No | No | string(100) | any |
| Account Segment 5 | Account Segment 5 | No | No | string(100) | any |
| Account Segment 6 | Account Segment 6 | No | No | string(100) | any |
| Account Segment 7 | Account Segment 7 | No | No | string(100) | any |
| Account Segment 8 | Account Segment 8 | No | No | string(100) | any |
| Account Segment 9 | Account Segment 9 | No | No | string(100) | any |
| Account Segment 10 | Account Segment 10 | No | No | string(100) | any |
| Account Segment 11 | Account Segment 11 | No | No | string(100) | any |
| Account Segment 12 | Account Segment 12 | No | No | string(100) | any |
| Account Segment 13 | Account Segment 13 | No | No | string(100) | any |
| Account Segment 14 | Account Segment 14 | No | No | string(100) | any |
| Account Segment 15 | Account Segment 15 | No | No | string(100) | any |
| Account Segment 16 | Account Segment 16 | No | No | string(100) | any |
| Account Segment 17 | Account Segment 17 | No | No | string(100) | any |
| Account Segment 18 | Account Segment 18 | No | No | string(100) | any |
| Account Segment 19 | Account Segment 19 | No | No | string(100) | any |
| Account Segment 20 | Account Segment 20 | No | No | string(100) | any |

## Tag Columns

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Tag | Indicates the type of header row | No | No | - | Tag |
| Object Number* | The parent object's number, used to add a tagging to a header level object | Yes | No | string(30) | any |
| Line Number | The invoice line | No | No | int(11) | any |
| Name* | The Tag's name | Yes | No | string(30) | any |
| Description | Description of the tag | No | No | text | any |
| System Tag | System Tag, defaults to false if not specified | No | No | boolean | Yes/No |

## Invoice Tax Columns

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Invoice Tax Line | Indicates the type of header row | No | No | - | Invoice Tax Line |
| Invoice Number* | Invoice Number | No | No | string(40) | any |
| Invoice Line Number | Include if line level tax | No | No | int(11) | any |
| Invoice Charge Number | Invoice Charge Number tracks the order of the charges. Typically, shipping charge is 1, handling charge is 2, and misc charge is 3. Numbering is not strictly enforced the line numbers to a specific type of charge.<br>The invoice charge number does not map to an invoice line number. All charges belong to the invoice itself.<br>An invoice can have shipping, handling, and/or misc charges. Each charge is a separate object in the database. Tax lines can be added against each charge. | No | No | integer(11) | any |
| Line Number | Line order for multiple tax lines, 1 if a single tax line | No | No | int(11) | any |
| Tax Amount | The amount of the tax | Yes | no | decimal(32,4) | any |
| Tax Rate | Tax Rate | No | No | decimal(16,10) | any |
| Tax Code | Tax Code | No | No | string(255) | Must exist in Coupa |
| Tax Rate Type | Tax Rate Type | No | No | string(255) | any |
| Tax Location | Tax Location | No | No | string(255) | any |
| Tax Description | Tax Description | No | No | string(255) | any |
| Tax Supply Date | Tax Supply Date | No | No | datetime | any |
| Taxable Amount | Compliance specific field for information only | No | No | decimal(32,4) | any |
| Type | Determines the type of tax. No value specified = TaxLine | No | No | string(255) | TaxLine, WithholdingTaxLine |
| Base Amount | Value of the taxable amount if different than the line total | No | No | decimal(30,4) | Any |

## Invoice Header Assignment

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Document* | Yes | No | | InvoiceHeader Id | |
| Assignee Type* | Yes | No | string(255) | Assignee Type | |
| Assignee* | Yes | No | | Assignee | |
| Comment | No | No | | Comment | |
| Supplier Name | No | No | | Supplier Name | |
| Supplier Number | No | No | | Supplier Number | |
| Invoice Number | No | No | | Invoice Number | |
| Invoice Date | No | No | | Invoice Date | |
| Action | No | No | | Action, possible values are Assign and Unassign. Default to Assign | |
