---
title: "Master Data File Formats"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/ccw-flat-files-(csv)/master-data-file-formats"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/ccw-flat-files-(csv)/master-data-file-formats"
status_code: 200
fetched_at: "2026-04-09T12:00:52+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "CCW Flat Files (CSV)"
  - "Master Data File Formats"
---

# Master Data File Formats

Customers, before attempting to integrate the file formats described in this document, please review the following notes first:

## If you are in the middle of an implementation

Please contact your Coupa Solutions Architect for assistance with file imports.

## If you have legacy, custom integration formats that differ significantly from what is described below

Please contact your Coupa CVM about switching to the formats described in this document.

## Everyone else

Please contact Coupa support for assistance with adding any of the fields below to an existing integration file.

## Master Data

**Description:** Data representing an individual segment

**Supported loads:** Delta File, Full File

**Supported Delimiters:** Pipe(|), Comma(,)

**Supported file extensions:** .csv, .txt

| **Fields** | **Data Type & Length** | **Mandatory** | **Allowed Values** | **Example** |
| --- | --- | --- | --- | --- |
| Name | string(255) | Yes | Any | Service QA |
| Code | string(255) | No | Any | 64121 |
| Description | string(500) | No | Any | IT Services Cost Center |
| Status | Int(1) | Yes | 1 for Active, 0 for inactive | 1 |

## Master Data Relationships

**Description:** Defines the relationship between 2 segments, so that valid child segment options are filtered based on parent segment choice

**Supported loads:** Delta File (recommended), Full File

**Supported Delimiters:** Pipe(|), Comma(,)

**Supported file extensions:** .csv, .txt

| **Fields** | **Data Type & Length** | **Mandatory** | **Allowed Values** | **Example** |
| --- | --- | --- | --- | --- |
| Status | Int(1) | Yes | 1 for Active, 0 for inactive | 1 |
| Parent Segment Name | string(255) | Yes | Any | CUSTOMER’s Master Data1 unique name (must match to Unique name value of record on Master Data1 integration) |
| Parent Segment Code | string(255) | No | Any | CUSTOMER's Master Data1 code. |
| Child Segment Name | string(255) | Yes | Any | CUSTOMER’s Master Data2 name (must match to Unique name value of record on Master Data2 integration). |
| Child Segment Code | string(255) | No | Any | CUSTOMER's Master Data2 code. |

## Accounts

**Description:** CCW stand-alone customers only (Non BSM) can use this integration to load accounts into CCW.

**Supported loads:** Delta File (recommended), Full File

**Supported Delimiters:** Pipe(|), Comma(,)

**Supported file extensions:** .csv, .txt

| **Fields** | **Data Type & Length** | **Mandatory** | **Allowed Values** | **Example** |
| --- | --- | --- | --- | --- |
| Status | Int(1) | Yes | 1 for Active, 0 for inactive | 1 |
| Account | string(100) | Yes | Any | 0100-2522-1545 |
| Name | string(200) | No | Any | Top of the house booking account |

## Work Location

**Description:** Load work location data associated with a CW, so that CW onboarding can be assigned to a Work location

**Supported loads:** Delta File (recommended), Full File

**Supported Delimiters:** Pipe(|), Comma(,)

**Supported file extensions:** .csv, .txt

| **Fields** | **Data Type & Length** | **Mandatory** | **Allowed Values** | **Example** |
| --- | --- | --- | --- | --- |
| Status | int | Yes | 1 for Active, 0 for inactive | 0 |
| Code | string(100) | Yes | Any | CCW01234 |
| Name | string(200) | No | Any | Arcade Research |
| Address Line1 | string(400) | Yes | Any | 8978 - westlake |
| Address Line2 | string(400) | No | Any | Suire # 201 |
| City | string(100) | Yes | Any | Cleveland |
| State | string(100) | Yes | Any | Ohio |
| Postal Code | string(20) | No | Any | 44234 |
| Country | string(3) | Yes | Any, ISO Alpha3 | USA |

## User

**Description:** CCW stand-alone customers only (Non BSM) can use this integration to load users into CCW.

**Supported loads:** Delta File (recommended), Full File

**Supported Delimiters:** Pipe(|), Comma(,)

**Supported file extensions:** .csv, .txt

| **Fields** | **Data Type & Length** | **Mandatory** | **Allowed Values** | **Example** |
| --- | --- | --- | --- | --- |
| Status | int(1) | Yes | 1 for Active, 0 for inactive | 0 |
| User ID | string(100) | Yes | Any | STPHCAR |
| Last Name | string(100) | Yes | Any | Doe |
| First Name | string(100) | Yes | Any | John |
| Middle Name | string(100) | No | Any | |
| Email | string(400) | Yes | Any | jdoe@coupadocument.com |
| CCW User Role | string(512) | Yes | Any | Engaging Manager |
| Supervisor ID | string(100) | No | Any | HUMJINK |
| Job Title | string(400) | No | Any | Production Manager |
| Spend Limit | Number(45,8) | No | Any | 0.00 |
| SSO Attribute | String(100) | No | Any | STPHCAR |
| Work Location Code | String(100) | No | Any | NJB1F002C23 |
| Master Data Segment 1 Name | String(255) | No | Any | Company ID (CCW Mapping = Organization) |
| Master Data Segment 2 Name | String(255) | No | Any | Cost Center ID (CCW Mapping = Cost Center) |
| Master Data Segment 3 Name | String(255) | No | Any | GL ID (CCW Mapping = GL Account) |
| Master Data Segment 4 Name | String(255) | No | Any | Service Method ID (CCW Mapping = Program) |
| Master Data Segment 5 Name | String(255) | No | Any | Supervisory Org ID (CCW Mapping = Project) |
| Master Data Segment 6 Name | String(255) | No | Any | Site Location |
| Master Data Segment 7 Name | String(255) | No | Any | Profit Center |
| Master Data Segment 8 Code | String(255) | No | Any | ServiceMethod |
| Master Data Segment 9 Code | String(255) | No | Any | Labor Class |
| Master Data Segment 10 Code | String(255) | No | Any | Matrix |
| Master Data Segment 11 Code | String(255) | No | Any | Department |
