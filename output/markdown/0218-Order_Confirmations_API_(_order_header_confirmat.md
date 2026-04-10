---
title: "Order Confirmations API (/order_header_confirmations)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/order-confirmations-api-(order_header_confirmations)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/order-confirmations-api-(order_header_confirmations)"
status_code: 200
fetched_at: "2026-04-09T11:59:51+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Order Confirmations API (/order_header_confirmations)"
---

# Order Confirmations API (/order_header_confirmations)

The URL to access order confirmations is: `https://{your_instance}/api/order_header_confirmations/`

## Actions

The Order Confirmations API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/order_header_confirmations` | index | Query order confirmations. |
| GET | `/api/order_header_confirmations/:id` | show | Show order confirmations. |
| PATCH | `/api/order_header_confirmations/:id` | update | Update order confirmations. When the confirmation is line level, moves the confirmation lines to buyer_draft. |
| PUT | `/api/order_header_confirmations/:id` | update | Update line-level order confirmations. Moves the confirmation lines to buyer_draft. |
| PUT | `api/order_header_confirmations/:id/integration_approval_rejected` | update | Moves all lines in the `pending integration` status to the `overridden` status. See note below the table for more information. |
| POST | `/api/order_header_confirmations/:id/accept_header` | accept_header | Buyers can accept order header confirmations from suppliers when the order confirmation status is pending_buyer_review. confirmation_level must be header. |
| POST | `/api/order_header_confirmations/:id/reject_header` | reject_header | Buyers can reject order header confirmations from suppliers when the order confirmation status is pending_buyer_review. confirmation_level must be header. Requires the reason-insight-events element in the request body. |
| POST | `/api/order_header_confirmations/:id/submit` | submit | Submit a line-level order confirmation that is in a draft state. |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

The `/integration_approval_rejected` endpoint requires the Partial Order Confirmations feature to be enabled and requires an `integration_version` query parameter. For example: `api/order_header_confirmations/:id/integration_approval_rejected?integration_version=1`. For more information, see [Review Lines on a Purchase Order for Partial Confirmations](https://compass.coupa.com/en-us/products/product-documentation/supply-chain-collaboration/review-lines-on-a-purchase-order-for-partial-confirmations).

## Elements

The Order Confirmations API contains the following elements:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Date record was created in Coupa. | | | | | yes | datetime |
| created-by | ID of the user who created the order. | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| exported | Indicates if the transaction has been exported. | | | | | yes | boolean |
| external-reference-number | External Reference Number. | | | | | yes | string(255) |
| id | Coupa's internal ID. | | | | yes | yes | integer |
| integration-message | Integration message. | | | | | yes | text |
| last-exported-at | Date of last export. | | | | | yes | datetime |
| order-header | Purchase order. | | | | | yes | OrderHeaderConfirmation |
| order-line-confirmations | Order line confirmations. | | | | yes | yes | OrderLineConfirmation |
| reason-insight-events | Reason insight events. | Only when submitting a reject_header request. | | | yes | | ReasonInsightEvent |
| status | Order confirmation status. | | | | | yes | string(255) |
| updated-at | Date of last update. | | | | | yes | datetime |
| updated-by | ID of the user who last updated the order. | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
