---
title: "Account Group API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/account-group-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/account-group-api"
status_code: 200
fetched_at: "2026-04-09T11:59:26+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Account Group API"
---

# Account Group API

Use the account groups API to create and manage account groups to mimic your business'
financial structure.

## Associations

This API is associated with [Accounts API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account-group-type | Type | yes | | 1, 2 | yes | yes | integer |
| account-type | account_type | yes | | | yes | yes | [AccountType](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | name | yes | yes | | yes | yes | string(80) |
| segment-10-col | segment_10_col | | | | yes | yes | string(255) |
| segment-10-op | segment_10_op | | | | yes | yes | string(255) |
| segment-10-val | segment_10_val | | | | yes | yes | string(255) |
| segment-11-col | segment_11_col | | | | yes | yes | string(255) |
| segment-11-op | segment_11_op | | | | yes | yes | string(255) |
| segment-11-val | segment_11_val | | | | yes | yes | string(255) |
| segment-12-col | segment_12_col | | | | yes | yes | string(255) |
| segment-12-op | segment_12_op | | | | yes | yes | string(255) |
| segment-12-val | segment_12_val | | | | yes | yes | string(255) |
| segment-13-col | segment_13_col | | | | yes | yes | string(255) |
| segment-13-op | segment_13_op | | | | yes | yes | string(255) |
| segment-13-val | segment_13_val | | | | yes | yes | string(255) |
| segment-14-col | segment_14_col | | | | yes | yes | string(255) |
| segment-14-op | segment_14_op | | | | yes | yes | string(255) |
| segment-14-val | segment_14_val | | | | yes | yes | string(255) |
| segment-15-col | segment_15_col | | | | yes | yes | string(255) |
| segment-15-op | segment_15_op | | | | yes | yes | string(255) |
| segment-15-val | segment_15_val | | | | yes | yes | string(255) |
| segment-16-col | segment_16_col | | | | yes | yes | string(255) |
| segment-16-op | segment_16_op | | | | yes | yes | string(255) |
| segment-16-val | segment_16_val | | | | yes | yes | string(255) |
| segment-17-col | segment_17_col | | | | yes | yes | string(255) |
| segment-17-op | segment_17_op | | | | yes | yes | string(255) |
| segment-17-val | segment_17_val | | | | yes | yes | string(255) |
| segment-18-col | segment_18_col | | | | yes | yes | string(255) |
| segment-18-op | segment_18_op | | | | yes | yes | string(255) |
| segment-18-val | segment_18_val | | | | yes | yes | string(255) |
| segment-19-col | segment_19_col | | | | yes | yes | string(255) |
| segment-19-op | segment_19_op | | | | yes | yes | string(255) |
| segment-19-val | segment_19_val | | | | yes | yes | string(255) |
| segment-1-col | segment_1_col | | | | yes | yes | string(255) |
| segment-1-op | segment_1_op | | | | yes | yes | string(255) |
| segment-1-val | segment_1_val | | | | yes | yes | string(255) |
| segment-20-col | segment_20_col | | | | yes | yes | string(255) |
| segment-20-op | segment_20_op | | | | yes | yes | string(255) |
| segment-20-val | segment_20_val | | | | yes | yes | string(255) |
| segment-2-col | segment_2_col | | | | yes | yes | string(255) |
| segment-2-op | segment_2_op | | | | yes | yes | string(255) |
| segment-2-val | segment_2_val | | | | yes | yes | string(255) |
| segment-3-col | segment_3_col | | | | yes | yes | string(255) |
| segment-3-op | segment_3_op | | | | yes | yes | string(255) |
| segment-3-val | segment_3_val | | | | yes | yes | string(255) |
| segment-4-col | segment_4_col | | | | yes | yes | string(255) |
| segment-4-op | segment_4_op | | | | yes | yes | string(255) |
| segment-4-val | segment_4_val | | | | yes | yes | string(255) |
| segment-5-col | segment_5_col | | | | yes | yes | string(255) |
| segment-5-op | segment_5_op | | | | yes | yes | string(255) |
| segment-5-val | segment_5_val | | | | yes | yes | string(255) |
| segment-6-col | segment_6_col | | | | yes | yes | string(255) |
| segment-6-op | segment_6_op | | | | yes | yes | string(255) |
| segment-6-val | segment_6_val | | | | yes | yes | string(255) |
| segment-7-col | segment_7_col | | | | yes | yes | string(255) |
| segment-7-op | segment_7_op | | | | yes | yes | string(255) |
| segment-7-val | segment_7_val | | | | yes | yes | string(255) |
| segment-8-col | segment_8_col | | | | yes | yes | string(255) |
| segment-8-op | segment_8_op | | | | yes | yes | string(255) |
| segment-8-val | segment_8_val | | | | yes | yes | string(255) |
| segment-9-col | segment_9_col | | | | yes | yes | string(255) |
| segment-9-op | segment_9_op | | | | yes | yes | string(255) |
| segment-9-val | segment_9_val | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
