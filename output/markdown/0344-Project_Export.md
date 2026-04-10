---
title: "Project Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/project-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/project-export"
status_code: 200
fetched_at: "2026-04-09T12:00:25+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Project Export"
---

# Project Export

Export of these records is included as a Standard CSV
Export.

## Project

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| id | Project ID | integer | No/No | |
| name | Project Name | string(255) | Yes/Yes | |
| Mention Name | Mention Name | string(255) | No/Yes | |
| Description | Description | text | No/No | |
| Active | Active | boolean | No/No | |
| Open | Open | boolean | No/No | |
| Start date | Start date | datetime | Yes/No | |
| End date | End date | datetime | Yes/No | |
| Commodity ID | Commodity ID the project is associated with | integer | No/No | |
| Created By ID | The user ID that created the project | integer | No/No | |
| Created Date | The date the user create the project | datetime | No/No | |
| Last Updated By ID | The user ID that most recently updated the project | integer | No/No | |
| Last Updated Date | The date the project was most recently updated | datetime | No/No | |
