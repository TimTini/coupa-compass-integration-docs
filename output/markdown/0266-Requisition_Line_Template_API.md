---
title: "Requisition Line Template API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/requisition-line-template-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/requisition-line-template-api"
status_code: 200
fetched_at: "2026-04-09T12:00:00+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Requisitions API (/requisitions)"
  - "Requisition Line Template API"
---

# Requisition Line Template API

## Associations

This API is associated with the [Requisitions API](https://compass.coupa.com/x286199.xml).

## Elements

The following elements are available for the Requisition Line
Template API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | | | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| name | RequisitionLineTemplate name | yes | yes | | | yes | string(100) |
| created_by | User who created | | | | | yes | |
| updated_by | User who updated | | | | | yes | |
