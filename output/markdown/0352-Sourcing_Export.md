---
title: "Sourcing Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/sourcing-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/sourcing-export"
status_code: 200
fetched_at: "2026-04-09T12:00:27+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Sourcing Export"
---

# Sourcing Export

Sourcing exports include various details of Sourcing
event records.

## Quote award columns

Columns that detail supplier responses or response lines
that have been awarded.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Award | Quote Award | Quote Award | FALSE | | |
| 2 | Quote Award ID | Quote Award ID | FALSE | FALSE | integer | any |
| 3 | Created At Date | Created At Date | FALSE | FALSE | datetime | any |
| 4 | Updated At Date | Updated At Date | TRUE | FALSE | datetime | any |
| 5 | Event Awardable ID | Event Awardable ID | FALSE | FALSE | integer | any |
| 6 | Event Awardable Type | Event Awardable Type | FALSE | FALSE | string(255) | any |

## Quote request columns

Columns with header level details for a Sourcing event.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Request | Quote Request | FALSE | FALSE | | |
| 2 | Quote Request Header ID | Quote Request Header ID | FALSE | FALSE | integer | |
| 3 | Original ID | Original ID | FALSE | FALSE | integer | |
| 4 | Revision | Revision | FALSE | FALSE | string(255) | |
| 5 | Event Header Name | Event Header Name | FALSE | FALSE | text | |
| 6 | Created At Date | Created At Date | FALSE | FALSE | datetime | |
| 7 | Created by ID | Created by ID | FALSE | FALSE | integer | |
| 8 | Updated At Date | Updated At Date | FALSE | FALSE | datetime | |
| 9 | Updated by ID | Updated by ID | FALSE | FALSE | integer | |
| 10 | Start Date | Start Date | FALSE | FALSE | datetime | |
| 11 | End Date | End Date | FALSE | FALSE | datetime | |
| 12 | State | State | FALSE | FALSE | string(255) | |
| 13 | Event Type | Event Type | TRUE | FALSE | string(255) | |
| 14 | Type | Type | FALSE | FALSE | string(255) | |
| 15 | Start On Submit | Start On Submit | FALSE | FALSE | boolean | |
| 16 | Bid On Start | Bid On Start | FALSE | FALSE | boolean | |
| 17 | Time To Respond | Time To Respond | FALSE | FALSE | integer | |
| 18 | Beaten Price Options - Total Event | Beaten Price Options - Total Event | FALSE | FALSE | | |
| 19 | Beaten Price Options - Any Lot | Beaten Price Options - Any Lot | FALSE | FALSE | | |
| 20 | Beaten Price Options - Individual Line | Beaten Price Options - Individual Line | FALSE | FALSE | | |
| 21 | Incremental Bidding Options - Any Lot Allow - Tie For First Place | Incremental Bidding Options - Any Lot Allow - Tie For First Place | FALSE | FALSE | | |
| 22 | Incremental Bidding Options - Any Lot - Require To Improve Size | Incremental Bidding Options - Any Lot - Require To Improve Size | FALSE | FALSE | | |
| 23 | Incremental Bidding Options - Any Lot - Size | Incremental Bidding Options - Any Lot - Size | FALSE | FALSE | | |
| 24 | Incremental Bidding Options - Any Lot - Size Total | Incremental Bidding Options - Any Lot - Size Total | FALSE | FALSE | | |
| 25 | Incremental Bidding Options - Individual Line Allow - Tie For First Place | Incremental Bidding Options - Individual Line Allow - Tie For First Place | FALSE | FALSE | | |
| 26 | Incremental Bidding Options - Individual Line - Require To Improve - Size | Incremental Bidding Options - Individual Line - Require To Improve - Size | FALSE | FALSE | | |
| 27 | Incremental Bidding Options - Individual Line - Size | Incremental Bidding Options - Individual Line - Size | FALSE | FALSE | | |
| 28 | Incremental Bidding Options - Individual Line - Size Total | Incremental Bidding Options - Individual Line - Size Total | FALSE | FALSE | | |
| 29 | Incremental Bidding Options - Total Event Allow - Tie For First Place | Incremental Bidding Options - Total Event Allow - Tie For First Place | FALSE | FALSE | | |
| 30 | Incremental Bidding Options - Total Event - Require To Improve - Size | Incremental Bidding Options - Total Event - Require To Improve - Size | FALSE | FALSE | | |
| 31 | Incremental Bidding Options - Total Event - Size | Incremental Bidding Options - Total Event - Size | FALSE | FALSE | | |
| 32 | Incremental Bidding Options - Total Event - Size Total | Incremental Bidding Options - Total Event - Size Total | FALSE | FALSE | | |
| 33 | Suppliers See | Suppliers See | FALSE | FALSE | string(255) | |
| 34 | Automatic Bid Extensions | Automatic Bid Extensions | FALSE | FALSE | boolean | |
| 35 | Competitive Bidding | Competitive Bidding | FALSE | FALSE | boolean | |
| 36 | Currency Code | Currency Code | FALSE | FALSE | | |
| 37 | Banner Title | Banner Title | FALSE | FALSE | string(255) | |
| 38 | Banner Text | Banner Text | FALSE | FALSE | text | |
| 39 | Commodity Name | Commodity Name | FALSE | FALSE | | |
| 40 | Custom Field 1 | Custom Field 1 | FALSE | FALSE | string(255) | |
| 41 | Custom Field 1 | Custom Field 1 | FALSE | FALSE | string(255) | |
| 42 | Custom Field 3 | Custom Field 3 | FALSE | FALSE | string(255) | |
| 43 | Custom Field 4 | Custom Field 4 | FALSE | FALSE | string(255) | |
| 44 | Custom Field 5 | Custom Field 5 | FALSE | FALSE | string(255) | |
| 45 | Custom Field 6 | Custom Field 6 | FALSE | FALSE | string(255) | |
| 46 | Custom Field 7 | Custom Field 7 | FALSE | FALSE | string(255) | |
| 47 | Custom Field 8 | Custom Field 8 | FALSE | FALSE | string(255) | |
| 48 | Custom Field 9 | Custom Field 9 | FALSE | FALSE | string(255) | |
| 49 | Custom Field 10 | Custom Field 10 | FALSE | FALSE | string(255) | |
| 50 | Custom Field 11 | Custom Field 11 | FALSE | FALSE | string(255) | |
| 51 | Custom Field 12 | Custom Field 12 | FALSE | FALSE | string(255) | |
| 52 | Custom Field 13 | Custom Field 13 | FALSE | FALSE | string(255) | |
| 53 | Custom Field 14 | Custom Field 14 | FALSE | FALSE | string(255) | |
| 54 | Custom Field 15 | Custom Field 15 | FALSE | FALSE | string(255) | |
| 55 | Custom Field 16 | Custom Field 16 | FALSE | FALSE | string(255) | |
| 56 | Custom Field 17 | Custom Field 17 | FALSE | FALSE | string(255) | |
| 57 | Custom Field 18 | Custom Field 18 | FALSE | FALSE | string(255) | |
| 58 | Custom Field 19 | Custom Field 19 | FALSE | FALSE | string(255) | |
| 59 | Custom Field 20 | Custom Field 20 | FALSE | FALSE | string(255) | |
| 60 | Savings | Savings | FALSE | FALSE | decimal(32,4) | |
| 61 | Weight Attachments Score | Weight Attachments Score (Points) | FALSE | FALSE | integer | |
| 62 | Weight Questionnaires Score | Weight Questionnaires Score (Points) | FALSE | FALSE | integer | |
| 63 | Weight Items Score | Weight Items Score (Points) | FALSE | FALSE | integer | |
| 64 | Closed At State | Closed At State | FALSE | FALSE | string(255) | |
| 65 | Allow Multiple Response | Allow Multiple Response | FALSE | FALSE | boolean | |
| 66 | Sealed Bids | Sealed Bids | FALSE | FALSE | boolean | |
| 67 | Item Required Fields | Item Required Fields | FALSE | FALSE | text | |
| 68 | Pause Start Time | Pause Start Time | FALSE | FALSE | datetime | |
| 69 | Paused At State | Paused At State | FALSE | FALSE | string(255) | |
| 70 | Creatable From Object ID | Creatable From Object ID | FALSE | FALSE | integer | |
| 71 | Creatable From Object Type | Creatable From Object Type | FALSE | FALSE | string(255) | |
| 72 | Followed From Event # | Followed From Event # | FALSE | FALSE | integer | |
| 73 | Reporting Savings | Reporting Savings | FALSE | FALSE | decimal(32,4) | |
| 74 | Next Revision Event ID | Next Revision Event ID | FALSE | FALSE | integer | |
| 75 | Allow Award Individual Line Items | Allow Award Individual Line Items | FALSE | FALSE | boolean | |
| 76 | Event Timezone | Event Timezone | FALSE | FALSE | string(255) | |
| 77 | End At Price | End At Price | FALSE | FALSE | decimal(30,6) | |
| 78 | Max Number Of Steps | Max Number Of Steps | FALSE | FALSE | integer | |
| 79 | Price Increase Interval | Price Increase Interval | FALSE | FALSE | integer | |
| 80 | Planned Savings | Planned Savings | FALSE | FALSE | decimal(30,6) | |
| 81 | Reporting Planned Savings | Reporting Planned Savings | FALSE | FALSE | decimal(30,6) | |
| 82 | Allow Suppliers To Choose Currency | Allow Suppliers To Choose Currency | FALSE | FALSE | boolean | |
| 83 | Sealing Type | Sealing Type | FALSE | FALSE | integer | one_step_unsealing, two_steps_unsealing |
| 84 | Sealing Stage | Sealing Stage | FALSE | FALSE | integer | all_envelopes_sealed, envelope1_unsealed, envelope2_unsealed |
| 85 | Base Price Calculation Method | Base Price Calculation Method | FALSE | FALSE | integer | |
| 86 | Cost Avoidance | Cost Avoidance | FALSE | FALSE | decimal(30,4) | |
| 87 | Public | Public | FALSE | FALSE | boolean | |
| 88 | Allow Supplier To Send Attachments | Allow Supplier To Send Attachments | FALSE | FALSE | boolean | |
| 89 | Allow Evaluators To View Event | Allow Evaluators To View Event | FALSE | FALSE | boolean | |
| 90 | Related Requisitions | Related Requisitions | FALSE | FALSE | | |
| 91 | Related Contracts | Related Contracts | FALSE | FALSE | | |
| 92 | Related Orders | Related Orders | FALSE | FALSE | | |
| 93 | Related Invoices | Related Invoices | | | | |

