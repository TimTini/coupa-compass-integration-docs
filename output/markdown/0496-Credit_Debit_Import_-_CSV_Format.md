---
title: "Credit/Debit Import - CSV Format"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/creditdebit-import-csv-format"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/creditdebit-import-csv-format"
status_code: 200
fetched_at: "2026-04-09T12:00:59+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "Credit/Debit Import - CSV Format"
---

# Credit/Debit Import - CSV Format

## Mandatory and optional sections and fields

Some sections are mandatory, while others are optional. Within each section, some fields are mandatory, optional, or conditional. Values in the Mandatory column indicate whether or not a field within the section is mandatory:

Mandatory

The field is always required.

Optional

It is always optional whether or not to populate this field.

Conditional on other fields

This field may or may not be mandatory, depending on the values of preceding fields. See the Description column for details.

As agreed during implementation

During the implementation phase, your Coupa Treasury representative will have defined which of these fields are relevant for your purposes. Consult the documentation provided during implementation or contact your Coupa representative for more details.

## File Header

This section is optional, but we recommend including a header in your file.

| Field | Format | Description | Mandatory |
| --- | --- | --- | --- |
| H1 | H | Indicates that the record is a file header. | Yes |
| H2 | C or D | C = Credit transfer<br>D = Direct debit | Yes |
| H3 | Max 35 text | Optional file identifier: file name or batch number. | No |

## Transcation identification segment

The transaction section (fields 1-82) is mandatory, although not all fields are mandatory.

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 1 | Transaction type | C or D | C = Credit Transfer<br>D = Direct Debit | Yes |
| 2 | Transaction identifier | Max 35 text | Unique transaction identifier. If invoice records will accompany transaction details, this field must be populated. | As agreed during implementation |

## Initiating Party Account Information

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 3 | IBAN | Max 34 text<br>Must be a valid IBAN. Do not use spaces or any other formatting characters. | Either IBAN or account number must be provided. For SEPA transactions, IBAN is required. Otherwise, IBAN is optional. It is recommended to always provide the IBAN if available. | Conditional on other fields |
| 4 | Account number | Max 34 text<br>Do not use spaces or any other formatting characters. | Either IBAN or Account number must be provided. It is recommended to always provide the IBAN if available. | Conditional on other fields |
| 5 | Account currency | 3-character ISO 4217 Currency Code | Account currency | Mandatory |
| 6 | Bank SWIFT BIC | Max 11 text<br>Must be a valid SWIFT BIC (8 or 11 characters). | Mandatory for SEPA credit transfers, otherwise optional. It is recommended to always provide the SWIFT BIC if available. | Conditional on other fields |
| 7 | Bank code | Max 35 text<br>Do not use spaces or any other formatting characters. | Mandatory if the SWIFT BIC is not available, otherwise optional. It is recommended to always provide the bank code, if available.<br>If the branch ID needs to be provided, please delimit it with a pipe character (\|). For example **aaaaaa\|bbb**, where **aaaaaa** is a bank code and **bbb** is a branch code. For cases where only the branch ID needs to be provided, please use **\|bbb**, including the pipe character. | Conditional on other fields |
| 8 | Bank country | ISO 3166-1 alpha-2 Country Code | If IBAN and BIC are not specified, the bank country code must be provided. | Conditional on other fields |
| 9 | Country subdivision | Max 35 text | If field 22 = US, please provide state. If field 22 = CA, please provide province. Otherwise, do not populate. | Conditional on other fields |

## Transaction Block

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 10 | End-to-end identifier | Max 35 text | Customer-to-customer identifier. In Coupa Treasury, this is the End-to-end reference. | Optional |
| 11 | Amount | Numeric amount, decimal separation is a dot. | Transaction amount | Mandatory |
| 12 | Currency | 3-character ISO 4217 Currency Code | Transaction currency | Mandatory |
| 13 | Execution date | ISO8601 Date (yyyy-mm-dd) | Transaction execution date | Mandatory |
| 14 | Remittance information | Max 140 text | Unsructured remittance information | Optional |
| 15 | Expense regulation | CRED<br>DEBT<br>SHAR | Designation of party that will bear charges for transaction expenses.<br>CRED = Creditor (Beneficiary)<br>DEBT = Debtor (Payer)<br>SHAR = Shared<br>Default is SHAR<br>For SEPA transactions, only enter SHAR in this field. | Optional |
| 16 | Category purpose | SALA<br>INTC | SALA = Salary payments<br>INTC = Intercompany<br>Default is none. | Optional |
| 17 | Priority | NURG<br>URGP | NURG = Regular Payment<br>URGP = Urgent Payment<br>Default is NURG. | Optional |

