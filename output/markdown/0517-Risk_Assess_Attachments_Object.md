---
title: "Risk Assess Attachments Object"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-attachments-object"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations/risk-assess-attachments-object"
status_code: 200
fetched_at: "2026-04-09T12:01:04+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess REST API"
  - "GET Evaluations"
  - "Risk Assess Attachments Object"
---

# Risk Assess Attachments Object

Contains the files attached by evaluators or approvers at the overall evaluation level. Does not contain attachments added at lower levels, such as organization, category, or KPI.

## Associations

Access the Attachments object through the Evaluations API. For more information, see [Risk Assess Evaluations API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations).

## Elements

The following elements are available for the Attachments object:

| **Element** | **Data Type** | **Description** |
| --- | --- | --- |
| entityId | string | The unique entity ID of the attachment in CRA |
| fileName | string | The name of the file as uploaded by the user |
| links | Array of objects | Contains HATEOAS-style links, which facilitate navigation to specific APIs. Only currently populated for supplier-related objects, for example, a riskableObject that pertains to a supplier. For other APIs, the value is null. |
