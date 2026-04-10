---
title: "Payables/Invoices API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payablesinvoices-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payablesinvoices-api"
status_code: 200
fetched_at: "2026-04-09T11:59:52+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Payables API (/payables/)"
  - "Payables/Invoices API"
---

# Payables/Invoices API

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/payables/invoices/available_allocations` | available_allocations | /api/payables/invoices/available_allocations |
| PATCH | `/api/payables/invoices/:id/export` | export | Mark Invoice Payable as Exported |
| PUT | `/api/payables/invoices/:id/export` | export | Mark Invoice Payable as Exported |
| GET | `/api/payables/invoices` | index | Query Invoice Payables |
| PATCH | `/api/payables/invoices/:id/pay_externally` | pay_externally | Mark Invoice Payable as Paid and stop tracking in Coupa |
| PUT | `/api/payables/invoices/:id/pay_externally` | pay_externally | Mark Invoice Payable as Paid and stop tracking in Coupa |
| GET | `/api/payables/invoices/:id` | show | Show Invoice Payable |
| PATCH | `/api/payables/invoices/:id/track_externally` | track_externally | Stop Tracking Invoice Payable in Coupa |
| PUT | `/api/payables/invoices/:id/track_externally` | track_externally | Stop Tracking Invoice Payable in Coupa |
| PATCH | `/api/payables/invoices/:id/track_in_coupa` | track_in_coupa | Start Tracking Invoice Payable in Coupa |
| PUT | `/api/payables/invoices/:id/track_in_coupa` | track_in_coupa | Start Tracking Invoice Payable in Coupa |

## Elements

Keys: `id`

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| accounting-amount | Total of reconciliation lines in accounting currency | | | | | yes | decimal(46,20) |
| accounting-currency | Accounting currency | | | | | yes | [Currency](https://r32.coupadev.com/integration_documents/obj_show/Currency) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| currency | Currency of payable | | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| document-id | Unique ID of associated document | | | | | yes | string |
| document-type | The type of the document being paid | | | | | yes | string |
| exported-to-tradefin-at | Date exported to tradefin | | | | | yes | datetime |
| id | Unique ID of this payable | | | | | yes | integer |
| last-exported-at | Last export date | | | | | yes | datetime |
| maturity-date | Maturity Date | | | | | yes | datetime |
| paid-amount | Total amount paid | | | | | yes | decimal(46,20) |
| paid-date | Paid date | | | | | yes | datetime |
| payable-amount | The amount of the document which is ready to be paid | | | | | yes | |
| received-allocations | Received allocations | | | | | yes | [Payables::Allocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payable-allocations-api) |
| reconciliation-lines | Reconciliation lines | | | | | yes | Invoice::ReconciliationLine |
| remaining-amount | Remaining amount to pay | | | | | yes | decimal(46,20) |
| remittance-amount | Total amount to pay | | | | | yes | decimal(46,20) |
| reporting-total | Total of reconciliation lines in reporting dashboard currency | | | | | yes | decimal(46,20) |
| sent-allocations | Sent allocations | | | | | yes | [Payables::Allocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payable-allocations-api) |
| status | Current status of the payable | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| wc-eligibility | Working capital eligibility status | | | | | yes | string(255) |
