---
title: "Purchase Order Change API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-change-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-change-api"
status_code: 200
fetched_at: "2026-04-09T11:59:54+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Purchase Orders API (/purchase_orders)"
  - "Purchase Order Change API"
---

# Purchase Order Change API

## Overview

Use this API to modify orders that are already in flight, either
in approvals or sent to the supplier.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Purchase Order Changes GET API is not
intended to retrieve PO revisions to out to ERP.

For PO Revisions, always use PO GET API with exported = false, and use the 'version'
value to identify whether the PO is a new one or a revised PO.

## Actions

Purchase order changes API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| PUT | `/api/purchase_order_changes/:id/add_approver` | add_approver | Manually add an approver for an order header change |
| POST | `/api/purchase_order_changes` | create | Create purchase order change. Cannot submit POST call for purchase orders in draft or pending approval statuses. |
| GET | `/api/purchase_order_changes` | index | Query purchase order changes |
| PUT | `/api/purchase_order_changes/:id/remove_approval` | remove_approval | Remove an approver who was manually added |
| GET | `/api/purchase_order_changes/:id` | show | Show purchase order change |
| PUT | `/api/purchase_order_changes/:id/submit_for_approval` | submit_for_approval | Submit purchase order change for approval |
| PUT | `/api/purchase_order_changes/:id` | update | Update purchase order change. Cannot update records created through the Coupa Supplier Portal. |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| acknowledged-at | acknowledged_at | | | | | yes | date |
| approvals | `` attribute with `` value must be included for PUT/PATCH to an existing PO change request. | Yes* | | Current approver `` must exist in Coupa | yes | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| attachments | Attachments | | | | | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| current-approval | Current/Pending Approval | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| department | department | | | | yes | | [Department](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/departments-api-(departments)) |
| easy_form_response_id | Easy Form Response Id | | | | | yes | |
| exported | Indicates if transaction has been exported | | | | | yes | boolean |
| hide-price | Hide Price from supplier. True or False | No | No | | yes | | Order Header Change |
| id | Coupa's unique identifier for the PO change request. Req'd for PUT update to existing change request | Yes* | | Valid PO change request ID | yes | yes | integer |
| justification | justification | | | | | yes | |
| order-header-id | ID of the order that is being changed. Req'd for new POST change request | Yes* | | Valid PO header ID | yes | yes | integer |
| order-line-changes | Order line changes | | | | yes | yes | |
| payment-method | payment_method | | | | yes | | string(255) |
| payment-term | payment terms | | | | yes | yes | [Payment Term](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/payment-terms-api-(payment_terms)) |
| pcard | pcard | | | | yes | yes | Pcard |
| po-number | PO Number | | | | | yes | string(20) |
| price-hidden | Hide Price from supplier. True or False | | | | | yes | boolean |
| reject-reason | Reject reason | | | | | yes | [Comment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/comments-api) |
| requester | Requesting Account's login | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| requisition-header-id | requisition_header_id | | | | | yes | integer |
| ship-to-address | Ship to address | | | | | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| ship-to-user | Ship to user | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| shipping-term | shipping terms | | | | yes | yes | [Shipping Term](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/shipping-terms-api-(shipping_terms)) |
| source-part-num | source_part_num | | | | yes | yes | string(255) |
| status | PO Status | | | | | yes | string(255) |
| supplier | Supplier | | | | | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| transmission-emails | Transmission Email comma separated list | No | No | any | yes | yes | text |
| transmission-method-override | Transmission Method Override | No | No | supplier_default, email, do_not_transmit | yes | yes | string(30) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| version | PO Supplier Version Number - Increase each time a PO is changed and triggers a resend to the supplier. | | | | | yes | integer |
| manufacturer_name | Manufacturer Name | | | | yes | yes | string(255) |
| manufacturer_part_number | Manufacturer Part Number | | | | yes | yes | string(255) |
| extra_line_attribute | | | | | yes | yes | |
| service_type | | | | | | yes | |
| currency | | | | | yes | yes | |
| milestones | | | | | yes | yes | |
| recurring-rules | Recurring rules | | | | | yes | - |
| total | PO Change document total | | | | | yes | decimal(32,4) |
| pending-cancel | Is the PO pending cancellation? True or False | | | | | yes | boolean |
| lines-count | Number of lines in the PO Change document | | | | | yes | integer |
| lines-pending-add-count | Number of lines pending addition in PO Change document | | | | | yes | integer |
| lines-pending-delete-count | Number of lines pending deletion in PO Change document | | | | | yes | integer |

## Example Calls

## Create a PO change request

Create a PO change request:

`POST https://{your_instance}.coupahost.com/api/purchase_order_changes`

## Payload

To POST, you need to include the ID of the original header, and
any elements you want to modify. Use the same format as the
original PO for the attribute changes.

```text
<?xml version="1.0" encoding="UTF-8"?>
<order-header-change>
<order-header-id>1000</order-header-id>
<!-- Requested changes to the PO -->
</order-header-change>
```

## 201 Success response

Coupa returns a new ``
with an ID for the change and the full PO, including any of
the changes you specified in your POST payload.

```text
<?xml version="1.0" encoding="UTF-8"?>
<order-header-change>
<id type="integer">501</id>
<created-at type="dateTime">2018-04-06T23:14:50+05:30</created-at>
<updated-at type="dateTime">2018-04-06T23:14:51+05:30</updated-at>
<order-header-id type="integer">123750</order-header-id>
<!-- Original PO with requested changes -->
</order-header-change>
```

The `` of the PO will be
`approved` if the change didn't require new approvals,
or `pending_approval` if the change does require new
approvals.

## Update a PO change request

You can modify a PO change request that's pending approval
by sending an [authenticated](https://compass.coupa.com//Integrate/Technical_Documentation/API/Get_Started/Get_Started#Authentication)
API call:

`POST https://{your_instance}.coupahost.com/api/purchase_order_changes/{id}`
where `{id}` is the `` attribute in
the 201 response. You can't modify a PO change request that's already approved.

## Payload

The payload format is essentially the same as the POST, except
that you need to include the current approver for the PO
change.

```text
<?xml version="1.0" encoding="UTF-8"?>
<order-header-change>
<approver>
<login>Approver Name</login>
</approver>
<!-- Requested changes to the PO -->
</order-header-change>
```

## 200 Response

The response is the same as a POST: the
`` with the ID and the full
PO, including any of the changes you specified in your PUT
payload.

```text
<?xml version="1.0" encoding="UTF-8"?>
<order-header-change>
<id type="integer">501</id>
<created-at type="dateTime">2018-04-06T23:14:50+05:30</created-at>
<updated-at type="dateTime">2018-04-06T23:14:51+05:30</updated-at>
<order-header-id type="integer">123750</order-header-id>
<!-- Original PO with requested changes -->
</order-header-change>
```

## 400 Bad request response

If you send a bad request, Coupa will provide a list of
errors.

```text
<?xml version="1.0" encoding="UTF-8"?>
<errors>
<error>
<!-- List of errors -->
</error>
</errors>
```
