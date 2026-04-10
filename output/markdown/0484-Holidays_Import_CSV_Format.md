---
title: "Holidays Import CSV Format"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/holidays-import-csv-format"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/holidays-import-csv-format"
status_code: 200
fetched_at: "2026-04-09T12:00:58+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "Holidays Import CSV Format"
---

# Holidays Import CSV Format

## Format Description

[PDF Version](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/Holidays_Import_CSV_Format.pdf)

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Date | date | Yes | The date of the holiday. |
| 2 | Calculation | char - 1 | Yes | 0 = Do not include date in calculations.<br>1 = Include date in calculations. |
| 3 | Detail | char - 1 | Yes | If the holiday refers to a currency, enter the three-digit ISO-code of that currency.<br>If the holiday refers to a country, enter the two-digit ISO-code of that country. |
| 4 | Name | char - 50 | Yes | The name of the holiday. |

## Import Function

The import function is
under Special Functions on System > Market Data/Scenarios > Holidays.

The import
function processes files in standard text formats:

- ASCII

- Unicode

## Format Rules

One file may contain entries
for multiple holidays. Each dataset contains exactly one holiday.

If imported a second
time, pre-existing datasets are not overwritten and are added to the list.

The file
cannot contain any headers or format descriptions. Do not enclose text in quotation
marks.

Each row in the file contains exactly one data set:

- ASCII Code 13: carriage return shows the end of a data set.

- ASCII Code 10: new line shows the end of a data set.

- The last data set concludes by an end of file (EOF).

In the table above, the value for “char” shows how many characters is the maximum
length for that field in the imported file.

Days and months are always 2-digit values,
whereas years are 4 digits. Date separator, date sequence, and file format must match your
user settings.

- **Field Separator** – semicolon (;), comma (,)

- **Date Separator** – slash (/), period (.), comma (,), < none >

- **Date Sequence** – mdy, dmy, ymd

- **File Format** – ASCII, Unicode

## Example Data Sets

12/25/2021;0;USD;Christmas Day

12/31/2021;1;US;New Year’s
Eve
