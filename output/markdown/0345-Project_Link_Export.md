---
title: "Project Link Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/project-link-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/project-link-export"
status_code: 200
fetched_at: "2026-04-09T12:00:25+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Project Link Export"
---

# Project Link Export

Export of these records is included as a Standard CSV
Export.

## Project Link

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| id | Project Link ID | integer | No/No | |
| Project ID | The project to which it is linked to | integer | No/Yes | |
| Linked Object ID | The object ID the project is linked to | integer | No/No | |
| Linked Object Type | The object type the project is linked to | string(255) | No/No | QuoteRequest, Contract, Supplier, Recommendation, RecommendationAssociation, JapaneseAuction, DutchAuction, CsoEvent, MasterContract, ContractLine, AmendmentContract, InternalSupplier, BenchmarkRecommendation, ExpenseMerchantRecommendationYou, ExpenseMerchantRecommendationCommunity, ExpenseMerchantRecommendation, ExpenseCategoryRecommendationYou, ExpenseCategoryRecommendationCommunity, ExpenseCategoryRecommendation, CategoryRecommendation, DashboardRecommendation, CommodityRecommendation, SupplierRecommendation, SpendGuardRecommendation |
| Created Date | The date the user created the project link | datetime | No/No | |
| Last Updated Date | The date the project link was most recently updated | datetime | No/No | |
