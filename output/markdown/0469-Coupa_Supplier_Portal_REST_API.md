---
title: "Coupa Supplier Portal REST API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-supplier-portal-rest-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-supplier-portal-rest-api"
status_code: 200
fetched_at: "2026-04-09T12:00:54+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Supplier Portal REST API"
---

# Coupa Supplier Portal REST API

The Coupa Supplier Portal (CSP) REST API allows you to integrate CSP data with third-party systems.

The API allows you to retrieve CSP data. Using this API, you can:

- Retrieve all invoices in the CSP.

- Retrieve data for a single CSP invoice.

## Requirements

- This feature is available upon request for [Coupa Advanced](https://compass.coupa.com/en-us/products/product-documentation/supplier-resources/for-suppliers/core-supplier-onboarding/get-started-with-the-csp/programs-for-you/coupa-advanced) Suppliers. Reach out to Coupa for more information.

- The Coupa Supplier Portal REST API feature consumes tokens. For more information, see [Tokens in the Coupa Supplier Portal.](https://compass.coupa.com/en-us/products/product-documentation/supplier-resources/for-suppliers/coupa-supplier-portal/set-up-the-csp/invoices/tokens-in-the-coupa-supplier-portal)

## Authentication

The CSP API uses OAuth 2.0 and requires creating an OAuth 2.0 client in the CSP and authenticating directly with your CSP instance. For more information, see [Set Up Authentication for the Coupa Supplier Portal REST API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-supplier-portal-rest-api/set-up-authentication-for-the-coupa-supplier-portal-rest-api).

## Base URL

The API uses your CSP URL, for example: 

`https://supplier.coupahost.com/api/v1/invoices`

- [Set Up Authentication for the Coupa Supplier Portal REST API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-supplier-portal-rest-api/set-up-authentication-for-the-coupa-supplier-portal-rest-api)

Create an OAuth 2.0 client and generate an access token in the Coupa Supplier Portal. Use the access token to access CSP data using the CSP REST API.

- [GET Invoices](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-supplier-portal-rest-api/get-invoices)

Use the Coupa Supplier Portal (CSP) REST API to access invoice data in the CSP.
