---
title: "Supplier Information Artifact API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/supplier-information-artifact-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/supplier-information-artifact-api"
status_code: 200
fetched_at: "2026-04-09T11:59:21+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Supplier Information API (/supplier_information)"
  - "Supplier Information Artifact API"
---

# Supplier Information Artifact API

## Associations

This API resource is associated with the [Supplier Information API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)-da-5810-da-5810).

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| agency | Agency that issued the supplier's diversity certificate | | | | | yes | |
| artifact-meta-type | Artifact/Attachment Sub-Type | | | | yes | yes | string(255) |
| artifact-type | Artifact/Attachment Type | | | | yes | yes | string(255) |
| attachments | Attachment | | | | | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| created-at | Created Date and Time | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | Description | | | | yes | yes | string(255) |
| effective-date | Attachment Effective Date | | | | yes | yes | datetime |
| expiry-date | Attachment Expiration Date | | | | yes | yes | datetime |
| id | Artifact/Attachment ID | | | | | yes | integer |
| supplier-id | Supplier ID | | | | yes | yes | string(255) |
| supplier-information-id | SIM ID | | | | | yes | integer |
| type | Type | | | | yes | yes | string(255) |
| updated-at | Last Updated Date and Time | | | | | yes | datetime |
| updated-by | User who last updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