## Quote Request Line columns

Columns with line-level details for a Sourcing event.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Request Line | Quote Request Line | FALSE | FALSE | | |
| 2 | Quote Request Line Id | Quote Request Line Id | FALSE | FALSE | integer | |
| 3 | Created At Date | Created At Date | FALSE | FALSE | datetime | |
| 4 | Created by ID | Created by ID | FALSE | FALSE | integer | |
| 5 | Updated At Date | Updated At Date | FALSE | FALSE | datetime | |
| 6 | Updated by ID | Updated by ID | FALSE | FALSE | integer | |
| 7 | Event # | Event # | FALSE | FALSE | integer | |
| 8 | Type | Type | TRUE | FALSE | string(255) | |
| 9 | Quantity | Quantity | FALSE | FALSE | decimal(30,6) | |
| 10 | UOM | UOM | FALSE | FALSE | integer | |
| 11 | Position | Position | FALSE | FALSE | integer | |
| 12 | Price Amount | Price Amount | FALSE | FALSE | decimal(30,6) | |
| 13 | Price Currency Code | Price Currency Code | FALSE | FALSE | integer | |
| 14 | Item ID | Item ID | FALSE | FALSE | integer | |
| 15 | Description | Description | FALSE | FALSE | string(255) | |
| 16 | Ship To Address ID | Ship To Address ID | FALSE | FALSE | integer | |
| 17 | Ship To Address Street Line 1 | Ship To Address Street Line 1 | FALSE | FALSE | | |
| 18 | Ship To Address Street Line 2 | Ship To Address Street Line 2 | FALSE | FALSE | | |
| 19 | Ship To Address City | Ship To Address City | FALSE | FALSE | | |
| 20 | Ship To Address State/Province | Ship To Address State/Province | FALSE | FALSE | | |
| 21 | Ship To Address Postal Code | Ship To Address Postal Code | FALSE | FALSE | | |
| 22 | Ship To Address Country Code | Ship To Address Country Code | FALSE | FALSE | | |
| 23 | Ship To Address Location Code | Ship To Address Location Code | FALSE | FALSE | | |
| 24 | Reporting Price Amount | Reporting Price Amount | FALSE | FALSE | decimal(30,6) | |
| 25 | Lot ID | Lot ID | FALSE | FALSE | integer | |
| 26 | Commodity Name | Commodity Name | FALSE | FALSE | integer | |
| 27 | Weight | Weight | FALSE | FALSE | integer | |
| 28 | Creatable From Object ID | Creatable From Object ID | FALSE | FALSE | integer | |
| 29 | Creatable From Object Type | Creatable From Object Type | FALSE | FALSE | string(255) | |
| 30 | Cost Formula ID | Cost Formula ID | FALSE | FALSE | integer | |
| 31 | Initial Price | Initial Price | FALSE | FALSE | decimal(30,6) | |
| 32 | Incremental Increase Unit | Incremental Increase Unit | FALSE | FALSE | string(255) | |
| 33 | Incremental Increase | Incremental Increase | FALSE | FALSE | decimal(30,6) | |
| 34 | Need By Date | Need By Date | FALSE | FALSE | datetime | |
| 35 | Price Amount In Event Currency | Price Amount In Event Currency | FALSE | FALSE | decimal(30,6) | |
| 36 | Form ID | Form ID | FALSE | FALSE | integer | |
| 37 | Manually Entered Base Price | Manually Entered Base Price | FALSE | FALSE | boolean | |
| 38 | Manufacturer Name | Manufacturer Name | FALSE | FALSE | string(255) | |
| 39 | Manufacturer Part Number | Manufacturer Part Number | FALSE | FALSE | string(255) | |

