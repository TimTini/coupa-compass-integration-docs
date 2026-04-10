---
title: "Payment Term Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/payment-term-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/payment-term-import"
status_code: 200
fetched_at: "2026-04-09T12:00:43+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Payment Term Import"
---

# Payment Term Import

## Payment Terms

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Code | Yes | Yes | string(255) | Payment Term Code | |
| Description | No | No | string(255) | Description of Payment Term | |
| Days For Net Payment | Yes | No | integer | Number of days in order to pay the invoice | |
| Days For Discount Payment | Yes | No | integer | Number of days in order to receive discount rate | |
| Discount Rate (%) | No | No | float | Discount percentage if paid within number of days for discount | |
| Type | Yes | No | string(50) | Type of Payment Term | DaysAfterNetPaymentTerm, SpecificDayPaymentTerm, BaseEomToDaysPaymentTerm, DaysToBaseEomPaymentTerm |
| Discount Cutoff Day | No | No | integer | Invoices before this day are eligible for discount else they will fall into the next month | 1..31 |
| Discount Due Month | Yes | No | integer | It is used to calculate the invoice's discount due date along with the discount due day | 0..6 |
| Discount Due Day | Yes | No | integer | It is used to calculate the invoice's discount due date. | 1..31 |
| Net Cutoff Day | No | No | integer | To determine payment due date if the invoice should be counted against this month or next | 1..31 |
| Net Due Month | Yes | No | integer | To determine the invoice's payment due date | 0..6 |
| Net Due Day | Yes | No | integer | To determine the invoice's payment due date | 1..31 |
| Content Groups | No | No | | Enter in content groups (for security) | |
| Active | Yes | No | boolean | Is this Payment Term available for selection? Yes/No | true |
