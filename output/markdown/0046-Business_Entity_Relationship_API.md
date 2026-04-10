---
title: "Business Entity Relationship API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)/business-entity-relationship-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)/business-entity-relationship-api"
status_code: 200
fetched_at: "2026-04-09T11:59:11+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Business Entities API (/business_entities)"
  - "Business Entity Relationship API"
---

# Business Entity Relationship API

## Association

This resource is associated with the [Business Entitites API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| business_entity_id | Business Entity ID | false | false | any | yes | yes | integer |
| related_business_entity_id | Related Business Entity ID | false | true | any | yes | yes | integer |
| relationship_type | Relationship Type | true | false | parent_child | yes | yes | string(255) |
| status | Status | false | false | any | yes | yes | string(255) |
| id | Coupa unique identifier | false | false | any | yes | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | any | yes | yes | datetime |
| created_by | User who created | false | false | any | yes | yes | |
| updated_by | User who updated | false | false | any | yes | yes | |
