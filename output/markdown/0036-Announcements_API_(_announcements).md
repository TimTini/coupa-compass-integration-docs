---
title: "Announcements API (/announcements)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/announcements-api-(announcements)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/announcements-api-(announcements)"
status_code: 200
fetched_at: "2026-04-09T11:59:09+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Announcements API (/announcements)"
---

# Announcements API (/announcements)

Use the announcement API to query announcements in Coupa
Mobile.

The URL to access Announcements is:
`https:///api/announcements`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Announcements API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/announcements` | index | Query announcements |
| GET | `/api/announcements/:id` | show | Show announcements |

## Elements

The following elements are available for the Announcements
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | | | | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| subject | Announcement subject | yes | | | | yes | string(255) |
| message | Announcement message | yes | | | | yes | text |
| short-description | Announcement short message | | | | | yes | |
| announceable-type | Announceable type | | | | | yes | string(255) |
| announceable-id | Announceable ID | | | | | yes | integer |
| start-at | Announcement start date | yes | | | | yes | datetime |
| new | New announcement | | | | | yes | boolean |
| created-by | User who created | | | | | yes | |
| updated-by | User who updated | | | | | yes | |
| summary | Announcement summary | | | | | yes | string(255) |
| Important | Announcement is important | | | | | yes | boolean |
