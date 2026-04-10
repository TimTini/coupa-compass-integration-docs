---
title: "Sourcing Quote Response Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/sourcing-quote-response-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/sourcing-quote-response-export"
status_code: 200
fetched_at: "2026-04-09T12:00:28+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Sourcing Quote Response Export"
---

# Sourcing Quote Response Export

Sourcing exports include various details of Sourcing
event records.

## Quote Response columns

Columns detailing supplier responses at the header level.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Response | Quote Response | FALSE | FALSE | | |
| 2 | Quote Response Header ID | Quote Response Header ID | FALSE | FALSE | integer | |
| 3 | Created At Date | Created At Date | FALSE | FALSE | datetime | |
| 4 | Created by ID | Created by ID | FALSE | FALSE | integer | |
| 5 | Updated At Date | Updated At Date | FALSE | FALSE | datetime | |
| 6 | Updated by ID | Updated by ID | FALSE | FALSE | integer | |
| 7 | Event # | Event # | FALSE | FALSE | integer | |
| 8 | Comments | Comments | FALSE | FALSE | text | |
| 9 | Submitted At | Submitted At | TRUE | FALSE | datetime | |
| 10 | Quote Supplier ID | Quote Supplier ID | FALSE | FALSE | integer | |
| 11 | State | State | FALSE | FALSE | string(255) | |
| 12 | Position | Position | FALSE | FALSE | integer | |
| 13 | Type | Type | FALSE | FALSE | string(255) | |
| 14 | Name | Name | TRUE | TRUE | string(255) | |
| 15 | Track ID | Track ID | FALSE | FALSE | integer | |
| 16 | Quote Response Status | Quote Response Status | FALSE | FALSE | integer | |
| 17 | Updated By Supplier | Updated By Supplier | FALSE | FALSE | boolean | |
| 18 | Is Bargain | Is Bargain | FALSE | FALSE | boolean | |
| 19 | Best Total | Best Total | FALSE | FALSE | decimal(30,6) | |
| 20 | Nearby Best Total | Nearby Best Total | FALSE | FALSE | decimal(30,6) | |
| 21 | Is Best | Whether this response has the same price as the best response. This field is only valid for the best response from each supplier | FALSE | FALSE | boolean | |
| 22 | Rank | The rank of the response. This field is only valid for the best response from each supplier | FALSE | FALSE | integer | |
| 23 | Bid Total | Bid Total | FALSE | FALSE | decimal(30,6) | |
| 24 | All Responded | All Responded | FALSE | FALSE | boolean | |
| 25 | Awarded Supplier ID | The ID of the awarded master supplier record | FALSE | FALSE | integer | |
| 26 | Awarded | Awarded | FALSE | FALSE | | |
| 27 | Promoted | Promoted | FALSE | FALSE | boolean | |

## Quote Response Line columns

Columns that detail supplier responses at the line
level.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Response Line | Quote Response Line | FALSE | FALSE | | |
| 2 | Quote Response Line Id | Quote Response Line Id | FALSE | FALSE | integer | |
| 3 | Created At Date | Created At Date | FALSE | FALSE | datetime | |
| 4 | Created by ID | Created by ID | FALSE | FALSE | integer | |
| 5 | Updated At Date | Updated At Date | FALSE | FALSE | datetime | |
| 6 | Updated by ID | Updated by ID | FALSE | FALSE | integer | |
| 7 | Event Response ID | Event Response ID | FALSE | FALSE | integer | |
| 8 | Event Request Line ID | Event Request Line ID | FALSE | FALSE | integer | |
| 9 | Type | Type | FALSE | FALSE | string(255) | |
| 10 | Quantity | Quantity | FALSE | FALSE | decimal(30,6) | |
| 11 | Position | Position | FALSE | FALSE | integer | |
| 12 | Price Amount | Price Amount | TRUE | FALSE | decimal(30,6) | |
| 13 | Lot ID | Lot ID | FALSE | FALSE | integer | |
| 14 | Weight | Weight | FALSE | FALSE | integer | |
| 15 | Supplier Item Name | Supplier Item Name | FALSE | FALSE | string(255) | |
| 16 | Item Part Number | Item Part Number | FALSE | FALSE | string(255) | |
| 17 | Item Description | Item Description | FALSE | FALSE | text | |
| 18 | Price Currency Code | Price Currency Code | FALSE | FALSE | integer | |
| 19 | UOM | UOM | FALSE | FALSE | integer | |
| 20 | Reporting Price Amount | Reporting Price Amount | FALSE | FALSE | decimal(30,6) | |
| 21 | Lead Time | Lead Time | FALSE | FALSE | integer | |
| 22 | Price Amount In Event Currency | Price Amount In Event Currency | TRUE | FALSE | decimal(30,6) | |
| 23 | Form Response ID | Form Response ID | FALSE | FALSE | integer | |

## Quote Response Status columns

Columns that detail supplier response status.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Response Status | Quote Response Status | FALSE | FALSE | | |
| 2 | Quote Response Status Id | Quote Response Status Id | FALSE | FALSE | integer | |
| 3 | Name | Name | TRUE | TRUE | string(255) | |
| 4 | Active | Active | FALSE | FALSE | boolean | |
| 5 | Created At Date | Created At Date | FALSE | FALSE | datetime | |
| 6 | Updated At Date | Updated At Date | FALSE | FALSE | datetime | |