## Quote request user columns

Columns that detail the team from the buyer side.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Request User | Quote Request User | FALSE | FALSE | | |
| 2 | Quote Request User Id | Quote Request User Id | FALSE | FALSE | integer | |
| 3 | Quote Request ID | Quote Request ID | FALSE | FALSE | integer | |
| 4 | User ID | User ID | FALSE | TRUE | integer | |
| 5 | Attitude | Attitude | FALSE | TRUE | string(255) | creator, owner, watcher, evaluator |
| 6 | Evaluation State | Evaluation State | FALSE | FALSE | string(255) | |
| 7 | Evaluation File | Evaluation File | FALSE | FALSE | string(255) | |
| 8 | Evaluation Sections | Evaluation Sections | FALSE | FALSE | integer | |
| 9 | Created At Date | Created At Date | FALSE | FALSE | datetime | |
| 10 | Updated At Date | Updated At Date | FALSE | FALSE | datetime | |

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

## Quote response line columns

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

## Quote response status columns

Columns that detail supplier response status.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Response Status | Quote Response Status | FALSE | FALSE | | |
| 2 | Quote Response Status Id | Quote Response Status Id | FALSE | FALSE | integer | |
| 3 | Name | Name | TRUE | TRUE | string(255) | |
| 4 | Active | Active | FALSE | FALSE | boolean | |
| 5 | Created At Date | Created At Date | FALSE | FALSE | datetime | |
| 6 | Updated At Date | Updated At Date | FALSE | FALSE | datetime | |

