---
title: "System - Market Data Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/system-market-data-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/system-market-data-import"
status_code: 200
fetched_at: "2026-04-09T12:00:59+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "System - Market Data Import"
---

# System - Market Data Import

## Format Descriptions

[PDF Version](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/System_Market-Data-Import_Format_Description.pdf)

This document describes the interface for importing market data (FX rates, implicit volatilities, interest rates, interest rate volatilities and security/commodity rates and credit spreads) into the System component of Coupa Treasury. Two types of import format are available: Market Data Import Format 2.0 (Flexible) and Market Data Import Format 1.0 (Fixed).

## Differences between Formats 2.0 (Flexible) and 1.0 (Fixed)

| **Market Data Import Format 2.0** | **Market Data Import Format 1.0** |
| --- | --- |
| The character following the prefix is automatically set as the field separator.<br>All non-numeric values, with the exception of the dash (-) are permissible field separators. | The field separator is the semicolon (;). |
| Permissible date formats are dmy, mdy, and ymd, indicated in a separate field.<br>The date format specified for the first set of data applies to all sets of data of a file. | The date format is dmy. |
| Permissible date separators are periods (.), dashes (-), and slashes (/). | The date separator is the period (.). |
| Permissible decimal separators are periods (.) and commas (,). | The decimal separator is the comma (,). |
| A decimal separator is mandatory for all decimals, even in the absence of decimal places. | Decimal separators are optional. |

## Market Data Import Format 2.0 (Flexible)

**Field definition**

**Import of FX Rates**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: d | char - 1 | Yes | Enter "d" to mark the data set for the import of FX rates. |
| 2 | Date settings | char - 3 | Yes | Permissible date conventions are dmy, mdy, and ymd. |
| 3 | Date | date | Yes | Date for which the FX rate is valid. |
| 4 | Currency | char - 3 | Yes | ISO code for the currency of the FX rate. |
| 5 | Ask rate | decimal | No | Rate in relation to the group currency. When the ask rate is empty or ≤0, it is automatically set to the mid rate. |
| 6 | Mid rate | decimal | Yes | Rate in relation to the group currency. The mid rate must be greater than 0. |
| 7 | Bid rate | decimal | No | Rate in relation to the group currency. When the bid rate is empty or ≤0, it is automatically set to the mid rate. |

**Import of Implicit Volatilities (historical volatilities can be calculated in Coupa Treasury from FX rates)**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: v | char - 1 | Yes | Enter "v" to mark the data set for volatilities. |
| 2 | Date settings | char - 3 | Yes | Permissible date conventions are dmy, mdy, and ymd. |
| 3 | Date | date | Yes | Date for which the volatility is valid. |
| 4 | Currency 1 | char - 3 | Yes | ISO code for the first currency of the volatility. |
| 5 | Currency 2 | char - 3 | Yes | ISO code for the second currency of the volatility. |
| 6 | Time range | integer | Yes | Time range for averaging. |
| 7 | Strike | decimal | Yes | Strike for averaging. |
| 8 | Volatility | decimal | Yes | Volatility value between currency 1 and currency 2. |

**Import of Interest Rates**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: z | char - 1 | Yes | Enter "z" to mark the data set for adding interest rates. |
| 2 | Date settings | char - 3 | Yes | Permissible date conventions are dmy, mdy, and ymd. |
| 3 | Date | date | Yes | Date for which the interest rate is valid. |
| 4 | Currency | char - 3 | Yes | Currency as ISO code. |
| 5 | Time range | integer | Yes | The number of days in the time range. |
| 6 | Period | char - 4 | No | Any value available to select from the Period dropdown menu. |
| 7 | Interest rate in % | decimal | Yes | |

**Import of Interest Rate Volatilities**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: i | char - 1 | Yes | Enter "i" to mark the data set for adding interest volatilities. |
| 2 | Date settings | char - 3 | Yes | Permissible date conventions are dmy, mdy, and ymd. |
| 3 | Date | date | Yes | Date for which the volatility is valid. |
| 4 | Currency | char - 3 | Yes | Currency as ISO code. |
| 5 | Time range | integer | Yes | The number of days in the time range. |
| 6 | Period | char - 4 | No | Any value available to select from the Period dropdown menu. |
| 7 | Interest rate in % | decimal | Yes | Volatility of the interest rate. |

**Import of Security Rates**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: w | char - 1 | Yes | Enter "w" to mark the data set for adding security rates. |
| 2 | Date settings | char - 3 | Yes | Permissible date conventions are dmy, mdy, and ymd. |
| 3 | Date | date | Yes | Date for which the security rate is valid. |
| 4 | ISIN | char - 50 | Yes | ISIN of the security. |
| 5 | Rate | decimal | Yes | Rate for the security for the date. |

