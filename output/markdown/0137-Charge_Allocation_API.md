---
title: "Charge Allocation API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/charges-api-(charges)/charge-allocation-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/charges-api-(charges)/charge-allocation-api"
status_code: 200
fetched_at: "2026-04-09T11:59:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Charges API (/charges)"
  - "Charge Allocation API"
---

# Charge Allocation API

## Overview

Coupa Pay Virtual card charges can use charge allocation to
apportion charges and percentages of a charge to different
accounts. When you have the Coupa Pay Virtual Card entitlement, you
can GET a charge or charges with charge allocation data from
the Charge API
endpoint: `https://{your_instance_name}/api/charges` or
you can see the OpenAPI docs
here: `https://{your_instance_name}/api_docs/14`

## Elements

| **Field Name** | **Field Description** | **Required Field?** | **Unique** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account | account | yes | | | | yes | [Account](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)) |
| amount | dollar amount for this allocation | | | | | yes | decimal(30,2) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [**User**](https://compass.coupa.com/x285915.xml) |
| currency | Currency | yes | | | | yes | [**Currency**](https://compass.coupa.com/x285819.xml) |
| id | Coupa unique identifier | | | | | yes | integer |
| pct | percent | yes | | | | yes | decimal(16,10) |
| period | budget period | | | | | yes | [Period](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [**User**](https://compass.coupa.com/x285915.xml) |
