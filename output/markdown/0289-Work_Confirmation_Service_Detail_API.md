---
title: "Work Confirmation Service Detail API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-service-detail-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-service-detail-api"
status_code: 200
fetched_at: "2026-04-09T12:00:06+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Work Confirmation Header API"
  - "Work Confirmation Service Detail API"
---

# Work Confirmation Service Detail API

Information about service sheet details.

## Associations

This API resource is available through the [Work Confirmation Header](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api) API.

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency | yes | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| description | Detailed description of work being submitted | yes | | | | yes | string(250) |
| id | Coupa’s Internal ID | | | | | yes | integer |
| notes | Notes from the supplier related to the work submitted | | | | | yes | text |
| price | Price | | | | | yes | decimal(30,6) |
| quantity | Quantity | | | | | yes | decimal(30,6) |
| rate-card | Rate specified in the service sheet detail line | | | | | yes | WorkConfirmation::ServiceDetail |
| timesheet | Time sheet | | | | | yes | [WorkConfirmation::Timesheet](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-timesheet-api) |
| total | Total amount as per the order currency.<br>By default, this field contains full precision values. To use rounded values, reach out to customer support. | | | | | yes | decimal(30,6) |
| uom | Unit of Measure | | | | | yes | [Uom](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/unit-of-measure-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| worker-assignments | Worker assignment specified in the detail line | | | | | yes | [WorkConfirmation::WorkerAssignment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-worker-assignment-api) |
