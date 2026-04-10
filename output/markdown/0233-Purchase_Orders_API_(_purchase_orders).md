---
title: "Purchase Orders API (/purchase_orders)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)"
status_code: 200
fetched_at: "2026-04-09T11:59:54+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Purchase Orders API (/purchase_orders)"
---

# Purchase Orders API (/purchase_orders)

## Overview

When working with the Purchase Orders API, you've got a few resource endpoints you can work from:

| **Resource** | **Path** | **Description** |
| --- | --- | --- |
| PO headers | `/api/purchase_orders` | Full purchase orders that contain PO lines, payment terms, addresses and more. |
| PO lines | `/api/purchase_order_lines` | Detailed information about PO lines like item info and accounting details. See [Purchase Order Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961) and [Order Line Allocations API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/order-line-allocations-api) for details. |
| PO changes | `/api/purchase_order_changes` | Create and manage PO change requests regardless if they drive approvals or not. |
| Reason insights | `/api/reason_insights/` | Provide reasons when reopening an order. |

## Actions

Purchase Orders API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| PUT | `/api/purchase_orders/:id/cancel` | cancel | Cancel |
| PUT | `/api/purchase_orders/:id/close` | close | Close a purchase order. See [Closing Purchase Orders](https://compass.coupa.com/x295731.xml) for more info. |
| POST | `/api/purchase_orders` | create | Create a purchase order as part of the [external purchase orders](https://compass.coupa.com/x295747.xml) feature. Do not use for Coupa-based POs. |
| PUT | `/api/purchase_orders/:id/ignore_window_and_issue` | ignore_window_and_issue | Ignore Windows And Issue |
| GET | `/api/purchase_orders` | index | Query purchase orders |
| PUT | `/api/purchase_orders/:id/issue` | issue | Issue and send the PO to the supplier. |
| PUT | `/api/purchase_orders/:id/issue_without_send` | issue_without_send | Issue without sending the PO to the supplier. |
| PUT | `/api/purchase_orders/:id/release_from_buyer_hold` | release_from_buyer_hold | Release purchase order on buyer hold |
| PUT | `/api/purchase_orders/:id/reopen` | reopen | Reopen a soft-closed purchase order. See [Closing Purchase Orders](https://compass.coupa.com/x295731.xml) for more info on soft close. |
| GET | `/api/purchase_orders/:id` | show | Show purchase order |
| PATCH | `/api/purchase_orders/:id` | update | Update purchase order |
| PUT | `/api/purchase_orders/:id` | update | Update purchase order |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| acknowledged-at | acknowledged_at | | | | | yes | datetime |
| acknowledged-flag | Has PO been acknowledged by Supplier? | | | | yes | yes | boolean |
| attachments | attachments | | | | yes | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| change-type | Last type of change on PO, it represents whether PO was changed through change request or through revise | change, revision, confirmation | | yes | string(255) | | |
| confirmation_status | Confirmation Status | no | pending_supplier_action, confirmed, pending_buyer_action, completed, overridden, archived, pending_integration, integration_failed, backgrounded, po_revise_backgrounded, po_change_backgrounded, pending_approval, po_change_failed, reconfirmation_backgrounded, supplier_draft, buyer_draft, partially_confirmed | | yes | string(255) | |
| coupa-accelerate-status | Status indicating whether the invoice has discount payment terms via Static Discounting | accelerated | | yes | string(255) | | |
| created-at | Date record was created in Coupa. | | | | | yes | datetime |
| created-by | Coupa ID of User who created Invoice | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency of transaction | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| current-integration-history-records | Current integration history records | | | | | yes | [Integration History Record](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-history-record-api) |
| exported | Indicates if transaction has been exported.<br>By default, you cannot update other fields while updating the exported field. To change this behavior, reach out to customer support. | | | | | yes | boolean |
| hide-price | Hide Price from supplier. True or False | no | no | | yes | | boolean |
| id | Coupa's internal ID | | | | | yes | integer |
| internal-revision | Internal Revision Number - Increases each time a change is made to a PO whether that change is internal or causes the PO to be resent to the supplier. | | yes | integer | | | |
| invoice-stop | Invoice Stop flag | | | | | yes | boolean |
| last-exported-at | Date and time transaction was last exported in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| milestones | Milestones | | | | yes | yes | Procurement::Milestone |
| order-lines | order_lines | yes | | | yes | yes | [Order Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961) |
| payment-method | payment_method | | | | yes | yes | string(255) |
| payment-term | Payment Terms | | | | yes | yes | [Payment Term](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/payment-terms-api-(payment_terms)) |
| pcard | pcard | | | | yes | yes | Pcard |
| po-number | PO Number | yes | yes | | yes | yes | string(20) |
| price-hidden | Hide Price from supplier. True or False | | | | | yes | boolean |
| reason-insight-events | Reason insight events for changes, reopens, etc. | | | yes | [Reason Insight Event](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/reason-insights-events-api) | | |
| requester | Requesting Account's login | | | | yes | | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| requisition-header | Requisition Header | | | | | yes | [Requisition Header](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)) |
| ship-to-address | ship_to_address | no | no | any | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| ship-to-attention | The user for whom the order will be addressed. Ship to the attention. | no | no | any | yes | yes | string(255) |
| ship-to-user | ship_to_user | yes | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| shipping-term | Payment Terms | | | | yes | yes | [ShippingTerm](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/shipping-terms-api-(shipping_terms)) |
| status | PO Status | | | buyer_hold, cancelled, closed, currency_hold, draft, error, expensed, issued, supplier_hold, supplier_window_hold, exported | | yes | string(50) |
| supplier | Supplier Coupa internal ID number | yes | | | yes | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| supplier-site | Supplier Site | no | no | any | yes | yes | [Supplier Site](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/supplier-sites-api-(supplier_sites)) |
| transmission-emails | Transmission Email comma separated list | no | no | any | yes | yes | text |
| transmission-method-override | Transmission Method Override | no | no | supplier_default, email, do_not_transmit | yes | yes | string(30) |
| transmission-status | Transmission Status | no | no | created, deferred, deferred_processing, pending_manual, pending_manual_cancel, awaiting_online_purchase, scheduled_for_email, sent_via_email, scheduled_for_cxml, scheduled_for_xml, sent_via_cxml, sent_via_xml, sent_manually, purchased_online, transmission_failure | | yes | string |
| total | Total | no | | | | | decimal(32,4) |
| type | Type of Order | | | ExternalOrderHeader | yes | | string(255) |
| updated-at | Last Updated at Date | | | | | yes | datetime |
| updated-by | Coupa ID of User who created Invoice | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| version | PO Supplier Version Number - Increase each time a PO is changed and triggers a resend to the supplier. | yes | yes | integer | | | |
| classification | Classification | | | msp, supplier, vms | yes | yes | string(255) |
| currency | Currency of transaction | | | | | yes | |
| confirm-by-hrs | Confirm by | | | | | yes | integer |
| order-confirmation-level | Confirmation Level | | | | | yes | int(11) |
| user-members | User members | | | | | yes | User |
| user-group-members | User group members | | | | | yes | User |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- There are dependent fields that become queryable based the value from the source field. For example, if you query against `po-method=email`, then po-email can be added as an additional query criteria. Please see fields with Yes*.

- For large data set and for performance optimization, you should always limit your result with some GET criteria.

- PO changes do not always increment the version number. See [Fields that Cause a Purchase Order Revision](https://compass.coupa.com/x295749.xml) for more info. The `updated-at` field can always be used to determine whether any changes have been made.

- In order to see `invoice-total` returned in the API query, you need to set the `default_purchase_orders_filter` to `default`. After updating the default PO API filter, **invoice-total** shows in the API GET call.

## Code examples

## Delete an order line using PUT

```text
<?xml version="1.0" encoding="UTF-8"?>
<order-header>
<order-lines>
<order-line>
<id>coupa_line_id</id>
<_delete>true</_delete>
</order-line>
</order-lines>
</order-header>
```

## Reopen a soft-closed PO

See [Closing Purchase Orders](https://compass.coupa.com/x295731.xml) for more info on soft close.

## Using a reason insight ID

```text
<?xml version="1.0" encoding="UTF-8"?>
<order-header>
<reason-insight-id>1</reason-insight-id>
<reason-insight-event-comment>comment body</reason-insight-event-comment>
</order-header>
```

## Using a reason insight code

```text
<?xml version="1.0" encoding="UTF-8"?>
<order-header>
<reason-insight-code>code</reason-insight-code>
<reason-insight-event-comment>comment body</reason-insight-event-comment>
</order-header>
```