**Import of Commodity Rates**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: r | char - 1 | Yes | Enter "r" to mark the data set for adding commodity rates. |
| 2 | Date settings | char - 3 | Yes | Permissible date conventions are dmy, mdy, and ymd. |
| 3 | Date | date | Yes | Date for which the commodity rate is valid |
| 4 | Commodity | char - 3 | Yes | Commodity rate as ISO code |
| 5 | Period | char - 4 | Yes | Any value available to select from the Period dropdown menu. |
| 6 | Buying rate | decimal | Yes | Rate in relation to the group commodity currency. |
| 7 | Mid-marketrate | decimal | Yes | Rate in relation to the group commodity currency. |
| 8 | Selling rate | decimal | Yes | Rate in relation to the group commodity currency. |

**Import of Credit Spreads**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: c | char - 1 | Yes | Enter "c" to mark the data set for adding credit spreads. |
| 2 | Date settings | char - 3 | Yes | Permissible date conventions are dmy, mdy, and ymd. |
| 3 | Date | date | Yes | Date for which the credit spread is valid. |
| 4 | Entity | char - 50 | Yes | Abbreviation for the entity in Coupa Treasury. |
| 5 | Period | char - 3 | Yes | Any value available to select from the Period dropdown menu. |
| 6 | Credit spread | decimal | Yes | Credit spread in basis points. |

## Functional Description

The function is located on the page **System > Market Data / Scenarios > Import**.

Required setting: on **System > System Settings > System Settings** under **Market Data**,select** Receive by File **or **Receive by Web**.

The import function can process text files coded in one of the following standards:

- ASCII

- Unicode

One file may contain information about FX rates, implicit volatilities, interest rates, interest rate volatilities, security rates, commodity rates and credit spreads.

## Format Rules

The file may not contain any headers or format descriptions.

Each row in the file contains exactly one data set:

- ASCII Code 13: carriage return denotes the end of a data set.

- ASCII Code 10: new-line denotes the end of a data set.

- The last data set concludes by an end-of-file (EOF).

Permissible field separators are all non-numeric values, with the exception of the dash (-).

The field separator may not appear elsewhere within the sets of data.

Field separators must also be placed

- for fields of a fixed length.

- for optional fields left blank.

Field separators, date separators and decimal separators are detected automatically.

For decimal values:

- Permissible separators are commas (,) and periods (.).

- Separators are mandatory, even in the absence of decimal places.

- Thousands separators are not allowed.

- Negative amounts are marked with a minus sign (-). Spaces between the minus sign and the amount are allowed.

- Examples: **12345,99** or *-*
**12345.00**or **12345,** or **0,0231**

For integer values:

- Decimal or thousands separators are not permitted

- Example: **12345**

Empty data sets are dismissed.

For text values, there are no quotation marks. The char value is the maximum number of characters for that field.

Days and months are always 2-digit values, whereas years are 4 digits. Date sequence may be dmy, mdy, or ymd (lower-case). Date separator may be slash (/), comma (,), or dash (-).

- Examples: **31.12.2021, 12-31-2021, 2021/12/31**

## Example Data Sets

**Import of FX Rates**

d;dmy;26.09.2021;USD;1,3361;1,3391;1,3421

d;mdy;09-27-2021;USD;1,3362;1,3392;1,3422

d;ymd;2021/09/28;USD;1,3363;1,3393;1,3423

d|dmy|25.09.2021|USD|1,3364|1,3394|1,3424

d;dmy;22.09.2021;CHF;1,1;1,1;1,2

**Import of Implicit Volatilities**

v;dmy; 29.09.2021;CAD;EUR;30;0,;8,39

**Import of Interest Rates**

z;dmy; 29.09.2021;CAD;60;;2,46833

**Import of Interest Rate Volatilities**

i;dmy; 29.09.2021;CAD;30;;8,39

**Import of Security Rates**

w;dmy; 29.09.2021;6511811640;120,9551

**Import of Commodity Rates**

r;dmy; 29.09.2021;XAU;3M;675,465;675,465;675,465

**Import of Credit Spreads**

c;dmy; 29.09.2021;DB Frankfurt;5Y;135,52

## Market Data Import Format 1.0 (Fixed)

**Field definition**

**Import of FX Rates**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: d | char - 1 | Yes | Enter "d" to mark the data set for the import of FX rates. |
| 2 | Date | date | Yes | Date for which FX rate is valid. |
| 3 | Currency | char - 3 | Yes | Currency of FX rate as ISO code. |
| 4 | Ask rate | decimal | No | Rate in relation to group currency; when the ask rate is left empty or ≤0 it will be populated with the mid rate. |
| 5 | Mid rate | decimal | Yes | Rate in relation to group currency; the mid rate cannot be ≤0. |
| 6 | Bid rate | decimal | No | Rate in relation to group currency; when the bid rate is left empty or ≤0 it will be populated with the mid rate. |

**Import of Implicit Volatilities (historical volatilities can be calculated in Coupa Treasury from FX Rates)**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: v | char - 1 | Yes | Enter "v" to mark the data set for volatilities. |
| 2 | Date | date | Yes | Date for which volatility is valid. |
| 3 | Currency 1 | char - 3 | Yes | First currency of volatility as ISO code. |
| 4 | Currency 2 | char - 3 | Yes | Second currency of volatility as ISO code. |
| 5 | Time range | integer | Yes | Time range for averaging. |
| 6 | Strike | decimal | Yes | Strike for averaging. |
| 7 | Volatility | decimal | Yes | Volatility value between currency 1 and currency 2. |

