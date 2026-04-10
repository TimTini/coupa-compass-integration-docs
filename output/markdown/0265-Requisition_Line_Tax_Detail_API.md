---
title: "Requisition Line Tax Detail API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/requisition-line-tax-detail-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/requisitions-api-(requisitions)/requisition-line-tax-detail-api"
status_code: 200
fetched_at: "2026-04-09T12:00:00+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Requisitions API (/requisitions)"
  - "Requisition Line Tax Detail API"
---

# Requisition Line Tax Detail API

## Associations

This API is associated with the [Requisitions API](https://compass.coupa.com/x286199.xml).

## Elements

The following elements are available for the Requisition Line
Tax Detail API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cfop | Cfop | | | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| ncm | Ncm | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
