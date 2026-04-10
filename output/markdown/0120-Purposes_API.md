---
title: "Purposes API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/purposes-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/purposes-api"
status_code: 200
fetched_at: "2026-04-09T11:59:29+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Purposes API"
---

# Purposes API

Use the purposes API to query, create, or update personal or supplier remit-to address
information.

## Associations

This API is associated with [Address API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757),
[Contact API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/supplier-information-contact-api) and [Suppliers API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797).

Use the purposes API to query, create, or update the
purpose of supplier contact information.

## Elements

The following elements are available for the Purposes API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa's unique identifier for the address | | | | | yes | integer |
| kind | | yes | | | yes | yes | string(255) |
| name | Address 'Nickname' | yes | | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
