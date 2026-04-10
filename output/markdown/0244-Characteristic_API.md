---
title: "Characteristic API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api/characteristic-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api/characteristic-api"
status_code: 200
fetched_at: "2026-04-09T11:59:56+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Quality Collaboration API"
  - "Characteristic API"
---

# Characteristic API

Access characteristic data when working with the Quality Collaboration API.

## Associations

This resource is associated with the Quality Collaboration API. For more information, see [Quality Collaboration API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | ID of the characteristic. | | | | no | yes | integer |
| lineNum | Line number. | | | | no | yes | integer |
| inspectionId | Inspection ID. | | | | no | yes | integer |
| name | Name of the characteristic. | | | | yes | yes | string |
| type | Type of characteristic. | | | - required<br>- optional | yes | yes | string |
| isQuantitative | Whether the characteristic is quantitative. | | | | yes | yes | boolean |
| remarks | Remarks associated with the characteristic. | | | | no | yes | string |
| specification | Specification of the characteristic. | | | | no | yes | string |
| requirement | Requirement for the characteristic. | | | | yes | no | string |
| valueType | Type of value. | | | -<br>none<br>-<br>numeric<br>-<br>decision<br>-<br>choice | yes | yes | string |
| recordingType | Recording type. | | | summarized | yes | yes | string |
| characteristicValues | Details about the characteristic value. | | | | yes | yes | [CharacteristicValue](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api/characteristic-value-api) |
| expectedResults | Details about the expected results. | | | | yes | yes | [ExpectedResult](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api/expected-result-api) |
| expectedLimits | Details about the expected limits. | | | | yes | yes | [ExpectedLimit](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api/expected-limit-api) |
| recordedCharacteristic | Details about the recorded characteristic. | | | | no | yes | [RecordedCharacteristic](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/quality-collaboration-api/recorded-characteristic-api) |
