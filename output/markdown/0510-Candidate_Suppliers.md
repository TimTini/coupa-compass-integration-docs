---
title: "Candidate Suppliers"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/candidate-suppliers"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/candidate-suppliers"
status_code: 200
fetched_at: "2026-04-09T12:01:02+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess Quick Integration File Formats"
  - "Candidate Suppliers"
---

# Candidate Suppliers

The Candidate Suppliers quick integration import allows Risk
Assess users to directly upload spreadsheets via the HTTPS
protocol. This allows customers to perform inbound imports in an
automated manner without the need of a user interface.

## Post URL

`https://.hiperos.com/QuickIntegration/CandidateSuppliers`

## Candidate Suppliers

| **Field** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| EngagementNumber (*) | Engagement number of the Candidate Supplier. NOTE: this field is required but can be left blank if the EngagementName is populated. If both EngagementNumber and EngagementName are both included, EngagementNumber is used. | yes | yes | String(64) | any |
| EngagementName (*) | Engagement name of the Candidate Supplier. NOTE: this field is required but can be left blank if the EngagementNumber is populated. | yes | | String(256) | any |
| ExternalReference (*) | Enter the unique reference key to link to external systems (ERP system, etc). NOTE: this field is required but can be left blank if the SupplierName is populated. | yes | | String(256) | any |
| SupplierName (*) | Enter the name of the supplier. NOTE: this field is required but can be left blank if the ExternalReference is populated. | yes | | String(256) | any |
| SupplierContactUserName (*) | Risk Assess username for the responsible individual at the supplier company. Can create a new user here, but existing users must be on the supplier. NOTE: Always required. | yes | | String(256) | any |
| SupplierContactFirstName (*) | First name for Supplier Contact. Can create a new user here, but existing users must be on the supplier. NOTE: Required only if creating a new user. | yes | | String(64) | any |
| SupplierContactLastName (*) | Last name for Supplier Contact. Can create a new user here, but existing users must be on the supplier. NOTE: Required only if creating a new user. | yes | | String(64) | any |
| Status | Indicates whether the candidate supplier is active and available to the R.Portal workflow (i.e., able to be enrolled in programs and engagements) or if the candidate supplier is inactive and unavailable to the workflow. Defaults to "Active" if blank on create. Valid values are "Active", "Inactive", or blank. | | | String | Defaults to "Active" if blank on create. Valid values are "Active", "Inactive", or blank. |
| Rank | Indicates how the candidate is rated (rank-ordered) with respect to other candidate suppliers. Can be any positive integer starting with 0 and can go to anything above. | | | Integer | 0 or above |
| CandidateNotes | Remarks/comments about the candidate supplier. | | | | |
| Awarded | Indicates if the candidate supplier is awarded or not. Defaults to not awarded for new imports if left blank. Candidate Suppliers can be awarded through this import, but an award cannot be reversed. Valid values are "True" or "False". For a new import, if you do not want to award the Candidate Supplier right away, leave this blank for awarded being set to false. | | | | |
| udfs_<fieldname> | Enter one column for each Candidate Supplier UDF to be entered. Enter the field name of the UDF to import in each column, and the value for each candidate supplier in the rows. Must match an existing r.portal UDF name for Candidate Suppliers. NOTE: field name must be in the format udfs_<fieldname> | | | | |

(*)Required
