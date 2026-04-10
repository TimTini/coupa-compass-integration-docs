---
title: "Integration Record Response API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-record-response-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-record-response-api"
status_code: 200
fetched_at: "2026-04-09T11:59:48+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Integrations API (/integrations)"
  - "Integration Record Response API"
---

# Integration Record Response API

## Association

This resource is associated with [Integration History Record API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-history-record-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| response-code | response_code | | | | yes | yes | string(255) |
| response-message | response_message | | | | yes | yes | text |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
