---
title: "Tag API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/tag-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/tag-api"
status_code: 200
fetched_at: "2026-04-09T11:59:32+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Tag API"
---

# Tag API

Use the Tag API to specify tags and to specify whether tags are external.

## Associations

The tag API resource is associated with many Coupa objects, including the [invoice](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)-da-5926-da-5926), and sourcing APIs.

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | Name | yes | yes | | yes | yes | string(30) |
| system-tag | System tag | | | | yes | yes | boolean |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| active | Tagging active state | | | | yes | yes | boolean |

## Example

When using the Tag API, `` should always be **wrapped inside **
``.

Here is an example:

```text
<invoice-lines>
<invoice-line>
<taggings>
<tagging>
<tag>
<name>header_tag</name>
<system_tag>true</system_tag>
</tag>
<description>API Desc</description>
</tagging>
</taggings>
</invoice-line>
</invoice-lines>
```
