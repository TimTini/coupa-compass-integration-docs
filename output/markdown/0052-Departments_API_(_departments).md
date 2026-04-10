---
title: "Departments API (/departments)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/departments-api-(departments)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/departments-api-(departments)"
status_code: 200
fetched_at: "2026-04-09T11:59:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Departments API (/departments)"
---

# Departments API (/departments)

Use the departments API to mimic your business' operating
structure and organize content groups and users accordingly.

The URL to access departments
is: `https:///api/departments`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Departments API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/departments` | create | Create department |
| GET | `/api/departments` | index | Query departments |
| GET | `/api/departments/:id` | show | Show department |
| PUT | `/api/departments/:id` | update | Update department |

## Elements

The following elements are available for the Departments
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Control whether the Department is Active or Inactive | | | true, false | yes | yes | boolean |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | Department Name | yes | yes | | yes | yes | string |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
