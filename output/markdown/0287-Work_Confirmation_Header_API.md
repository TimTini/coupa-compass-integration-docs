---
title: "Work Confirmation Header API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api"
status_code: 200
fetched_at: "2026-04-09T12:00:05+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Work Confirmation Header API"
---

# Work Confirmation Header API

Retrieve information about service sheets. You can query all service sheets or request information about a single sheet by its ID.

## Overview

The Work Confirmation API allows you to retrieve information about service sheets.

The URL to access the Work Confirmation endpoint is: `https://{your_instance_name}/api/work_confirmation/headers`

For more information, see [Create or Edit a Service Sheet](https://compass.coupa.com/x293075.xml).

## Actions

The Work Confirmation API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/work_confirmation/headers` | index | Query service sheets. |
| GET | `/api/work_confirmation/headers/:id` | show | Query a single service sheet by ID. |

## Elements

The following elements are available for the Work Confirmation API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| approvals | Service Sheet approvals | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| comments | Service Sheet comments | | | | | yes | [Comment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/comments-api) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created the service sheet | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| created-by-fullname | Full name of the creator of the Purchase Order | | | | | yes | string |
| currency | Currency of the associated Purchase Order | | | | | yes | Currency |
| id | Coupa’s Internal ID | | | | | yes | integer |
| lines | Service Sheet lines | | | | | yes | [WorkConfirmation::Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-line-api) |
| order-header | Associated Purchase Order header | | | | | yes | [OrderHeader](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/order-confirmations-api-(order_header_confirmations)) |
| order-total | Total amount of the associated Purchase Order | | | | | yes | decimal |
| order-total-received-amount | Total amount received against the associated Purchase Order | | | | | yes | decimal |
| po-number | Purchase Order of the service sheet | | | | | yes | string |
| requested-by-fullname | Full name of the requester of the Purchase Order | | | | | yes | string |
| status | Service Sheet Status | | | | | yes | string(255) |
| submitted-at | Timestamp record was submitted in Coupa | | | | | yes | datetime |
| supplier | Supplier | | | | | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| supplier-display-name | Supplier display name | | | | | yes | string |
| supplier-reviews | Service Sheet quality assessment reviews | | | | | yes | SupplierReview |
| total | Total service sheet amount | | | | | yes | decimal |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
