---
title: "Lookup Values API (/lookup_values)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/lookup-values-api-(lookup_values)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/lookup-values-api-(lookup_values)"
status_code: 200
fetched_at: "2026-04-09T11:59:15+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Lookup Values API (/lookup_values)"
---

# Lookup Values API (/lookup_values)

Use the lookup values API to create a hierarchy of accounts.

The URL to access lookup
values is: `https:///api/lookup_values`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Lookup Values API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/lookup_values` | create | Create lookup value |
| GET | `/api/lookup_values` | index | Query lookup values |
| GET | `/api/lookup_values/:id` | show | Show lookup value |
| PUT | `/api/lookup_values/:id` | update | Update lookup value |

## Elements

The following elements are available for the Lookup Values
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account-type | account_type | | | | yes | yes | [AccountType](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| active | A false value will inactivate the account making it no longer available to users. A true value will make it active and available to users. | | | | yes | yes | boolean |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| depth | depth | | | | | yes | integer |
| description | Description of the lookup value | | | | yes | yes | string |
| external-ref-code | Used for Identification of individual Lookup Value when using Hierarchical Lookups. This field is a concatenation of the External Ref Num fields starting with the root LookupValue. It does not get set by the integration, but is used to identify an existing lookup to update. | | yes | | | yes | string |
| external-ref-num | External Ref Num (actual account value when used in accounting) | | yes | | yes | yes | string |
| id | Coupa unique identifier | | | | | yes | integer |
| is-default | is_default | | | | yes | yes | boolean |
| lookup | Name of the lookup | yes | | | yes | yes | Lookup |
| lookup-id | lookup_id | | | | yes | yes | integer |
| name | Name of the lookup value | yes | yes | | yes | yes | string |
| parent | External Ref Code of Parent element | | | | yes | yes | LookupValue |
| parent-id | parent_id | | | | yes | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- When dealing with large data sets of Lookup Values, always limit your GET with some
criteria.

- The lookups for which you are creating these lookup values should already exist in the
system.

- [Lookup Values API Example Calls](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/lookup-values-api-(lookup_values)/lookup-values-api-example-calls)