## Receiver information block

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 18 | Name | Max 70 text | | Mandatory |
| 19 | Street and building number | Max 70 text | | Optional |
| 20 | Postal code | Max 16 text | | Optional |
| 21 | Town name | Max 35 text | If any data is provided in fields 19-20, then field 21 is mandatory. Otherwise, the field is optional. | Conditional on other fields |
| 22 | Country | ISO 3166-1 alpha-2 Country Code | | Mandatory |
| 23 | Country subdivision | Max 35 text | If field 22 = US, please provide state. If field 22 = CA, please provide province. Otherwise, do not populate. | Conditional on other fields |
| 24 | IBAN | Max 34 text<br>Text must be a valid IBAN. Do not use spaces or any other formatting characters. | Either IBAN or account number must be provided. For SEPA transactions, IBAN is required. Otherwise, IBAN is optional. It is recommended to always provide the IBAN if available. | Conditional on other fields |
| 25 | Account number | Max 34 text<br>Do not use spaces or any other formatting characters. | Either account number or IBAN must be provided. If IBAN is provided, it is still recommended to provide the account number. | Conditional on other fields |
| 26 | Bank SWIFT BIC | Max 11 text<br>Must be a valid SWIFT BIC (8 or 11 characters) | Mandatory for SEPA Credit Transfers, otherwise optional. It is recommended to always provide the SWIFT BIC if available. | Conditional on other fields |
| 27 | Bank code | Max 35 text<br>Do not use spaces or any other formatiing characters | Mandatory if the SWIFT BIC is not available, otherwise optional. It is recommended to always provide the bank code if available.<br>If the branch ID needs to be provided, please delimit it with a pipe character. For example **aaaaaa\|bbb**, where **aaaaaa** is a bank code and **bbb** is a branch code. For cases where only the branch ID needs to be provided, please use **\|bbb**, including the pipe character. | Conditional on other fields |
| 28 | Bank country | ISO 3166-1 alpha-2 Country Code | If IBAN and BIC are not specified, the bank country code must be provided. | Conditional on other fields |
| 29 | Bank country subdivision | Max 35 text | If field 28 = US, please provide state. If field 28 = CA, please provide province. Otherwise do not populate. | Conditional on other fields |

## Direct Debit Information

This section is mandatory for SEPA Direct Debits.

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 30 | Creditor ID | Max 35 text | SEPA creditor ID | Conditional on other fields |
| 31 | Unique mandate reference | Max 35 text | | Conditional on other fields |
| 32 | Mandate signature date | ISO 8601 Date (yyyy-mm-dd) | | Conditional on other fields |
| 33 | Sequence type | FRST<br>FNAL<br>OOFF<br>RCUR | FRST = first<br>FNAL = final<br>OOFF = one off<br>RCUR = recurring | Conditional on other fields |
| 34 | Direct debit type | CORE<br>CORE1<br>B2B | | Conditional on other fields |

## Initiating Party Information

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 35 | Name | Max 70 text | | Optional |
| 36 | Street and building number | Max 70 text | | Optional |
| 37 | Postal code | Max 16 text | | Optional |
| 38 | Town name | Max 35 text | If any data is provided in fields 36-37, then field 38 must be populated. | Conditional on other fields |
| 39 | Country | ISO 3166-1 alpha-2 Country Code | | Optional |
| 40 | Country subdivision | Max 35 text | If field 39 = US, please provide state. If field 39 = CA, please provide province. Otherwise, do not populate. | Conditional on other fields |

## Ultimate Initiating Party Information

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 41 | Name | Max 70 text | | Optional |
| 42 | Street and building number | Max 70 text | | Optional |
| 43 | Postal code | Max 16 text | | Optional |
| 44 | Town name | Max 35 text | If any data is provided in fields 42-43, then field 44 must be populated. | Conditional on other fields |
| 45 | Country | ISO 3166-1 alpha-2 Country Code | | Optional |
| 46 | Country subdivision | Max 35 text | If field 45 = US, please provide state. If field 45 = CA, please provide province. Otherwise, do not populate. | Conditional on other fields |

