---
title: "Legal Payment Receipt Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/legal-payment-receipt-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/legal-payment-receipt-import"
status_code: 200
fetched_at: "2026-04-09T12:00:41+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Legal Payment Receipt Import"
---

# Legal Payment Receipt Import

## Overview

This Legal Payment Receipt loader is a CFDI XML file format specifically for suppliers
doing business in and from Mexico so that they can load legally compliant payment receipts,
Complementos de Pago, in a supported XML/CSV format.

We support the parsing and mapping of this CFDI XML only on supplier originated invoices
via either CSP upload or SFTP. The XML file does not need to be converted into the Coupa CSV
format by the supplier. For the buyer side, we do not currently support direct parsing of
the XML.

The Forms import process reads files from `./Incoming/LegalPaymentReceipt/`
in the SFTP. These files will be moved to the archive folder located at
`./Incoming/Archive/LegalPaymentReceipt/` before being processed in
alphanumeric order.

## Keys

- UUID

## Validations

Coupa uses the field UUID to lookup an existing record.

## Legal Payment Receipt

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Legal Payment Receipt | No | No | | Legal Payment Receipt | |
| UUID | No | Yes | string(255) | CFDI UUID | |
| Document Date | No | No | datetime | CFDI Document Date | YYYY-MM-DDTHH:MM:SS+HH:MM |
| Payment Received Date | No | No | datetime | Payment Received Date | YYYY-MM-DDTHH:MM:SS+HH:MM |
| Amount | No | No | decimal(32,6) | Amount | |
| Currency | No | No | string | Currency Code | |
| Check Number | No | No | string(255) | Any kind of identification number which identifies the payment | |
| Buyer Bank Name | No | No | string(255) | Buyer Bank Name | |
| Buyer Bank Reference | No | No | string(255) | Buyer Bank Reference | |
| Supplier Bank Reference | No | No | string(255) | Supplier Bank Reference | |
| Form of Payment | No | No | string(255) | Form of Payment | |
| Buyer Account Number | No | No | | Buyer Account Number | |
| Supplier Account Number | No | No | | Supplier Account Number | |
| Supplier Tax Number | No | No | string(255) | Supplier Tax Number | |
| Buyer Tax Number | No | No | string(255) | Buyer Tax Number | |
| Invoice Payment Receipt | No | No | | Invoice Payment Receipt | |
| Document UUID | No | No | | Document UUID | |
| Exchange Rate | No | No | | Exchange Rate | |
| Payment Method | No | No | | Payment Method | |

## Invoice payment receipt columns

| **Column** | **Description** | **Hidden** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| Invoice Payment Receipt | Defines the type of row | false | true | false | - | Invoice Payment Receipt |
| Document UUID | Document UUID | false | false | false | string(255) | any |
| Amount | Amount | false | false | false | decimal(32,6) | any |
| Currency | Currency Code | false | false | false | string(6) | any |
| Exchange Rate | Exchange Rate | false | false | false | decimal(32,6) | any |
| Payment Method | Payment Method | false | false | false | string(255) | any |
