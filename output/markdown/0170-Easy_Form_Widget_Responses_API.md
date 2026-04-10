---
title: "Easy Form Widget Responses API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/easy-form-responses-api-(easy_form_responses)/easy-form-widget-responses-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/easy-form-responses-api-(easy_form_responses)/easy-form-widget-responses-api"
status_code: 200
fetched_at: "2026-04-09T11:59:41+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Easy Form Responses API (/easy_form_responses)"
  - "Easy Form Widget Responses API"
---

# Easy Form Widget Responses API

## Overview

Easy Form Widget Reponses API is associated with the [Easy Form Responsess](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/easy-form-responses-api-(easy_form_responses)) API.

## Elements

| **Element** | **Description** | **Req'd** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- |
| answer | End user response. Depending on the widget type, this field may contain text, name, id, child easy form response, or a list of values.<br>For example: @@BLOCK_0@@<br>![](https://compass.coupa.com/DITARoot/icons/important.png) Note:<br>With the May 2023 release the StateIsoCode will be available for SIM Easy Form Responses. The easy_form_widget_response for region will have its answer changed from: `state, country` to: {country: country, state: state, state_iso_code: ISO-3166-2 codes} For example, if the country does not have state options, the experience will be like the following {country: Antarctica, state: NA, state_iso_code: nil} | | yes | string(255) | | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | |
| created-by | User who created | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| easy-form-id | Easy form ID associated with this easy form response | | | | yes | integer(11) |
| easy-form-response-id | Easy form response ID associated with this widget | | | | yes | integer(11) |
| easy-form-widget-id | Easy form widget ID associated with this widget response | | | | yes | integer(11) |
| encrypted-answer | The answer for widget response | | | | yes | string(20000) |
| field-name | The value of the widget's **Reporting Name** field on form builder page | | | | yes | |
| id | Coupa unique identifier | | | | yes | integer(11) |
| type | Type of widget response | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | |
| updated-by | User who updated | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| widget-label | User name for widget | | | | yes | string(255) |
| widget-type | Type of widget | | | | yes | string(255) |
| supplier_visible_attachment | Supplier visible attachment | | | yes | | boolean |
