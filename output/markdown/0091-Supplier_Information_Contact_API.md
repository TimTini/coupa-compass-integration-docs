---
title: "Supplier Information Contact API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/supplier-information-contact-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/supplier-information-contact-api"
status_code: 200
fetched_at: "2026-04-09T11:59:23+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Supplier Information API (/supplier_information)"
  - "Supplier Information Contact API"
---

# Supplier Information Contact API

## Associations

This API resource is associated with the [Supplier Information API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)-da-5810-da-5810).

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Created Date and Time | | | | | yes | datetime |
| created-by | Created by User | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| email | Email Address | | | | yes | yes | string(255) |
| id | Contact ID | | | | | yes | integer |
| kind | Contract Kind/Type | yes | | Primary, Standard | yes | yes | string(255) |
| name-additional | Name Additional | | | | yes | yes | string(255) |
| name-family | Last Name/Family Name | | | | yes | yes | string(255) |
| name-fullname | Full Name | | | | yes | yes | string(255) |
| name-given | Given/First Name | | | | yes | yes | string(255) |
| name-prefix | Name Prefix | | | | yes | yes | string(255) |
| name-suffix | Name Suffix | | | | yes | yes | string(255) |
| notes | Contact Notes | | | | yes | yes | string(255) |
| phone-fax | Fax | | | | yes | yes | Phone Number |
| phone-mobile | Mobile Phone Number | | | | yes | yes | Phone Number |
| phone-work | Work Phone Number | | | | yes | yes | Phone Number |
| purposes | | no | yes | any | | | array |
| supplier-information-id | Supplier information | | | | | yes | integer |
| updated-at | Last Updated Date and Time | | | | | yes | datetime |
| updated-by | Last Updated by User | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
