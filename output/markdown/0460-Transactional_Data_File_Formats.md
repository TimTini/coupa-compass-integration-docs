---
title: "Transactional Data File Formats"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/ccw-flat-files-(csv)/transactional-data-file-formats"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/ccw-flat-files-(csv)/transactional-data-file-formats"
status_code: 200
fetched_at: "2026-04-09T12:00:52+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "CCW Flat Files (CSV)"
  - "Transactional Data File Formats"
---

# Transactional Data File Formats

Customers, before attempting to integrate the file formats described in this document, please review the following notes first:

## If you are in the middle of an implementation

Please contact your Coupa Solutions Architect for assistance with file imports.

## If you have legacy, custom integration formats that differ significantly from what is described below

Please contact your Coupa CVM about switching to the formats described in this document.

## Everyone else

Please contact Coupa support for assistance with adding any of the fields below to an existing integration file.

## Contingent Worker (CW)

**Description:** Contingent Worker data export that customers consume into enterprise applications to manage access provisioning, asset provisioning, etc.

**Supported load:** Delta File

**Supported Delimiters:** Pipe(|), Comma(,)

**Supported file extensions:** .csv, .txt

| **Fields** | **Data Type & Length** | **Mandatory** | **Allowed Values** | **Example** |
| --- | --- | --- | --- | --- |
| Status Flag | string(2) | Yes | N, T, X, C, R, RT [Status : N – New Contingent Worker, T – Terminate Contingent Worker, X – No Show Contingent Worker, C – CW info Changes, R – Rehire, utilization of previously assigned CW’s external reference ID, RT- Rollback termination]. | N |
| CCW CW Number | string(200) | Yes | Any | CCW-CW-000001 |
| External reference ID 1 | string(200) | No | Any | Blank or 000001 |
| External reference ID 2 | string(200) | No | Any | Blank or 0NST1 |
| External reference ID 3 | string(200) | No | Any | Blank or QR12E |
| CCW ID | string(15) | Yes | Any | 00001231 |
| Last Name | string(100) | Yes | Any | Pearson |
| First Name | string(100) | Yes | Any | Michael |
| Middle Name | string(100) | No | Any | B |
| Start Date | string(10) | Yes | Any Date, YYYY-MM-DD | 2018-03-01 |
| End Date | string(10) | Yes | Any Date, YYYY-MM-DD | 2019-04-01 |
| Email | string(400) | Yes | Any | mikeHarshley_test@coupatest |
| Phone Number | String(20) | No | Any | Phone number captured in system |
| Manager ID | string(100) | No | Any | 038976 |
| Manager Email | string(400) | Yes | Any | robertc@CCW.com |
| Alternate Hiring Manager Email | string(400) | Yes | Any | joec@CCW.com |
| Work Location Code | string(40) | Yes | Any, work Location code assigned to CW | NJB01F02C1 |
| Job Code | string(400) | Yes | Any | A23G |
| Job Title | string(400) | Yes | Any | Talent Acquisition Consultant |
| Supplier Name | string(400) | Yes | Any | Test Tech Solutions |
| Supplier Email | string(400) | Yes | Any | jamescon@Customer.com |
| Supplier Reference Number | string(200) | Yes | Any | 0099898780 |
| Supplier City | string(400) | Yes | Any | Cuyahoga |
| Supplier State | string(400) | Yes | Any | Ohio |
| Supplier Zip Code | string(10) | Yes | Any | 43532 |
| Regular Bill Rate | number(45,8) | Yes | Any | 200.00 |
| Requisition Number | string(200) | Yes | Any | CCW-Req-30234 |
| Termination Reason | string(400) | No | | Engagement Completed |
| Type of Service | string(100) | No | Any | 80936 |
| Master Data Segment 1 Name | string(255) | Yes | Any | Master Data Segment 1 name assigned to CW |
| Master Data Segment 1 Code | string(255) | No | Any | Master Data Segment 1 code assigned to CW |
| Master Data Segment 2 Name | string(255) | Yes | Any | Master Data Segment 2 name assigned to CW |
| Master Data Segment 2 Code | string(255) | No | Any | Master Data Segment 2 code assigned to CW |
| Master Data Segment 3 Name | string(255) | Yes | Any | Master Data Segment 3 name assigned to CW |
| Master Data Segment 3 Code | string(255) | No | Any | Master Data Segment 3 code assigned to CW |
| Master Data Segment 4 Name | string(255) | Yes | Any | Master Data Segment 4 name assigned to CW |
| Master Data Segment 4 Code | string(255) | No | Any | Master Data Segment 4 code assigned to CW |
| Master Data Segment 5 Name | string(255) | Yes | Any | Master Data Segment 5 name assigned to CW |
| Master Data Segment 5 Code | string(255) | No | Any | Master Data Segment 5 code assigned to CW |
| Master Data Segment 6 Name | string(255) | Yes | Any | Master Data Segment 6 name assigned to CW |
| Master Data Segment 6 Code | string(255) | No | Any | Master Data Segment 6 code assigned to CW |
| Master Data Segment 7 Name | string(255) | Yes | Any | Master Data Segment 7 name assigned to CW |
| Master Data Segment 7 Code | string(255) | No | Any | Master Data Segment 7 code assigned to CW |
| Master Data Segment 8 Name | string(255) | Yes | Any | Master Data Segment 8 name assigned to CW |
| Master Data Segment 8 Code | string(255) | No | Any | Master Data Segment 8 code assigned to CW |
| Master Data Segment 9 Name | string(255) | Yes | Any | Master Data Segment 9 code assigned to CW |
| Master Data Segment 9 Code | string(255) | No | Any | Master Data Segment 9 code assigned to CW |
| Master Data Segment 10 Name | string(255) | Yes | Any | Master Data Segment 10 code assigned to CW |
| Master Data Segment 10 Code | string(255) | No | Any | Master Data Segment 10 code assigned to CW |
| Master Data Segment 11 Name | string(255) | Yes | Any | Master Data Segment 10 code assigned to CW |
| Master Data Segment 11 Code | string(255) | No | Any | Master Data Segment 11 code assigned to CW |
| Requisition Question 1 | string(100) | No | Any | |
| Requisition Question 2 | string(100) | No | Any | |
| Requisition Question 3 | string(100) | No | Any | |
| Requisition Question 4 | string(100) | No | Any | |
| Requisition Question 5 | string(100) | No | Any | |
| Requisition Question 6 | string(100) | No | Any | |
| Requisition Question 7 | string(100) | No | Any | |
| Requisition Question 8 | string(100) | No | Any | |
| Requisition Question 9 | string(100) | No | Any | |
| Requisition Question 10 | string(100) | No | Any | |

