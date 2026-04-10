---
title: "Receipt Requests API (/receipt_requests)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipt-requests-api-(receipt_requests)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipt-requests-api-(receipt_requests)"
status_code: 200
fetched_at: "2026-04-09T11:59:59+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Receipt Requests API (/receipt_requests)"
---

# Receipt Requests API (/receipt_requests)

## Introduction

Use the Receipt Requests API to create, update, or query receipt requests for your transaction.

The URL to access the Receipt Requests API is: `/api/receipt_requests`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

![](https://compass.coupa.com/DITARoot/icons/tip.png)
Tip: To add a user as an approver, append the user ID number as show in the below example. `/api/receipt_requests/:id/add_approver?approver_id=33`

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| DELETE | `/api/receipt_requests/:id` | destroy | Delete receipt request |
| GET | `/api/receipt_requests` | index | List receipt requests |
| GET | `/api/receipt_requests/:id` | show | Show receipt request |
| POST | `/api/receipt_requests/:id/submit` | submit | Submit receipt request for approval |
| POST | `/api/receipt_requests/:id/withdraw` | withdraw | Withdraw receipt request |
| PUT | `/api/receipt_requests/:id/add_approver` | add_approver | Add a user as an approver |
| PUT | `/api/receipt_requests/:id/remove_approval` | remove_approver | Remove a user as an approver |
| PUT | `/api/receipt_requests/:id/add_watcher` | add_watcher | Add a user as a watcher |
| PUT | `/api/receipt_requests/:id/remove_watcher` | remove_watcher | Remover a user as a watcher |

## Receipt Request Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | | any | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| type | Type | | | any | | yes | string(255) |
| status | Status | | | any | | yes | string(255) |
| lines | Request lines | | | any | | yes | [] |
| created_by | User who created | | | any | | yes | |
| updated_by | User who updated | | | any | | yes | |
