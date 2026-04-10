---
title: "Category Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/category-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/category-import"
status_code: 200
fetched_at: "2026-04-09T12:00:34+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Category Import"
---

# Category Import

## Overview

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

You must haveCategory Planner to bulk import categories.

You can use the Category CSV loader to bulk import categories for use with Category Planner.

## Unique Keys

- Name

## Validations

Stakeholders and owners must have the correct Category Planner permissions in Coupa to be added to categories. If they don't have the correct permissions, the Category bulk loader doesn't add them to the category. For more information, see
[Understand Category Planner Roles and Permissions](https://compass.coupa.com/x341843.xml).

The following values must already exist in Coupa:

- Commodities List

- Stakeholder Name:Stakeholder Department

- Owner Name:Owner Department

- Analytics Mapping Name

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Commodities List, Stakeholder Name:Stakeholder Department, and Owner Name:Owner Department are semicolon (;) separated. The rest of the fields are comma (,) separated.

When you use the Category loader to add stakeholders and owners, it generates custom departments with the values you specify.

## Category

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| ID | No | No | integer | Id. If id is passed we try to update that category with the values passed in the csv. If id is not passed, we will create a new category. | |
| Name* | Yes | Yes | string(100) | Name. A category with the same name should not exist in Coupa | |
| Description | No | No | text | Description | |
| Commodities List* | Yes | No | | Commodities List. Must exist in Coupa | |
| Stakeholder Name:Stakeholder Department | No | No | | Stakeholder Name:Stakeholder Department. Stakeholder name must exist in Coupa | |
| Owner Name:Owner Department* | Yes | No | | Owner Name:Owner Department. Owner name must exist in Coupa | |
| Analytics Mapping Name* | Yes | No | | Analytics Mapping Name. Must exist in Coupa | |
| Total Budget | No | No | | Total budget for the current operating cycle | |
| Used Budget | No | No | | Used budget for the current operating cycle | |
