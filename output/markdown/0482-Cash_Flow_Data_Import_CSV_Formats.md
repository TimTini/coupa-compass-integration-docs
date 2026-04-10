---
title: "Cash Flow Data Import CSV Formats"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/cash-flow-data-import-csv-formats"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/cash-flow-data-import-csv-formats"
status_code: 200
fetched_at: "2026-04-09T12:00:57+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "Cash Flow Data Import CSV Formats"
---

# Cash Flow Data Import CSV Formats

## Format Descriptions

[PDF Version](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/Cash_Flow_Data_Import_CSV_Formats.pdf)

## LMCSH 6

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | AccountID | char - 50 | Yes | Account Name, ID for Reporting, Account No. or Account No. GL as set up in Coupa Treasury |
| 2 | Amount | decimal | Yes | |
| 3 | Value Date | date | Yes | |
| 4 | CategoryID | integer | No | ID # of planning category as defined in Coupa Treasury |
| 5 | Cash Flow Type | integer | No | 0 = Planning data (standard)<br>1 = Transaction |
| 6 | Payment Reference | char - 250 | No | |

## LMCSH 12

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | AccountID | char - 50 | Yes | Account Name, ID for Reporting, Account No. or Account No. GL as set up in Coupa Treasury |
| 2 | Amount | decimal | Yes | |
| 3 | Value Date | date | Yes | |
| 4 | Booking Date | date | Yes | |
| 5 | CategoryID | integer | No | ID # of planning category as defined in Coupa Treasury |
| 6 | Project | char - 50 | No | Internal Reference |
| 7 | Portfolio | char - 50 | No | Internal Reference |
| 8 | BC | char - 10 | No | |
| 9 | G/L Account | char - 50 | No | |
| 10 | Hedge Name | char -50 | No | Hedge name abbreviation |
| 11 | Cash Flow Type | integer | No | 0 = Planning data (standard)<br>1 = Transaction |
| 12 | Payment Reference | char - 250 | No | |

## LMCSH 14

As of release 18.1, this format replaces
CashFlow 13. The additional field 14 adds booking on the mirror account. Import files in
CashFlow 13 remain valid. Choose Version LMCSH 14 on the import page when manually importing
CashFlow 13 format files.

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | AccountID | char - 50 | Yes | Account Name, ID for Reporting, Account No. or Account No. GL as set up in Coupa Treasury |
| 2 | Amount | decimal | Yes | |
| 3 | Value Date | date | Yes | |
| 4 | Booking Date | date | Yes | |
| 5 | CategoryID | integer | No | ID # of planning category as defined in Coupa Treasury |
| 6 | Project | char - 50 | No | Internal Reference |
| 7 | Portfolio | char - 50 | No | Internal Reference |
| 8 | BC | char - 10 | No | |
| 9 | G/L Account | char - 50 | No | |
| 10 | Hedge Name | char - 50 | No | Hedge name abbreviation |
| 11 | Counterparty | char - 50 | No | |
| 12 | Cash Flow Type | integer | No | 0 = Planning data (standard)<br>1 = Transaction |
| 13 | Payment Reference | char - 250 | No | |
| 14 | Booking on Mirror Account | integer | No | 0 = No booking on Mirror Account<br>1 = Booking on Mirror Account<br>If this field is empty, Coupa Treasury makes no booking on the mirror account. |

## LMCSH 16

As of release 18.2, format LMCSH 16 is
available. It is an extension of LMCSH 14 with 2 extra fields, allowing for the deletion of
specific cash flows at the same time as uploading new ones. Field 15 specifies if there is
to be any deletion. Field 16 defines the type of match necessary for deletion. If there is
no cash flow to delete, Coupa Treasury ignores fields 15 and 16.

Use of the deletion
feature in field 15 depends on the user having sufficient rights within Coupa Treasury.

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | AccountID | char - 50 | Yes | Account Name, ID for Reporting, Account No. or Account No. GL as set up in Coupa Treasury |
| 2 | Amount | decimal | Yes | |
| 3 | Value Date | date | Yes | |
| 4 | Booking Date | date | Yes | |
| 5 | CategoryID | integer | No | ID # of planning category as defined in Coupa Treasury |
| 6 | Project | char - 50 | No | Internal Reference |
| 7 | Portfolio | char - 50 | No | Internal Reference |
| 8 | BC | char - 10 | No | |
| 9 | G/L Account | char - 50 | No | |
| 10 | Hedge Name | char - 50 | No | Hedge name abbreviation |
| 11 | Counterparty | char - 50 | No | |
| 12 | Cash Flow Type | integer | No | 0 = Planning data (standard)<br>1 = Transaction |
| 13 | Payment Reference | char - 250 | No | |
| 14 | Booking on Mirror Account | integer | No | 0 = No booking on Mirror Account<br>1 = Booking on Mirror Account<br>If this field is empty, Coupa Treasury makes no booking on the mirror account. |
| 15 | Deletion | integer | No | 0 = no deletion (default)<br>1 = deletion |
| 16 | Type of Match for Deletion | integer | No | 0 = Account, amount, booking date, value date, project, portfolio, BC, cash flow type, and payment reference must match. A mirror cash flow must also exist.<br>1 = Account, amount, value date, payment reference, and cash flow type must match. |

