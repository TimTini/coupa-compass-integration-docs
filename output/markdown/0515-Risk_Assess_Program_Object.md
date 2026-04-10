---
title: "Risk Assess Program Object"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-program-object"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-program-object"
status_code: 200
fetched_at: "2026-04-09T12:01:04+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess REST API"
  - "GET Evaluations"
  - "Risk Assess Program Object"
---

# Risk Assess Program Object

The Program object contains evaluation program data related to an evaluation. The Program object contails framework, regulations, scoring setup, and timeline for the evaluation process.

## Associations

Access the Program object through the Evaluations API. For more information, see [Risk Assess Evaluations API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations).

## Elements

The following elements are available for the Program object:

| **Element** | **Data Type** | **Description** |
| --- | --- | --- |
| entityId | string | Unique identifier for the program in CRA. |
| name | string | Designation of the program. |
| status | string | Current status of the program within CRA. |
| links | Array of objects | Contains HATEOAS-style links, which facilitate navigation to specific APIs. Only currently populated for supplier-related objects, for example, a riskableObject that pertains to a supplier. For other APIs, the value is null. |
