---
title: "Default Receiving Location API (/default receiving location)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/default-receiving-location-api-(default-receivinglocation)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/default-receiving-location-api-(default-receivinglocation)"
status_code: 200
fetched_at: "2026-04-09T11:59:40+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Default Receiving Location API (/default receiving location)"
---

# Default Receiving Location API (/default receiving location)

## Overview

Use the Default Receiving Location API to update or get a
list of default receiving locations. The URL to access pick
lists
is: `https://{your_instance_name}/api/default_receiving_locations`

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | /api/default_receiving_locations | create | /api/default_receiving_locations/api/default_receiving_locations/api/default_receiving_locations |
| GET | /api/default_receiving_locations | index | /api/default_receiving_locations/api/default_receiving_locations/api/default_receiving_locations |
| GET | /api/default_receiving_locations/:id | show | /api/default_receiving_locations/:id/api/default_receiving_locations/:id/api/default_receiving_locations/:id |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| item | item | yes | | | | yes | Item |
| item-id | Item identifier | | | | yes | | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| warehouse | warehouse | yes | yes | | | yes | Warehouse |
| warehouse-id | Warehouse identifier | | | | yes | | integer |
| warehouse-location | warehouse location | yes | | | | yes | WarehouseLocation |
| warehouse-location-id | Warehouse Location identifier | | | | yes | | integer |
