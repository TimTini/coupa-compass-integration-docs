---
title: "User UDF Imports"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/user-udf-imports"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/user-udf-imports"
status_code: 200
fetched_at: "2026-04-09T12:01:01+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess Quick Integration File Formats"
  - "User UDF Imports"
---

# User UDF Imports

## User UDF Imports

| **Field** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| EmailAddress | [* required] - Hiperos username associated with the user for which the UDF value is populated | yes | | String(256) | Uses regular expressions:<br>Default: ^[\w.+'-]+@[\w\.-]+\.(\w{2,7})$ Used when http context doen't exist<br>Filtering on top level domains: ^[\w.+'-]+@[\w\.-]+\.(TOPLEVELDOMAINLIST)$ Used for a logged in user<br>*Note: regex can be chaned per client via a localization change request.<br>AND Can't contain ..<br>AND Can't contain .@<br>AND Can't contain whitespace |
| <UDF fieldname> | fieldname of the UDF in CRA system | | | | |
