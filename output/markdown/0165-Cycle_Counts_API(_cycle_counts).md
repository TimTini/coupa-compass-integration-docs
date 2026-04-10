---
title: "Cycle Counts API(/cycle_counts)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/cycle-count-lines-api-(cycle_count_lines)/cycle-counts-api(cycle_counts)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/cycle-count-lines-api-(cycle_count_lines)/cycle-counts-api(cycle_counts)"
status_code: 200
fetched_at: "2026-04-09T11:59:39+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Cycle Count Lines API (/cycle_count_lines)"
  - "Cycle Counts API(/cycle_counts)"
---

# Cycle Counts API(/cycle_counts)

## Associations

This resource is associated with [Cycle Count Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/cycle-count-lines-api-(cycle_count_lines)).

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | /api/cycle_counts | index | Query Cycle Counts |
| GET | /api/cycle_counts/:id | show | Show Cycle Counts |
| PUT | /api/cycle_counts/submit | submit | Submit Cycle Counts |
| PATCH | /api/cycle_counts/:id/submit | submit | Submit Cycle Counts |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://r34.coupadev.com/integration_documents/obj_show/User) |
| cycle-count-lines | Cycle count lines | | | | | yes | CycleCountLine |
| id | Coupa unique identifier | | | | | yes | integer |
| status | Status of the cycle count | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
