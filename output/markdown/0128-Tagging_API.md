---
title: "Tagging API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/tagging-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/tagging-api"
status_code: 200
fetched_at: "2026-04-09T11:59:32+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Tagging API"
---

# Tagging API

Use the Tagging API to bring in and export tags to your third-party system.

## Elements

| **Element** | **Description** | **Type** | **API In** | **API Out** | **Required** | **Length** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Tagging active state | boolean | yes | yes | | | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | datetime | | yes | | | |
| created-by | User who created | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) | | yes | | | |
| description | Description on the Tag on an Object (Tags on different objects can have different descriptions) | text | yes | yes | | | |
| id | Coupa unique identifier | integer | | yes | | | |
| tag | tag | [Tag](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/tag-api) | yes | yes | | | |
| updated-by | User who most recently updated the tag. | integer | | yes | | | |
