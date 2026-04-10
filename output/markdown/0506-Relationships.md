---
title: "Relationships"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/relationships"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/relationships"
status_code: 200
fetched_at: "2026-04-09T12:01:02+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess Quick Integration File Formats"
  - "Relationships"
---

# Relationships

The Relationships quick integration import allows Coupa users to
directly upload spreadsheets via the HTTPS protocol. This allows
customers to perform inbound imports in an automated manner without
the need of a relationship interface.

## Post URL

`https://.hiperos.com/QuickIntegration/Relationships`

## Relationships

| **Field** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| RelationshipNumber (*) | Enter the relationship number. | Yes | yes | String(64) | any |
| RelationshipName (*) | Enter the name of the relationship. | Yes | | String(256) | any |
| Description | Enter a brief description of the relationship. | | | String(Max) | any |
| RelationshipMgrUsername (*) | Enter the username of the internal Client manager. Must match an existing username. | Yes | | String(256) | |
| SupplierName (*) | Enter the name of the supplier associated to the relationship. Must match an existing supplier name. | Yes | | String(64) | any |
| AccountMgrUsername (*) | Enter the name of external (supplier) account manager associated to the relationship. Must match an existing supplier employee name. | Yes | | String(256) | |
| Organizations (*) | Enter the name of organizations associated to the relationship. Must match an existing organization defined under Organization Unit Management. Multiple values must be separated with the pipe character (\|). | Yes | | String(256) | |
| Activated | [Yes or No] Enter Yes to activate the relationship. | | | Boolean | yes |
| ContractNumber | Enter the contract number of the relationship. | | | String(64) | any |
| ContractAmount | Enter the contract amount of the relationship. | | | | |
| CurrencyCode | Enter the currency code.AUD > Australian Dollar<br>CAD > Canadian Dollar<br>CNY > Chinese Yuan<br>EUR > Euro<br>GBP > British Pound<br>USD > US Dollar | | | | AUD > Australian Dollar<br>CAD > Canadian Dollar<br>CNY > Chinese Yuan<br>EUR > Euro<br>GBP > British Pound<br>USD > US Dollar |
| StartDate (*) | Enter the start effective date of the relationship. | Yes | | DateTime | any |
| ExpirationDate | Enter the end date of the relationship. | | | DateTime | any |
| ContractDocumentFileName | Enter the document filename to attach as the contract.<br>Must send actual file to Hiperos Support to be loaded on the server and linked to the relationship. | | | | any |
| RiskRating | Enter the risk rating of the relationship. Must match an existing risk rating defined under Setup Data Management. | | | String(64) | any |
| Geography | Enter the name of the country. Must match an existing geography defined under Setup Data Management. Multiple values must be separated with the @ symbol. | | | | |
| Classification | Enter the name of the classification. Must match an existing classification defined under Setup Data Management. | | | String(64) | |
| Category | Enter the name of the category. Must match an existing category defined under Setup Data Management. | | | String(64) | |
| SubCategory | Enter the subcategory of the relationship. | | | String(64) | |
| HiperosFamily | Enter the name of the Hiperos category family. Must match an existing Hiperos category family type. Contact Hiperos 3PM Support ([support@hiperos.com](mailto:support@hiperos.com) ) or the assigned Client Services representative for a complete list. | | | | |
| HiperosCategory | Enter the name of the Hiperos category. Must match an existing Hiperos category type. Contact Hiperos 3PM Support ([support@hiperos.com](mailto:support@hiperos.com) ) or the assigned Client Services representative for a complete list. | | | | |
| HiperosSubCategory | Enter the name of the Hiperos subcategory. Must match an existing Hiperos subcategory type. Contact Hiperos 3PM Support ([support@hiperos.com](mailto:support@hiperos.com) ) or the assigned Client Services representative for a complete list. | | | | |
| ClientAccess | Enter the access of the internal relationship. Multiple values must be separated with the pipe character (\|).<br>Manager Only<br>Team<br>All | | | String(64) | |
| SupplierAccess | Enter the access of the external relationship. Multiple values must be separated with the pipe character (\|).<br>Manager Only<br>Team<br>All | | | String(64) | |
| RelationshipGroupAccess | Enter the name of the group that has access to the relationship. Must match an existing group name defined under Group Management. Multiple values must be separated with the pipe character (\|). | | | | |
| AtRiskFee | Enter the at risk fee of the relationship. | | | | |

(*)Required
