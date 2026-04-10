---
title: "Approvals API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)/approvals-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)/approvals-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Approvals API (/approvals)"
  - "Approvals API Example Calls"
---

# Approvals API Example Calls

## Example

In this example, we queried for a single approval with an ID of 12622. We did a GET to the
URL:
`//.coupahost.com/api/requisitions?status=ordered&created-at[gt]=2010-01-01&created-at[lt]=2010-02-01`

**Approvals GET Response**

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

**Approving or Rejecting**

The following describes how you can use the Coupa API to perform actions on Approvals.

**Approving**

<instance url>/api/approvals/<approval id>/approve

**Rejecting**

<instance url>/api/approvals/<approval id>/reject

**Adding Reason**

In both cases, an approval must be Pending (and not already approved or rejected) for the
action to be valid. It is also possible to provide a "Reason" for the rejection through the
XML request directly. For example, to reject an approval by id of 12612 and provide a reason
of "Rejected by Integration", you would use the following request:

```text
https://<instance url>/api/approvals/12612/reject?reason=Rejected%20by%20Integration
```

Successful requests will return HTTP 200 Response. The body of the response will include
the created requisition. Unsuccessful requests will return HTTP 400 Bad Request. The body of
the response will include validation errors formatted as XML.
