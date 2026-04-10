---
title: "SAML Basics"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-user-authentication/saml-basics"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-user-authentication/saml-basics"
status_code: 200
fetched_at: "2026-04-09T12:01:08+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core User Authentication"
  - "SAML Basics"
---

# SAML Basics

Introductory information about how Coupa utilizes SAML for SSO.

## Introduction

Coupa supports the use of SAML 2.0 (Security Assertion Markup
Language) for SSO (Single Sign On) support between Coupa and your
Identity Management solution. This allows the user to click on a
link to Coupa and automatically be signed in if they were already
logged in to your SSO.

Once SAML is enabled for your Coupa service you have the ability
to allow some users to bypass SAML and log in using Coupa
credentials. This is a safeguard in case your SAML server is
offline, and an administrator still needed access to Coupa to
disable SAML.

## Advantages

Integrating your Coupa instance through SAML provides several
benefits, including:

- Users do not need to remember a new password for Coupa

- Coupa does not store or maintain password information,
alleviating any audit/risk concerns

- Centralize account control through your Intranet and corporate
standards

- SAML is an industry-accepted standard for SSO

## User Experience

- A user visits a webpage on your Coupa instance.

- Coupa redirects the user to your SSO site for
authentication.

- Your SSO site returns a webpage that directs the user's browser
to post the SAML response to a Coupa-provided URL.

- Coupa verifies the response. Upon success, the
newly-authenticated user will not be required to re-authenticate
with your SSO site until the session times out. The session timeout
can be configured by an administrator
