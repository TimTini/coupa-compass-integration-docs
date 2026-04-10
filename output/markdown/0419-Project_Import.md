---
title: "Project Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/project-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/project-import"
status_code: 200
fetched_at: "2026-04-09T12:00:43+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Project Import"
---

# Project Import

## Project

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Project | No | No | | Project | |
| Name* | Yes | Yes | string(255) | The Tag's name | |
| Project ID | No | No | integer | System generated Project ID for existing project | |
| Status | No | No | string(25) | Status of the project | |
| Content Groups | No | No | BusinessGroup | Content Group list for the project | |
| Description | No | No | text | The Tagging's description | |
| Allow anyone to join | No | No | boolean | If this project open to everyone to join or not | |
| Who can view members | No | No | integer | Who can view members of the project. Owners or anyone with access to the project | anyone_with_access_to_this_project, project_owners_only |
| Project Owners | No | No | | Owner/s of the project | |
| Project Members | No | No | | Member/s of the project | |
| Start Date | Yes | No | datetime | Start Date of the task | |
| End Date | Yes | No | datetime | End Date of the project | |
| External Ref Number | No | No | string(255) | External Ref Number of the project | |
| Commodity | No | No | | Commodity of the project | |
| Category | Yes | No | | Category of the project | |
| Department | No | No | | Department of the project | |
| Show Sourcing Tab | No | No | | Enable Sourcing tab or not | |
| Show Contracts Tab | No | No | | Enable Contracts tab or not | |
| Show Suppliers Tab | No | No | | Enable Suppliers tab or not | |
| Show Sourcing Calculated Fields | No | No | boolean | Enable Sourcing calculated fields or not | |
| Show Contracts Calculated Fields | No | No | boolean | Enable Contracts calculated fields or not | |
| Show Suppliers Calculated Fields | No | No | boolean | Enable Suppliers calculated fields or not | |
| Additional Planned Savings | No | No | decimal(32,4) | Additional Planned Savings of the project | |
| Additional Negotiated Savings | No | No | decimal(32,4) | Additional Negotiated Savings of the project | |
| Additional Realized Savings | No | No | decimal(32,4) | Additional Realized Savings of the project | |
| Task | No | No | | Task | |
| Title* | Yes | No | | Title of the task | |
| Task ID | No | No | | System generated Task ID for the task | |
| Assign To | No | No | | Owner's login of the task for the project | |
| Due Date | No | No | | Due Date of the task | |
| Original Estimate | No | No | | Original Estimate of the task in days | |
| Task completion % | No | No | | Percentage of the task completion | |
| Linked Object | No | No | | Linked Object | |
| Object Type* | Yes | No | | Type of the linked object | |
| Object ID | No | No | | ID of the linked object | |
| Object Name | No | No | | Name of the linked object | |
| Tag | No | No | | Tag | |
| System Tag | No | No | | System Tag, defaults to false if not specified | |

## Task

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Task | Describes the type of header row | No | No | | task |
| Title* | Title of the task | Yes | No | | |
| Task ID | System generated Task ID for the task | No | No | | |
| Assign To | Owner's login of the task for the project | No | No | | |
| Due Date | Due Date of the task | No | No | | |
| Original Estimate | Original Estimate of the task in days | No | No | | |
| Task completion % | Percentage of the task completion | No | No | | |

## Linked Object

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Linked Object | Describes the type of header row | No | No | | linked_object |
| Object Type* | Type of the linked object | Yes | No | | |
| Object ID | ID of the linked object | No | No | | |
| Object Name | Name of the linked object | No | No | | |

## Tag

| **Column Name** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Tag | Describes the type of header row | No | No | | tag |
| System Tag | System Tag, defaults to false if not specified | No | No | | Must be an existing tag |
