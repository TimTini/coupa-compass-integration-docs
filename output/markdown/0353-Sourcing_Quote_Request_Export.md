---
title: "Sourcing Quote Request Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/sourcing-quote-request-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/sourcing-quote-request-export"
status_code: 200
fetched_at: "2026-04-09T12:00:28+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Sourcing Quote Request Export"
---

# Sourcing Quote Request Export

Sourcing exports include various details of Sourcing
event records.

## Sourcing Event

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Quote Request | Quote Request | | No/No | |
| Quote Request Header ID | Quote Request Header ID | integer | No/No | |
| Original ID | Original ID | integer | No/No | |
| Revision | Revision | string(255) | No/No | |
| Quote Request Header Name | Quote Request Header Name | text | No/No | |
| Created At Date | Created At Date | datetime | No/No | |
| Created by ID | Created by ID | integer | No/No | |
| Updated At Date | Updated At Date | datetime | No/No | |
| Updated by ID | Updated by ID | integer | No/No | |
| Start Date | Start Date | datetime | No/No | |
| End Date | End Date | datetime | No/No | |
| State | State | string(255) | No/No | |
| Event Type | Event Type | string(255) | Yes/No | |
| Type | Type | string(255) | No/No | |
| Start On Submit | Start On Submit | boolean | No/No | |
| Bid On Start | Bid On Start | boolean | No/No | |
| Time To Respond | Time To Respond | integer | No/No | |
| Beaten Price Options - Total Event | Beaten Price Options - Total Event | | No/No | |
| Beaten Price Options - Any Lot | Beaten Price Options - Any Lot | | No/No | |
| Beaten Price Options - Individual Line | Beaten Price Options - Individual Line | | No/No | |
| Incremental Bidding Options - Any Lot Allow - Tie For First Place | Incremental Bidding Options - Any Lot Allow - Tie For First Place | | No/No | |
| Incremental Bidding Options - Any Lot - Require To Improve Size | Incremental Bidding Options - Any Lot - Require To Improve Size | | No/No | |
| Incremental Bidding Options - Any Lot - Size | Incremental Bidding Options - Any Lot - Size | | No/No | |
| Incremental Bidding Options - Any Lot - Size Total | Incremental Bidding Options - Any Lot - Size Total | | No/No | |
| Incremental Bidding Options - Individual Line Allow - Tie For First Place | Incremental Bidding Options - Individual Line Allow - Tie For First Place | | No/No | |
| Incremental Bidding Options - Individual Line - Require To Improve - Size | Incremental Bidding Options - Individual Line - Require To Improve - Size | | No/No | |
| Incremental Bidding Options - Individual Line - Size | Incremental Bidding Options - Individual Line - Size | | No/No | |
| Incremental Bidding Options - Individual Line - Size Total | Incremental Bidding Options - Individual Line - Size Total | | No/No | |
| Incremental Bidding Options - Total Event Allow - Tie For First Place | Incremental Bidding Options - Total Event Allow - Tie For First Place | | No/No | |
| Incremental Bidding Options - Total Event - Require To Improve - Size | Incremental Bidding Options - Total Event - Require To Improve - Size | | No/No | |
| Incremental Bidding Options - Total Event - Size | Incremental Bidding Options - Total Event - Size | | No/No | |
| Incremental Bidding Options - Total Event - Size Total | Incremental Bidding Options - Total Event - Size Total | | No/No | |
| Suppliers See | Suppliers See | string(255) | No/No | |
| Automatic Bid Extensions | Automatic Bid Extensions | boolean | No/No | |
| Competitive Bidding | Competitive Bidding | boolean | No/No | |
| Currency Code | Currency Code | | No/No | |
| Banner Title | Banner Title | string(255) | No/No | |
| Banner Text | Banner Text | text | No/No | |
| Commodity Name | Commodity Name | | No/No | |
| Custom Field 1 | Custom Field 1 | string(255) | No/No | |
| Custom Field 1 | Custom Field 1 | string(255) | No/No | |
| Custom Field 3 | Custom Field 3 | string(255) | No/No | |
| Custom Field 4 | Custom Field 4 | string(255) | No/No | |
| Custom Field 5 | Custom Field 5 | string(255) | No/No | |
| Custom Field 6 | Custom Field 6 | string(255) | No/No | |
| Custom Field 7 | Custom Field 7 | string(255) | No/No | |
| Custom Field 8 | Custom Field 8 | string(255) | No/No | |
| Custom Field 9 | Custom Field 9 | string(255) | No/No | |
| Custom Field 10 | Custom Field 10 | string(255) | No/No | |
| Custom Field 11 | Custom Field 11 | string(255) | No/No | |
| Custom Field 12 | Custom Field 12 | string(255) | No/No | |
| Custom Field 13 | Custom Field 13 | string(255) | No/No | |
| Custom Field 14 | Custom Field 14 | string(255) | No/No | |
| Custom Field 15 | Custom Field 15 | string(255) | No/No | |
| Custom Field 16 | Custom Field 16 | string(255) | No/No | |
| Custom Field 17 | Custom Field 17 | string(255) | No/No | |
| Custom Field 18 | Custom Field 18 | string(255) | No/No | |
| Custom Field 19 | Custom Field 19 | string(255) | No/No | |
| Custom Field 20 | Custom Field 20 | string(255) | No/No | |
| Savings | Savings | decimal(32,4) | No/No | |
| Weight Attachments Score | Weight Attachments Score (Points) | integer | No/No | |
| Weight Questionnaires Score | Weight Questionnaires Score (Points) | integer | No/No | |
| Weight Items Score | Weight Items Score (Points) | integer | No/No | |
| Closed At State | Closed At State | string(255) | No/No | |
| Allow Multiple Response | Allow Multiple Response | boolean | No/No | |
| Sealed Bids | Sealed Bids | boolean | No/No | |
| Item Required Fields | Item Required Fields | text | No/No | |
| Pause Start Time | Pause Start Time | datetime | No/No | |
| Paused At State | Paused At State | string(255) | No/No | |
| Creatable From Object ID | Creatable From Object ID | integer | No/No | |
| Creatable From Object Type | Creatable From Object Type | string(255) | No/No | |
| Followed From Event # | Followed From Event # | integer | No/No | |
| Reporting Savings | Reporting Savings | decimal(32,4) | No/No | |
| Next Revision Event ID | Next Revision Event ID | integer | No/No | |
| Allow Award Individual Line Items | Allow Award Individual Line Items | true | No/No | |
| Event Timezone | Event Timezone | string(255) | No/No | |
| End At Price | End At Price | decimal(30,6) | No/No | |
| Max Number Of Steps | Max Number Of Steps | integer | No/No | |
| Price Increase Interval | Price Increase Interval | integer | No/No | |
| Planned Savings | Planned Savings | decimal(30,6) | No/No | |
| Reporting Planned Savings | Reporting Planned Savings | decimal(30,6) | No/No | |
| Allow Suppliers To Choose Currency | Allow Suppliers To Choose Currency | boolean | No/No | |
| Sealing Type | Sealing Type | integer | No/No | one_step_unsealing, two_steps_unsealing |
| Sealing Stage | Sealing Stage | integer | No/No | all_envelopes_sealed, envelope1_unsealed, envelope2_unsealed |
| Base Price Calculation Method | Base Price Calculation Method | integer | No/No | |
| Cost Avoidance | Cost Avoidance | decimal(30,4) | No/No | |
| Public | Public | boolean | No/No | |
| Allow Supplier To Send Attachments | Allow Supplier To Send Attachments | boolean | No/No | |
| Allow Evaluators To View Event | Allow Evaluators To View Event | boolean | No/No | |
| Related Requisitions | Related Requisitions | | No/No | |
| Related Contracts | Related Contracts | | No/No | |
| Related Orders | Related Orders | | No/No | |
| Related Invoices | Related Invoices | | No/No | |
| Hidden | Hidden | boolean | No/No | |
| Template ID | Template ID | integer | No/No | |

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
| 17 | Ship To Address Street Line 1 | Ship To Address Street Line 1 | FALSE | FALSE | string(255) | |
| 18 | Ship To Address Street Line 2 | Ship To Address Street Line 2 | FALSE | FALSE | string(255) | |
| 19 | Ship To Address City | Ship To Address City | FALSE | FALSE | string(255) | |
| 20 | Ship To Address State/Province | Ship To Address State/Province | FALSE | FALSE | string(255) | |
| 21 | Ship To Address Postal Code | Ship To Address Postal Code | FALSE | FALSE | string(255) | |
| 22 | Ship To Address Country Code | Ship To Address Country Code | FALSE | FALSE | string(4) | |
| 23 | Ship To Address Location Code | Ship To Address Location Code | FALSE | FALSE | | |
| 24 | Reporting Price Amount | Reporting Price Amount | FALSE | FALSE | decimal(30,6) | |
| 25 | Lot ID | Lot ID | FALSE | FALSE | integer | |
| 26 | Commodity Name | Commodity Name | FALSE | FALSE | string(255) | |
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

## Quote Request User columns

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
