---
title: "Address API (/addresses)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757"
status_code: 200
fetched_at: "2026-04-09T11:59:09+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Address API (/addresses)"
---

# Address API (/addresses)

Use the address API to query, create, or update personal or supplier remit-to address information.

The URL to access addresses is: `https:///api/addresses`

- Use this URL to query personal address information:

```text
https://<instance url>/api/users/<user ID>/addresses
```

- Use this URL to query supplier remit-to address information:

```text
https://<instance url>/api/suppliers/<user ID>/addresses
```

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Addresses API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/addresses` | create | Create address |
| GET | `/api/addresses` | index | Query addresses |
| GET | `/api/addresses/:id` | show | Show address |
| PUT | `/api/addresses/:id` | update | Update address |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: When you call `\`GET /api/users//addresses\``, the system returns only personal addresses associated with that user. Use the `\`address-type\`` field in the response to distinguish personal addresses from company or remit-to addresses returned by other address endpoints.

## Elements

The following elements are available for the Addresses API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | A no value will make the address inactive making it no longer available to users. A yes value will make it active and available to users. | | | | yes | yes | boolean |
| attention | Address Default Attention Line | | | | yes | yes | string(255) |
| business-group-name | Content Group Name for Address | | | | yes | yes | string(255) |
| city | City Name | yes | | | yes | yes | string(255) |
| content-groups | Content groups. | | | | yes | yes | [ContentGroup](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)) |
| country | country | yes | | | yes | yes | Country |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa's unique identifier for the address | | | | | yes | integer |
| local-tax-number | local_tax_number | yes | | | yes | yes | string(255) |
| location-code | location_code | | yes | | yes | yes | string(255) |
| name | Address 'Nickname' | | | | yes | yes | string(255) |
| postal-code | Postal Code | yes | | | yes | yes | string(255) |
| purposes | Purposes for Multiple Contacts and Addresses for Suppliers | | | | yes | yes | Purpose |
| state | State Abbreviation | | | See note below this table to download a list of allowable values. | yes | yes | string(255) |
| state-iso-code | ISO Code for the State<br>Note<br>In 36.1, the allowable syntax for field values changed to the format: `CC-SSS`, where `CC` represents the two-character country code and `SSS` represents the one-to-three-character alpha-numeric subdivision code. For example, **US-CA**. See note below this table to download a list of allowable values. | | | See note below this table to download a list of allowable values. | yes | yes | string(255) |
| street1 | Address Line 1 | yes | | | yes | yes | |
| street2 | Address Line 2 | | | | yes | yes | string(255) |
| street3 | Address Line 3 | | | | yes | yes | string(255) |
| street4 | Address Line 4 | | | | yes | yes | string(255) |
| tax-registrations | Tax registrations | | | | | yes | [Tax Registration](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| vat-country | vat_country | | | | yes | yes | Country |
| vat-number | vat_number | | | | yes | yes | string(255) |
| external-src-ref | External Source Reference | | | | yes | | string(255) |
| external-src-name | External Source Name | | | | yes | | string(255) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- Starting with the May 2023 release, state ISO codes and names have changed. To see a complete list of the changes and allowable values, download the [Subdivision Code Changes Excel file](https://compass.coupa.com/a/105722).

- The reference object Country and the respective country name, code or ID must already exist in the system.

- If the address is deactivated or inactive, the address record and its attributes cannot be updated using the API.
