---
title: "Account Allocations API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-validation-rules-api-(account_validation_rules)/account-allocations-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-validation-rules-api-(account_validation_rules)/account-allocations-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:07+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Account Validation Rules API (/account_validation_rules)"
  - "Account Allocations API Example Calls"
---

# Account Allocations API Example Calls

## Account Allocations GET

Our Account Allocations API allows you to query against a number
of core attributes on the account allocations record.

This is the URL you use to query account information

- `https:///api/accounts`

- Typically you would use one of the account allocation
segments or account allocation code to find the account allocations
id in order to use the GET

Successful requests will return HTTP 200 OK. The body of the
response will include the accounts allocations matching your search
criteria. Unsuccessful requests will return HTTP 404 Not Found. The
error message will indicate no results matching your search
criteria.

## Account Allocations POST

Our Account Allocations API allows you to create an account
allocations in Coupa.

This is the URL you can POST this information to:

- `https:///api/accounts`

Successful requests will return HTTP 200 Created. The body of
the response will include the account allocations that was created,
including the ID if you needed to do further processing.

Unsuccessful requests will return HTTP 400 Bad Request. The body
of the response will include validation errors formatted as
XML.

## Account Allocations PUT

Our Account Allocations API allows you to update an existing
account allocations in Coupa.

This is the URL you can PUT this information to:

- ```text
https://<instance url>/api/accountAllocations
```

- Typically you would use one of the account allocations segments
or account allocations code to find the account id in order to use
the PUT

Successful requests will return HTTP 200 OK. The body of the
response will include the account allocations that was just
updated.

Unsuccessful requests will return HTTP 400 Bad Request. The body
of the response will include validation errors formatted as
XML.
