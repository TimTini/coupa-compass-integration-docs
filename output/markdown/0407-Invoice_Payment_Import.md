---
title: "Invoice Payment Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/invoice-payment-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/invoice-payment-import"
status_code: 200
fetched_at: "2026-04-09T12:00:40+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Invoice Payment Import"
---

# Invoice Payment Import

## Overview

The Invoice Payments Import process read files from the
`./Incoming/InvoicePayments` folder in the SFTP. These files will be moved
to the archive folder located at `./Archive/Incoming/InvoicePayments/` before
being processed in Alphanumeric order. Flat Files are then transformed to Coupa's XML
format.

In the standard integration, a validation routine determines whether a payment has already
been applied to an invoice by comparing the payment date, check number, and amount fields to
the payment record.

## Void/Check Cancelations

The Coupa Integration does not support deleting or voiding a check directly. The best
practice in this scenario is to create a new 'payment' for negative the amount of the check
to cancel. The check # can be the same or have a string such as 'Void' appended.

## Keys/Validations

Coupa finds invoices in approved status and scope based on the following criteria:

- If the `Invoice ID` / `Number` is provided, *only*
the Invoice ID / Number is matched.

- If the `Supplier Name` and/or `Supplier Number` is
provided, Coupa searches for the supplier.

- If a matching supplier is found, Coupa uses the supplier as a filtering criterion.

- If a matching supplier is not found, Coupa does not include the supplier as part of
the scope.

- If the `Invoice Date` is provided, Coupa scopes approved invoices to that
invoice date.

- The `Invoice Date` is needed if a customer reuses the same invoice
number for different calendar years.

- Coupa will create a payment only if exactly one invoice is found from the above
queries.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: Invoice payments can't be updated via Integration.

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Supplier Name | Supplier Name. Include at least the suppler name or number. | TRUE* | FALSE | string(100) | any |
| Supplier Number | Supplier Number. Include at least the supplier name or number. | TRUE* | FALSE | string(255) | any |
| Invoice Number | Invoice Number | TRUE | FALSE | string(40) | any |
| Invoice Date | Invoice Date of invoice related to current payment | FALSE | FALSE | | any |
| Invoice ID | Database ID of the invoice | FALSE | FALSE | | any |
| Expense Report Id | Expense Report Id | FALSE | FALSE | | any |
| Paid | This is the paid field on the invoice header. It's set to a true or false value. | FALSE | FALSE | boolean | true,false/Yes,No/Y,N/T,F |
| Paid-in-Full Date | Paid-in-Full Date | FALSE | FALSE | datetime | YYYY-MM-DDTHH:MM:SS+HH:MM |
| Paid-in-Full Note | Paid-in-Full Note | FALSE | FALSE | string(255) | any |
| Check Amount Paid | Check Amount Paid | FALSE | FALSE | decimal(32,4) | any |
| Check # / Note | Check # / Note | FALSE | FALSE | string(255) | any |
| Check Payment Date | Check Payment Date | FALSE | FALSE | datetime | YYYY-MM-DDTHH:MM:SS+HH:MM |

* One of `Supplier Name` or `Supplier Number` is
required.
