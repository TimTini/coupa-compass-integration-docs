---
title: "Customer Support Contact API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/customer-support-contact-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/customer-support-contact-api"
status_code: 200
fetched_at: "2026-04-09T11:59:19+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
  - "Customer Support Contact API"
---

# Customer Support Contact API

## Association

This resource is associated with the [Suppliers API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | | true | true | any | yes | yes | integer |
| active | | false | false | any | yes | yes | boolean |
| purposes | | false | false | any | yes | yes | [] |
| id | Coupa unique identifier | false | false | any | yes | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| email | | false | false | any | yes | yes | |
| fullname | | false | false | any | yes | yes | |
| created_by | User who created | false | false | any | yes | yes | |
| updated_by | User who updated | false | false | any | yes | yes | |
| user | User | false | false | any | | yes | |
