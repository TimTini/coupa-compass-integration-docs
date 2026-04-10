---
title: "Approvals API (/approvals)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)"
status_code: 200
fetched_at: "2026-04-09T11:59:32+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Approvals API (/approvals)"
---

# Approvals API (/approvals)

Use the approvals API to create, update, or query the approval
of a document. This includes specific endpoints to take action
(reject/hold/approve) as well as requisition details like
requestor, line items, and shipping details.

The URL to access the approvals API is:

```text
https://<instance>/api/approvals/<approval id>
```

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info. To learn more about implementing
remote approvals, see [Remote Approvals via API](https://compass.coupa.com/x294550.xml).

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| PUT | `/api/approvals/:id/approve` | approve | Perform Approve action on an approval |
| PUT | `/api/approvals/:id/hold` | hold | Perform Hold action on an approval |
| GET | `/api/approvals` | index | Query approvals |
| PUT | `/api/approvals/:id/reject` | reject | Perform Reject action on an approval |
| GET | `/api/approvals/:id` | show | Show approval |
| PUT | `/api/approvals/:id` | update | Update approval |

## Elements

These are the elements available for the Approvals API

| **Field Name** | **Field Description** | **Req'd** | **Unique?** | **Allowable Values** | **In** | **Out** | **Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| approvable-id | The document ID that was approved | | | | | yes | integer |
| approvable-type | The document type that was approved (requisition, purchase order, etc) | | | | | yes | string(255) |
| approval-chain-id | ID of the approval chain this approval is located in | | | | | yes | integer |
| approval-date | The date the approval occurred | | | | | yes | datetime |
| approved-by | The user name that made the approval | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| approver | approver | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)), Approval Group |
| approver-id | The user ID that made the approval | | | | | yes | integer |
| approver-type | The role of the approver | | | | | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| delegate | delegate | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)), Approval Group |
| delegate-id | The delegate ID that made the approval (if applicable) | | | | | yes | integer |
| delegates | Delegates | | | | | yes | Delegate Approval |
| holdable | Hold the approval or not | | | | | yes | boolean |
| id | Coupa unique identifier | | | | | yes | integer |
| note | Reason for approval or reject | | | | | yes | text |
| position | The position in the approval chain this approval occurred | | | | | yes | integer |
| reasons | Reasons | | | | | yes | Approval Reason |
| status | The status of the approval (approved, escalated, rejected, etc) | | | | | yes | string(50) |
| type | How the approval occured (override approval, approval chain approval, etc) | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

## Example

In this example, we queried for a single approval with an ID of
12622. We did a GET to the URL:

```text
https://<instance url>/api/approvals/12622
```

## Approvals GET Response

```text
<?xml version="1.0" encoding="UTF-8"?>
<approval>
<id type="integer">12622</id>
<created-at type="datetime">2012-02-15T14:56:22-08:00</created-at>
<updated-at type="datetime">2012-04-23T11:49:25-07:00</updated-at>
<position type="integer">1</position>
<approval-chain-id nil="true" />
<status>approved</status>
<approval-date type="datetime">2012-02-15T14:56:59-08:00</approval-date>
<note />
<type>ManagementHierarchyApproval</type>
<approvable-type>RequisitionHeader</approvable-type>
<approvable-id type="integer">2696</approvable-id>
<approver>
<id type="integer">3</id>
<login>vpierre</login>
<email>upgrade+vp@coupa.com</email>
<employee-number />
<firstname>Victor (CFO)</firstname>
<lastname>Pierre</lastname>
<salesforce-id nil="true" />
</approver>
<created-by>
<id type="integer">9</id>
<login>bjenkins</login>
<email>upgrade+bj@coupa.com</email>
<employee-number />
<firstname>Bob (VP Procurement)</firstname>
<lastname>Jenkins</lastname>
<salesforce-id nil="true" />
</created-by>
<updated-by>
<id type="integer">17</id>
<login>coupa_metrics_gatherer</login>
<email>do_not_reply_metrics@coupa.com</email>
<employee-number nil="true" />
<firstname>Coupa</firstname>
<lastname>Metrics</lastname>
<salesforce-id nil="true" />
</updated-by>
</approval>
```

## Approving or Rejecting

The following describes how you can use the Coupa API to perform
actions on Approvals.

## Approving

`/api/approvals/{id}/approve`

## Rejecting

`/api/approvals/{id}/reject`

## Adding Reason

In both cases, an approval must be Pending (and not already
approved or rejected) for the action to be valid. It is also
possible to provide a "Reason" for the rejection through the XML
request directly. For example, to reject an approval by id of 12612
and provide a reason of "Rejected by Integration", you would use
the following request:

```text
PUT https://{instance url}/api/approvals/12612/reject?reason=Rejected%20by%20Integration
```

Successful requests will return `HTTP 200 Response`. The body of the
response will include the created requisition. Unsuccessful requests will return

```text
HTTP 400 Bad Request
```

. The body of the response will include
validation errors formatted as XML.
