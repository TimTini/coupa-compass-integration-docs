---
title: "Rate Card API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/rate-card-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/rate-card-api"
status_code: 200
fetched_at: "2026-04-09T11:59:17+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Rate Card API"
---

# Rate Card API

Use the Rate Card API to create, update, or query rate
cards.

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Elements

The following elements are available for the Rate
Card API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | false | false | any | | yes | boolean |
| rate-card-lines | Rate card lines | false | false | any | | yes | rate card line |
| ncm | NCM | false | false | any | yes | | string(255) |
| cfop | CFOP | false | false | any | yes | | string(255) |
| id | Coupa unique identifier | false | false | any | yes | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| created-by | User who created | false | false | any | | yes | |
| updated-by | User who updated | false | false | any | | yes | |
| rateable-type | Rateable type | false | false | any | | yes | string(255) |
