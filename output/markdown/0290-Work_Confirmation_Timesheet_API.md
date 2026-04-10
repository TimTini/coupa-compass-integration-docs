---
title: "Work Confirmation Timesheet API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-timesheet-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api/work-confirmation-timesheet-api"
status_code: 200
fetched_at: "2026-04-09T12:00:06+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Work Confirmation Header API"
  - "Work Confirmation Timesheet API"
---

# Work Confirmation Timesheet API

Information about service sheet timesheets.

## Associations

This API resource is available through the [Work Confirmation Header](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/work-confirmation-header-api) API.

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| day-1 | Day 1 time sheet entry | | | | | yes | decimal(30,6) |
| day-2 | Day 2 time sheet entry | | | | | yes | decimal(30,6) |
| day-3 | Day 3 time sheet entry | | | | | yes | decimal(30,6) |
| day-4 | Day 4 time sheet entry | | | | | yes | decimal(30,6) |
| day-5 | Day 5 time sheet entry | | | | | yes | decimal(30,6) |
| day-6 | Day 6 time sheet entry | | | | | yes | decimal(30,6) |
| day-7 | Day 7 time sheet entry | | | | | yes | decimal(30,6) |
| id | Internal ID of the time sheet record | | | | | yes | integer |
| start-date | Calendar date of first entry on this time sheet | | | | | yes | date |
| type | Type of time sheet | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
