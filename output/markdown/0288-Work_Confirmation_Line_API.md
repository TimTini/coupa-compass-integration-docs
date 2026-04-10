---
title: "Work Confirmation Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-line-api"
status_code: 200
fetched_at: "2026-04-09T12:00:05+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Work Confirmation Header API"
  - "Work Confirmation Line API"
---

# Work Confirmation Line API

Information about service sheet lines.

## Associations

This API resource is available through the [Work Confirmation Header](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api) API.

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| attachments | Attachments | | | | | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency | | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| custom-fields | Custom fields | | | | | yes | Custom fields |
| delivered-at | Date work was completed | | | | | yes | datetime |
| description | Service Sheet Line description | | | | | yes | string(255) |
| id | Coupa’s Internal ID | | | | | yes | integer |
| ontime-status | Captures whether the work submitted is on-time or late | | | | | yes | |
| order-line-id | Coupa’s Internal Purchase Order Line ID | | | | | yes | integer |
| position | Position | | | | | yes | integer |
| price | Price | | | | | yes | decimal(30,6) |
| quantity | Quantity | | | | | yes | decimal(30,6) |
| rate-card | Rate card | | | | | yes | WorkConfirmation::Line |
| service-details | Service details | | | | | yes | [WorkConfirmation::ServiceDetail](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-service-detail-api) |
| service-end-date | Service end date | | | | | yes | |
| service-start-date | Service start date | | | | | yes | |
| service-type | Purchase Order Line Type (amount_deliverable, quantity_deliverable or resource) | | | | | yes | |
| timesheet | Time sheet | | | | | yes | [WorkConfirmation::Timesheet](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-timesheet-api) |
| total | Total amount as per the order currency.<br>By default, this field contains full precision values. To use rounded values, reach out to customer support. | | | | | yes | decimal(30,6) |
| type | Type | | | | | yes | string(255) |
| uom | Unit of Measure | | | | | yes | Uom |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
