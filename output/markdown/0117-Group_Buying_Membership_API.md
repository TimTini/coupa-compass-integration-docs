---
title: "Group Buying Membership API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/group-buying-membership-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/group-buying-membership-api"
status_code: 200
fetched_at: "2026-04-09T11:59:29+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Group Buying Membership API"
---

# Group Buying Membership API

Use the Group Buying Membership API to create and manage group-buying memberships for group
carts.

## Associations

This API is associated with:

- [Purchase Orders API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/purchase-orders-api-(purchase_orders)/purchase-order-lines-api-da-5961-da-5961)

- [Requisitions API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions))

- [Users API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users))

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | false | false | any | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | | yes | datetime |
| purchasing_document_id | Purchasing document id | false | false | any | | yes | integer |
| purchasing_document_type | Purchasing document type | false | false | any | | yes | string(255) |
| buying_member_type | Buying member type | false | false | any | | yes | string(255) |
| buying_member_id | Buying member id | false | true | any | | yes | integer |
| deleted | Deleted | false | false | any | | yes | boolean |
| buying_member | Buying member | false | false | any | | yes | user |
| purchasing_document | Purchasing document | false | false | any | | yes | user |
| created_by | User who created | false | false | any | | yes | user |
| updated_by | User who updated | false | false | any | | yes | user |
