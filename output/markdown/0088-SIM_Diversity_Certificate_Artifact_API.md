---
title: "SIM Diversity Certificate Artifact API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/sim-diversity-certificate-artifact-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/sim-diversity-certificate-artifact-api"
status_code: 200
fetched_at: "2026-04-09T11:59:21+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Supplier Information API (/supplier_information)"
  - "SIM Diversity Certificate Artifact API"
---

# SIM Diversity Certificate Artifact API

## Associations

This API resource is associated with the [Supplier Information API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)-da-5810-da-5810).

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| effective-date | Attachment Effective Date | | | | yes | yes | datetime |
| expiry-date | Attachment Expiration Date | | | | yes | yes | datetime |
| description | Description | | | | yes | yes | string(255) |
| agency-id | Agency ID | | | | yes | yes | integer |
| id | Artifact/Attachment ID | | | | yes | yes | integer |
| created-at | Created Date and Time | | | | yes | yes | datetime |
| updated-at | Last Updated Date and Time | | | | yes | yes | datetime |
| agency | Agency | | | | yes | yes | |
| created-by | User who created | | | | yes | yes | |
| updated-by | User who last updated | | | | yes | yes | |
