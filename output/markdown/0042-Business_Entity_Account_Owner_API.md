---
title: "Business Entity Account Owner API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)/business-entity-account-owner-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)/business-entity-account-owner-api"
status_code: 200
fetched_at: "2026-04-09T11:59:10+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Business Entities API (/business_entities)"
  - "Business Entity Account Owner API"
---

# Business Entity Account Owner API

## Association

This resource is associated with the [Business Entitites API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | User ID | true | true | any | yes | yes | integer |
| id | Coupa unique identifier | false | false | any | yes | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| email | Email | false | false | any | yes | yes | |
| fullname | Full Name | false | false | any | yes | yes | |
| purposes | Purposes | false | false | any | yes | yes | [] |
| created_by | User who created | false | false | any | yes | yes | |
| updated_by | User who updated | false | false | any | yes | yes | |
