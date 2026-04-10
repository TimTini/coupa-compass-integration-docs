---
title: "Extended Suppliers"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/extended-suppliers"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/extended-suppliers"
status_code: 200
fetched_at: "2026-04-09T12:01:01+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess Quick Integration File Formats"
  - "Extended Suppliers"
---

# Extended Suppliers

## Post URL

`https://.hiperos.com/QuickIntegration/ExtendedSuppliers`

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- The syntax for populating parent-child UDFs is to separate the
2 values with an ""@""

- The syntax for populating Money and Currency UDFs is to
separate the 2 values with a "" "" (space)

- Use the setup data code or set up data type code for UDFs of
type Set-up Data and Setup Data type.

- The syntax for populating multi-select set-up data UDFs is to
separate the values with an ""@""

- Use the username field to populate UDFs of type User
Selector

- The syntax for populating multi-select UDFs is to separate the
values with a ""|"" (pipe character)

- The syntax for populating Table UDFs is:
Row1Col1|Row1Col2|Row1Col~Row2Col1|Row2Col2|Row2Col3. Separate
values for each column in a given row using the | (pipe character)
separate rows with the ~

- The syntax for populating the Unit of Measure UDF is: value|uom
string i.e. (15.0|each) Note: The uom string must be an exact match
to the configuration in the component.

- Enter ""true"" to populate a Checkbox UDF with a check. (note:
all letters must be lower case)

- The syntax for populating date range UDFs is to separate the 2
values with a ""|"" (pipe) For example: 01/01/2012|12/31/2012

## Extended Suppliers

