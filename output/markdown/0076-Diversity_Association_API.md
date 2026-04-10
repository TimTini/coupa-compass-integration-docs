---
title: "Diversity Association API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/diversity-association-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/diversity-association-api"
status_code: 200
fetched_at: "2026-04-09T11:59:19+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
  - "Diversity Association API"
---

# Diversity Association API

## Associations

This API is associated with the [Suppliers API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797).

## Elements

The following elements are available for the Diversity
Association API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| country | Country Sub Object | | | | yes | yes | Country |
| country-id | Country | yes | | | yes | | integer |
| created-at | Created Date and Time | | | | | yes | datetime |
| diversity-category | Diversity Category Sub Object | | | | yes | yes | [Diversity Category](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/diversity-category-and-subcategory-apis) |
| diversity-category-id | Diversity category | yes | yes | | yes | | integer |
| diversity-subcategory | Diversity Subcategory Sub Object | | | | yes | yes | [DiversitySubcategory](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/diversity-category-and-subcategory-apis) |
| diversity-subcategory-id | Diversity subcategory | yes | | | yes | | integer |
| id | Diversity Association ID | | | | yes | yes | integer |
| sim-diversity-certificate-artifacts | Supplier Diversity Artifact Sub Object | | | | yes | yes | [SIM Diversity Certificate Artifact](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/sim-diversity-certificate-artifact-api) |
| updated-at | Last Updated Date and Time | | | | | yes | datetime |
