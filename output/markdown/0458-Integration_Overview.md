---
title: "Integration Overview"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/ccw-flat-files-(csv)/integration-overview"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/ccw-flat-files-(csv)/integration-overview"
status_code: 200
fetched_at: "2026-04-09T12:00:52+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "CCW Flat Files (CSV)"
  - "Integration Overview"
---

# Integration Overview

Coupa primarily exchanges files with customers via the SFTP protocol. We support both username/password or SSH key authentication. SFTP is preferable to FTP as both the control and data channels are encrypted. Customer systems must connect to Coupa enterprise’s (Coupa P2P) FTP server to exchange data between Coupa Enterprise (CE) and Coupa Contingent Workforce (CCW).

## sFTP user account

You can create and manage your SFTP accounts for exchanging data with the Coupa Enterprise Administration page. In case you have issues, please coordinate with the Implementation team for additional help. Using the sFTP Account Page you can:

- Create and manage an sFTP user account.

- Manage the SSH key to authenticate the account.

- Reset your password.

## Folder format

- CCW-specific incoming files must be placed under
`/Incoming/CCW`

- CCW-specific outgoing files will be placed under
`/Outgoing/CCW`

## Encryption

sFTP is a secure file transfer protocol and supports the full security and authentication functionality of SSH. In addition to sFTP protocol, Coupa Contingent Workforce also supports an additional layer of encryption that uses PGP standard, ensuring customer data is secured while at rest. During implementation for:

- Inbound file: CCW integration resource will share PGP public key (if applicable)

- Outbound file: Customer must provide PGP public key to CCW implementation resource (if applicable)

## Integration workflow

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_flat_files/images/image23.png)

## Callouts

- CCW supports Delta feed (Changes only) and Full feed for Master Data, however we recommend the Delta feed.

- Across all inbound integrations, if the customer chooses to use the full file, the Status column must be excluded.

- CCW integrates with Coupa enterprise to synchronize user data and one chart of account (COA) identified for CCW.

- CCW supports master data integration for segment fields that are not exhausted by COA segments (11 segment fields that can support a combination of COA segments and HR-only fields, if COA consumes 3 segment
**s, then integration can support integration for rest of the 8 segments).**

## Unified integrations

Master Data: User

- The following user data is synchronized between CE and CCW:

- Status, User Name, First Name, Last Name, Nick Name, Email, Phone Number, Role(only initial sync-up), Default Currency, Employee Number.

- Supervisor Hierarchy is synchronized to support hierarchy-based approval flow.

## Authentication

CCW client users are authorized using SSO authentication by Coupa Enterprise against Customer’s SSO authenticator. Once authenticated, users having CCW License and Role can access the CCW application.

Coupa Contingent Workforce is unified with Coupa Enterprise to synchronize User and Chart of Account data.

## Master Data: Chart of Accounts

- CCW synchronizes with Coupa Enterprise to identify one Chart of account for CCW

- As part of synchronization, CCW will apply changes to:

- Chart of Account

- Account or Lookup Values based on CCW COA definition.
