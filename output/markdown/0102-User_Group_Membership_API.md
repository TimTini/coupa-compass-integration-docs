---
title: "User Group Membership API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)/user-group-membership-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)/user-group-membership-api"
status_code: 200
fetched_at: "2026-04-09T11:59:26+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Users API (/users)"
  - "User Group Membership API"
---

# User Group Membership API

## Actions

User Group allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/user_group_memberships` | create | Create an user group membership |
| GET | `/api/user_group_memberships` | index | Query User group memberships |
| GET | `/api/user_group_memberships/:id` | show | Show an user group membership |
| PATCH | `/api/user_group_memberships/:id` | update | Update an user group membership |
| PUT | `/api/user_group_memberships/:id` | update | Update an user group membership |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| id | Coupa unique identifier | | | | | yes | integer |
| owner | Indicates whether the user is admin or not | | | | yes | yes | boolean |
| participant | Indicates whether the user is participant or not | | | | yes | yes | boolean |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| user | user | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| user-group | Group | | | | yes | yes | [User Group](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)/user-groups-api) |
| user-group-id | User group ID or Project ID | | | | yes | yes | integer |
| user-id | User Id | | | | yes | yes | integer |
| user-group-type | User group or Project are the valid types | | | | | yes | string(255) |
