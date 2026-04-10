---
title: "AGS-APAY Integration (For Internal Use Only)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/ccw-flat-files-(csv)/ags-apay-integration-(for-internal-use-only)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/ccw-flat-files-(csv)/ags-apay-integration-(for-internal-use-only)"
status_code: 200
fetched_at: "2026-04-09T12:00:52+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "CCW Flat Files (CSV)"
  - "AGS-APAY Integration (For Internal Use Only)"
---

# AGS-APAY Integration (For Internal Use Only)

## Integrations Reference Document

Services/Architects, if you have questions please reach out to the CCW services team. Use the following page as reference:

[https://coupadev.atlassian.net/wiki/spaces/CVS/pages/1153018562/Contingent+Workforce](https://coupadev.atlassian.net/wiki/spaces/CCWE/pages/1838546951/AGS+APAY)

Configurations Used

## Fee Settings

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image1.png)
![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image2.png)

## Location Settings

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image3.png)
![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image4.png)
![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image5.png)

## Timesheet Localization Settings

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image6.png)

## Tax Settings

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image7.png)

## Data Staging Information

Below is the worker template I used to create the workers for all data staged. You will not necessarily need to review this upload template, but it might be a good item to reference if you are validating that data was staged correctly based on the above configurations.

## Example - Worker 1 Time and Expense

## One timesheet

- Taxes=Yes; Timesheets only; 6%

- Overtime=No

- Double time=No

- Single or Multiple Charge Number=Single

- MSP/VMS Fees and Funding:

- MSP Fee=Supplier 2.5%

- VMS Fee=Supplier 0.5%

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image8.png)

## One expense

- MSP/VMS fees and funding: None (not a Misc. Fee type of expense)

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image9.png)

## Example - Worker 2 Time and Expense

## One timesheet

- Taxes=Yes; Timesheets only; 6%

- Overtime=Yes

- Double time=No

- Single or Multiple Charge Number=Multiple

- MSP/VMS Fees and Funding:

- MSP Fee=Supplier 2.6%

- VMS Fee=Client 0.4%

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image10.png)

## One expense

- MSP/VMS fees and funding: Yes (Misc. Fee type of expense)

- MSP Fee=Client 2%

- VMS Fee=Client 1%

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image11.png)

## Example - Worker 3 Time and Expense

## One timesheet

- Taxes=No

- Overtime=No

- Double time=No

- Single or Multiple Charge Number=Multiple

- MSP/VMS Fees and Funding:

- MSP Fee=Supplier 2.7%

- VMS Fee=Client 0.3%

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image12.png)

## One expense

- MSP/VMS fees and funding: None (not a Misc. Fee type of expense)

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image13.png)

## Example - Worker 4 Time and Expense

## One timesheet

- Taxes=No

- Overtime=Yes

- Double time=Yes

- Single or Multiple Charge Number=Single

- MSP/VMS Fees and Funding:

- MSP Fee=Supplier 2.8%

- VMS Fee=Client 0.2%

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image14.png)

## One expense

- MSP/VMS fees and funding: Yes (Misc. Fee type of expense)

- MSP Fee=Client 2%

- VMS Fee=Client 1%

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image15.png)

## Calculations

For reference, please also refer to the
**Calculations** tab on: APAY Sample Data and File 8.6.19 (internal only).xlsx

Timesheet

| **Sample Reg Hours** | **Sample Supplier Bill Rate** | **Sample Final Bill Rate** | **Sample MSP Funding Config** | **Sample MSP Fee** | **Sample VMS Funding Config** | **Sample VMS Fee** | **Total Final Amount** | **Client Amount** | **Supplier Amount** | **AGS Amount (MSP)** | **Coupa Amount (VMS)** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 10 | 10 | Client | 2% | Client | 1% | 100 | 103 | 100 | 2 | 1 |
| 10 | 10 | 10 | Supplier | 2% | Client | 1% | 100 | 101 | 98 | 2 | 1 |
| 10 | 10 | 10 | Supplier | 2% | Supplier | 1% | 100 | 100 | 97 | 2 | 1 |
| 10 | 10 | 10 | Client | 2% | Supplier | 1% | 100 | 102 | 99 | 2 | 1 |

## Expense

| **Sample Final Bill Rate** | **Sample MSP Funding Config** | **Sample MSP Fee** | **Sample VMS Funding Config** | **Sample VMS Fee** | **Total Final Amount** | **Client Amount** | **Supplier Amount** | **AGS Amount (MSP)** | **Coupa Amount (VMS)** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | Client | 2% | Client | 1% | 100 | 103 | 100 | 2 | 1 |
| 10 | Supplier | 2% | Client | 1% | 100 | 101 | 98 | 2 | 1 |
| 10 | Supplier | 2% | Supplier | 1% | 100 | 100 | 97 | 2 | 1 |
| 10 | Client | 2% | Supplier | 1% | 100 | 102 | 99 | 2 | 1 |

## Taxes

Tax percentage is configured in CLM Advanced by either AGS or Coupa during implementation, as defined by the client.

- **Client Tax Amount** = Tax % * 0.01 * Client Amount

- **Supplier Tax Amount** = Tax % * 0.01 * Supplier Amount

- **MSP Tax Amount** = Tax % * 0.01 * AGS Amount

- **Coupa Tax Amount** = Tax % * 0.01 * Coupa Amount

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

The way we are calculating the taxes allows a Supplier-funded model or a Client-funded model to properly calculate the taxes (not overstated for Client-funded).

## File 2 Adjustments

## Worker 1: Rate change

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image16.png)

## Worker 2 Timesheet adjustment

Hours change from 40 Regular, 10 OT to 38 Regular:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image17.png)

## Worker 3 Timesheet adjustment

Charge number change from
**07652-14365** to
**04062-76102:**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image18.png)

## Worker 4 Expense adjustment

Amount change from
**$35** to
**$45:**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image19.png)

## File 3 Adjustments

## MSP Markup for the Supplier

Supplier config changed from 2.5% to 3.1%:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image20.png)

## VMS Markup for the Supplier

Supplier config changed from 0.5% to 0.9%:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image21.png)

Taxes for the Boca Raton location changed from 6% to 6.5%:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image22.png)
