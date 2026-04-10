---
title: "Task API (/tasks)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/task-api-(tasks)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/task-api-(tasks)"
status_code: 200
fetched_at: "2026-04-09T11:59:24+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Task API (/tasks)"
---

# Task API (/tasks)

## Overview

The Task API lets you perform standard GET, PUT, POST, and DELETE actions. You can also access Tasks associated with Projects or Groups through their own endpoints: `/projects/{project_id}/tasks` and `/user_groups/{user_group_id}/tasks`
**.**

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Task API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/user_groups/:user_group_id/tasks` | create | Create group task |
| POST | `/api/projects/:project_id/tasks` | create | Create project task |
| POST | `/api/tasks` | create | Create task |
| DELETE | `/api/projects/:project_id/tasks/:id` | destroy | Delete project task |
| DELETE | `/api/tasks/:id` | destroy | Delete task |
| GET | `/api/user_groups/:user_group_id/tasks` | index | Query group task |
| GET | `/api/projects/:project_id/tasks` | index | Query project task |
| GET | `/api/tasks` | index | Query task |
| GET | `/api/user_groups/:user_group_id/tasks/:id` | show | Show a group task |
| GET | `/api/projects/:project_id/tasks/:id` | show | Show project task |
| GET | `/api/tasks/:id` | show | Show task |
| PATCH | `/api/user_groups/:user_group_id/tasks/:id` | update | Update group task |
| PUT | `/api/user_groups/:user_group_id/tasks/:id` | update | Update group task |
| PATCH | `/api/projects/:project_id/tasks/:id` | update | Update project task |
| PUT | `/api/projects/:project_id/tasks/:id` | update | Update project task |
| PATCH | `/api/tasks/:id` | update | Update task |
| PUT | `/api/tasks/:id` | update | Update task |
| POST | `/api/quote_requests/:quote_request_id/tasks` | create | Add a task to a Sourcing event. |
| DELETE | `/api/quote_requests/:quote_request_id/tasks/:id` | destroy | Deletes a task from a Sourcing event. |
| GET | `/api/quote_requests/:quote_request_id/tasks` | Index | Gets tasks associated with a Sourcing event. |
| GET | `/api/quote_requests/:quote_request_id/tasks/:id` | show | Gets details for a task associated with a Sourcing event. |
| PATCH | `/api/quote_requests/:quote_request_id/tasks/:id` | update | Updates a task associated with a Sourcing event. |
| PUT | `/api/quote_requests/:quote_request_id/tasks/:id` | update | Updates a task associated with a Sourcing event. |

## Elements

The following elements are available for the Task API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | description | | | | yes | yes | text |
| due-date | due date | | | | yes | yes | datetime |
| duration | duration | | | | yes | yes | float |
| id | Coupa unique identifier | | | | | yes | integer |
| linkable | Association to which the task is linked to. Possible values are UserGroup/Project | yes | | | | yes | Task |
| linkable-id | Id of the User group or Project that the task is linked to | | | | yes | yes | integer |
| linkable-type | linked object type.Task cn be linked to User group or a Project | | | | yes | yes | string(255) |
| owner | Owner | yes | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| owner-id | User id to whom the task is assigned | | | | yes | yes | integer |
| percentage | percentage | | | 0 to 100 | yes | yes | integer |
| quote-task-attributes | Extra attributes for the sourcing event task | | | | yes | yes | [QuoteTaskAttributes](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-task-attributes-api) |
| resolved-at | Timestamp the task was resolved in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| resolved-by | User who resolved the task | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| start-date | start date | | | | yes | yes | datetime |
| status | status of task | | | | yes | yes | string(255) |
| task-id | Unique identifier for a task which is non editable. This is auto generated. This will be used as an unique identifier to update tasks in loaders | | | | | yes | integer |
| title | title | yes | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

## Get tasks associated with a Sourcing event

Method

GET `/api/quote_requests/10163/tasks`

Example cURL request

```text
curl --location 'https://<your-instance>.com/api/quote_requests/10163/tasks' \
--header 'Accept: application/xml' \
--header 'Accept: application/json' \
--header 'Accept: application/octet-stream'
```

Example response

```text
<?xml version="1.0" encoding="UTF-8"?>
<tasks type="array">
<task>
<id type="integer">179</id>
<created-at type="dateTime">2025-04-25T13:55:52-04:00</created-at>
<updated-at type="dateTime">2025-04-25T13:55:52-04:00</updated-at>
<title>Send request for quotes </title>
<description nil="true"/>
<status>pending</status>
<owner-id nil="true"/>
<due-date nil="true"/>
<duration nil="true"/>
<percentage type="integer">0</percentage>
<linkable-id type="integer">10163</linkable-id>
<linkable-type>QuoteRequest</linkable-type>
<resolved-at nil="true"/>
<owner nil="true"/>
<resolved-by nil="true"/>
<created-by>
<id type="integer">207</id>
<login>email@company.com</login>
<employee-number nil="true"/>
</created-by>
<updated-by>
<id type="integer">207</id>
<login>email@company.com</login>
<employee-number nil="true"/>
</updated-by>
</task>
<task>
<id type="integer">180</id>
<created-at type="dateTime">2025-04-25T13:55:59-04:00</created-at>
<updated-at type="dateTime">2025-04-25T13:55:59-04:00</updated-at>
<title>Choose supplier</title>
<description nil="true"/>
<status>pending</status>
<owner-id nil="true"/>
<due-date nil="true"/>
<duration nil="true"/>
<percentage type="integer">0</percentage>
<linkable-id type="integer">10163</linkable-id>
<linkable-type>QuoteRequest</linkable-type>
<resolved-at nil="true"/>
<owner nil="true"/>
<resolved-by nil="true"/>
<created-by>
<id type="integer">207</id>
<login>email@company.com</login>
<employee-number nil="true"/>
</created-by>
<updated-by>
<id type="integer">207</id>
<login>email@company.com</login>
<employee-number nil="true"/>
</updated-by>
</task>
</tasks>
```

## Add a task to a Sourcing event

Method

POST `/api/quote_requests/10163/tasks`

Request body

```text
{
"title": "New Task for 10163",
"quote_task_attributes":{"phase": "setup"},
"percentage": 0
}
```

Example cURL request

```text
curl --location 'https://<your-instance>.com/api/quote_requests/10163/tasks' \
--header 'Accept: application/xml' \
--header 'Accept: application/json' \
--header 'Accept: application/octet-stream' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
"title": "New Task for 10163",
"quote_task_attributes":{"phase": "setup"},
"percentage": 0
}'
```