## Contingent Worker External Reference Number

**Description:** Customer’s system ID assigned to uniquely identified CW. Used as a reference check when processing CW Export, invoice from CCW **[ Example changes, terminations to CCW, timesheet management, building rehire business logic in customer’s HR system (if applicable)]. **External Reference ID 2 and External Reference ID 3 are available only for CW export configured at Confirm CW, or if a customer chooses to update these fields after a candidate is confirmed.

**Supported load:** Delta File (recommended)

**Supported Delimiters:** Pipe(|), Comma(,)

**Supported file extensions:** .csv, .txt

| **Fields** | **Data Type & Length** | **Mandatory** | **Allowed Values** | **Example** |
| --- | --- | --- | --- | --- |
| CCW CW Number | string(100) | Yes | Any | CCW-CW-000001 |
| CW external reference ID 1 | string(100) | Yes | Any | CCW external reference ID in Customer’s system (89876790) |
| CW external reference ID 2 | string(100) | No | Any | CCW external reference ID in Customer’s system (89876790) |
| CW external reference ID 3 | string(100) | No | Any | CCW external reference ID in Customer’s system (89876790) |
| Work Email | string(100) | No | Any | sam.peter@ccwdoc.com |

## Invoice Data

**Description:** Batch data approved in CCW, which can include data related to approved timesheet, approved expense, Payment line Item against a Statement of Work.

