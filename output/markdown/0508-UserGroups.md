---
title: "UserGroups"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/usergroups"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-quick-integration-file-formats/usergroups"
status_code: 200
fetched_at: "2026-04-09T12:01:02+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess Quick Integration File Formats"
  - "UserGroups"
---

# UserGroups

The User Groups quick integration import allows Risk
Assess users to directly upload spreadsheets via the HTTPS
protocol. This allows customers to perform inbound imports in an
automated manner without the need for an Engagement interface.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- This import adds an existing user to an existing
UserGroup.

- You cannot remove UserGroups using this import.

- This import won't create a new UserGroup.

## Post URL

`https://.hiperos.com/QuickIntegration/UserGroups`

## User Groups

| **Field** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| GroupName (*) | Enter the name of the group. Must match an existing group name defined under Group Management. | Yes | | String(256) | any |
| Description (*) | Enter a short description of the group. | Yes | | String(max) | any |
| Activated (*) | Enter Yes to activate the user group. | Yes | | Boolean | Yes or No |
| Member (*) | Enter the email address of the internal Client user. Must match an existing username/email address. | Yes | | String(256) | any |

(*)Required
