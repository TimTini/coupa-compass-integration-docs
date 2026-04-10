---
title: "GET Suppliers"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-suppliers"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-suppliers"
status_code: 200
fetched_at: "2026-04-09T12:01:04+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess REST API"
  - "GET Suppliers"
---

# GET Suppliers

Retrieve a list of suppliers belonging to the tenant.

## Endpoint

| **Endpoint** | `/api/suppliers` |
| --- | --- |
| **Method** | GET |

## Headers

| **Header** | **Argument** |
| --- | --- |
| Authorization | Bearer token |
| Accept | application/json or application/xml |

## Parameters

| **Paremeter** | **Description** |
| --- | --- |
| limit | (Optional) Maximum number of items in the response. Maximum: 50. |
| offset | (Optional) Number of items to skip from the start. Default: 0. |
| status | (Optional) Supplier status. For example: Active, Inactive. |
| sourceSystem | (Optional) Filter by source system. |

## Get suppliers

Endpoint

GET `/api/suppliers`

Example cURL request

```text
curl --location 'https://<your-instance>.risk.com/api/suppliers' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••'
```

Example response

```text
{
"result": {
"totalCount": 1,
"suppliers": [
{
"entityId": "8df17abd-1ce4-47dd-96a9-03c310ddd230",
"name": "Auto_BulkUpload_BE_05032023234658_T2",
"supplierNumber": "392",
"status": "General_Active",
"createdAt": "2023-08-29T17:36:04.303Z",
"modifiedAt": "2023-08-29T18:17:07.363Z",
"sourceId": null,
"sourceObjectType": null,
"sourceSystem": null
}
]
},
"errors": [],
"success": true
}
```

- [GET Supplier Extension Fields](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-suppliers/get-supplier-extension-fields)

Retrieves all extension field records for a specific supplier using the CRA Entity ID.
