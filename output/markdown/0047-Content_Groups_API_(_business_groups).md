---
title: "Content Groups API (/business_groups)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)"
status_code: 200
fetched_at: "2026-04-09T11:59:11+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Content Groups API (/business_groups)"
---

# Content Groups API (/business_groups)

Create content groups and assign to users to restrict access to
other objects in Coupa. Content groups are also known as business
groups in some more back-end cases.

The URL to access content
groups is: `https:///api/business_groups`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Content Groups API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/business_groups` | create | Create business group |
| GET | `/api/business_groups` | index | Query business groups |
| GET | `/api/business_groups/:id` | show | Show business group |
| PUT | `/api/business_groups/:id` | update | Update business group |

## Elements

The following elements are available for the Content Groups
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | description | | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | name | yes | yes | | yes | yes | string(100) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

When dealing with large data sets of content groups, always limit your GET with some
criteria.
