---
title: "Projects API (/projects)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/projects-api-(projects)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/projects-api-(projects)"
status_code: 200
fetched_at: "2026-04-09T11:59:15+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Projects API (/projects)"
---

# Projects API (/projects)

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/projects` | create | Create a Project |
| GET | `/api/projects` | index | Show all of the Projects |
| GET | `/api/projects/:id` | show | Show a specific Project |
| PUT | `/api/projects/:id` | update | Update an existing Project |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| additional-negotiated-savings | Additional Negotiated Savings | | | | yes | yes | decimal(32,4) |
| additional-planned-savings | Additional Planned Savings | | | | yes | yes | decimal(32,4) |
| additional-realized-savings | Additional Realized Savings | | | | yes | yes | decimal(32,4) |
| active | Active | | | | yes | yes | boolean |
| commodity | Commodity | | | | yes | yes | [Commodity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)) |
| commodity-id | Unique identifier for a commodity which is non editable | | | | | yes | integer |
| completion-percentage | Completion Percentage | | | | | yes | integer |
| content-groups | Content groups | | | | yes | yes | [Business Group](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)) |
| copy-project-id | copy_project_id | | | | | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | Description | | | | yes | yes | text |
| display-date-range-warning | Provide a warning if task dates fall outside of project dates | | | | yes | yes | boolean |
| enabled-tabs | Project has list of tabs enabled for linked objects | | | | yes | yes | text |
| end-date | End date | | | | yes | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| mention-name | Mention name | | yes | | | yes | string(255) |
| name | Name | yes | yes | | yes | yes | string(255) |
| open | Project is open for everyone to join or owner must invite others | | | | yes | yes | boolean |
| project-id | Unique identifier for a project which is non editable | | | | | yes | integer |
| start-date | Start date | | | | yes | yes | datetime |
| status | Project status | | | | | yes | string(25) |
| template-group | Project Template | | | | yes | yes | Template Group |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| users | Users | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| external-reference-number | User to sync up a 3rd party Project ID with Coupa | | | | yes | yes | string(255) |
| show-sourcing-rollup-fields | Show sourcing rollup field if the flag is enabled | | | | yes | yes | boolean |
| allow-users-to-view-member | This will determine who can and cannot see the members tab | | | anyone_with_access_to_this_project, project_owners_only | yes | yes | string |
| category | The category associated with the project | | | | yes | yes | Category |
| category-plan | Category Plan | yes | | | yes | yes | CategoryPlan |
| department | The department associated with the project | | | | yes | yes | Category |
| taggings | Tags associated with the project | | | | yes | yes | Tags |
| show_contracts_rollup_fields | Show contracts rollup field if the flag is enabled | | | | yes | yes | boolean |
| show_suppliers_rollup_fields | Show suppliers rollup field if the flag is enabled | | | | yes | yes | boolean |
