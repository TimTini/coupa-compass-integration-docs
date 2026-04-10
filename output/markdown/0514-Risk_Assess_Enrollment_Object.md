---
title: "Risk Assess Enrollment Object"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-enrollment-object"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-enrollment-object"
status_code: 200
fetched_at: "2026-04-09T12:01:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess REST API"
  - "GET Evaluations"
  - "Risk Assess Enrollment Object"
---

# Risk Assess Enrollment Object

Contains details recorded when an object is enrolled for evaluation. Includes the target of evaluation (such as a supplier or engagement) and evaluation-specific configurations, including assigned evaluators, approvers, and other relevant data.

## Associations

Access the Enrollment object through the Evaluations API. For more information, see [Risk Assess Evaluations API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations).

## Elements

The following elements are available for the Enrollment object:

| **Element** | **Data Type** | **Description** |
| --- | --- | --- |
| entityId | string | Unique entity ID associated with the enrollment in CRA. |
| name | string | Designation of the enrollment. |
| links | Array of objects | Contains HATEOAS-style links, which facilitate navigation to specific APIs. Only currently populated for supplier-related objects, for example, a riskableObject that pertains to a supplier. For other APIs, the value is null. |
