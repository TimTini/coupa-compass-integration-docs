---
title: "Business Entity Address API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)/business-entity-address-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)/business-entity-address-api"
status_code: 200
fetched_at: "2026-04-09T11:59:11+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Business Entities API (/business_entities)"
  - "Business Entity Address API"
---

# Business Entity Address API

## Association

This resource is associated with the [Business Entitites API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| name | Address 'Nickname' | false | false | any | yes | yes | string(255) |
| location_code | location_code | false | true | any | yes | yes | string(255) |
| street1 | Address Line 1 | true | false | any | yes | yes | string(255) |
| street2 | Address Line 2 | false | false | any | yes | yes | string(255) |
| street3 | Address Line 3 | false | false | any | yes | yes | string(255) |
| street4 | Address Line 4 | false | false | any | yes | yes | string(255) |
| city | City Name | true | false | any | yes | yes | string(255) |
| state | State Abbreviation | false | false | any | yes | yes | string(255) |
| postal_code | Postal Code | true | false | any | yes | yes | string(255) |
| attention | Address Default Attention Line | false | false | any | yes | yes | string(255) |
| active | A no value will make the address inactive making it no longer available to users. A yes value will make it active and available to users. | false | false | any | yes | yes | boolean |
| business_group_name | Content Group Name for Address | false | false | any | yes | yes | string |
| vat_number | VAT identification number used for value added tax purposes | false | false | any | yes | yes | string(255) |
| local_tax_number | Local Tax Number | true | false | any | yes | yes | string(255) |
| vat_country | VAT Country | false | false | any | yes | yes | |
| country | country | true | false | any | yes | yes | |
| content_groups | Content Groups | false | false | any | yes | yes | [] |
| purposes | Purposes | false | false | any | yes | yes | [] |
| id | Coupa Internal Address ID | false | false | any | yes | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| tax_registrations | Tax Registrations | false | false | any | yes | yes | [] |
| created_by | User who created | false | false | any | yes | yes | |
| updated_by | User who updated | false | false | any | yes | yes | |
| type | Address type | false | false | any | | yes | string(255) |
| state-iso-code | ISO Code for the State | false | false | any | yes | yes | string(255) |
| external-src-name | External Source Name | false | false | any | yes | | string(255) |
| external-src-ref | External Source Reference | false | false | any | yes | | string(255) |
