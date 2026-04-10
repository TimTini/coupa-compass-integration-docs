---
title: "Content Group Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/content-group-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/content-group-import"
status_code: 200
fetched_at: "2026-04-09T12:00:35+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Content Group Import"
---

# Content Group Import

## Overview

Content Groups are sometimes called Business Groups in Coupa.
The Content Groups Import process read files from
`./Incoming/BusinessGroups/` in the SFTP. These
files will be moved to the archive folder located
at `./Incoming/Archive/BusinessGroups/` before
being processed in alphanumeric order.

## Content Group

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | Yes | Yes | string(100) | Name for Content Group | |
| Description | No | No | string(255) | Description of Content Group | |