**Import of Interest Rates**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: z | char - 1 | Yes | Enter "z" to mark the data set for adding interest rates. |
| 2 | Date | date | Yes | Date for which interest rate is valid. |
| 3 | Currency | char - 3 | Yes | Currency as ISO code. |
| 4 | Time range | integer | Yes | The number of days in the time range. |
| 5 | Period | char - 4 | No | Period; permitted values as they can be selected from dropdown menu in Coupa Treasury. |
| 6 | Interest rate in % | decimal | Yes | |

**Import of Interest Rate Volatilities**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: i | char - 1 | Yes | Enter "i" to mark the data set for adding interest volatilities. |
| 2 | Date | date | Yes | Date for which volatility is valid. |
| 3 | Currency | char - 3 | Yes | Currency as ISO code. |
| 4 | Time range | integer | Yes | The number of days in the time range. |
| 5 | Period | char - 4 | No | Period; permitted values as they can be selected from dropdown menu in Coupa Treasury. |
| 6 | Interest rate volatility | decimal | Yes | Volatility of interest rate. |

**Import of Security Rates**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: w | char - 1 | Yes | Enter "w" to mark the data set for adding security rates. |
| 2 | Date | date | Yes | Date for which security rate is valid. |
| 3 | ISIN | char - 50 | Yes | ISIN of security. |
| 4 | Rate | decimal | Yes | Rate for security for stated day. |

**Import of Commodity Rates**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: r | char - 1 | Yes | Enter "r" to mark the data set for adding commodity rates. |
| 2 | Date | date | Yes | Date for which commodity rate is valid. |
| 3 | Commodity | char - 3 | Yes | Commodity rate as ISO code. |
| 4 | Period | char - 4 | Yes | Period; permitted values as they can be selected from dropdown menu in Coupa Treasury. |
| 5 | Buying rate | decimal | Yes | Rate in relation to group commodity currency. |
| 6 | Mid-market rate | decimal | Yes | Rate in relation to group commodity currency. |
| 7 | Selling rate | decimal | Yes | Rate in relation to group commodity currency. |

**Import of Credit Spreads**

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | Prefix: c | char - 1 | Yes | Enter "c" to mark the data set for adding credit spreads. |
| 2 | Date | date | Yes | Date for which credit spread is valid. |
| 3 | Entity | char - 50 | Yes | Short name of Coupa Treasury entity. |
| 4 | Period | char - 3 | Yes | Period; permitted values as they can be selected from dropdown menu in Coupa Treasury. |
| 5 | Credit spread | decimal | Yes | Credit spread in basis points. |

## Functional Description

The import function can process text files coded in one of the following standards:

- ASCII

- Unicode

One file may contain information about FX rates, implicit volatilities, interest rates, interest rate volatilities, security rates, commodity rates and credit spreads.

The function is located on the page **System > Market Data > Import.**

Required setting: **System > Administration > System Settings > Market Data** must be set to "File" or "File or Web".

## Format Rules

The file may not contain any headers or format descriptions.

Each row in the file contains exactly one data set:

- ASCII Code 13: carriage return denotes the end of a data set.

- ASCII Code 10: new-line denotes the end of a data set.

- The last data set concludes by an end-of-file (EOF).

The data set field delimiter is the semicolon (;). The semicolon may not appear elsewhere within the sets of data.

Field separators must also be placed

- for fields of a fixed length.

- for optional fields left blank. .

For decimal values:

- Permissible separator is the comma (,).

- Separators are optional for numbers without decimal places.

- Thousands separators are not allowed.

- Negative amounts are marked with a minus sign (-). Spaces between the minus sign and the amount are allowed.

- Examples: **12345,99** or *-*
**12345.00**or **12345**or **0,0231**

For integer values:

- Decimal or thousands separators are not permitted.

- Example: **12345**

Empty data sets are dismissed.

For text values, there are no quotation marks. The char value is the maximum number of characters for that field.

Days and months are always 2-digit values, whereas years are 4 digits. Date sequence is dmy (lower case). Permissable date separator is the period (.).

- Example: **31.10.2021**

## Example Data Sets

**Import of FX Rates**

d;26.09.2021;USD;1,3362;1,3392;1,3422

**Import of Implicit Volatilities**

v;29.09.2021;CAD;EUR;30;0,;8,39

**Import of Interest Rates**

z;29.09.2021;CAD;60;;2,46833

**Import of Interest Rate Volatilities**

i;29.09.2021;CAD;30;;8,39

**Import of Security Rates**

w;29.09.2021;6511811640;120,9551

**Import of Commodity Rates**

r;29.09.2021;XAU;3M;675,465;675,465;675,465

**Import of Credit Spreads**

c;29.09.2021;DB Frankfurt;5Y;135,52
