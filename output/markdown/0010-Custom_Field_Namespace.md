---
title: "Custom Field Namespace"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/custom-field-namespace"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/custom-field-namespace"
status_code: 200
fetched_at: "2026-04-09T11:59:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Get Started with the API"
  - "Custom Field Namespace"
---

# Custom Field Namespace

Custom-fields are added to a `` namespace to avoid name conflicts and to make customer-added fields more easily identifiable.

Newly-created custom fields don't have the **API Global Namespace** option. They're in the new custom field namespace by default. If you disable the global namespace option for existing custom fields, they'll be placed in the custom field namespace, the checkbox will disappear, and you won't be able to add them back to the global namespace.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Expense category custom fields and attendee-type custom fields do not yet support being added to the custom fields namespace.

## API example using XML

For the API, new custom fields are wrapped in a parent `` attribute.

```text
<custom-fields>
<custom-field-1>Name of first custom field</custom-field-1>
<custom-field-2>Name of second custom field</custom-field-2>
</custom-fields>
```

## API example using JSON

For the API, new custom fields are contained in a parent `custom-fields` attribute.

```text
{
"custom-fields": {
"custom-field-1": "Name of first custom field",
"custom-field-2": "Name of second custom field"
}
}
```