## Payment Instructions

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 47 | Payment instruction 1 | Max 50 text | Payment instructions are to be used for special country/payment type specific instructions. (For example, TaxId, KID No).<br>For detailed information, please contact your Implementation Manager or see country-specific documentation. | Optional |
| 48 | Payment instruction 2 | Max 50 text | | Optional |
| 49 | Payment instruction 3 | Max 50 text | | Optional |
| 50 | Payment instruction 4 | Max 50 text | | Optional |
| 51 | Payment instruction 5 | Max 50 text | | Optional |
| 52 | Payment instruction 6 | Max 50 text | | Optional |
| 53 | Payment instruction 7 | Max 50 text | | Optional |
| 54 | Payment instruction 8 | Max 50 text | | Optional |
| 55 | Payment instruction 9 | Max 50 text | | Optional |
| 56 | Payment instruction 10 | Max 50 text | | Optional |

## Sending Bank General Information

Also see fields 6-9.

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 57 | Bank name | Max 70 text | | Optional |
| 58 | Street and building number | Max 70 text | | Optional |
| 59 | Postal code | Max 16 text | | Optional |
| 60 | Town name | Max 35 text | If any data is provided in fields 58-59, then field 60 must be populated. | Conditional on other fields |

## Receiving Bank General Information

Also see fields 26-29.

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 61 | Bank name | Max 70 text | | Optional |
| 62 | Street and building number | Max 70 text | | Optional |
| 63 | Postal code | Max 16 text | | Optional |
| 64 | Town name | Max 35 text | If any data is provided in fields 62-63, then field 64 must be populated. | Conditional on other fields |

## Intermediary Bank Information

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 65 | Bank name | Max 70 text | | Optional |
| 66 | Street and building number | Max 70 text | | Optional |
| 67 | Postal code | Max 16 text | | Optional |
| 68 | Town name | Max 35 text | If any data is provided in fields 66-67, then field 68 must be populated. | Conditional on other fields |
| 69 | Country | ISO 3166-1 alpha-2 Country Code | | Optional |
| 70 | Country subdivision | | If field 69 = US, please provide state. If field 69 = CA, please provide province. Otherwise, do not populate. | Conditional on other fields |
| 71 | IBAN | Max 34 text<br>Text must be a valid IBAN. Do not use spaces or any other formatting characters. | | Optional |
| 72 | Account number | Max 34 text<br>Do not use spaces or any other formatting characters. | | Optional |
| 73 | Bank SWIFT BIC | Max 11 text<br>Must be a valid SWIFT BIC (8 or 11 characters). | This is the only recommended field if an intermediary bank is used in the settlement instructions. | Optional |
| 74 | Bank code | Max 35 text<br>Do not use spaces or any other formatting characters. | If the branch ID needs to be provided, please delimit it with a pipe character. For example **aaaaaa\|bbb**, where **aaaaaa** is a bank code and **bbb** is a branch code. For cases where only the branch ID needs to be provided, please use **\|bbb**, including the pipe character. | Optional |

## Additional Information

Information in this section is not sent to the bank.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Important:

Do not provide data in these fields unless instructed by Coupa.

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| 75 | Category ID | Integer | Planning category ID as defined in coupa Teasury. | As agreed during implementation |
| 76 | Project ID | Integer | Project ID as defined in Coupa Treasury. | As agreed during implementation |
| 77 | Portfolio ID | Integer | Portfolio ID as defined in Coupa Treasury. | As agreed during implementation |
| 78 | Comments | Max 255 text | | As agreed during implementation |
| 79 | Cash forecast value date | ISO 8601 date (yyyy-mm-dd) | Specify/override cash forecast value date. If not specified, Coupa Treasury will use internally defined rules to automatically assign a value date to the cash forecast entry. | As agreed during implementation |
| 80 | Template ID | Integer | | As agreed during implementation |
| 81 | Intended transaction type | Integer or max 50 text | If applicable, Coupa will provide the values to reference transaction types during implementation. | As agreed during implementation |
| 82 | Username | Max 50 text | | As agreed during implementation |

## Invoice Details for Credits

This section is optional.

