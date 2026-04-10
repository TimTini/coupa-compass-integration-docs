---
title: "Invoices API (/invoices) | Coupa"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)"
content_type: "text/html"
classification: "placeholder"
fetched_at: "2026-04-10T01:57:11+00:00"
---

# Invoices API (/invoices) | Coupa

The discovered page did not expose a standard <article> block, so a placeholder was generated.

**Requested URL:** [https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices))

Page text preview: Invoices API (/invoices) | Coupa

Skip to Content

EN
- EN - English
- DE - Deutsch
- JA - 日本語
- FR - Français

We’ve upgraded our documentation! This page is part of our legacy documentation and is no longer being maintained. Visit the new site for the most up-to-date content, improved search, and all release notes. Take me to the new site

On This Page

- Invoices API (/invoices)
- - Last edited on: 16 July 2025

What can we help you find? Products Coupa Product Documentation Invoices API (/invoices)

Invoices API (/invoices)

Use the invoice API to create, update, or query invoices associated with a purchase order.

Overview

The URL to access invoices is: https://{your_instance_name}/api/invoices

As of Release 29, Coupa has enhanced the invoicing API to be fully functional, on parity with other invoice buyer channels. For more information about this update, see Extended Invoicing API Coverage for Invoice Creation .

See Integration Best Practices for more info.

Note

For invoice_date and original_invoice_date, provide only the date. Avoid adding the timestamp to prevent issues related to credit note linking.

Actions

The Invoices API allows you to:

Verb 	Path 	Action 	Desc
