---
title: "Policy API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/announcements-api-(announcements)/policy-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/announcements-api-(announcements)/policy-api"
status_code: 200
fetched_at: "2026-04-09T11:59:09+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Announcements API (/announcements)"
  - "Policy API"
---

# Policy API

## Associations

This API is associated with the [Announcements API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/announcements-api-(announcements)).

## Elements

The following elements are available for the Policy API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | | | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| name | Policy name | | true | true | | yes | string(100) |
| text | Policy description | | | | | yes | text |
| created_by | User who created | | | | | yes | |
| updated_by | User who updated | | | | | yes | |