| **Field** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| ParentExternalReference | Enter the unique reference key of the supplier parent to link to external systems (ERP system, etc). | | Yes | String(256) | any |
| ExternalReference | Enter the unique reference key to link to external systems (ERP system, etc). | | Yes | String(256) | any |
| SupplierNumber | Enter the unique reference number. | | Yes | String(256) | any |
| SupplierName (*) | Enter the name of the supplier. | Yes | | String(256) | any |
| SupplierMgrUserName (*) | Enter the username of the internal Client supplier manager. | Yes | | String(256) | any |
| SupplierMgrFirstName | Enter the first name of the internal Client supplier manager. | | | String(64) | any |
| SupplierMgrLastName | Enter the last name of the internal Client supplier manager. | | | String(64) | any |
| AccountMgrEmail (*) | Enter the email address of external supplier account manager. | Yes | | String(256) | any |
| AlternateAccountMgrEmail | Enter the alternate email address of the external user. | | | String(256) | any |
| AccountMgrFirstName (*) | Enter the first name of external supplier account manager. | Yes | | String(64) | any |
| AccountMgrLastName (*) | Enter the last name of external supplier account manager. | Yes | | String(64) | any |
| ShortName | Enter the supplier short name. | | | String(64) | any |
| ParentName | Enter the supplier parent name. | | | String(256) | any |
| LegalName | Enter the supplier legal name. | | | String(64) | any |
| DUNSNumber | Enter the unique nine digit number for identifying and tracking (nn-nnn-nnnn). | | | String(64) | any |
| TickerSymbol | Enter the supplier ticker symbol. | | | String(64) | any |
| IndustryClassification | Enter the industry type. Must match an existing industry classification code defined under Setup Data Management. | | | String(64) | any |
| Classification | Enter the classification type. Must match an existing classification defined under Setup Data Management. | | | String(64) | any |
| MinorityType | Enter the minority type. | | | | None<br>African-American<br>Asian-India American<br>Asian-Pacific American<br>Hispanic-American<br>Native-American<br>Woman-owned |
| RiskRating | Enter the level of risk associated with the supplier. Must match an existing risk rating defined under Setup Data Management. | | | String(64) | |
| TaxIDNumber | Enter the US tax exempt ID number. | | | String(64) | |
| VATNumber | Enter the European VAT number. | | | String(64) | |
| OnExclusionList | [Yes or No] Enter Yes to indicate the supplier is on the US State Department's Terrorist Exclusion List. | | | Boolean | |
| SupplierGroup | Enter the name of the supplier group. | | | | |
| AutoApproveCompliance | [Yes or No] Enter Yes to indicate the supplier program responses for all compliance programs are automatically approved (if compliant). | | | | |
| Phone | Enter the supplier phone number. | | | String(64) | |
| Fax | Enter the supplier fax number. | | | String(64) | |
| Website | Enter the supplier web site. | | | String(256) | |
| BusinessType | Enter the business type. Must match an existing business type defined under Setup Data Management. | | | String(256) | |
| SupplierType | Enter the supplier type. Must match an existing supplier type defined under Setup Data Management. | | | String(256) | |
| YearEstablished | Enter the year the supplier was founded. | | | String(60) | |
| EDIEnabled | Enter the EDI enabled type. | | | | |
| None | | | | | |
| All Types | | | | | |
| AS2 | | | | | |
| EDI via VAN | | | String(256) | | |
| LifeCycleStatus | Enter the life cycle status of the supplier. Must match an existing life cycle status. See Supplier Life Cycle Status Management. | | | | |
| UltimateCountry | Enter the default country of origin. | | | String(64) | |
| DefaultLanguage | Enter the default culture. | | | | |
| WorkspaceList | Enter the name of the workspace the supplier should be included. Multiple values must be separated with the pipe character (\|). If the workspace does not exist, the import creates it and adds the supplier. If the workspace does exist, the import adds the supplier to that workspace. NOTE: all suppliers are added to the main workspace (Hiperos 3PM). See Your Active Workspaces. | | | | |
| Status | Enter the status of the supplier. | | | String(64) | |
| OnHold | [Yes or No] Enter Yes to indicate the supplier is on hold. | | | | |
| HoldReason | Enter the reason the supplier is on hold. | | | String(64) | |
| Description | Enter a brief description of the supplier. | | | String(Max) | |
| udfs_<fieldname> | Enter one column for each Supplier UDF to be entered. Enter the field name of the UDF to import in each column, and the value for each supplier in the rows. Must match an existing r.portal UDF name for Suppliers. NOTE: field name must be in the format udfs_<fieldname> | | | | |
| LocationType | Enter the location type. Must match an existing address type defined under Setup Data Management. | | | String(64) | |
| LocationCountry | Enter the location country. | | | String(64) | |
| LocationAddress1 | Enter the first line of the address. | | | String(128) | |
| LocationAddress2 | Enter the second line of the address. | | | String(128) | |
| LocationAddress3 | Enter the third line of the address. | | | String(64) | |
| LocationAddress4 | Enter the fourth line of the address. | | | String(64) | |
| LocationCity | Enter the location city. | | | String(64) | |
| LocationState | Enter the location state. | | | String(64) | |
| LocationPostalCode | Enter the location postal code. | | | String(64) | |
| LocationCounty | Enter the location county. | | | String(64) | |
| LocationDUNSNumber | Enter the location D-U-N-S Number (nn-nnn-nnnn). | | | String(256) | |
| LocationContactUserName | Enter the location contact username. | | | | |
| LocationNumber | Enter the location number. For internal use only. | | | | |
| udfsl_<fieldname> | Enter one column for each Supplier Location UDF to be entered. Enter the field name of the UDF to import in each column, and the value for each supplier location in the rows. Must match an existing r.portal UDF name for Supplier Locations. NOTE: field name must be in the format udfsl_<fieldname> | | | | |
| SupplierIDType | Enter the supplier identifier type. Must be either Tax ID or ERP ID. | | | String(256) | |
| SupplierIDCategory | Enter the supplier identifier category. Must match an existing supplier ID category defined under Setup Data Management. | | | String(256) | |
| SupplierIDSubCategory | Enter the supplier identifier subcategory. Must match an existing supplier ID subcategory defined under Setup Data Management. | | | String(256) | |
| SupplierIDValue | Enter the supplier identifier unique reference key. | | | String(256) | |
| udfsi_<fieldname> | Enter one column for each Supplier Identifier UDF to be entered. Enter the field name of the UDF to import in each column, and the value for each supplier identifier in the rows. Must match an existing r.portal UDF name for Supplier Identifiers. NOTE: field name must be in the format udfsi_<fieldname> | | | | |

(*)Required
