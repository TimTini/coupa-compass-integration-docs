---
title: "User Group Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/user-group-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/user-group-import"
status_code: 200
fetched_at: "2026-04-09T12:00:49+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "User Group Import"
---

# User Group Import

## Overview

This import will allow you to maintain the User Groups. The
Forms import process reads files from
`./Incoming/UserGroups/` in the SFTP. These
files will be moved to the archive folder located
at `./Incoming/Archive/UserGroups/` before
being processed in alphanumeric order.

## Keys

- Name

## Validations

Coupa uses the field Name to lookup an existing
record.

## Group

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | Yes | Yes | string(255) | Name | |
| Id | No | No | integer | Unique identifier Coupa assigns when a new record is created. It can’t be modified, but can be used to update the record. | |
| Active | No | No | boolean | Whether this Project or Group is currently Active. | |
| Owner | No | No | | Owner group receives notifications on Approval Group errors. Field is called Parent Group in the UI. | |
| Users By Login | No | No | | A semi-colon seperated list of Logins for all users of this project or group. | |
| Users By Employee Number | No | No | | A semi-colon seperated list of Employee Numbers for all users of this project or group. | |
| Description | No | No | text | Description | |
| Can Approve | No | No | boolean | Group has the ability to be an approver. | |
| Open | No | No | boolean | When true, a Project or Group is open for everyone to join. When false, an owner must invite others. | |
| Content Groups | No | No | | A comma separated list of Content Groups for the Project or Group. | |
