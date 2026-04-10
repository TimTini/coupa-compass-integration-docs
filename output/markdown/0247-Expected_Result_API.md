---
title: "Expected Result API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api/expected-result-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api/expected-result-api"
status_code: 200
fetched_at: "2026-04-09T11:59:56+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Quality Collaboration API"
  - "Expected Result API"
---

# Expected Result API

Access expected result data when working with the Quality Collaboration API.

## Associations

This resource is associated with the Quality Collaboration API. For more information, see [Quality Collaboration API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Limit ID. | | | | no | yes | integer |
| characteristicId | Characteristic ID. | | | | no | yes | integer |
| targetValue | Target value. | | | | yes | no | integer |
| numericValue | Numeric value. | | | | no | yes | integer |
| valuePrecision | Value precision. | | | | yes | yes | integer |
| qualitativeValue | Qualitative value. | | | | yes | yes | string |