## Quote supplier columns

Columns that detail suppliers participating in the
event.

| **Position** | **Column Name** | **Description** | **Req/Unique** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Quote Supplier | Quote Supplier | FALSE | FALSE | | |
| 2 | Quote Supplier ID | Quote Supplier ID | FALSE | FALSE | integer | |
| 3 | Created At Date | Created At Date | FALSE | FALSE | datetime | |
| 4 | Created by ID | Created by ID | FALSE | FALSE | integer | |
| 5 | Updated At Date | Updated At Date | FALSE | FALSE | datetime | |
| 6 | Updated by ID | Updated by ID | FALSE | FALSE | integer | |
| 7 | Type | Type | FALSE | FALSE | string(255) | |
| 8 | Supplier ID | Supplier ID | TRUE | FALSE | integer | |
| 9 | Supplier Name | Supplier Name | TRUE | TRUE | string(255) | |
| 10 | Supplier Email | Supplier Email | TRUE | FALSE | string(255) | |
| 11 | Supplier Contact Name | Supplier Contact Name | FALSE | FALSE | string(255) | |
| 12 | Supplier Display Name | Supplier Display Name | FALSE | FALSE | string(255) | |
| 13 | Event Request ID | Event Request ID | FALSE | FALSE | integer | |
| 14 | Supplier Default locale | Supplier Default locale | FALSE | FALSE | string(255) | |
| 15 | Emailed | Emailed | FALSE | FALSE | boolean | |
| 16 | Changes Review Confirmed | Changes Review Confirmed | FALSE | FALSE | boolean | |
| 17 | Revision Changes Reviewed | Revision Changes Reviewed | FALSE | FALSE | boolean | |
| 18 | Terms Accepted | Terms Accepted | FALSE | FALSE | boolean | |