**Supported load:** Delta File

**Supported Delimiters:** Pipe(|), Comma(,)

**Supported file extensions:** .csv, .txt

## Invoice header

| **Sr. No.** | **Fields** | **Data Type & Length** | **Mandatory** | **Allowed Values** | **Example** |
| --- | --- | --- | --- | --- | --- |
| 1 | Record Type | string(1) | Yes | Static value ‘H’ | H |
| 2 | Batch Number | string(255) | Yes | Any, Batch Number | CCW-BAT000001-1019 |
| 3 | Batch Creation Date | date | Yes | Batch Creation date<br>ISO8601 format of YYYY-MM-DD | 2018-12-16 |
| 4 | Batch Approval Date | date | Yes | Batch Approve date<br>ISO8601 format of YYYY-MM-DD | 2018-12-16 |
| 5 | Invoice Number | string(100) | Yes | Any, Invoice Number | CCW-INV-000001-1019 |
| 6 | Total Invoice Lines | int | Yes | Total number of lines in invoice | 1 |
| 7 | Invoice Total Net Amount | number(45,8) | Yes | Total Invoice Amount without Tax<br>2 decimal precision | 100.00 |
| 8 | Invoice Total Tax Amount | number(45,8) | Yes | Invoice Total Tax Amount<br>2 decimal precision | 0.00 |
| 9 | Invoice Total Gross Amount | number(45,8) | Yes | Total Invoice Amount with Tax Amount<br>2 decimal precision | 100.00 |

## Invoice lines

