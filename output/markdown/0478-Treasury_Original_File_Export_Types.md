---
title: "Treasury Original File Export Types"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-sftp-integrations/treasury-original-file-export-types"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-sftp-integrations/treasury-original-file-export-types"
status_code: 200
fetched_at: "2026-04-09T12:00:56+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury sFTP Integrations"
  - "Treasury Original File Export Types"
---

# Treasury Original File Export Types

You can select which original files should be exported to sFTP with various Standard integrations. You can also configure custom Original File export integrations. Original file exports include two types.

## Bank file integrations

Bank Files are the original files received by the bank and are not yet assigned to a legal entity or an account. You can download the files from Treasury Management at
Banking > Bank Connectivity > Bank Files Overview
.

For more information, see [Bank Files Overview](https://compass.coupa.com/en-us/products/product-documentation/treasury-management-product-documentation/banking/bank-connectivity/bank-files-overview).

These integrations are included in Standard:

| **Type** | **Description** | **sFTP folder** |
| --- | --- | --- |
| Standard Treasury End-of-Day Account Statement Bank File Export | Exports all bank files of type **Account Statements** (only end of day statement formats) received within the last 7 days. | `/Outgoing/OriginalBankFile/AccountStatements/EndofDays` |
| Standard Treasury Intraday Account Statement Bank File Export | Exports all bank files of type **Account Statements** (only intraday statement formats) received within the last 7 days and which have not yet been exported and marks files as exported. | `/Outgoing/OriginalBankFile/AccountStatements/Intradays` |
| Standard Treasury Bank Transaction Report Bank File Export | Exports all bank files of type **Bank Transaction** Report received within the last 7 days and which have not yet been exported and marks files as exported. | `/Outgoing/OriginalBankFile/BankTransactionReports` |
| Standard Treasury Payment Status Report Bank File Export | Exports all bank files of type **Payment Status Report** received within the last 7 days and which have not yet been exported and marks files as exported. | `/Outgoing/OriginalBankFile/PaymentStatusReports` |
| Standard Treasury Bank Service Fees Bank File Export | Exports all bank files of type **Bank Service Fees** received within the last 7 days and which have not yet been exported and marks files as exported. | `/Outgoing/OriginalBankFile/BankServiceFees` |
| Standard Treasury PDF Account Statement Bank Files Export | Exports all bank files of format PDF and File Identifier BKA received within the last 7 days and which have not yet been exported and marks files as exported. | `/Outgoing/OriginalBankFile/PdfAccountStatements` |

## Account statement integrations

Accounts Statements are the original statements received by the Bank and are assigned to a legal entity and an account. You can download the files from Treasury Management at
Treasury > Cash Management > Account Statements
.

These integrations are included in Standard:

| **Type** | **Description** | **sFTP folder** |
| --- | --- | --- |
| Standard Treasury Original Account Statement Export | Exports all account statements processed within the last 7 days and which have not yet been exported and marks files as exported. | `/Outgoing/OriginalAccountStatement` |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: If you need export capabilities beyond the standard integrations, you can create custom Original File export integrations using **Automation Views** in Treasury Management. For details, see [Custom Treasury export integrations](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-sftp-integrations/treasury-csv-exports#AutoViewCustomInteg) and [Automation Views in Treasury Management](https://compass.coupa.com/en-us/products/product-documentation/treasury-management-product-documentation/getting-started-with-treasury-management/automated-processes-and-integrations/automation-views-in-treasury-management).

## File names

Depending on the integration type, files may have different files names. Use date/time stamps to ensure that files do not override each other. Outbound files from Coupa use the following formats:

| **Business Object** | **File Name (ZIP)** | **File Name (Original File)** | **To or From COUPA** |
| --- | --- | --- | --- |
| Original Bank Files | originalbankfiles_<YYYYMMDD_HHMMSSZ>.zip | <File Name> | From Coupa |
| Original Account Statements | accountstatements_<YYYYMMDD_HHMMSSZ>.zip | <File Format>_<YYYYMMDD_HHMMSSZ> | From Coupa |
