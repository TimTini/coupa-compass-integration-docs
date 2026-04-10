---
title: "Custom Object API (/custom_objects/id)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/custom-object-api-(custom_objectsid)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/custom-object-api-(custom_objectsid)"
status_code: 200
fetched_at: "2026-04-09T11:59:39+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Custom Object API (/custom_objects/id)"
---

# Custom Object API (/custom_objects/id)

## Introduction

Use the Custom Objects API to create, update, or query the data records for your Custom
Objects. If you need to define a new [Custom Object](https://compass.coupa.com/x294250.xml), use
the UI.

The URL to access the Custom Objects API is:
`https:///api/custom_objects/{object_id}`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/custom_objects/{object_id}/object_instances/` | create | Create a new data record for the Custom Object |
| PUT | `/api/custom_objects/{object_id}/object_instances/{instance_id}` | update | Modify an existing data record |
| GET | `/api/custom_objects/{object_id}/object_instances/` | index | Lists all of the data records for the Custom Object |
| GET | `/api/custom_objects/{object_id}/object_instances/{instance_id}` | show | Lists an individual data record |

## Elements (Object Instance)

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| created-by | User who created | | | any | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| custom-object-code | Custom object code | | | any | | yes | string |
| custom-object-name | Custom object name | | | any | | yes | string |
| form-response-id | ID of form response that created the instance | | | any | | yes | integer |
| id | Coupa Internal ID | | | any | | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| updated-by | User who updated | | | any | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Elements are only used for GET calls. POST or PUT calls will only include the custom
fields used in your custom object definition. See the below sample for details.

## Sample Payloads

Since a Custom Object is made entirely of custom fields, you need to contain your custom
fields in the `custom-field` namespace. A basic POST or PUT should take this
form:

```text
<object-instance>
<custom-fields>
<custom-field-1>custom-field-1-value</custom-field-1>
<custom-field-2>custom-field-2-value</custom-field-2>
...
<custom-field-10>custom-field-10-value</custom-field-10>
<custom-fields>
</object-instance>
```
