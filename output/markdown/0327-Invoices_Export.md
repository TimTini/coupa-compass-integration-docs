---
title: "Invoices Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/invoices-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/invoices-export"
status_code: 200
fetched_at: "2026-04-09T12:00:19+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Invoices Export"
---

# Invoices Export

## Overview

The Invoice Export process from Coupa queries for all Invoices that are approved and have NOT been exported. The frequency of the integration run is once every hour. The generated files will be placed into `./Outgoing/Invoices` on the [Standard SFTP setup](https://coupadocs.atlassian.net/wiki/display/integrate/SFTP+Overview). Once the files are successfully placed into the sFTP folder the invoices will be marked/flagged as exported.

Export of these records is included as a Standard CSV Export.

## Voids

Voided Invoices can also be exported and will be placed into `./Outgoing/Invoices/`. Currently this is the only change to an Invoice that is captured in the integration.

## Row Types

The invoice export file can contains the following types of rows, each with its own column format:

- Invoice Header

- Invoice Line

- Invoice Line Allocation

- Invoice Charge

- Invoice Charge Allocation

- Tax Line

- Withholding Tax Line

- Matching Allocation

- Failed Tolerance

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: Invoice Header line counts include header rows and rows from the associated objects.

## Invoice

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, or Line Split or Tax Line. | | No/No | |
| id | The unique identifier Coupa assigned to the invoice. | integer | No/No | |
| created-at | When the invoice was created in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ. | datetime | No/No | |
| updated-at | When the invoice was last updated in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ. | datetime | No/No | |
| status | The current status of the invoice. Possible values are: new, ap_hold, draft, on_hold, pending_receipt, disputed, pending_approval, approved, voided, booking_hold, save_as_draft, abandoned | string(50) | No/No | |
| internal-note | Text field for comments made by employees. Not visible to the supplier. | text | No/No | |
| invoice-date | The date of the invoice in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ. | datetime | Yes/No | |
| delivery-date | The date of supply in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ. | datetime | No/No | |
| invoice-number | The user-created invoice number. | string(40) | Yes/No | |
| line-level-taxation | Flag indicating if the invoice has taxes at the line level. True or False. If True, adds fourth header: Tax Line. | boolean | Yes/No | |
| supplier-note | Text field for comments from the supplier. Visible to both Coupa users and the supplier. | text | No/No | |
| header-tax-amount | The amount of tax calculated on the invoice summary. | decimal | No/No | |
| header-tax-rate | The tax rate indicated on the invoice summary. | | No/No | |
| header-tax-code | The tax rate code for the invoice summary tax rate. Must match an existing tax rate code within Coupa. | | No/No | |
| paid | Flag indicating if the invoice was paid or not. Manually set. True or False. Default is False. | boolean | No/No | |
| payment-date | The date of the invoice was marked as paid in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| payment-notes | Text field for comments on the payment. Visible only to Coupa users. | text | No/No | |
| exported | Flag indicating if the invoice was exported to the ERP. True or False. | | No/No | |
| account-type-id | The unique identifier Coupa assigned to the Chart of Accounts. | integer | No/No | |
| account-type-name | The name of the Chart of Accounts within Coupa. | | No/No | |
| payment-term | The payment term code on the invoice. | | No/No | |
| handling-amount | Summary handling amount added to the invoice by the supplier. | decimal(32,4) | No/No | |
| misc-amount | Summary charge added to the invoice by the supplier. | decimal(32,4) | No/No | |
| shipping-amount | Summary shipping charge added to the invoice by the supplier. | decimal(32,4) | No/No | |
| total | The total amount of the invoice, including all summary amounts. | decimal | No/No | |
| currency | The currency code of the transaction. | | No/No | |
| accounting-total-amount | The total amount of the invoice using the Chart of Accounts currency. Doesn't include line and summary amounts. | decimal | No/No | |
| accounting-total-currency | The currency code of the Chart of Accounts. | | No/No | |
| supplier-id | The unique identifier Coupa assigned to the supplier. | integer | Yes/No | |
| supplier-name | The name of the supplier. | string(100) | No/No | |
| supplier-number | The number of the supplier. | | No/No | |
| created-by-email | The email address of the user who created the invoice. | | No/No | |
| created-by-employee-number | The employee number of the user who created the invoice. | | No/No | |
| created-by-login | The login name of the user who created the invoice. | | No/No | |
| updated-by-email | The email address of the user who last updated the invoice. | | No/No | |
| updated-by-employee-number | The employee number of the user who last updated the invoice. | | No/No | |
| updated-by-login | The login name of the user who last updated the invoice. | | No/No | |
| attachment-texts | The URLs of the attached files. The files can be set to the supplier, but cannot be downloaded as part of the CSV export. | string | No/No | |
| comments | Not currently used. | string(255) | No/No | |
| remit-to-address-code | Remit to Address Code | | No/No | |
| remit-to-address-attention | Remit to Address Attention | | No/No | |
| remit-to-address-street1 | Remit to Address Line 1 | | No/No | |
| remit-to-address-street2 | Remit to Address Line 2 | | No/No | |
| remit-to-address-city | Remit to Address City | | No/No | |
| remit-to-address-state | Remit to Address State | | No/No | |
| remit-to-address-postal-code | Remit to Address Postal Code | | No/No | |
| remit-to-address-country-code | Remit to Address Country Code | | No/No | |
| remit-to-address-country-name | Remit To Address Country Name | | No/No | |
| remit-to-address-name | Remit To Address Name | | No/No | |
| remit-to-address-vat-number | The VAT number associated with the remit-to address (for tax and compliance purposes). | | No/No | |
| remit-to-address-vat-country-code | The country code for the remit-to address (for tax and compliance purposes). | | No/No | |
| remit-to-address-vat-country-name | The country name for the remit-to address (for tax and compliance purposes). | | No/No | |
| supplier-vat-number | The VAT number of the supplier. | | No/No | |
| supplier-vat-country-code | The VAT country code of the supplier. | | No/No | |
| document-type | The type of document. Possible values are Invoice or Credit Note, or nil. | string | No/No | |
| original-invoice-number | The credit note must refer to the original invoice. Required if document-type is set to Credit Note. | string(40) | Yes/No | |
| original-invoice-date | The date that the original invoice was issued. | datetime | Yes/No | |
| canceled | Balanced out transaction and no payment needed. | | No/No | |
| bill-to-address-legal-entity-name | The legal name of the bill-to address company. This is often different the then company name | | No/No | |
| bill-to-address-attention | The contact person at the bill-to address. | | No/No | |
| bill-to-address-street1 | The first bill-to address line. | | No/No | |
| bill-to-address-street2 | The second bill-to address line. | | No/No | |
| bill-to-address-city | The bill-to address city. | | No/No | |
| bill-to-address-state | The bill-to address state. | | No/No | |
| bill-to-address-postal-code | The bill-to address zip or postal code. | | No/No | |
| bill-to-address-country-code | The bill-to address country code. | | No/No | |
| bill-to-address-country-name | The bill-to address country name. | | No/No | |
| bill-to-address-name | The user-friendly name given to the bill-to address to make it more easily identifiable. | | No/No | |
| ship-to-address-attention | The contact person at the bill-to address. | | No/No | |
| ship-to-address-street1 | The first ship-to address line. | | No/No | |
| ship-to-address-street2 | The second ship-to address line. | | No/No | |
| ship-to-address-city | The ship-to address city. | | No/No | |
| ship-to-address-state | The ship-to address state or province. | | No/No | |
| ship-to-address-postal-code | The ship-to address zip or postal code. | | No/No | |
| ship-to-address-country-code | The ship-to address country code. | | No/No | |
| ship-to-address-country-name | The ship-to address country name. | | No/No | |
| ship-to-address-name | The user-friendly name given to the ship-to address to make it more easily identifiable. | | No/No | |
| supplier-remit-to-code | The name/code given to the supplier remit-to address by the supplier | | No/No | |
| supplier-remit-to-supplier-name | The user-friendly name given to the remit-to address by the supplier to make it more easily identifiable | | No/No | |
| supplier-remit-to-street1 | The supplier-created remit-to first address line. | | No/No | |
| supplier-remit-to-street2 | The supplier-created remit-to second address line. | | No/No | |
| supplier-remit-to-city | The supplier-created remit-to city. | | No/No | |
| supplier-remit-to-state | The supplier-created remit-to state. | | No/No | |
| supplier-remit-to-postal-code | The supplier-created remit-to zip or postal code. | | No/No | |
| supplier-remit-to-country-code | The supplier-created remit-to country code. | | No/No | |
| supplier-remit-to-country-name | The supplier-created remit-to country name. | | No/No | |
| Fiscal Rep. Name | Fiscal Rep. Name | | No/No | |
| Fiscal Rep. VAT ID | Fiscal Rep. Vat Id | | No/No | |
| Fiscal Rep. Address Code | Fiscal Rep. Address Code | | No/No | |
| Fiscal Rep. Address Street 1 | Fiscal Rep. Address Street 1 | | No/No | |
| Fiscal Rep. Address Street 2 | Fiscal Rep. Address Street 2 | | No/No | |
| Fiscal Rep. Address City | Fiscal Rep. Address City | | No/No | |
| Fiscal Rep. Address State | Fiscal Rep. Address State | | No/No | |
| Fiscal Rep. Address Postal Code | Fiscal Rep. Address Postal Code | | No/No | |
| Fiscal Rep. Address Country Code | Fiscal Rep. Address Country Code | | No/No | |
| discount_due_date | The date the invoice needs to be paid by in order to get the early-payment discount. Calculated by Coupa based on payment-term in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| net_due_date | The date the invoice needs to be paid by. Calculated by Coupa based payment-term in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| discount_amount | The value of the discount if the invoice is paid by the discount_due_date. Calculated by Coupa basedtotal and payment-term. | decimal(32,4) | No/No | |
| late-payment-penalties | Late Payment Penalties | string(255) | No/No | |
| margin-scheme | A reference to the margin scheme used | string(255) | No/No | |
| cash-accounting-scheme-reference | A reference to the cash accounting scheme used | string(255) | No/No | |
| exchange-rate | Exchange Rate | decimal(30,9) | No/No | |
| early-payment-provisions | Early Payment Provisions (This field has been deprecated) | string(255) | No/No | |
| pre-payment-date | Pre-Payment Date | datetime | No/No | |
| reverse-charge-reference | Reverse Charge Reference | string(255) | No/No | |
| discount-percent | Discount % | float | No/No | |
| credit-note-differences-with-original-invoice | Credit Note differences with Original Invoice | decimal(30,4) | No/No | |
| customs-declaration-number | Customs Declaration Number | string(60) | No/No | |
| customs-office | Customs Office | text | No/No | |
| customs-declaration-date | Customs Declaration Date | datetime | No/No | |
| payment-order-reference | A code given by banks to use it instead of a bank account transfer. | string(255) | No/No | |
| payment-order-number | Payment Order Number | | No/No | |
| Resolution Number | Resolution Number | | No/No | |
| advance-payment-received-amount | Amount of advance payment received | decimal(30,4) | No/No | |
| series | The serial number used by the Company for internal control of the information. | string(30) | No/No | |
| folio-number | The internal folio number used by the Company. | string(255) | No/No | |
| buyer-representative-name | Buyer Representative Name | | No/No | |
| supplier-representative-name | Supplier Representative Name | | No/No | |
| payment-schedule-terms | Payment Schedule Terms | | No/No | |
| vat-chargeability-system | VAT Chargeability System | | No/No | |
| customer-account-number | Customer Account Number | | No/No | |
| use-of-invoice | The purpose invoice is going to be used for. | string(10) | No/No | |
| form-of-payment | The specific code in accordance with a catalogue: cash, check, transfer of funds, etc. | string(10) | No/No | |
| type-of-receipt | Type of the invoice: income, expense, transfer, payroll or payment. | string(10) | No/No | |
| payment-method | Installments or lump sum payments. | string(10) | No/No | |
| issuance-place | Issuance Place | string(255) | No/No | |
| confirmation | This is a unique number provided by the Tax Authorities or the PAC. | string(255) | No/No | |
| withholding-tax-override | Withholding Tax Override | decimal(30,3) | No/No | |
| type-of-relationship | Relationship of this document to its parent invoice. Chosen from a catalog. | string(10) | No/No | |
| invoice-reference-number | The IRN is a unique ID generated using SHA256 algorithm and based on the parameters GST reg number, document number, financial year, and document type | string(255) | No/No | |
| gross-total | Gross Total | decimal | No/No | |
| registered-company-registration-number | Registration number of the registered company | | No/No | |
| registered-company-place-of-registration | Place of registration of the registered company | | No/No | |
| registered-company-type | The type of the registered company | | No/No | |
| registered-company-managing-directors | A list of managing directors of the registered company | | No/No | |
| credit-reason | The reason of creating the credit | string(255) | No/No | |
| registered-company-permit-number | Permit number of the registered company | | No/No | |
| registered-company-permit-date | Permit date of the registered company | | No/No | |
| registered-company-liquidator-name | Liquidator name of the registered company | | No/No | |
| registered-company-share-capital | Share capital of the registered company | | No/No | |
| Tax Nature | Estonia compliance required field | | No/No | |
| registered-company-unique-shareholder | Unique shareholder of the registered company | | No/No | |
| registered-company-liable-company | Liable company of the registered company | | No/No | |
| registered-company-tax-regime | Tax Regime of the registered company | | No/No | |
| registered-company-legal-status | Legal status of the company (for tax and compliance purposes). | | No/No | |
| QST Registration Number | QST Registration Number | | No/No | |
| Authorised Person | Authorised Person | | No/No | |
| Authorised Person Address | Authorised Person Address | | No/No | |
| Authorised Person VAT ID | Authorised Person VAT ID | | No/No | |
| Date of Registration | Date of Registration | | No/No | |
| Sole Registration Code | Sole Registration Code | | No/No | |
| registered-company-mercantile-register | Mercantile Register | | No/No | |
| origin-currency-net | Net Amount in local currency | decimal(32,4) | Yes/No | |
| taxes-in-origin-country-currency | Tax Amount in local currency | decimal(32,4) | Yes/No | |
| origin-currency-gross | Gross Amount in local currency | decimal(32,4) | Yes/No | |
| self-billing-reference | Self billing reference - used for compliant countries like The Netherlands | string(191) | No/No | |
| registered-company-legal-type | Legal type of the company (for tax and compliance purposes). | | No/No | |
| registered-company-registered-seat | Registered seat of the company (for tax and compliance purposes). | | No/No | |
| registered-company-chairman-of-the-board | Name of the chairperson of the board (for tax and compliance purposes). | | No/No | |
| registered-company-court-of-registration | Court where the company is registered (for tax and compliance purposes). | | No/No | |
| registered-company-liquidation-remark | Remark if the company is in liquidation (for tax and compliance purposes). | | No/No | |
| registered-company-commercial-register-number | Commercial register number of the company (for tax and compliance purposes). | | No/No | |
| registered-company-license-number | Company License Number | | No/No | |
| registered-company-register-legal-entities | Register Legal Entities | | No/No | |
| registered-company-name | Registered Company Name | | No/No | |
| company-in-examinership | Company in examinership | | No/No | |
| company-is-being-wound-up | Company is being wound up | | No/No | |
| company-receiver-appointed | Receiver of the property of a company has been appointed | | No/No | |
| preference-agreement | Preference Agreement | | No/No | |
| file-reference-number | File Reference No. | | No/No | |
| number-of-issued-stocks | Number of Issued Stocks | | No/No | |
| issued_share-capital | Unpaid Share Capital | | No/No | |
| supplier-telephone-number | Supplier Telephone Number | | No/No | |
| permanent-account-number | Permanent Account Number (PAN) | | No/No | |
| Disputed Invoice Number | Disputed Invoice Number | | No/No | |
| Channel | Channel the invoice was created from | string(80) | No/No | |
| Taxable Amount | Taxable Amount | | No/No | |
| invoice-from-code | The name/code given to the supplier invoice-from address by the supplier. | | No/No | |
| invoice-from-supplier-name | The user-friendly name given to the invoice-from address by the supplier to make it more easily identifiable | | No/No | |
| invoice-from-street1 | The supplier-created invoice-from first address line. | | No/No | |
| invoice-from-street2 | The supplier-created invoice-from second address line. | | No/No | |
| invoice-from-city | The supplier-created invoice-from city. | | No/No | |
| invoice-from-state | The supplier-created invoice-from state. | | No/No | |
| invoice-from-postal-code | The supplier-created invoice-from zip or postal code. | | No/No | |
| invoice-from-country-code | The supplier-created invoice-from country code. | | No/No | |
| invoice-from-country-name | The supplier-created invoice-from country name. | | No/No | |
| ship-from-code | The name/code given to the supplier ship-from address by the supplier | | No/No | |
| ship-from-supplier-name | The user-friendly name given to the ship-from address by the supplier to make it more easily identifiable | | No/No | |
| ship-from-street1 | The supplier-created ship-from first address line. | | No/No | |
| ship-from-street2 | The supplier-created ship-from second address line. | | No/No | |
| ship-from-city | The supplier-created ship-from city. | | No/No | |
| ship-from-state | The supplier-created ship-from state. | | No/No | |
| ship-from-postal-code | The supplier-created ship-from zip or postal code. | | No/No | |
| ship-from-country-code | The supplier-created ship-from country code. | | No/No | |
| ship-from-country-name | The supplier-created ship-from country name. | | No/No | |
| supplier-tax-registration-number | The supplier-created supplier-tax-number. | | No/No | |
| supplier-tax-registration-country-code | The supplier-created supplier-tax-registration country code. | | No/No | |
| supplier-tax-registration-country-name | The supplier-created supplier-tax-registration country name. | | No/No | |
| supplier-tax-registration-local | The supplier-created supplier-tax-registration local indicator. | | No/No | |
| buyer-tax-registration-number | The buyer-created buyer-tax-number. | | No/No | |
| buyer-tax-registration-country-code | The buyer-created buyer-tax-registration country code. | | No/No | |
| buyer-tax-registration-country-name | The buyer-created buyer-tax-registration country name. | | No/No | |
| buyer-tax-registration-local | The buyer-created buyer-tax-registration local indicator. | | No/No | |
| dispute-method | Dispute Method, Possible values are: Auto, Manual | string(10) | No/No | |
| is-ers-invoice | Is ERS Invoice | boolean | No/No | |
| date-received | The date when the invoice is received by enterprise via email | | No/No | |
| sender-email | The sender email who sent the invoice to enterprise via email | | No/No | |
| inbox-name | Inbox which the invoice was received into | | No/No | |
| amount-due | Amount due to the supplier - Invoice Total without withholding and customer accounting taxes | decimal(46,6) | No/No | |
| tax-due-to-supplier | Tax due to the supplier | decimal(46,6) | No/No | |
| customer-accounting-tax | Customer accounting tax | decimal(46,6) | No/No | |
| payment-channel | Where the invoice payment will be handled. Examples are ERP, Coupa Pay Virtual Card, Coupa Pay Invoice | string(40) | No/No | |
| date-of-discovery-of-facts-decisive-for-correction | Date of Discovery of Facts Decisive for Correction | datetime | No/No | |
| place-of-supply | Place Of Supply | string(255) | No/No | |
| split-payment-mechanism | Split Payment Mechanism | boolean | No/No | |
| gross-total-less-discount | Total less discount | decimal(32,4) | No/No | |
| net-total-less-discount | Net total less discount | decimal(32,4) | No/No | |
| total-taxes-less-discount | Total taxes less discount | decimal(32,4) | No/No | |
| customer-accounting-tax-less-discount | Customer accounting tax less discount | decimal(32,4) | No/No | |
| amount-due-less-discount | Amount due less discount | decimal(32,4) | No/No | |
| endorsement-on-invoices | Endorsement On Invoices | string(255) | No/No | |
| new-means-of-transport | New Means Of Transport | string(255) | No/No | |
| place-of-issuance | Place Of Issuance | string(255) | No/No | |
| amount-of-advance-payment | Amount Of Advance Payment | decimal(46,20) | No/No | |
| transaction-uuid | Unique identifier created by the tax authority's system for a specific document | string(50) | No/No | |
| transaction-notification-date | Date on which the invoice is received from the tax authority's system | datetime | No/No | |
| supplier-invoice-issuer-name | Supplier Invoice Issuer Name | string(255) | No/No | |
| supplier-invoice_reviewer-name | Supplier Invoice Reviewer Name | string(255) | No/No | |
| supplier-payment-collector-name | Supplier Payment Collector Name | string(255) | No/No | |
| invoice-issuance-time | Invoice Issuance Time | | No/No | |
| cash-register-operator-id | Cash Register Operator | | No/No | |
| means-of-payment | Means Of Payment | | No/No | |
| unique-identification-code-of-cash-receipt | Unique Identification Code Of Cash Receipt | | No/No | |
| security-code-of-issuer | Security Code Of Issuer | | No/No | |
| state-tax-number | State Tax ID Number | | No/No | |
| state-tax-number-for-substitute-taxpayer | State Tax ID Number for Substitute Taxpayer | | No/No | |
| municipal-tax-number | Municipality Tax ID Number | | No/No | |
| serial-code-of-fiscal-invoice | Serial Code of Fiscal Invoice | | No/No | |
| verification-code | Verification Code | | No/No | |
| type-of-document | Type of Document | | No/No | |
| protocol-number | Protocol Number | | No/No | |
| nature-of-operation | Nature of Operation | | No/No | |
| type-of-operation | Type of Operation | | No/No | |
| freight-type | Freight Type | | No/No | |
| vehicle-license-plate | Vehicle License Plate | | No/No | |
| national-enrollment-of-conveyor | National Enrollment of Conveyor | | No/No | |
| volume-amount | Volume Amount | | No/No | |
| volume-gross-weight | Volume Gross Weight | | No/No | |
| volume-liquid-weight | Volume Liquid Weight | | No/No | |
| volume-brand | Volume Brand | | No/No | |
| volume-type | Volume Type | | No/No | |
| volume-numbering | Volume Numbering | | No/No | |
| currency-tax-rounding-mode | Currency Tax Rounding Method | | No/No | |
| payment-agreement-notes | Payment Agreement Notes | ReasonInsight | No/No | |
| parent-invoice-header-id | Parent Invoice Header ID | integer | No/No | |

## Invoice Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | integer | No/No | |
| invoice-line-id | The unique identifier Coupa assigns to the invoice line. | integer | No/No | |
| created-at | When the invoice line was created at in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| updated-at | When the invoice line was last updated at in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| total | The total amount of the invoice, excluding all distributed summary amounts. | decimal(46,20) | No/No | |
| accounting-total | The total amount of the invoice line using the Chart of Accounts currency. | decimal(46,20) | No/No | |
| accounting-total-currency | The currency code of the Chart of Accounts. | | No/No | |
| line-num | The line number of the invoice line, as it appears on the invoice. Line numbers aren't necessarily listed sequential, but will appear sequentially on the invoice. | integer | No/No | |
| description | The invoice line description, usually taken from the description of the item. | string(1550) | Yes/No | |
| order-header-num | The unique identifier assigned to the corresponding purchase order within Coupa (if any). | | No/No | |
| po-number | The number given to the corresponding purchase order within Coupa (if any). | | No/No | |
| order-header-requested-by-email | The email address of the user who created the corresponding purchase order. | | No/No | |
| order-header-requested-by-employee-number | The employee number of the user who created the purchase order. | | No/No | |
| order-header-requested-by-login | the username of the person who created the purchase order. | | No/No | |
| order-line-id | The unique identifier Coupa assigns to the corresponding line on the purchase order (if any). | integer | No/No | |
| order-line-num | The line number of the corresponding purchase order line (if any). | | No/No | |
| order-line-commodity | The commodity ID of the line item on the purchase order (if any). | | No/No | |
| price | The price of the order line item. | decimal(46,20) | Yes/No | |
| quantity | The quantity of the order line item. | decimal(30,6) | No/No | |
| uom | The unit of measure code. it must already exist in Coupa. | | No/No | |
| price-per-weight | The price per weight of the order line item. | decimal(30,6) | No/No | |
| net-weight | The net weight of the order line item. | decimal(30,6) | No/No | |
| weight-uom | The unit of measure code of weight. it must already exist in Coupa. | | No/No | |
| bulk-price | Describes the non unit quantity price. This can be used to provide price agreed for a bulk quantity. This should be accompanied with 'Bulk Price Quantity' and optionally 'Bulk Price UoM', 'Bulk Price Conversion Numerator' and 'Bulk Price Conversion Denominator'. | | No/No | |
| bulk-price-qty | Describes the number of units of the line item the 'Bulk Price' describes the price for. | | No/No | |
| bulk-price-uom | Describes the UoM to express the Bulk Price. This is required if the line UoM is different than 'Bulk Price UoM'. | | No/No | |
| bulk-price-conversion-numerator | Numerator value for the ratio to convert from 'Bulk Price UoM' to line UoM. Value defaults from corresponding PO line if invoice line UoM matches PO line UoM and the PO Bulk Price UoM matches the invoice 'Bulk Price UoM'. | | No/No | |
| bulk-price-conversion-denominator | Denominator value for the ratio to convert from 'Bulk Price UoM' to line UoM. A blank is interpreted as 1 as long as 'Bulk Price UoM' is present. | | No/No | |
| status | The current status of the invoice line. Possible values are: new, ap_hold, draft, on_hold, pending_receipt, disputed, pending_approval, approved, voided, booking_hold, save_as_draft | string(255) | No/No | |
| tax-rate | The tax rate indicated on the invoice line. Only has a value if the header item line level taxation is set toTrue. | | No/No | |
| tax-location | Only has a value if the header item line level taxation is set to True. | | No/No | |
| tax-code | The tax rate code for the line tax rate. Must match an existing tax rate code within Coupa. Only has a value if the header item line level taxation is set to True. | | No/No | |
| tax-amount | Only has a value if the header item line level taxation is set to True. | | No/No | |
| total-tax | The amount of total tax of the invoice line with multiple tax lines. | decimal | No/No | |
| tax-description | The line level tax description. | | No/No | |
| tax-supply-date | The line level tax supply date in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | | No/No | |
| account-code | The account code from Coupa. All segments are concatenated with a hyphen ( - ). | | No/No | |
| account-active | A flag in Coupa to indicate if the account is active and can be selected. True or False. | | No/No | |
| original-date-of-supply | Original Date of Supply | datetime | No/No | |
| delivery-note-number | Delivery Note Number | string(255) | No/No | |
| discount-amount | Discount Amount | decimal(30,3) | No/No | |
| company-uom | The unit of measurement that the company uses internally (for comercial purposes). | string(255) | No/No | |
| property-tax-account | Property Tax Account | string(255) | No/No | |
| commodity-name | The Name of the Invoice Line Commodity | | No/No | |
| supplier-part-number | Part or identification number of the goods. | | No/No | |
| customs-declaration-number | Customs Declaration Number | string(255) | No/No | |
| hsn-sac | HSN/SAC | string(255) | No/No | |
| unspsc | UNSPSC | string(255) | No/No | |
| category | Used to automate tax codes in Coupa Invoicing. Acceptable values: Goods or Services. | string(255) | No/No | goods, services |
| subcategory | Used to automate tax codes in Coupa Invoicing. Acceptable values: Raw materials, Investment goods or Services exceptions. | string(255) | No/No | raw_materials, investment_goods, services_exceptions |
| deductibility | Used to automate tax codes in Coupa Invoicing. Acceptable values: Fully, Partially or Not. | string(255) | No/No | fully_deductible, partially_deductible, not_deductible |
| billing-notes | A text field for adding notes to a billing line. | text | No/No | |
| segment-1 | Account segment within Coupa. | | No/No | |
| segment-2 | Account segment within Coupa. | | No/No | |
| segment-3 | Account segment within Coupa. | | No/No | |
| segment-4 | Account segment within Coupa. | | No/No | |
| segment-5 | Account segment within Coupa. | | No/No | |
| segment-6 | Account segment within Coupa. | | No/No | |
| segment-7 | Account segment within Coupa. | | No/No | |
| segment-8 | Account segment within Coupa. | | No/No | |
| segment-9 | Account segment within Coupa. | | No/No | |
| segment-10 | Account segment within Coupa. | | No/No | |
| segment-11 | Account segment within Coupa. | | No/No | |
| segment-12 | Account segment within Coupa. | | No/No | |
| segment-13 | Account segment within Coupa. | | No/No | |
| segment-14 | Account segment within Coupa. | | No/No | |
| segment-15 | Account segment within Coupa. | | No/No | |
| segment-16 | Account segment within Coupa. | | No/No | |
| segment-17 | Account segment within Coupa. | | No/No | |
| segment-18 | Account segment within Coupa. | | No/No | |
| segment-19 | Account segment within Coupa. | | No/No | |
| segment-20 | Account segment within Coupa. | | No/No | |
| account-name | The account name from Coupa. | | No/No | |
| created-by-email | The email address of the user who created the invoice. | | No/No | |
| created-by-employee-number | The employee number of the user who created the invoice. | | No/No | |
| created-by-login | The username of the user who created the invoice. | | No/No | |
| updated-by-email | The email address of the user who last updated the invoice. | | No/No | |
| updated-by-employee-number | The employee number of the user who last updated the invoice. | | No/No | |
| updated-by-login | The username of the user who last updated the invoice. | | No/No | |
| distributed-tax-amount | The amount of tax for the line item based on weighted summary expense distribution. | decimal(32,4) | No/No | |
| distributed-shipping-amount | The amount of shipping for the line item based on weighted summary expense distribution. | decimal(32,4) | No/No | |
| distributed-handling-amount | The amount of handling for the line item based on weighted summary expense distribution. | decimal(32,4) | No/No | |
| distributed-misc-amount | The amount of misc for the line item based on weighted summary expense distribution. | decimal(32,4) | No/No | |
| match-reference | Three-way match attribute to connect with Receipt and Invoice Header. | string(255) | No/No | |
| fiscal-code | Fiscal Code | string(255) | No/No | |
| classification-of-goods | Classification of Goods | string(255) | No/No | |
| municipality-taxation-code | Municipality Taxation Code | string(255) | No/No | |
| item-barcode | Item Barcode | string(255) | No/No | |

## Invoice Line Allocation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, or Line Split or Tax Line. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | integer | No/No | |
| invoice-line-id | The unique identifier Coupa assigns to the invoice line. | integer | No/No | |
| line-num | The line number of the invoice line, as it appears on the invoice. Line numbers aren't necessarily listed sequential, but will appear sequentially on the invoice. | | No/No | |
| order-header-num | The number given to the corresponding purchase order within Coupa (if any). | | No/No | |
| order-line-id | The unique identifier Coupa assigns to the corresponding line on the purchase order (if any). | | No/No | |
| order-line-num | The line number of the corresponding purchase order line (if any). | | No/No | |
| account-allocation-id | The unique identifier Coupa assigns to the account allocation. Split line accounting must be enabled. | integer | No/No | |
| account-allocation-sequence | The unique sequential counter Coupa assigns to the account allocation split. Split line accounting must be enabled. | | No/No | |
| account-allocation-amount | The dollar amount for this account allocation. Split line accounting must be enabled. | decimal(32,4) | No/No | |
| account-allocation-percent | The percentage of the total amount allocated to this split. Split line accounting must be enabled. | decimal(16,10) | Yes/No | |
| account-code | The account code from Coupa. All segments are concatenated with a hyphen ( - ). | | No/No | |
| account-active | A flag in Coupa to indicate if the account is active and can be selected. True or False. | | No/No | |
| billing-notes | A note to capture any information on this account allocation split. | text | No/No | |
| segment-1 | Account segment within Coupa. | | No/No | |
| segment-2 | Account segment within Coupa. | | No/No | |
| segment-3 | Account segment within Coupa. | | No/No | |
| segment-4 | Account segment within Coupa. | | No/No | |
| segment-5 | Account segment within Coupa. | | No/No | |
| segment-6 | Account segment within Coupa. | | No/No | |
| segment-7 | Account segment within Coupa. | | No/No | |
| segment-8 | Account segment within Coupa. | | No/No | |
| segment-9 | Account segment within Coupa. | | No/No | |
| segment-10 | Account segment within Coupa. | | No/No | |
| segment-11 | Account segment within Coupa. | | No/No | |
| segment-12 | Account segment within Coupa. | | No/No | |
| segment-13 | Account segment within Coupa. | | No/No | |
| segment-14 | Account segment within Coupa. | | No/No | |
| segment-15 | Account segment within Coupa. | | No/No | |
| segment-16 | Account segment within Coupa. | | No/No | |
| segment-17 | Account segment within Coupa. | | No/No | |
| segment-18 | Account segment within Coupa. | | No/No | |
| segment-19 | Account segment within Coupa. | | No/No | |
| segment-20 | Account segment within Coupa. | | No/No | |
| account-name | The account name from Coupa. | | No/No | |
| currency_code | The currency code of the transaction. | | No/No | |
| accounting-total | The total amount of the invoice using the Chart of Accounts currency. Doesn't include line and summary amounts. | decimal(32,4) | No/No | |
| accounting_currency | The currency code of the Chart of Accounts. | | No/No | |
| distributed-tax-amount | The amount of tax for the line item based on weighted summary expense distribution. | decimal(32,4) | No/No | |
| distributed-shipping-amount | The amount of shipping for the line item based on weighted summary expense distribution. | decimal(32,4) | No/No | |
| distributed-handling-amount | The amount of handling for the line item based on weighted summary expense distribution. | decimal(32,4) | No/No | |
| distributed-misc-amount | The amount of misc for the line item based on weighted summary expense distribution. | decimal(32,4) | No/No | |

## Invoice Charge

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, Line Split, Charge, Charge Split, Tax Line, or Payment. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | integer | No/No | |
| invoice-charge-id | The unique identifier Coupa assigns to the invoice charge. | integer | No/No | |
| line-type | The kind of charge. Possible values are InvoiceShippingCharge, InvoiceHandlingCharge, or InvoiceMiscCharge. | string(255) | No/No | |
| created-at | When the invoice charge was created at in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| updated-at | When the invoice charge was last updated at in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| total | The total amount of the charge. | decimal | No/No | |
| percent | The percent value of this charge (only for percent-based charges & allowances. Not yet used.) | decimal(16,10) | No/No | |
| accounting-total | The total amount of the invoice charge using the Chart of Accounts currency. | decimal(30,4) | No/No | |
| accounting-total-currency | The currency code of the Chart of Accounts. | | No/No | |
| line-num | The line number of the invoice charge, as it appears on the invoice. Line numbers aren't necessarily listed sequential, but will appear sequentially on the invoice. | integer | No/No | |
| description | The invoice charge description. | string(1550) | No/No | |
| tax-rate | The tax rate indicated on the invoice charge. | | No/No | |
| tax-location | The location for tax on this charge | | No/No | |
| tax-code | The tax rate code for the charge tax rate. Must match an existing tax rate code within Coupa. | | No/No | |
| tax-amount | The amount of the tax on this charge | | No/No | |
| total-tax | The amount of total tax on this charge | decimal | No/No | |
| tax-description | The charge level tax description. | | No/No | |
| tax-supply-date | The charge level tax supply date in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | | No/No | |
| account-code | The account code from Coupa. All segments are concatenated with a hyphen ( - ). | | No/No | |
| account-active | A flag in Coupa to indicate if the account is active and can be selected. True or False. | | No/No | |
| billing-notes | A text field for adding notes to a billing line. | text | No/No | |
| segment-1 | Account segment within Coupa. | | No/No | |
| segment-2 | Account segment within Coupa. | | No/No | |
| segment-3 | Account segment within Coupa. | | No/No | |
| segment-4 | Account segment within Coupa. | | No/No | |
| segment-5 | Account segment within Coupa. | | No/No | |
| segment-6 | Account segment within Coupa. | | No/No | |
| segment-7 | Account segment within Coupa. | | No/No | |
| segment-8 | Account segment within Coupa. | | No/No | |
| segment-9 | Account segment within Coupa. | | No/No | |
| segment-10 | Account segment within Coupa. | | No/No | |
| segment-11 | Account segment within Coupa. | | No/No | |
| segment-12 | Account segment within Coupa. | | No/No | |
| segment-13 | Account segment within Coupa. | | No/No | |
| segment-14 | Account segment within Coupa. | | No/No | |
| segment-15 | Account segment within Coupa. | | No/No | |
| segment-16 | Account segment within Coupa. | | No/No | |
| segment-17 | Account segment within Coupa. | | No/No | |
| segment-18 | Account segment within Coupa. | | No/No | |
| segment-19 | Account segment within Coupa. | | No/No | |
| segment-20 | Account segment within Coupa. | | No/No | |
| account-name | The account name from Coupa. | | No/No | |
| created-by-email | The email address of the user who created the invoice. | | No/No | |
| created-by-employee-number | The employee number of the user who created the invoice. | | No/No | |
| created-by-login | The username of the user who created the invoice. | | No/No | |
| updated-by-email | The email address of the user who last updated the invoice. | | No/No | |
| updated-by-employee-number | The employee number of the user who last updated the invoice. | | No/No | |
| updated-by-login | The username of the user who last updated the invoice. | | No/No | |

## Invoice Charge Allocation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, or Line Split or Tax Line. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | integer | No/No | |
| invoice-charge-id | The unique identifier Coupa assigns to the invoice charge. | integer | No/No | |
| line-num | The line number of the invoice charge, as it appears on the invoice. Line numbers aren't necessarily listed sequential, but will appear sequentially on the invoice. | | No/No | |
| account-allocation-id | The unique identifier Coupa assigns to the account allocation. Split line accounting must be enabled. | integer | No/No | |
| account-allocation-sequence | The unique sequential counter Coupa assigns to the account allocation split. Split line accounting must be enabled. | | No/No | |
| account-allocation-amount | The dollar amount for this account allocation. Split line accounting must be enabled. | decimal(30,4) | No/No | |
| account-allocation-percent | The percentage of the total amount allocated to this split. Split line accounting must be enabled. | decimal(16,10) | Yes/No | |
| account-code | The account code from Coupa. All segments are concatenated with a hyphen ( - ). | | No/No | |
| account-active | A flag in Coupa to indicate if the account is active and can be selected. True or False. | | No/No | |
| billing-notes | A note to capture any information on this account allocation split. | text | No/No | |
| segment-1 | Account segment within Coupa. | | No/No | |
| segment-2 | Account segment within Coupa. | | No/No | |
| segment-3 | Account segment within Coupa. | | No/No | |
| segment-4 | Account segment within Coupa. | | No/No | |
| segment-5 | Account segment within Coupa. | | No/No | |
| segment-6 | Account segment within Coupa. | | No/No | |
| segment-7 | Account segment within Coupa. | | No/No | |
| segment-8 | Account segment within Coupa. | | No/No | |
| segment-9 | Account segment within Coupa. | | No/No | |
| segment-10 | Account segment within Coupa. | | No/No | |
| segment-11 | Account segment within Coupa. | | No/No | |
| segment-12 | Account segment within Coupa. | | No/No | |
| segment-13 | Account segment within Coupa. | | No/No | |
| segment-14 | Account segment within Coupa. | | No/No | |
| segment-15 | Account segment within Coupa. | | No/No | |
| segment-16 | Account segment within Coupa. | | No/No | |
| segment-17 | Account segment within Coupa. | | No/No | |
| segment-18 | Account segment within Coupa. | | No/No | |
| segment-19 | Account segment within Coupa. | | No/No | |
| segment-20 | Account segment within Coupa. | | No/No | |
| account-name | The account name from Coupa. | | No/No | |
| currency_code | The currency code of the transaction. | | No/No | |
| accounting-total | The total amount of the invoice using the Chart of Accounts currency. Doesn't include line and summary amounts. | decimal(30,4) | No/No | |
| accounting_currency | The currency code of the Chart of Accounts. | | No/No | |

## Tax Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | | No/No | |
| invoice-number | The user-created invoice number. | | No/No | |
| invoice-line-id | The unique identifier Coupa assigns to the invoice line. | | No/No | |
| invoice-line-number | The line number of the corresponding invoice line. | | No/No | |
| invoice-charge-id | The unique identifier Coupa assigns to the invoice charge | | No/No | |
| invoice-charge-number | The line number of the invoice charge | | No/No | |
| tax-line-number | The line number of the corresponding of the tax line. | integer | No/No | |
| tax-line-id | The unique identifier Coupa assigns to the tax line. | integer | No/No | |
| amount | The amount of tax calculated on the line. | decimal(32,4) | No/No | |
| rate | The tax rate indicated on the invoice line. | float | No/No | |
| tax-rate-type | The tax rate type description on the line | | No/No | |
| code | The tax rate code for the invoice line tax rate. Must match an existing tax rate code within Coupa. | | No/No | |
| amount-engine | Amount calculated by either Coupa Native or External Tax Engine based on configuration | decimal(32,4) | No/No | |
| code-engine | Code returned by External Tax Engine based on configuration | string(255) | No/No | |
| rate-engine | Rate returned by External Tax Engine based on configuration | decimal(30,6) | No/No | |
| description | The tax line description. | string(255) | No/No | |
| location | The taxable location for this tax line. | string(255) | No/No | |
| date | The tax line date in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| kind-of-factor | Kind of Factor indicates the specific type of Withholding which applies to the line item | string(255) | No/No | |
| basis | Basis indicates the CFDI base amount of the invoice or line item to which withholding tax was applied | decimal(30,6) | No/No | |
| Base Amount | Base indicates the base amount of the invoice or line item to which tax was applied | decimal(30,4) | No/No | |
| Supplier Withholding Rate | CFDI Withholding Rate | decimal(30,4) | No/No | |
| Supplier Withholding Amount | CFDI Withholding Amount | decimal(30,4) | No/No | |
| nature-of-tax | Nature of Tax indicates the specific type of tax which applies to the line item e.g. VAT or Withholding | string(255) | No/No | |
| Withholding Amount | Withholding Amount | decimal(30,4) | No/No | |
| Direct/Withholding Tax/TCS Tax | WithholdingTaxLine, TcsTaxLine or TaxLine | string(255) | No/No | |
| product-tax-classification | Product Tax Classification | string(255) | No/No | |

## Withholding Tax Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment. | | No/No | |
| invoice-id | The unique identifier Coupa assigns to the invoice. | | No/No | |
| invoice-number | The user-created invoice number. | | No/No | |
| invoice-line-id | The unique identifier Coupa assigns to the invoice line. | | No/No | |
| invoice-line-number | The line number of the corresponding purchase order line (if any). | | No/No | |
| tax-line-number | The line number of the corresponding of the tax line. | integer | No/No | |
| tax-line-id | The unique identifier Coupa assigns to the tax line. | integer | No/No | |
| amount | The amount of tax calculated on the line. | decimal(32,4) | No/No | |
| rate | The tax rate indicated on the invoice line. | float | No/No | |
| code | The tax rate code for the invoice line tax rate. Must match an existing tax rate code within Coupa. | | No/No | |
| description | The tax line description. | string(255) | No/No | |
| location | The taxable location for this tax line. | string(255) | No/No | |
| date | The tax line date in the format YYYY-MM-DDTHH:MM:SS+HH:MM. | datetime | No/No | |
| kind-of-factor | Kind of Factor indicates the specific type of Withholding which applies to the line item | string(255) | No/No | |
| basis | Basis indicates the CFDI base amount of the invoice or line item to which withholding tax was applied | decimal(30,6) | No/No | |
| Withholding Base | Base indicates the base amount of the invoice or line item to which withholding tax was applied | decimal(30,4) | No/No | |
| Supplier Withholding Rate | CFDI Withholding Rate | decimal(30,4) | No/No | |
| Supplier Withholding Amount | CFDI Withholding Amount | decimal(30,4) | No/No | |
| nature-of-tax | Nature of Tax indicates the specific type of tax which applies to the line item e.g. VAT or Withholding | string(255) | No/No | |
| Withholding Amount | Withholding Amount | decimal(30,4) | No/No | |
| Direct/Withholding Tax | WithholdingTaxLine or TaxLine | string(255) | No/No | |

## Matching Allocation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row | | No/No | |
| order-line-id | The unique identifier Coupa assigns to the corresponding line on the purchase order (if any). | integer | No/No | |
| order-header-number | The order header number. | | No/No | |
| order-line-num | The order line number | | No/No | |
| invoice-line-id | The unique identifier Coupa assigns to the invoice line. | integer | No/No | |
| receipt-id | The unique identifier Coupa assigns to the receipt. | integer | No/No | |
| match-reference-key | The match reference key as described in the receipt used to trigger a match attempt to a candidate invoice line. | | No/No | |
| quantity | The quantity of the invoice line item. | decimal(32,6) | Yes/No | |
| amount | The total amount of the receipt allocation to this invoice line. | decimal(32,4) | Yes/No | |
| uom | The unit of measure code. It must already exist in Coupa. | | No/No | |
| currency | The currency code of the transaction. | | No/No | |
| status | Describes the current status of this allocation record, If the allocation described in this record is active or has been voided. Can have values in Void, Matched. | string(50) | No/No | |

## Failed tolerance columns

| **#** | **Column Name** | **Description** | **Type** | **Req/Unique** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| 1 | code | Code | string(255) | Yes/No | Any |
| 2 | failable-id | Failable ID | integer(11) | No/No | Any |
| 3 | failable-type | Failable Type | string(255) | No/No | Any |
| 4 | resolved | Resolved | boolean | No/No | Yes/No, True/False |
| 5 | resolution-strategy | Resolution Strategy | string(25) | No/No | Any |
| 6 | breach-amount | Breach Amount | string(255) | No/No | Any |
| 7 | breach-limit | Breach Limit | string(255) | No/No | Any |
| 8 | breach-detail-1 | Breach Detail 1 | string(255) | No/No | Any |
| 9 | breach-detail-2 | Breach Detail 2 | string(255) | No/No | Any |
| 10 | breach-detail-3 | Breach Detail 3 | string(255) | No/No | Any |

## Invoice Reconciliation Line

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Type | Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or ReconciliationLine. | | No/No | |
| Adjustment Date | The date the payment was made | datetime | No/No | |
| Type of document | The type of document that was paid | string | No/No | |
| Amount | The total amount paid | decimal(46,20) | No/No | |
| Invoice ID | The document ID that is being paid | | No/No | |
| Created By ID | The user ID that created the payment | integer | No/No | |
| Created By Login | The user login that created the invoice payment | | No/No | |
| Created Date | The date the payment initially drafted | datetime | No/No | |
| Updated By ID | The user ID that most recently updated the payment | integer | No/No | |
| Updated By Login | Ther user login that most recently updated the invoice payment | | No/No | |
| Updated Date | The date the payment was most recently updated | datetime | No/No | |
| Note | Note associated with the payment | string(255) | No/No | |
| Category | Category of the reconciliation (payment, discount, adjustment, credit) | string(255) | No/No | payment, discount, adjustment, tax, credit, tax_line_adjustment, system_adjustment, auto_adjustment, prepayment_adjustment, recurring_adjustment, post_approval_early_payment_discount |

## Invoice To Pay

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Describes the type of row. Possible value is InvoicePayable | | No/No | |
| id | The ID of the invoice | integer | No/No | |
| created-at | The date the invoice was created on | datetime | No/No | |
| updated-at | The date the invoice was last updated on | datetime | No/No | |
| status | The status of the invoice | string(255) | No/No | |
| paid-date | The date the invoice was marked as fully paid | datetime | No/No | |
| paid-total | The total amount paid | decimal | No/No | |
| remaining-total | The total amount remaining to be paid | decimal | No/No | |
| remittance-total | The total remittance amount required | decimal | No/No | |
| accounting-total | The total of the invoice in the CoA currency | decimal | No/No | |
| exported | A flag indicating if the invoice has been marked as exported | | No/No | |
| last-exported-at | The date that the invoice was last marked as exported | datetime | No/No | |
| discount-amount | The discount amount taken | | No/No | |
| discount-rate | The discount rate taken | | No/No | |
| discount-due-date | The discount due date | | No/No | |
| document-type | The type of invoice | string | No/No | |
| payment-channel | The payment channel on the associated InvoiceHeader | | No/No | |
| payable-type | The type of associated payable. Value is InvoiceHeader | string | No/No | |
| payable-id | The ID of the associated InvoiceHeader | | No/No | |
| net-due-date | The net due date of the invoice | | No/No | |
| supplier-name | The suppliers name from the associated InvoiceHeader | | No/No | |
| supplier-number | The suppliers number from the associated InvoiceHeader | | No/No | |
| invoice-number | The invoice number from the associated InvoiceHeader | | No/No | |
| chart-of-account-code | The Chart of Accounts name | | No/No | |
| legal-entity-name | The Chart of Accounts Legal Entity name | | No/No | |
| wc-eligibility | Eligible for Coupa Pay Working Capital | string(255) | No/No | |
