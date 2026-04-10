---
title: "IC Netting - FX Rates Import - CSV Format"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/ic-netting-fx-rates-import-csv-format"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/ic-netting-fx-rates-import-csv-format"
status_code: 200
fetched_at: "2026-04-09T12:00:58+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "IC Netting - FX Rates Import - CSV Format"
---

# IC Netting - FX Rates Import - CSV Format

## Format Description

[PDF Version](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/IC_Netting_-_FX_Rates_Import_-_CSV_Format.pdf)

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Netting code | char - 7 | Yes | Recon code in IC Balances. |
| 2 | Currency | char - 3 | Yes | Currency ISO code. |
| 3 | Bank buying rate | decimal | Yes | |
| 4 | Bank selling rate | decimal | No | |

## Import Function

The import function is
under Special Functions on Recon & Netting > IC Netting > Rates. The import
function processes files in standard text formats:

- ASCII

- Unicode

## Format Rules

One file may contain multiple
data sets. The file cannot contain any headers or format descriptions. Do not enclose text
in quotation marks.

Each row in the file contains exactly one data set:

- ASCII Code 13: carriage return shows the end of a data set.

- ASCII Code 10: new line shows the end of a data set.

- The last data set concludes by an end of file (EOF).

In the table above, the value for “char” shows how many characters is the maximum
length for that field in the imported file.

- **Field Separator** – semicolon (;), comma (,)

- **Decimal Separator** – period (.), comma (,)

## Example Data Sets

N0504;USD;1.2869;1.2929

N2001;EUR;1,352;1,3162
