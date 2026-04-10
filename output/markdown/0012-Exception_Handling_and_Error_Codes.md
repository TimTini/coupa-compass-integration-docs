---
title: "Exception Handling and Error Codes"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/exception-handling-and-error-codes"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/exception-handling-and-error-codes"
status_code: 200
fetched_at: "2026-04-09T11:59:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Get Started with the API"
  - "Exception Handling and Error Codes"
---

# Exception Handling and Error Codes

An exception is thrown when something goes wrong when executing a request. The exception will
contain an error code and may also contain a short description which will help you understand
what went wrong during the request. There are many reasons an exception may occur, below are
some common reasons:

- Your code expects a value from a field that is currently null

- An insert or update statement fails to pass a validation rule

- Assigning a query that returns no records

- Accessing a list index that is out of bounds

For the list of standard HTTP status codes, click here: [https://httpstatuses.com/](https://httpstatuses.com/)

## Query rate limitations

Coupa limits the number of requests made to the
API to 25 requests per second and a burst query limit of 20 calls. So, if you make calls
more quickly than the rate limit, Coupa will querey up to 20 calls.