If invoice details need to be provided, invoice details record(s) must immediately follow corresponding transaction details record.

Credit records (see field 1 description) must include a transaction identifier and the value provided in the invoice record must match corresponding transaction identifier. Multiple invoice records can accompany single C-record. Data population requirements for fields in the invoice record depend on thefinancial institution that will receive credit/debit transfer initiation instruction.

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| I-1 | Data record type identifier | I | I = Invoice details | Mandatory |
| I-2 | Transcation identifier | Max 35 text | Unique transaction identifier, must match the value in preceding C-record | Mandatory |
| I-3 | Related Remittance Identification | Max 35 text | If multiple invoice records (I-record) accompany the C-record, this value must be identical in each I-record. | Conditional on other fields |
| I-4 | Remittance advice delivery method | Code | Use one of the following values:<br>EDIC – EDI<br>EMAL – Email<br>FAXI – Fax<br>POST – Post<br>SMSM – SMS message<br>URID - URI | Conditional on other fields |
| I-5 | Remittance advice electronics address | Max 2048 text | If multiple I-records accompany the C-record, this value must be identical in each I-record. If field I-4 has the value EMAL, the value in I-5 must be a valid email address. | Conditional on other fields |
| I-6 | Remittance advice postal address – name | Max 70 text | Populate only if field I-4 has the value POST. If multiple I-records accompany the C-record, this value must be identical in each I-record. If any data exists in fields I-7 through I-11, then I-6 must have a value. | Conditional on other fields |
| I-7 | Remittance advice postal address – address line | Max 70 text | Populate only if field I-4 has value POST. If multiple I-records accompany the C-record, this value must be identical in each I-record. | Conditional on other fields |
| I-8 | Postal code | Max 16 text | Populate only if field I-4 has value POST. If multiple I-records accompany the C-record, this value must be identical in each I-record. | Conditional on other fields |
| I-9 | Town name | Max 35 text | Populate only if field I-4 has value POST. If multiple I-records accompany the C-record, this value must be identical in each I-record. If any data is provided in fields I-7 through I-9, field I-10 must be populated. | Conditional on other fields |
| I-10 | Country | ISO 3166-1 alpha-2 Country Code | Populate only if field I-4 has value POST. If multiple I-records accompany the C-record, this value must be identical in each I-record. | Conditional on other fields |
| I-11 | Country subdivision | Max 35 text | Populate only if field I-4 has the value POST. If multiple I-records accompany the C-record, this value must be identical in each I-record. If field I-11 = US, please provide the state; if field I-11 = CA, please provide the province. Otherwise, do not populate. | Conditional on other fields |
| I-12 | Document type | Code or max 35 text | Use one of the following values:<br>AROI =account receivable open item<br>BOLD =bill of landing<br>INV = commercial invoice<br>CMCN = commercial contract<br>CNFA = credit note related to financial adjustment<br>CREN =credit note<br>DEBN = debit note<br>DISP = dispatch advice<br>DNFA = debit note related to financial adjustment<br>HIRI = hire invoice<br>MSIN = metered service invoice<br>SBIN = self-billed invoice<br>SOAC = statement of account<br>TSUT = trade services utility transaction<br>VCHR = voucher<br>Otherwise, provide a custom value up to 35 characters long. | Conditional on other fields |
| I-13 | Document number | Max 35 text | | Conditional on other fields |
| I-14 | Related date | ISO8601 Date (yyyy-mm-dd) | | Conditional on other fields |
| I-15 | Due payable amount | Unsigned numeric amount (decimal separator is a dot) | | Conditional on other fields |
| I-16 | Due payable amount currency | 3-character ISO 4217 Currency Code | | Conditional on other fields |
| I-17 | Discount applied amount | Unsigned numeric amount (decimal separator is a dot) | | Conditional on other fields |
| I-18 | Discount applied amount currency | 3-character ISO 4217 Currency Code | | Conditional on other fields |
| I-19 | Credit note amount | Unsigned numeric amount (decimal separator is a dot) | | Conditional on other fields |
| I-20 | Credit note amount currency | 3-character ISO 4217 Currency Code | | Conditional on other fields |
| I-21 | Tax amount | Unsigned numeric amount (decimal separator is a dot) | | Conditional on other fields |
| I-22 | Tax amount currency | 3-character ISO 4217 Currency Code | | Conditional on other fields |
| I-23 | Remitted amount | Unsigned numeric amount (decimal separator is a dot) | | Conditional on other fields |
| I-24 | Remitted amount currency | 3-character ISO 4217 Currency Code | | Conditional on other fields |
| I-25 | Creditor reference information type | Code or max 35 text | Use one of the following values:<br>DISP =dispatch advice<br>FXDR = foreign exchange deal reference<br>PUOR = purchase order<br>RADM = remittance advice message<br>RPIN = related payment instruction<br>SCOR = structured communication reference<br>Otherwise, provide a custom value up to 35 characters long. | Conditional on other fields |
| I-26 | Creditor reference information | Max 35 text | | Conditional on other fields |
| I-27 | Additional remittance information | Max 140 text | | Conditional on other fields |

