---
title: "Cash Flow Export - CSV Format"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/cash-flow-export-csv-format"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/cash-flow-export-csv-format"
status_code: 200
fetched_at: "2026-04-09T12:00:57+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "Cash Flow Export - CSV Format"
---

# Cash Flow Export - CSV Format

## Format Description

[PDF Version](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/Cash_Flow_Export_-_CSV_Format.pdf)

## Cash Flows Export Standard CSV

| **#** | **Name** | **Type** | **Comment** |
| --- | --- | --- | --- |
| 1 | GL Account No. | char - 30 | GL account number as set up in Coupa Treasury |
| 2 | Account No. | char - 50 | |
| 3 | Bookings GL Account No. | char - 30 | Bookings GL account number as set up in Coupa Treasury |
| 4 | Bookings Account No. | char - 50 | |
| 5+ | Varies according to chosen filter criteria | Determined by table data | |

## Export Function

On **Cash Flows**, the export
function is under the **More** button.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image4.png)

On
**Cash Flows (classic)**, the export function is at the top of the data
table.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image5.png)

## Format Rules

The export function uses the
user-defined **Export Format Settings** under **User Settings**.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image6.png)

The file does not contain any headers or format
descriptions.

One file can contain transactions from multiple bank
accounts.

Each row in the file contains exactly one dataset:

- ASCII Code 13: carriage return denotes the end of a data set.

- ASCII Code 10: new line denotes the end of a data set.

For text values, there are no quotation marks. The char value is the maximum number of
characters for that field.

Days and months are always 2-digit values and years are
4-digit values.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Negative amounts use a leading minus sign
(-). Whole integers have no decimals. There are no thousands
separators.

## Example Data Sets

Optional fields may
remain empty. Empty fields are denoted by field separators only. The sample datasets below
contain empty fields.

- Field Separator = semicolon (;)

- Date Separator = period (.)

- Date Sequence = dmy

- Decimal Separator = comma (,)

GL_BoA_Acc_EUR;1234567893;GL_DB_ Acc_EUR;98765432190;TWAG-BoA
FFM-EUR;TWAG;13.05.2019;623147,19;Other Income;Account Statement;TWAG-ALPEN-EUR

GL_DB_
Acc_EUR;98765432190;GL_BoA_Acc_EUR;1234567893;TWAG-ALPEN-EUR;TWAG;13.05.2019;-623147,19;Other
Income;Account Statement;TWAG-BoA FFM-EUR

GL_BoA_Acc_EUR;1234567893;;;TWAG-BoA
FFM-EUR;TWAG;13.05.2019;623147,19;Other Income;File;