| **Sr. No.** | **Fields** | **Data Type & Length** | **Mandatory** | **Business Logic** | **Example** | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Timesheet** | **Expense** | **SOW (Fixed)** | | | | | |
| 1 | Record Type | string(1) | Yes | Static value ‘L’ | Static value ‘L’ | Static value ‘L’ | L |
| 2 | Invoice Number | string(100) | Yes | Invoice Number | Invoice Number | Invoice Number | CCW-INV-000001-MMYY |
| 3 | Invoice line number | int | Yes | Invoice line number | Invoice line number | Invoice line number | 1 |
| 4 | Invoice line Date | date | Yes | Week ending date | Expense from Date | Payment line item approved date | 2018-12-16 |
| 5 | Invoice Line Type | string(10) | Yes | Static value “Timesheet” | Static value “Expense” | Static value “SOW” | Timesheet |
| 6 | Line Item description | string(1550) | No | CW number – Week Ending Date | CW number – Expense from Date | Payment line item description | CCW-CW-00001 – 2018-12-16 |
| 7 | Report ID | string(400) | No | Timesheet Number | Expense Report Number | SOW Number | 1604479 |
| 8 | Expense Type | string(100) | No | Will be blank | Expense type associated with the invoice line | Will be Blank | Hotel |
| 9 | Supplier Name | string(400) | No | Supplier Name | Supplier Name | Supplier Name | Test Supplier INC |
| 10 | CCW Supplier Number | string(400) | No | Supplier Number in CCW | Supplier Number in CCW | Supplier Number in CCW | SUP-9987 |
| 11 | Supplier HR Reference Number | string(100) | No | Customer’s ERP system’s supplier number (Accounting vendor ID - if configured in CCW, else will be sent blank) | Customer’s ERP system’s supplier number (Accounting vendor ID - if configured in CCW, else will be sent blank) | Customer’s ERP system’s supplier number (Accounting vendor ID - if configured in CCW, else will be sent blank) | 00909088 |
| 12 | Supplier Number | string(400) | No | Supplier’s vendor ID in Customer’s ERP (vendor ID - if configured in CCW, else will be sent blank) | Supplier’s vendor ID in Customer’s ERP (vendor ID - if configured in CCW, else will be sent blank) | Supplier’s vendor ID in Customer’s ERP (vendor ID - if configured in CCW, else will be sent blank) | 0010005 |
| 13 | Remit to Line 1 | string(400) | No | Any, Supplier’s Remit location line 1 | Any, Supplier’s Remit location line 1 | Any, Supplier’s Remit location line 1 | Centerpoint at East Gate |
| 14 | Remit to Line 2 | string(400) | No | Any, Supplier’s Remit location line 2 | Any, Supplier’s Remit location line 2 | Any, Supplier’s Remit location line 2 | 161 Gaither Drive, Suite 210 |
| 15 | Remit to City | string(100) | No | Any, Supplier’s Remit location city | Any, Supplier’s Remit location city | Any, Supplier’s Remit location city | Mount Laurel |
| 16 | Remit to State | string(100) | No | Any, Supplier’s Remit location state | Any, Supplier’s Remit location state | Any, Supplier’s Remit location state | NJ |
| 17 | Remit to Postal Code | string(20) | No | Any, Supplier’s Remit location postal code | Any, Supplier’s Remit location postal code | Any, Supplier’s Remit location postal code | 08054 |
| 18 | Remit to Country | string(255) | No | Any, Supplier’s Remit location Country.<br>ISO 3-Alpha representation (Static info) | Any, Supplier’s Remit location Country.<br>ISO 3-Alpha representation (Static info) | Any, Supplier’s Remit location Country.<br>ISO 3-Alpha representation (Static info) | USA |
| 19 | Billing Supplier Name | string(400) | No | Billing Supplier Name | Billing Supplier Name | Billing Supplier Name | My MSP |
| 20 | Billing Supplier Number | string(400) | No | Billing Supplier's vendor ID in Customer's ERP (vendor ID if configured in CCW, otherwise will be sent blank) | Billing Supplier's vendor ID in Customer's ERP (vendor ID if configured in CCW, otherwise will be sent blank) | Billing Supplier's vendor ID in Customer's ERP (vendor ID if configured in CCW, otherwise will be sent blank) | 99897909 |
| 21 | Requirement Id | String(20) | No | Requirement number against CW is hired | Requirement number against CW is hired | Will be blank | CCW-REQ-1234 |
| 22 | CW Number | string(100) | No | CW number | CW number | Will be blank | CCW-CW-00001 |
| 23 | Purchase Order Number | string | No | PO number related to billing supplier | PO number related to billing supplier | PO number related to billing supplier | |
| 24 | Coupa Purchase Order ID | number | No | Coupa PO ID | Coupa PO ID | Coupa PO ID | |
| 25 | Purchase Order Line Number | number | No | Line number on PO | Line number on PO | Line number on PO | |
| 26 | PO Classification | string | No | When PO is there, it will be Supplier, MSP, Coupa, otherwise the value will be blank | When PO is there, it will be Supplier, MSP, Coupa, otherwise the value will be blank | When PO is there, it will be Supplier, MSP, Coupa, otherwise the value will be blank | Supplier |
| 27 | CW First Name | string(100) | No | CW First Name | CW First Name | Will be blank | Alax |
| 28 | CW Last Name | string(100) | No | CW Last Name | CW Last Name | Will be blank | Will |
| 29 | Manager ID | string(100) | No | Manager ID | Manager ID | Will be blank | 69767 |
| 30 | Manager Email | string(100) | No | Manager Email | Manager Email | Will be blank | vindyan@gmail.com |
| 31 | Manager First Name | string(100) | No | Manager First Name | Manager First Name | Will be blank | Steve |
| 32 | Manager Last Name | string(100) | No | Manager Last Name | Manager Last Name | Will be blank | Smith |
| 33 | CW external reference ID | string(200) | No | CT # 1 for CW | CT # 1 for CW | Will be blank | 00001 |
| 34 | Work Location ID | string(40) | No | CW Work Location ID | CW Work Location ID | Will be blank | CCW0078 |
| 35 | Work Location Name | string(100) | No | CW Work Location Name | CW Work Location Name | Will be blank | Locan |
| 36 | County | string(100) | No | CW Work Location County | CW Work Location County | Will be blank | Cuyahoga |
| 37 | State | string(100) | No | CW Work Location state | CW Work Location state | Will be blank | Ohio |
| 38 | Country | string(3) | No | CW Work Location country<br>ISO 3166 alpha-3 | CW Work Location country<br>ISO 3166 alpha-3 | Will be blank | USA |
| 39 | Postal Code | string(10) | No | CW Work Location Postal Code | CW Work Location Postal Code | Will be blank | 76429 |
| 40 | Pay Code | string(300) | No | Populated, if hours are entered against a pay code | Will be blank | Will be blank | |
| 41 | Regular Hours | number (45,8) | No | # of regular hours for the period / Week ending date<br>2 decimal precision | Will be blank | Will be blank | 40.00 |
| 42 | Over Time hours | number (45,8) | No | # of OT hours for the period / Week ending date<br>2 decimal precision, 0.00 if there is no OT Bill rate | Will be blank | Will be blank | 5.00 |
| 43 | Double Time hours | number (45,8) | No | # of DT hours for the period / Week ending date<br>2 decimal precision, 0.00 if there is no OT Bill rate | Will be blank | Will be blank | 5.00 |
| 44 | Total Hours | number (45,8) | No | Total # of hours for the period / Week ending date 2 decimal precision | Will be blank | Will be blank | 40.00 |
| 45 | Regular bill Rate | number (45,8) | No | Bill rate for Regular Hrs.<br>2 decimal precision | Will be blank | Will be blank | 25.00 |
| 46 | Over Time bill Rate | number (45,8) | No | Bill rate for Over Time Hrs.<br>2 decimal precision | Will be blank | Will be blank | 25.00 |
| 47 | Double Time bill Rate | number (45,8) | No | Bill rate for Double Time Hrs.<br>2 decimal precision | Will be blank | Will be blank | 25.00 |
| 48 | Supplier Regular Bill Rate | number (45,8) | No | Supplier Bill rate for Regular Hrs. 2 decimal precision | Will be blank | Will be blank | 25.00 |
| 49 | Supplier Over Time Bill Rate | number (45,8) | No | Supplier Bill rate for Over Time Hrs. 2 decimal precision | Will be blank | Will be blank | 25.00 |
| 50 | Supplier Double Time Bill Rate | number (45,8) | No | Supplier Bill rate for Double Time Hrs. 2 decimal precision | Will be blank | Will be blank | 25.00 |
| 51 | Regular Pay Rate | number (45,8) | No | Pay rate for Regular Hrs.<br>2 decimal precision | Will be blank | Will be blank | 25.00 |
| 52 | Over Time Pay Rate | number (45,8) | No | Pay rate for Over Time Hrs.<br>2 decimal precision | Will be blank | Will be blank | 25.00 |
| 53 | Double Time Pay Rate | number (45,8) | No | Pay rate for Double Time Hrs.<br>2 decimal precision | Will be blank | Will be blank | 25.00 |
| 54 | Regular Pay Amount | number (45,8) | No | Pay Amount for Regular Hrs. 2 decimal precision | Will be blank | Will be blank | 200.00 |
| 55 | Over Time Pay Amount | number (45,8) | No | Pay Amount for Over Time Hrs. 2 decimal precision | Will be blank | Will be blank | 250.00 |
| 56 | Double Time Pay Amount | number (45,8) | No | Pay Amount for Double Time Hrs. 2 decimal precision | Will be blank | Will be blank | 300.00 |
| 57 | Final Regular Pay Amount | number (45,8) | No | Final Pay Amount for Regular Hrs. 2 decimal precision | Will be blank | Will be blank | 200.00 |
| 58 | Final Over Time Pay Amount | number (45,8) | No | Final Pay Amount for Over Time Hrs. 2 decimal precision | Will be blank | Will be blank | 250.00 |
| 59 | Final Double Time Pay Amount | number (45,8) | No | Final Pay Amount for Double Time Hrs. 2 decimal precision | Will be blank | Will be blank | 300.00 |
| 60 | Supplier Regular Amount | number (45,8) | No | Supplier Pay Amount for Regular Hrs. 2 decimal precision | Will be blank | Will be blank | 25.00 |
| 61 | Supplier Over Time Amount | number (45,8) | No | Supplier Pay Amount for Over Time Hrs. 2 decimal precision | Will be blank | Will be blank | 25.00 |
| 62 | Supplier Double Time Amount | number (45,8) | No | Supplier Pay Amount for Double Time Hrs. 2 decimal precision | Will be blank | Will be blank | 25.00 |
| 63 | Total Supplier Amount | number (45,8) | No | Supplier Total Pay Amount for Time Hrs. 2 decimal precision | Will be blank | Will be blank | 75.00 |
| 64 | MSP Fee | number (45,8) | No | MSP Fee if applicable.<br>2 decimal precision | MSP Fee if applicable.<br>2 decimal precision | MSP Fee if applicable.<br>2 decimal precision | 2.00 |
| 65 | VMS Fee | number (45,8) | No | VMS Fee if applicable.<br>2 decimal precision | VMS Fee if applicable.<br>2 decimal precision | VMS Fee if applicable.<br>2 decimal precision | 0.50 |
| 66 | Line Amount | number (45,8) | Yes | Total Line Amount<br>2 decimal precision | Total Line Amount<br>>2 decimal precision | Total Line Amount<br>2 decimal precision | 100.00 |
| 67 | Line Tax Amount | number (45,8) | Yes | Total line tax amount<br>2 decimal precision, 0.00 if there is no tax | Total line tax amount<br>2 decimal precision, 0.00 if there is no tax | Total line tax amount<br>2 decimal precision, 0.00 if there is no tax | 0.00 |
| 68 | Currency Code | string(3) | Yes | Currency for invoice<br>ISO 4217, 3-Alpha | Currency for invoice<br>ISO 4217, 3-Alpha | Currency for invoice<br>ISO 4217, 3-Alpha | USD |
| 69 | Job Title | string(100) | No | CW's Job Title | CW's Job Title | Will be blank | Sr. Developer |
| 70 | Master Data Segment-1 Name | string(255) | No | Segment 1 assigned to CW | Segment 1 assigned to CW | Will be blank | 78967-52 |
| 71 | Master Data Segment-1 | string(255) | No | Segment 1 assigned to CW | Segment 1 assigned to CW | Will be blank | 78967-52 |
| 72 | Master Data Segment-2 Name | string(255) | No | Segment 2 assigned to CW | Segment 2 assigned to CW | Will be blank | |
| 73 | Master Data Segment-2 | string(255) | No | Segment 2 assigned to CW | Segment 2 assigned to CW | Will be blank | |
| 74 | Master Data Segment-3 Name | string(255) | No | Segment 3 assigned to CW | Segment 3 assigned to CW | Will be blank | |
| 75 | Master Data Segment-3 | string(255) | No | Segment 3 assigned to CW | Segment 3 assigned to CW | Will be blank | |
| 76 | Master Data Segment-4 Name | string(255) | No | Segment 4 assigned to CW | Segment 4 assigned to CW | Will be blank | |
| 77 | Master Data Segment-4 | string(255) | No | Segment 4 assigned to CW | Segment 4 assigned to CW | Will be blank | |
| 78 | Master Data Segment-5 Name | string(255) | No | Segment 5 assigned to CW | Segment 5 assigned to CW | Will be blank | |
| 79 | Master Data Segment-5 | string(255) | No | Segment 5 assigned to CW | Segment 5 assigned to CW | Will be blank | |
| 80 | Master Data Segment-6 Name | string(255) | No | Segment 6 assigned to CW | Segment 6 assigned to CW | Will be blank | |
| 81 | Master Data Segment-6 | string(255) | No | Segment 6 assigned to CW | Segment 6 assigned to CW | Will be blank | |
| 82 | Master Data Segment-7 Name | string(100) | No | Segment 7 assigned to CW | Segment 7 assigned to CW | Will be blank | |
| 83 | Master Data Segment-7 | string(100) | No | Segment 7 assigned to CW | Segment 7 assigned to CW | Will be blank | |
| 84 | Master Data Segment-8 Name | string(100) | No | Segment 8 assigned to CW | Segment 8 assigned to CW | Will be blank | |
| 85 | Master Data Segment-8 | string(100) | No | Segment 8 assigned to CW | Segment 8 assigned to CW | Will be blank | |
| 86 | Master Data Segment-9 Name | string(100) | No | Segment 9 assigned to CW | Segment 9 assigned to CW | Will be blank | |
| 87 | Master Data Segment-9 | string(100) | No | Segment 9 assigned to CW | Segment 9 assigned to CW | Will be blank | |
| 88 | Master Data Segment-10 | string(100) | No | Segment 10 assigned to CW | Segment 10 assigned to CW | Will be blank | |
| 89 | Master Data Segment-10 Name | string(100) | No | Segment 10 assigned to CW | Segment 10 assigned to CW | Will be blank | |
| 90 | Master Data Segment-11 | string(100) | No | Segment 11 assigned to CW | Segment 11 assigned to CW | Will be blank | |
| 91 | Master Data Segment-11 Name | string(100) | No | Segment 11 assigned to CW | Segment 11 assigned to CW | Will be blank | |
| 92 | Chart Of Account Name | string(200) | No | For customers using CCW with Coupa Core, COA name associated to account.<br>Will be empty for standalone customers | For customers using CCW with Coupa Core, COA name associated to account.<br>Will be empty for standalone customers | For customers using CCW with Coupa Core, COA name associated to account.<br>Will be empty for standalone customers | |
| 93 | Account Code | string(500) | Yes | Account Code | Account Code | Account Code | 0100-999-2521 |
| 94 | Account Name | string(500) | No | Account Name | Account Name | Account Name | |
| 95 | Account Segment-1 | string(2000) | No | Account Segment 1 Code | Account Segment 1 Code | Account Segment 1 Code | 0100 |
| 96 | Account Segment-1 Name | string(2000) | No | Account Segment 1 Name | Account Segment 1 Name | Account Segment 1 Name | Account Segment 1 Name |
| 97 | Account Segment-2 | string(2000) | No | Account Segment 2 Code | Account Segment 2 Code | Account Segment 2 Code | 999 |
| 98 | Account Segment-2 Name | string(2000) | No | Account Segment 2 Name | Account Segment 2 Name | Account Segment 2 Name | Account Segment 2 Name |
| 99 | Account Segment-3 | string(2000) | No | Account Segment 3 Code | Account Segment 3 Code | Account Segment 3 Code | 2521 |
| 100 | Account Segment-3 Name | string(2000) | No | Account Segment 3 Name | Account Segment 3 Name | Account Segment 3 Name | Account Segment 3 Name |
| 101 | Account Segment-4 | string(2000) | No | Account Segment 4 Code | Account Segment 4 Code | Account Segment 4 Code | |
| 102 | Account Segment-4 Name | string(2000) | No | Account Segment 4 Name | Account Segment 4 Name | Account Segment 4 Name | |
| 103 | Account Segment-5 | string(2000) | No | Account Segment 5 Code | Account Segment 5 Code | Account Segment 5 Code | |
| 104 | Account Segment-5 Name | string(2000) | No | Account Segment 5 Name | Account Segment 5 Name | Account Segment 5 Name | |
| 105 | Account Segment-6 | string(2000) | No | Account Segment 6 Code | Account Segment 6 Code | Account Segment 6 Code | |
| 106 | Account Segment-6 Name | string(2000) | No | Account Segment 6 Name | Account Segment 6 Name | Account Segment 6 Name | |
| 107 | Account Segment-7 | string(2000) | No | Account Segment 7 Code | Account Segment 7 Code | Account Segment 7 Code | |
| 108 | Account Segment-7 Name | string(2000) | No | Account Segment 7 Name | Account Segment 7 Name | Account Segment 7 Name | |
| 109 | Account Segment-8 | string(2000) | No | Account Segment 8 Code | Account Segment 8 Code | Account Segment 8 Code | |
| 110 | Account Segment-8 Name | string(2000) | No | Account Segment 8 Name | Account Segment 8 Name | Account Segment 8 Name | |
| 111 | Account Segment-9 | string(2000) | No | Account Segment 9 Code | Account Segment 9 Code | Account Segment 9 Code | |
| 112 | Account Segment-9 Name | string(2000) | No | Account Segment 9 Name | Account Segment 9 Name | Account Segment 9 Name | |
| 113 | Account Segment-10 | string(2000) | No | Account Segment 10 Code | Account Segment 10 Code | Account Segment 10 Code | |
| 114 | Account Segment-10 Name | string(2000) | No | Account Segment 10 Name | Account Segment 10 Name | Account Segment 10 Name | |
| 115 | Account Segment-11 | string(2000) | No | Account Segment 11 Code | Account Segment 11 Code | Account Segment 11 Code | |
| 116 | Account Segment-11 Name | string(2000) | No | Account Segment 11 Name | Account Segment 11 Name | Account Segment 11 Name | |
| 117 | Account Segment-12 | string(2000) | No | Account Segment 12 Code | Account Segment 12 Code | Account Segment 12 Code | |
| 118 | Account Segment-12 Name | string(2000) | No | Account Segment 12 Name | Account Segment 12 Name | Account Segment 12 Name | |
| 119 | Account Segment-13 | string(2000) | No | Account Segment 13 Code | Account Segment 13 Code | Account Segment 13 Code | |
| 120 | Account Segment-13 Name | string(2000) | No | Account Segment 13 Name | Account Segment 13 Name | Account Segment 13 Name | |
| 121 | Account Segment-14 | string(2000) | No | Account Segment 14 Code | Account Segment 14 Code | Account Segment 14 Code | |
| 122 | Account Segment-14 Name | string(2000) | No | Account Segment 14 Name | Account Segment 14 Name | Account Segment 14 Name | |
| 123 | Account Segment-15 | string(2000) | No | Account Segment 15 Code | Account Segment 15 Code | Account Segment 15 Code | |
| 124 | Account Segment-15 Name | string(2000) | No | Account Segment 15 Name | Account Segment 15 Name | Account Segment 15 Name | |
| 125 | Account Segment-16 | string(2000) | No | Account Segment 16 Code | Account Segment 16 Code | Account Segment 16 Code | |
| 126 | Account Segment-16 Name | string(2000) | No | Account Segment 16 Name | Account Segment 16 Name | Account Segment 16 Name | |
| 127 | Account Segment-17 | string(2000) | No | Account Segment 17 Code | Account Segment 17 Code | Account Segment 17 Code | |
| 128 | Account Segment-17 Name | string(2000) | No | Account Segment 17 Name | Account Segment 17 Name | Account Segment 17 Name | |
| 129 | Account Segment-18 | string(2000) | No | Account Segment 18 Code | Account Segment 18 Code | Account Segment 18 Code | |
| 130 | Account Segment-18 Name | string(2000) | No | Account Segment 18 Name | Account Segment 18 Name | Account Segment 18 Name | |
| 131 | Account Segment-19 | string(2000) | No | Account Segment 19 Code | Account Segment 19 Code | Account Segment 19 Code | |
| 132 | Account Segment-19 Name | string(2000) | No | Account Segment 19 Name | Account Segment 19 Name | Account Segment 19 Name | |
| 133 | Account Segment-20 | string(2000) | No | Account Segment 20 Code | Account Segment 20 Code | Account Segment 20 Code | |
| 134 | Account Segment-20 Name | string(2000) | No | Account Segment 20 Name | Account Segment 20 Name | Account Segment 20 Name | |
