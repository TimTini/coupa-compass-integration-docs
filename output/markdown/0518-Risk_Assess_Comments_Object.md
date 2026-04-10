---
title: "Risk Assess Comments Object"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-comments-object"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-comments-object"
status_code: 200
fetched_at: "2026-04-09T12:01:04+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess REST API"
  - "GET Evaluations"
  - "Risk Assess Comments Object"
---

# Risk Assess Comments Object

Contains comments provided by evaluators or approvers at the overall evaluation level. This object does not contain comments made at lower levels, such as organization, category, or KPI.

## Associations

Access the Comments object through the Evaluations API. For more information, see [Risk Assess Evaluations API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations).

## Elements

The following elements are available for the Comments object:

| **Element** | **Data Type** | **Description** |
| --- | --- | --- |
| entityId | string | Unique entity ID of the evaluation-level comment in CRA |
| comment | string | The content of the comment |
| links | Array of objects | Contains HATEOAS-style links, which facilitate navigation to specific APIs. Only currently populated for supplier-related objects, for example, a riskableObject that pertains to a supplier. For other APIs, the value is null. |
