---
title: "Risk Assess Organizations Object"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-organizations-object"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-organizations-object"
status_code: 200
fetched_at: "2026-04-09T12:01:04+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess REST API"
  - "GET Evaluations"
  - "Risk Assess Organizations Object"
---

# Risk Assess Organizations Object

Represents Organization Score Accumulators linked to the evaluation process. Accumulators compile the scores of Key Performance Indicators at the organizational level. The Object contains score accumulator records rather than the organizations themselves.

## Associations

Access the Organizations object through the Evaluations API. For more information, see [Risk Assess Evaluations API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations).

## Elements

The following elements are available for the Organizations object:

| **Element** | **Data Type** | **Description** |
| --- | --- | --- |
| entityId | string | Unique entity ID of the organization score accumulator in CRA |
| name | string | Name of the organization score accumulator |
| links | Array of objects | Contains HATEOAS-style links, which facilitate navigation to specific APIs. Only currently populated for supplier-related objects, for example, a riskableObject that pertains to a supplier. For other APIs, the value is null. |
