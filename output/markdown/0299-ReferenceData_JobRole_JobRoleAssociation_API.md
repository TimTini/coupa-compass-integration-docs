---
title: "ReferenceData::JobRole::JobRoleAssociation API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-assignments-api/referencedatajobrolejobroleassociation-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-assignments-api/referencedatajobrolejobroleassociation-api"
status_code: 200
fetched_at: "2026-04-09T12:00:08+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Worker Assignments API"
  - "ReferenceData::JobRole::JobRoleAssociation API"
---

# ReferenceData::JobRole::JobRoleAssociation API

Access Job Role Association data when working with the Worker Assignments API.

## Associations

This resource is associated with the Worker Assignments API. For more information, see [Worker Assignments API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-assignments-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | | | | | yes | boolean |
| code | Code | | | | | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| custom-fields | Custom fields | | | | | | |
| description | Description | | | | | yes | text |
| id | Coupa unique identifier | | | | | yes | integer |
| job-role | Job role | | | | | yes | ReferenceData::JobRole::JobRole |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| work-arrangement | Work arrangement | | | | | yes | ReferenceData::JobRole::WorkArrangement |
| work-hours | Work hours | | | | | yes | text |
| work-location | Work location | | | | | yes | ReferenceData::JobRole::JobRoleAssociation |
