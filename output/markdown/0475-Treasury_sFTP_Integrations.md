---
title: "Treasury sFTP Integrations"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-sftp-integrations"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-sftp-integrations"
status_code: 200
fetched_at: "2026-04-09T12:00:56+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury sFTP Integrations"
---

# Treasury sFTP Integrations

Use sFTP for Treasury CSV import and export integrations. Set up and manage your integrations using Coupa Core.

## Set up SFTP accounts

Setting up sFTP accounts for Treasury Management integrations is the same process as Core.

- In Coupa Core, navigate to
Setup > Integrations > sFTP Accounts
.

- Create your sFTP account.

- In the **Application** field, select **Treasury**.

For more information, see [sFTP Account Management](https://compass.coupa.com/x294101.xml).

## Manage Treasury integrations

Define settings for Treasury SFTP integrations.

- In Coupa Core, navigate to
Setup > Integrations > Integrations
.

- Locate the standard integration you want to manage and select the **Edit** icon.

- From Coupa indicated outbound integrations.

- To Coupa indicates inbound integrations.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: For inbound integrations, simply **drop the file** into the configured sFTP folder—no further action is required.

- Define these settings (These settings apply to outbound integrations only).

| Setting | Description |
| --- | --- |
| End System Type | Type of system to consume the files. |
| End System | System to consume the files. |
| Enable Encryption | When enabled, exported files are PGP encrypted. Key can be maintained in sFTP account. |
| Enable Scheduler | Schedule for the profile. |
| Remove new line | When selected, removes new lines from your export. Available for CSV integrations only. |
| Remove carriage return | When selected, removes carriage returns from your export. Available for CSV integrations only. |
| Delimiter | Select a delimiter for your export. Available for CSV integrations only. |
| Delta filter | Select whether you want to include a delta filter for your recent changes in your export. Available for CSV integrations only. |
| Send file even if empty | When selected, exports an empty (zip) file if there is no data. |
| Send unzip file | When selected, exported files are unzipped. Available for Original File integrations only. |
| Subfolder | Defines a subfolder for the export. The system automatically pluralizes the last segment of the folder name using a standard pluralization library. For example, if you enter a path like **bankfile/PDF**, the last segment is pluralized, resulting in **bankfile/PDFS**.<br>![](https://compass.coupa.com/DITARoot/icons/important.png) Note:<br>You cannot edit this value after creation. To make an update, you must recreate the integration. |

## Self-service for Treasury CSV export integrations

If you need export capabilities beyond the standard integrations, you can create custom export integrations using **Automation Views** that you configure in Treasury Management.

For more information, see [Custom Treasury CSV export integrations](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-sftp-integrations/treasury-csv-exports#AutoViewCustomInteg) and [Automation Views in Treasury Management](https://compass.coupa.com/en-us/products/product-documentation/treasury-management-product-documentation/getting-started-with-treasury-management/automated-processes-and-integrations/automation-views-in-treasury-management).
