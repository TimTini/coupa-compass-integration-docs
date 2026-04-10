---
title: "Account Statement Import - CSV Format"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/account-statement-import-csv-format"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/account-statement-import-csv-format"
status_code: 200
fetched_at: "2026-04-09T12:00:56+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "Account Statement Import - CSV Format"
---

# Account Statement Import - CSV Format

## Format Description - Standard 27

[PDF Version](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/topics/a/99436)

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Account Identification | char - 35 | Yes | Field 25 in MT940<br>Unique for each account<br>(SWIFT or bank code/account no.) |
| 2 | Statement No. | decimal - 10 | Yes | Field 28C in MT940 |
| 3 | Starting Date | date | Yes | Part of Field 60 in MT940 |
| 4 | Starting Balance | decimal | Yes | Part of Field 60 in MT940 |
| 5 | Closing Date | date | Yes | Part of Field 62 in MT940 |
| 6 | Closing Balance | decimal | Yes | Part of Field 62 in MT940 |
| 7 | Value Date | date | Yes | Subfield 1 in Field 61 |
| 8 | Booking Date | date | Yes | Subfield 2 in Field 61 |
| 9 | Currency | char - 3 | Yes | Part of Field 60 in MT940, currency as ISO code |
| 10 | Amount | decimal | Yes | Negative amounts with leading minus (-) |
| 11 | SWIFT | char - 11 | No | Part of Field 25 in MT940 |
| 12 | BLZ | char - 8 | No | Part of Field 25 in MT940 |
| 13 | BC | char - 3 | No | Part of Field 86 in MT940 |
| 14 | BC Addendum | char - 3 | No | Part of Field 86 in MT940 |
| 15 | Payment Reference | char - 255 | No | Key 20-29 in Feld 86 |
| 16 | Order Reference | char - 16 | No | Field 20 in MT940 |
| 17 | Related Reference | char - 16 | No | Field 21 in MT940 |
| 18 | Booking Key | char - 4 | No | Subfield 6 in Field 61 |
| 19 | Reference in Transaction | char - 16 | No | Subfield 7 in Field 61 |
| 20 | Bank Reference | char - 16 | No | Subfield 8 in Field 61 |
| 21 | Original Amount | char - 50 | No | Subfield 9 in Field 61 |
| 22 | Prima Nota | char - 10 | No | Key 10 in Field 86 |
| 23 | Bank Code - Payer | char - 15 | No | Key 30 in Field 86 |
| 24 | Account Number - Payer | char - 34 | No | Key 31 in Field 86 |
| 25 | Name - Payer | char - 100 | No | Key 32/33 in Field 86 |
| 26 | Addenda to Payment Reference | char - 100 | No | Key 60-63 in Field 86 |
| 27 | Booking Text | char - 27 | No | Key 00 in Field 86 |

## Import Function

The import function is on **Treasury** > **Cash Management** > **Enter Account Statements**.

In the **Account Statement Format** drop-down menu, select **tm5 Standard 27**.

The import function processes files in standard text formats:

- ASCII

- Unicode

## Format Rules

The file may not contain any headers or format descriptions.

Each row in the file contains exactly one data set:

- ASCII Code 13: carriage return denotes the end of a data set.

- ASCII Code 10: new-line denotes the end of a data set.

- The last data set concludes by an end-of-file (EOF).

In the table above, the value for “char” denotes how many characters is the maximum length for that field in the imported file.

Days and months are always 2-digit values, whereas years are 4 digits. The **Enter Account Statements** page allows you to define other format variables for the file:

- **Field Separator** – semicolon (;), comma (,)

- **Date Separator** – slash (/), period (.), comma (,), < none >

- **Date Sequence** – mdy, dmy, ymd

- **Decimal Marker** – period (.), comma (,)

- **File Format** – ASCII, Unicode

## Example Data Sets

Empty fields are only marked by field separators. The sample dataset below contains empty fields.

DEUTESBB/001046581;023/01;01/14/2009;10500.40;01/15/2009;12700.00;

01/14/2009;01/14/2009;EUR;2000.00;;;;;;;;;;;;;;;;;
