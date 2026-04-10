---
title: "Account Category API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/account-category-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/account-category-api"
status_code: 200
fetched_at: "2026-04-09T11:59:26+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Account Category API"
---

# Account Category API

Use the Account Category API to create and manage account categories to mimic your business'
financial structure.

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | | | | | yes | boolean |
| category-type | Category type | yes | | ap, ar, charges, deposit_account, dividend, escrow, factoring, guarantee, hr, letter_of_credit, lockbox, on_behalf, petty_cash, settlement, special_purpose, standard, taxes, trapped_cash, other | | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | Description | | | | | yes | string(500) |
| id | Coupa Internal ID | | | | | yes | integer |
| name | Name | yes | yes | | | yes | string(50) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
