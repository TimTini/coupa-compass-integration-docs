---
title: "Integrations API (/integrations)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)"
status_code: 200
fetched_at: "2026-04-09T11:59:46+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Integrations API (/integrations)"
---

# Integrations API (/integrations)

## Actions

The Integrations API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/integrations` | create | Create integration |
| GET | `/api/integrations` | index | Query integrations |
| GET | `/api/integrations/:id` | show | Show integration |
| PUT | `/api/integrations/:id` | update | Update integration |

## Elements

The following elements are available for the
Integrations API:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Values** | **Api_In** | **Api_Out ** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| business-object | Business Object | yes | | | yes | yes | string(255) |
| code | Unique Integration Code | yes | yes | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| direction | Direction | yes | | to_coupa, from_coupa | yes | yes | string(255) |
| end-system | End System | yes | | | yes | yes | string(255) |
| end-system-type | End System Type | yes | internal, payroll, erp, hr, third_party_partner, third_party_vendor, other | yes | yes | string(255) | |
| id | Coupa unique identifier | | | | | yes | integer |
| integration-type | Type of integration | | flat_file, api, corporate_credit_card_file, json, xml | yes | yes | string(255) | |
| name | Integration Name | yes | yes | | yes | yes | string(255) |
| standard | Standard | | | | | yes | boolean |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created_by | User who created | | | | | yes | |
| updated_by | User who updated | | | | | yes | |
