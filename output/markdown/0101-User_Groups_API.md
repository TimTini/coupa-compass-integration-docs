---
title: "User Groups API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)/user-groups-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)/user-groups-api"
status_code: 200
fetched_at: "2026-04-09T11:59:26+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Users API (/users)"
  - "User Groups API"
---

# User Groups API

## Actions

User Group allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/user_groups` | create | Create User Group |
| GET | `/api/user_groups` | index | Query User Groups |
| GET | `/api/user_groups/:id` | show | Show User Group |
| PATCH | `/api/user_groups/:id` | update | Update User Group |
| PUT | `/api/user_groups/:id` | update | Update User Group |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | | | Yes/No, True/False | yes | yes | boolean |
| can-approve | User group has the ability to be an approver | | | Yes/No, True/False | yes | yes | boolean |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | Description | | | | yes | yes | text |
| id | Coupa unique identifier | | | | | yes | integer |
| mention-name | Mention name | | yes | | | yes | string(255) |
| name | Name | yes | yes | | yes | yes | string(255) |
| open | User group is open for everyone to join or owner must invite others | Yes/No, True/False | yes | yes | boolean | | |
| owner | Owner | | | | yes | yes | [User Group](https://compass.coupa.com/x285917.xml) |
| type | Blank for Groups, Project for Projects | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| users | Users | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| avatar-thumb-url | URL for avatar thumbnail | | | | | yes | string |
