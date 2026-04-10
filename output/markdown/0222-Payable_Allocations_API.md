---
title: "Payable Allocations API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payable-allocations-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/payables-api-(payables)/payable-allocations-api"
status_code: 200
fetched_at: "2026-04-09T11:59:51+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Payables API (/payables/)"
  - "Payable Allocations API"
---

# Payable Allocations API

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/payables/allocations` | create | /api/payables/allocations |
| PUT | `/api/payables/allocations/:id/export` | export | /api/payables/allocations/:id/export |
| PATCH | `/api/payables/allocations/:id/export` | export | /api/payables/allocations/:id/export |
| GET | `/api/payables/allocations` | index | Query Payable Allocations |
| PUT | `/api/payables/allocations/:id/reverse` | reverse | Reverse this allocation and create negative reconciliation lines to free up the amount that was allocated |
| PATCH | `/api/payables/allocations/:id/reverse` | reverse | Reverse this allocation and create negative reconciliation lines to free up the amount that was allocated |
| GET | `/api/payables/allocations/:id` | show | Show Payable Allocation |
| PATCH | `/api/payables/allocations/:id` | update | /api/payables/allocations/:id |
| PUT | `/api/payables/allocations/:id` | update | /api/payables/allocations/:id |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Setting `bypass_strict_validations` = `false` ensures that
balances from a PayOrder are never consumed over the existing balance. Without this switch
enabled, it is possible to overallocate a payment posted on an order.

## Elements

Keys: `id`

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | User |
| exported | Indicates if transaction has been exported | | | | | yes | boolean |
| id | Coupa unique identifier | | | | | yes | integer |
| last-exported-at | Date of last update to the allocation | | | | | yes | datetime |
| payable-from-amount | Amount allocated in currency of the document sending the allocation | yes | | | yes | yes | decimal(46,20) |
| payable-from-currency | Currency of document sending the allocation | yes | | | yes | yes | Currency |
| payable-from-id | Coupa ID of the payable document sending the allocation | | | | yes | yes | integer |
| payable-from-type | Type of payable document sending the allocation | | | | yes | yes | string(255) |
| payable-to-amount | Amount allocated in currency of the document receiving the allocation | yes | | | yes | yes | decimal(46,20) |
| payable-to-currency | Currency of document receiving the allocation | yes | | | yes | yes | Currency |
| payable-to-id | Coupa ID of the payable document receiving the allocation | | | | yes | yes | integer |
| payable-to-type | Type of payable document receiving the allocation | | | | yes | yes | string(255) |
| payment-reference-id | Coupa ID of payment reference | | | | | yes | integer |
| payment-reference-type | Type of payment reference | | | | | yes | string(255) |
| reason-code | Code indicating the trigger for this allocation | | | payment, auto_payment, epr, epr_rejected, manual | yes | yes | string(40) |
| source | Originating system (ERP, Coupa Pay, UI, etc) | | | coupa_pay, erp, ui, api | | yes | string(255) |
| source-transaction-from-id | Coupa ID of the source transaction on the sending side | | | | | yes | string |
| source-transaction-from-reference | Reference number of the source transaction on the sending side | | | | | yes | string |
| source-transaction-from-type | Type of the source transaction on the sending side | | | | | yes | string |
| source-transaction-to-id | Coupa ID of the source transaction on the receiving side | | | | | yes | string |
| source-transaction-to-reference | Reference number of the source transaction on the receiving side | | | | | yes | string |
| source-transaction-to-type | Type of the source transaction on the receiving side | | | | | yes | string |
| status | Current status of the allocation | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | User |
