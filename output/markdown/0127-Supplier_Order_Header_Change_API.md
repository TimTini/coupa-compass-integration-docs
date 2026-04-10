---
title: "Supplier Order Header Change API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/supplier-order-header-change-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/supplier-order-header-change-api"
status_code: 200
fetched_at: "2026-04-09T11:59:32+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Supplier Order Header Change API"
---

# Supplier Order Header Change API

Use the Supplier Order Header Change API to create and manage supplier order changes.

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| acknowledged-at | acknowledged_at | | | | | yes | date |
| approvals | Approvals | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| current-parallel-approvals | Current parallel approvals | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| attachments | Attachments | | | | | yes | Attachment |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | User |
| currency | Currency | | | | yes | yes | Currency |
| current-approval | Current/Pending Approval | | | | | yes | Approval |
| department | department | | | | yes | | Department |
| exported | Indicates if transaction has been exported | | | | | yes | boolean |
| hide-price | Hide Price from supplier. True or False | | | | yes | | Order Header Change |
| id | Coupa unique identifier | | | | | yes | integer |
| justification | justification | | | | | yes | string |
| lines-count | Number of lines in the PO Change document | | | | | yes | integer |
| lines-pending-add-count | Number of lines pending addition in PO Change document | | | | | yes | integer |
| lines-pending-delete-count | Number of lines pending deletion in PO Change document | | | | | yes | integer |
| milestones | Milestones | | | | yes | yes | Procurement::Milestone |
| order-header-id | id of the order that is being changed | | | | yes | yes | integer |
| order-line-changes | Order line changes | | | | yes | yes | Order Line Change |
| payment-method | payment_method | | | | yes | | string(255) |
| payment-term | payment terms | | | | yes | yes | Payment Term |
| pcard | pcard | | | | yes | yes | Pcard |
| pending-cancel | Is the PO pending cancellation. True or False | | | | | yes | boolean |
| po-number | PO Number | | | | | yes | string(20) |
| price-hidden | Hide Price from supplier. True or False | | | | | yes | boolean |
| reason-insight-event | Reason Insight Event | yes | | | | yes | Reason Insight Event |
| recurring-rules | Recurring rules | | | | | yes | Procurement::Recurring Rule |
| reject-reason | Reject reason | | | | | yes | Comment |
| requester | Requesting Account's login | | | | | yes | User |
| requisition-header-id | requisition_header_id | | | | | yes | integer |
| ship-to-address | Ship to address | | | | yes | yes | Address |
| ship-to-attention | Attention user for the PO | | | | yes | | string(255) |
| ship-to-user | Ship to user | | | | yes | yes | User |
| shipping-term | shipping terms | | | | yes | yes | Shipping Term |
| status | PO Status | | | | | yes | string(255) |
| supplier | Supplier | | | | yes | yes | Supplier |
| supplier-initiated | Was this change initiated by a supplier. True or False | | | | | yes | boolean |
| supplier-site | Supplier Site | | | | yes | | Supplier Site |
| total | PO Change document total | | | | | yes | decimal(32,4) |
| transmission-emails | Tranmission Email comma seperated list | | | | yes | yes | text |
| transmission-method-override | Transmission Method Override | | | supplier_default, email, do_not_transmit | yes | yes | string(30) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| version | PO Supplier Version Number - Increase each time a PO is changed and triggers a resend to the supplier. | | | | | yes | integer |