## Cash Flow Deletion Format

To delete a
block of cash flows from imported files, use this format. Select any version when uploading.
All cash flows with matching criteria will be deleted.

| **#** | **Name** | **Type** | **Mandatory** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | AccountID | char - 50 | Yes | Account Name, ID for Reporting, Account No. or Account No. GL as set up in Coupa Treasury |
| 2 | x, y, or z | decimal | Yes | x – delete all data<br>y – delete all data from server import<br>z – delete all data from manual import |
| 3 | Value Date From | date | Yes | Starting date of range to be deleted (inclusive) |
| 4 | Value Date Until | integer | Yes | Ending date of range to be deleted (inclusive) |
| 5 | Cash Flow Type | integer | Yes | 0 = Planning data (standard)<br>1 = Transaction |

## Import Function

The import function only
exists on Cash Flows (classic). In the new cash management process, there is an Excel import
function. Documentation for it is in the in-app help.

The import function processes
files in standard text formats:

- ASCII

- Unicode

Files may contain planning data and transactions for bank and intercompany accounts.
Data from imported files gets added to the database but does not get
overwritten.

Deletion of imported cash flows is possible 3 ways:

- Import Cash Flow Deletion Format. This will delete all matching cash flows.

- Import LMCSH 16 file to delete specific cash flows while importing others.

- Use the Delete button on the Cash Flows page in tm5.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image7.png)

## Format Rules

Each cash flow file format
name denotes the number of fields it contains (LMCSH 6 contains 6 fields, LMCSH 16 contains
16 fields). If the file has more than the expected number of fields, Coupa Treasury shows an
error message.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image8.png)

The file must not contain any
headers or format descriptions.

Each row in the file contains exactly one data
set:

- ASCII Code 13: carriage return denotes the end of a data set.

- ASCII Code 10: new-line denotes the end of a data set.

- The last data set concludes with an end-of-file (EOF).

Select format variables in the **File Import** dialog:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image9.png)

- **Entity**- The entity must own the account on the imported cash flow

- **Field Separator** – semicolon (;), comma (,)

- **Date Separator** – slash (/), period (.), comma (,), < none >

- **Account Identification by** – Account Name, Account ID, Account No., GL Account
No.

- **Decimal Marker** – period (.), comma (,)

- **Date Sequence** – mdy, dmy, ymd

- **File Format** – ASCII, Unicode

- **Version** – LMCSH 6, LMCSH 12, LMCSH 14, LMCSH 16

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

For numbers without decimals, the decimal separator is
optional. Do not use thousands separators or enclose text in quotation marks. Mark
negative amounts with a minus sign (-).

## Example Data Sets

For any format
version, non-mandatory data fields may be empty. Empty fields still require field
separators. The sample data sets below contain examples with empty fields.

Field
separator = ;

Date separator = /

Date sequence = mdy

Decimal separator =
.

**LMCSH 6**

TWAG-DBF-EUR;150077.58;01/29/2009;12;0;Dispo aus
Datei

TWAG-BLG-EUR;26110.90;01/25/2009;;1;transaction to IC account

**LMCSH
12**

TWAG-DBF-USD;15007.58;01/29/2009;01/28/2009;12;PRJ31;PF032;805;6344523;order
USD;0;from file

TWAG-BLG-EUR;26110.90;01/25/2009;01/24/2009;;;;;;;1;

**LMCSH
14**

TWAG-ALPEN-EUR;150077.58;12/07/2017;12/06/2017;12;;;;;;AERO;0;from
file;1

**LMCSH
16**

TWAG-ALPEN-EUR;150077.58;12/07/2017;12/06/2017;12;;;;;;AERO;0;from
file;1;1;1

**Cash Flow Deletion
Format**

TWAG-DBF-EUR;x;01/29/2009;02/23/2009;0
