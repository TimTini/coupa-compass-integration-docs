---
title: "Setup Data"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/setup-data"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/setup-data"
status_code: 200
fetched_at: "2026-04-09T12:01:01+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess Quick Integration File Formats"
  - "Setup Data"
---

# Setup Data

## Setup Data

| **Field** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| TypeCode (*) | Must match an existing code under Setup Data Management. | yes | | String(64) | any |
| DataCode (*) | Enter the data code. | yes | | String(256) | any |
| DisplayName (*) | Enter the display name presented to the user. | yes | | String(256) | any |
| Culture | Enter the language of the setup data. | | | | |
| ParentCode | Must match an existing parent code under Setup Data Management. | | | String(256) | any |
| OrderNumber | Enter the row order number. This is the place where the new setup data displays. | | | Integer | |
| Description | Enter a short description of the setup data. | | | String(256) | |
| Activated (*) | Enter Yes to activate the organization. | yes | | Boolean | Yes/No |
| ActivateDate | Enter the date the setup data is active. | | | DateTime | any |
| ScoreValue | Enter the score value of the setup data element. | | | Decimal(10,2) | any |

(*)Required
