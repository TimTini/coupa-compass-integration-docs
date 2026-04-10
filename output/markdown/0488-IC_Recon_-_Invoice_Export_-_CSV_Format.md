---
title: "IC Recon - Invoice Export - CSV Format"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/ic-recon-invoice-export-csv-format"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/ic-recon-invoice-export-csv-format"
status_code: 200
fetched_at: "2026-04-09T12:00:58+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "IC Recon - Invoice Export - CSV Format"
---

# IC Recon - Invoice Export - CSV Format

## Format Description

[PDF Version](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/IC_Recon_-_Invoice_Export_-_CSV_Format.pdf)

## Receivables Export

| **#** | **Name** | **Type** | **Comment** |
| --- | --- | --- | --- |
| 1 | Invoice number | char - 50 | Invoice number on the receivables side |
| 2 | Debitor account number | char - 20 | Debitor account as it appears in Coupa Treasury |
| 3 | Invoice date | date | |
| 4 | Due date | date | |
| 5 | Amount | decimal | |
| 6 | Currency | char - 3 | ISO code of currency |
| 7 | Invoice flag | char - 50 | |
| 8 | Comment | char - 250 | |
| 9 | Delivery slip number | char - 50 | |
| 10 | XDoc no. | char - 50 | |
| 11 | Booking date | date | |
| 12 | Remark | char - 250 | |
| 13 | Project | char - 50 | |
| 14 | Potfolio | char - 50 | |

## Payables Export

| **#** | **Name** | **Type** | **Comment** |
| --- | --- | --- | --- |
| 1 | Invoice number | char - 50 | Invoice number on the payables side |
| 2 | Creditor account number | char - 20 | Creditor account as used for importing the confirmation file. For manual confirmation, the first creditor account number entered for the counterparty as **ID counterparty**. |
| 3 | Invoice date | date | |
| 4 | Due date | date | |
| 5 | Amount | decimal | |
| 6 | Currency | char - 3 | ISO code of currency |
| 7 | Invoice identifier | char - 50 | |
| 8 | Comment | char - 250 | |
| 9 | Delivery slip number | char - 50 | |
| 10 | XDoc no. | char - 50 | |
| 11 | Booking date | date | |
| 12 | Remark | char - 250 | |
| 13 | Project | char - 50 | |
| 14 | Portfolio | char - 50 | |

## Export Function

The export function is
under Special Functions on **Recon & Netting** > **AP/AR Recon** >
**Payments**.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image13a.png)

The export function produces
text files with the .csv file extension.

## Format Rules

The export function uses the
user-defined **Export Format Settings** under **User Settings**.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image6c.png)

The file does not contain any headers or format
descriptions.

One file can contain multiple data sets.

Each row in the file
contains exactly one data set:

- ASCII Code 13: carriage return denotes the end of a data set.

- ASCII Code 10: new line denotes the end of a data set.

The field delimiter is the semicolon (;).

For decimal values, the period (.) is
the decimal separator. There are no thousands separators.

For text values, there are
no quotation marks. The char value is the maximum number of characters for that
field.

Days and months are always 2-digit values and years are 4-digit values. There
are no date separators and the date sequence is ymd.

## Example Data Sets

745;104;05.01.2021;02.02.2021;1418258,41;EUR;;;;745;;

746;104;15.01.2021;12.02.2021;1892985,48;EUR;;;;746;;
