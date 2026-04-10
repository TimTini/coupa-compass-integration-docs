---
title: "CSV Table Export File Format"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/csv-table-export-file-format"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-csv-format-descriptions-(classic)/csv-table-export-file-format"
status_code: 200
fetched_at: "2026-04-09T12:00:57+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury CSV Format Descriptions (classic)"
  - "CSV Table Export File Format"
---

# CSV Table Export File Format

## Configuring Windows

[PDF Version](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/CSV_Table_Export_File_Format.pdf)

## Default Program to Open CSV

There is
more than one way to set default programs in Windows, but the description below applies to
configuring Windows 10. Configuration is also possible through the **Control Panel** or
within **Excel**. If these instructions do not work for your Windows version, please
consult Windows help.

Your PC should choose Excel by default to open your exported CSV
file. If you want to set, verify, or change the default application, right-click on any
saved CSV file.

Click on Properties.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image10.jpg)

This
opens the **Properties** window for this file. Under the **General** tab, **Type of
File** shows **Comma Separated Values File**. Under that, Windows shows the
application which opens this file type by default.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image11.png)

If you want to use a different default application, click **Change** and select a
different application from your list of apps.

## Regional Language Options

User settings
in tm5 determine the formatting of values in any exported CSV. To make sure your default
application recognizes the values correctly, you can check your regional settings in
Windows.

These settings are available in the Control Panel. To learn more have a look
at [this article](https://support.office.com/en-us/article/Change-the-Windows-regional-settings-to-modify-the-appearance-of-some-data-types-EDF41006-F6E2-4360-BC1B-30E9E8A54989) from Microsoft’s support site.

Regional
settings determine the way numbers, dates, currencies, and times display. For example, the
usual North American date format is DMY (March 1st, 2021), whereas European dates are
written DMY (1 March, 2021).

## User Settings

Your Coupa Treasury user settings
determine the format of an exported document. To view and change your settings, click the
**User Settings** button within the **User Menu** in Coupa Treasury.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image12.png)

This opens the **User Settings** pop-up window. Go to
**Export Format Settings** to see the existing values.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/images/image6a.png)

- **Date Separator** – slash (/), period (.), comma (,), < none >

- **Field Separator** – semicolon (;), comma (,)

- **Date Sequence** – mdy, dmy, ymd

- **Decimal Marker** – period (.), comma (,)

- **Text Delimiter** – single quotation mark (‘), double quotation mark (“), <
none >

- **File Encoding** – ASCII, Unicode
