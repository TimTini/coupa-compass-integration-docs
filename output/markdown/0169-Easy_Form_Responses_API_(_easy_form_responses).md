---
title: "Easy Form Responses API (/easy_form_responses)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/easy-form-responses-api-(easy_form_responses)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/easy-form-responses-api-(easy_form_responses)"
status_code: 200
fetched_at: "2026-04-09T11:59:41+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Easy Form Responses API (/easy_form_responses)"
---

# Easy Form Responses API (/easy_form_responses)

## Overview

Form responses are utilized in [SIM](https://compass.coupa.com/x61032.xml) and [Custom Objects](https://compass.coupa.com/x294250.xml).

To determine if the form response is related to SIM or a custom object, check the response payload:

- SIM-related form responses include the `supplier-id` field

- Custom object form responses include the `custom_object_name` and `custom_object_code` fields

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| PUT | `/api/users/:user_id/easy_form_responses/:id/add_approver` | add_approver | Manually add an approver for an easy form response |
| PUT | `/api/supplier_information/:supplier_information_id/easy_form_responses/:id/add_approver` | add_approver | Manually add an approver for an easy form response |
| PUT | `/api/users/:user_id/easy_form_responses/:id/approval` | approval | Submit an easy form response for approval |
| PUT | `/api/supplier_information/:supplier_information_id/easy_form_responses/:id/approval` | approval | Submit an easy form response for approval |
| GET | `/api/users/:user_id/easy_form_responses` | index | Query easy form responses |
| GET | `/api/supplier_information/:supplier_information_id/easy_form_responses` | index | Query easy form responses |
| GET | `/api/easy_form_responses` | index | Query easy form responses |
| PUT | `/api/users/:user_id/easy_form_responses/:id/remove_approval` | remove_approval | Remove an apporver who was manually added |
| PUT | `/api/supplier_information/:supplier_information_id/easy_form_responses/:id/remove_approval` | remove_approval | Remove an apporver who was manually added |
| PUT | `/api/users/:user_id/easy_form_responses/:id/review` | review | Review an easy form response |
| PUT | `/api/supplier_information/:supplier_information_id/easy_form_responses/:id/review` | review | Review an easy form response |
| GET | `/api/users/:user_id/easy_form_responses/:id` | show | Show an easy form response |
| GET | `/api/supplier_information/:supplier_information_id/easy_form_responses/:id` | show | Show an easy form response |
| PUT | `/api/users/:user_id/easy_form_responses/:id` | update | Update easy form response |
| PUT | `/api/supplier_information/:supplier_information_id/easy_form_responses/:id` | update | Update easy form response |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

StateIsoCode is available for SIM Easy Form Responses. The `region` element returns the following: `{country: country, state: state, state_iso_code: ISO-3166-2 codes}`. If the country does not have state options, the API returns the following: `{country: Antarctica, state: NA, state_iso_code: nil}`.

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| approvals | Approvals | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| current-approval | Current approval details | | | | | yes | |
| current-parallel-approvals | Current parallel approvals | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| easy-form-id | Easy form ID associated with this easy form response | yes | | | | yes | integer |
| easy-form-widget-responses | The widget responses | | | | | yes | [Easy Form Widget Response](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/easy-form-responses-api-(easy_form_responses)/easy-form-widget-responses-api) |
| id | Object unique identifier (must exist) | | | | | yes | integer |
| name | Name of the easy form response | | | | | yes | string(255) |
| requested-by | User that requested | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| status | Status of the easy form response | | | | | yes | string(255) |
| subject | Object associated with this easy form response | | | | | yes | [Invoice Header](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)-da-5926-da-5926) [Invoice Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-line-api) [Supplier Information](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)-da-5810-da-5810) [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| submitted-at | The date/time the response was submitted in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| preferred | Preferred | | | | yes | | string(255) |