## File Footer

This entire section is optional, although we recommend including a footer in your file.

| Field | Name | Format | Description | Mandatory |
| --- | --- | --- | --- | --- |
| F1 | Footer identifier | F | Indicates that the record is a file footer. | Mandatory |
| F2 | Transaction type | C or D | C = Credit transfer<br>D = Direct debit | Mandatory |
| F3 | File or batch identifier | Maxt 35 text | Optional file identifier: file name or batch number. | Optional |
| F4 | Total count of transaction | Number | Total number of transactions in the file. | Mandatory |
| F5 | Total sum of transactions | Numeric amount (decimal separator is a dot) | Total sum of transactions in the file, regardless of the currency. | Mandatory |

## Format rules

There are four sections to the credit/debit import format:

- Header

- Transaction

- Invoice

- Footer

Only the Transaction section (fields 1-82) is mandatory, although we recommend including a header and footer in each file.

Each file may contain multiple credits (C-records) or multiple debits (D-records), but a file may not have both credit and debit records. The Invoice section is only applicable for C-records. If invoices are relevant to the C-record, ensure the relevant data in the Invoices section (I-record) matches data in the C-record. Each C-record may have multiple associatd I-records within the same file.

The file may only contain transactions with a single initiating bank. In some cases, you must provide separate files per bank branch.

- Field delimiter is a comma (,).

- Fields which may contain commas must be wrapped in double quotes to prevent shifting or breaking the fields. Alternatively, all fields may be wrapped in quotation marks.

- Optional fields may be left empty, but must still be marked with a field delimiter to indicate an empty value. If all fields are quoted, the empty value should be marked by opening and closing quotation marks, followed by a field delimiter.

- File encoding may be ANSI or Unicode.

- For ANSI, only the Western European subset of characters is supported.

- Unicode should include the byte order mark, also known as Unicode signature.

## Example data set: credit

H,C,ID6645454 C,TransID100001,DE24200907000030004711,,EUR,SOLADEST,,DE,,E2E1234,199.33,EUR,2016-03-02,Remittance information,SHAR,,,Hans Mustermann,Hauptstrasse 1,12345,Musterstadt,DE,,DE36664900001234567892,,GENODE61OG1,,DE,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, C,TransID100002,DE24200907000030004711,,EUR,SOLADEST,,DE,,E2E5678,622.15,EUR,2016-03-02,Remittance information,SHAR,,,Maria Mustermann,Hauptstrasse 1,12345,Musterstadt,DE,,DE91370100501122334459,,PBNKDEFFXXX,,DE,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, F,C,ID6645454,2,821.48

## Example data set: debit

H,D,ID6645455 D,TransID200001,DE24200907000030004711,,EUR,SOLADEST,,DE,,E2E2345,1122.45,EUR,2016-03-02,Remittance information,SHAR,,,Hans Mustermann,Hauptstrasse 1,12345,Musterstadt,DE,,DE36664900001234567892,,GENODE61OG1,,DE,,,SEPA Mandate Reference 0001,2016-01-01,OOFF,CORE,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, D,TransID200002,DE24200907000030004711,,EUR,SOLADEST,,DE,,E2E5678,99.14,EUR,2016-03-02,Remittance information,SHAR,,,Maria Mustermann,Hauptstrasse 1,12345,Musterstadt,DE,,DE91370100501122334459,,PBNKDEFFXXX,,DE,,,SEPA Mandate Reference 0002,2016-01-01,OOFF,CORE,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, F,D,ID6645455,2,1221.59
