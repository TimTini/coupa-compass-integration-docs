---
title: "Approval Chain Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/approval-chain-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/approval-chain-import"
status_code: 200
fetched_at: "2026-04-09T12:00:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Approval Chain Import"
---

# Approval Chain Import

## Overview

The Approval chains Import process reads files from
`./Incoming/ApprovalChains/` in the SFTP. These files will be moved to the
archive folder located at `./Incoming/Archive/ApprovalChains/` before being
processed in alphanumeric order.

## Keys & Validations

`Approval Chain Name` and `Approval Chain Type` are the keys
to update an existing approval chain. Both these keys are needed in order to perform an
update. You cannot update the type of an existing approval chain.

You cannot create Orders and Requisitions approval chains with the same name. Loading an
approval name for orders with the same name of an existing one for requisitions through the
bulk loader will cause the Approval Chain Type to change from "requisition" to "order" (it's
also true vice versa).

Currently supported conditions and operations:

- Accounts (equals, contains) 

- Commodity (equals, contains, not contains) 

- Item (equals, contains, not contains) 

- Requester (equals, contains, not contains)

Approval chains created through the loader follow the same validations as those created
through the UI.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: Priority cannot be 50 because 50 is the management hierarchy.
This means that a chain that's less than 50 fires before management hierarchy while a
chain that's greater than 50 fires after management hierarchy.

## Approval Chain

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Approval Chain Name | No | No | | Unique Approval Chain Name | |
| Status | No | No | | Active or Inactive | |
| Approval Chain Type | No | No | | Some possible values: requisition requisition-submission-blocking requisition-approval-blocking requisition-hierarchy expense invoice invoice-submission-blocking invoice-submission-warning invoice-approval-blocking invoice-hierarchy contract-hierarchy contract contract-submission-blocking contract-submission-warning easy-form-user contract-round | |
| Priority | No | No | | Order in which to evaluate approval chain. Number from 1 to 49 and 51 to 99 | |
| Skip Approvers | No | No | | Skip Approvers prior to self if on approval chain | |
| Skip Management Hierarchy | No | No | | Skip Management Hierarchy if this chain matches | |
| Skip Further Approvers | No | No | | Skip Further Approvers if this chain matches | |
| Auto Approve Self | No | No | | Auto Approve Self if added to approval chain | |
| Dedupe OBO User and Auto Approve | No | No | | Override On Behalf Of user, keep the approval chain approver and auto approve the approval | |
| Always Evaluate | No | No | | Always Evaluate | |
| Parallel | No | No | | Parallel approvals supported | |
| Total Comparator | No | No | | The total comparator | |
| Minimum Total Amount | No | No | | Minimum allowed approval total | |
| Maximum Total Amount | No | No | | Maximum allowed approval total | |
| Total Currency | No | No | | Currency Code for total currency | |
| Minimum Approval Limit | No | No | | Minimum Approval Limit | |
| Maximum Approval Limit Amount | No | No | | Maximum Approval Limit Amount | |
| Maximum Approval Limit Currency | No | No | | Maximum Approval Limit Currency | |
| Maximum Approval Limit | No | No | | Maximum Approval Limit | |
| Operator | No | No | | The conditions operator | |
| Condition 1 | No | No | | Condition 1 - Colon : seperated list of val:field:condition | |
| Condition 2 | No | No | | Condition 2 | |
| Condition 3 | No | No | | Condition 3 | |
| Condition 4 | No | No | | Condition 4 | |
| Condition 5 | No | No | | Condition 5 | |
| Condition 6 | No | No | | Condition 6 | |
| Condition 7 | No | No | | Condition 7 | |
| Condition 8 | No | No | | Condition 8 | |
| Condition 9 | No | No | | Condition 9 | |
| Condition 10 | No | No | | Condition 10 | |
| Description | No | No | | Set custom notification text for the condition(s) you have set above. If you leave this field blank, the system will use the name of the configuration you set as the default text. | |
| Approver 1 | No | No | | Approver 1 - Colon : seperated value consisting of user_login;amount;currency_code | |
| Approver 2 | No | No | | Approver 2 | |
| Approver 3 | No | No | | Approver 3 | |
| Approver 4 | No | No | | Approver 4 | |
| Approver 5 | No | No | | Approver 5 | |
| Approver 6 | No | No | | Approver 6 | |
| Approver 7 | No | No | | Approver 7 | |
| Approver 8 | No | No | | Approver 8 | |
| Approver 9 | No | No | | Approver 9 | |
| Approver 10 | No | No | | Approver 10 | |
| Watcher 1 | No | No | | Watcher 1 - User Login to add as watcher | |
| Watcher 2 | No | No | | Watcher 2 | |
| Watcher 3 | No | No | | Watcher 3 | |
| Watcher 4 | No | No | | Watcher 4 | |
| Watcher 5 | No | No | | Watcher 5 | |
| Approver Params | No | No | | semi-colon ; seperated list of parameters. Each parameter begins with an identifier than any needed values seperated by a colon : Example identifiers are first_approver, middle_approvers and last_approver. sample values for these are skip, watcher, or approver. Other examples are escalation:User:&lt;UserLogin&gt;, escalation:ApprovalGroup:&lt;GroupName&gt; where the bracketed values should be replaced by the actual Login or Name. | |
| Validation Message | No | No | | Approval Chain Message / Description | |
| Signatory 1 | No | No | | Signatory 1 - User Login to as signatory | |
| Signatory 2 | No | No | | Signatory 2 | |
| Signatory 3 | No | No | | Signatory 3 | |
| Signatory 4 | No | No | | Signatory 4 | |
| Signatory 5 | No | No | | Signatory 5 | |
| Applies to Supplier | No | No | | Applies to Supplier | |

## Approval Group

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | Yes | Yes | string(255) | Name | |
| Id | No | No | integer | Unique identifier Coupa assigns when a new record is created. It can’t be modified, but can be used to update the record. | |
| Active | No | No | boolean | Whether this Project or Group is currently Active. | |
| Owner | No | No | | Owner group receives notifications on Approval Group errors. Field is called Parent Group in the UI. | |
| Users By Login | No | No | | A semi-colon seperated list of Logins for all users of this project or group. | |
| Users By Employee Number | No | No | | A semi-colon seperated list of Employee Numbers for all users of this project or group. | |
| Description | No | No | | Description | |
