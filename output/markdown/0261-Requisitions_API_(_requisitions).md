---
title: "Requisitions API (/requisitions)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)"
status_code: 200
fetched_at: "2026-04-09T11:59:59+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Requisitions API (/requisitions)"
---

# Requisitions API (/requisitions)

The URL to access requisitions is: `https://{your_instance_name}/api/requisitions`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Requisitions API Objects

This is the full list of expense objects available via the UI. However, not all objects listed here have endpoints–some are only referenced by objects, and can't be updated directly.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- If submitting this API using a static Chart of Accounts, any segment values included must be from an existing account.

- If submitting this API using a dynamic Chart of Accounts, any segment values included must match existing account segments or lookup values. If an account doesn't exist for a given segment value, the API automatically creates it.

## Actions

Requisitions API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| PUT | `/api/requisitions/:id/add_approver` | add_approver | Manually add an approver for a requisition |
| POST | `/api/requisitions/add_to_cart` | add_to_cart | Add To Cart |
| POST | `/api/requisitions` | create | Create a requisition in draft status, which will then need to be submitted manually |
| GET | `/api/requisitions/current_cart` | current_cart | Send current cart for user, if there is no current cart then create and send |
| GET | `/api/requisitions` | index | Query requisitions |
| GET | `/api/requisitions/mine` | mine | `/api/requisitions/mine` |
| PUT | `/api/requisitions/:id/remove_approval` | remove_approval | Remove an approver who was manually added |
| PUT | `/api/requisitions/:id/save_for_later` | save_for_later | Save For Later for API requisitions |
| GET | `/api/requisitions/:id` | show | Show requisition |
| POST | `/api/requisitions/submit_for_approval` | submit_for_approval | Create a requisition and attempt to submit it for approval / buyer action |
| PUT | `/api/requisitions/:id` | update | Update requisition |
| PUT | `/api/requisitions/:id/update_and_submit_for_approval` | update_and_submit_for_approval | Update requisition and submit for approval |
| DELETE | `/api/requisitions/:id` | destroy | Delete requisition |
| POST | `/api/requisitions/schedule_issuance` | schedule_issuance | Set an issuance date for requisition lines and optionally retry issuance after a set number of days if the requisition is not approved by the scheduled date.<br>Example payload:<br>@@BLOCK_0@@<br>For more information, see [Schedule PO Issuance API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/scheduled-po-issuance-api). |
| POST | `/api/requisitions/unschedule_issuance` | unschedule_issuance | Remove the scheduled issuance date and any retry interval from requisition lines.<br>Example payload:<br>@@BLOCK_1@@<br>For more information, see [Schedule PO Issuance API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/scheduled-po-issuance-api). |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| approvals | approvals | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| current-parallel-approvals | Current parallel approvals | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| approver | approver | | | | yes | | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| attachments | attachments | | | | | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| buyer-note | Any comments or notes from the Buyer | | | | yes | yes | text |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | yes | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency Code | | | | | yes | USD |
| current-approval | Current/Pending Approval | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| department | Requisition Department | | | | yes | yes | [Department](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/departments-api-(departments)) |
| exported | Indicates if transaction has been exported | | | | | yes | boolean |
| external-po-reference | External PO reference that allows customers to supply PO numbers that would override auto generated PO numbers | no | yes | any | yes | | string(255) |
| hide-price | Hide Price from supplier. True or False | no | no | | yes | | RequisitionHeader |
| id | Coupa unique identifier | | | | | yes | integer |
| justification | Requisition Justification Comments | | | | yes | yes | text |
| last-exported-at | Last Exported Time | | | | yes | | datetime |
| line-count | Requisition Header Line Count | no | no | any | | yes | integer |
| milestones | Milestones | | | | yes | yes | Procurement::Milestone |
| mobile-currency | Default currency used | | | | | yes | USD |
| mobile-total | total | | | | | yes | decimal |
| need-by-date | Item Need By Date | | | | yes | yes | datetime |
| pcard | Name of PCard | | | | yes | yes | Pcard |
| price-hidden | Hide price from supplier. True or False | | | | | yes | boolean |
| receiving-warehouse-id | Receiving Warehouse ID | no | no | any | yes | yes | integer |
| recurring-rules | Recurring Rules | | | | | yes | |
| reject-reason-comment | last reject reason comment | | | | | yes | string |
| req_title | Optional title of the Requisition | | | | yes | yes | string(50) |
| requested-by | requested_by | yes | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| requester | requested_by | yes | | | yes | | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| requisition-lines | requisition_lines | yes | | | yes | yes | RequisitionLine |
| ship-to-address | Name of Address | yes | | | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| ship-to-attention | Ship to Address Attention | | | | yes | yes | string(255) |
| status | Transaction status. To learn more about Requisition statuses, see [Requisition Status Definitions](https://compass.coupa.com/x295859.xml). | yes | | draft, cart, pending_buyer_action, pending_approval,<br>approved ordered partially_received, received,<br>abandoned, backgrounded, withdrawn | | yes | string(50) |
| submitted-at | submitted_at | | | | | yes | datetime |
| tags | | | | | yes | yes | [] |
| taggings | | | | | yes | yes | [] |
| total | Total in own currency | | | | | yes | decimal |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| user_members | User members | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| user_group_members | User group members | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

The created_by element defaults from the API User key, but it can be overridden by the Requisition API. Contact Coupa Support to allow the Requisition API to override the API User key value.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- In a requisition-line, you can use either a description (free-form) or an item (catalog item). If an item id is used, the item must exist. The <source-type></source-type> is not used and ignored.

- Currencies, users in the requested-by and suppliers must be in the system with a status of active.

- Item: If a preferred supplier and price is available for an item it will be used unless the unit-price is specified. If a unit-price is specified, it will override the default pricing available for the item. While it is not an error to specify a description and an item, using an item will set the description to the item description, ignoring the passed in the description field.

- Defaulting: Unless otherwise specified in the XML, the system will respect the relevant defaulting within the system. Such as defaulting payment and shipping terms from the supplier record.

- Line Numbering: The API expects the line-num to increment by one for each new line number. If you use the same line-num, the system will ignore all other lines with the same number.

- As part of the Version 30.2.2 release update, we've resolved an issue that prevented you from creating a requisition for users outside of the requester's Content Group. Now, the requisition API reflects the functionality of the UI.

- As part of the Version 34.4.0 release update, requisition API can be used to create a new requisition by inserting a line from another requisition - only if the status of source requisition is Draft. If the status of the requisition is not Draft, then no line from the requisition can be referenced to create another new requisition.

When the “created by” user is being set via API, that user’s content group access is validated for the creation of the requisition. See the table below for reference:

| **allow_created_by_override_via_api** | **Creator has access via Content Group** | **Requester has access via Content Group** | **Allow creation via API** |
| --- | --- | --- | --- |
| TRUE | Y | N/A | Y |
| TRUE | N | N/A | N |
| FALSE | N/A | N/A | Y |

## Default supplier item behavior

When a req with quantity based lines is created via API,the supplier item defaults on the req line using the following rules:

| **API payload** | **Expected result** |
| --- | --- |
| Item ID | Preferred or lowest priced supplier item |
| Item ID, supplier | Preferred or lowest priced supplier item matching the provided supplier id |
| Item ID, supplier, source part number | Preferred or lowest priced supplier item matching the provided supplier id and source part number |
| Item ID, supplier, source part number, supplier aux part number | Preferred or lowest priced supplier item matching the provided supplier id and source part num and supplier aux part number |
| Item ID, supplier, contract | Preferred or lowest priced supplier item matching the provided supplier id and contract id |
| Item ID, supplier, contract, price | Preferred or lowest priced supplier item matching the provided supplier id and contract id (price is not used in match) |
| Item ID, supplier, contract, source part number | Preferred or lowest priced supplier item matching the provided supplier id and contract id and source part number |
| Item ID, supplier, contract, source part number, supplier aux part number | Preferred or lowest priced supplier item matching the provided supplier id and contract id and source part num and supplier aux part number |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- If the supplier item is associated to a catalog, the catalog must be in "accepted" status and the current date is within the catalog start and end dates.

- If the supplier item is associated to a contract, the contract must be in "published" status and the current date is within the catalog start and end dates.
