---
title: "Set Up Okta User Provisioning with OAuth 2.0"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/set-up-okta-user-provisioning-with-oauth-2.0"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/set-up-okta-user-provisioning-with-oauth-2.0"
status_code: 200
fetched_at: "2026-04-09T11:59:06+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "OAuth 2.0 and OIDC"
  - "Set Up Okta User Provisioning with OAuth 2.0"
---

# Set Up Okta User Provisioning with OAuth 2.0

Configure the OIDC client for Okta User Provisioning.

## Prerequisites

- Ensure you are currently using Okta user provisioning via API.

- Ensure that the Okta App is on the newest version and that it does not have space for
the API key.

- The person authenticating the integration in Okta must have admin credentials in
Coupa. If not, the system will throw a 404 error when it tries to apply the
redirect.

## Configure the Coupa Platform

- Navigate to **Setup** > **integrations** > **OAuth2/OpenID Connect
Clients**.

- Click **Create**.

- Input the following values and click **Save**.

| **Field** | **Value** |
| --- | --- |
| Grant Type | Authorization Code |
| Name | Any |
| Redirect URL | https://system-admin.okta.com/admin/app/generic/oauth20redirect |
| Shared Secret | Enabled |
| Enable Scopes | core.user.read, core.user.write, offline_access, openid |

## Configure the Okta Application

- Within your Okta Coupa application, select **Enable API integration**.

- Input the following values and click **Save**.

| **Field** | **Value** |
| --- | --- |
| API endpoint | https://{your-instance-name}.coupahost.com/api |
| OAuth client identifier | Located in the OIDC client created in Coupa |
| OAuth client secret | Located in the OIDC client created in Coupa |

## Authentication issues

If you experience a 404 error when attempting to authenticate the API integration, please
check for the following issues:

- The person authenticating the integration in Okta must have admin credentials in
Coupa.

- Make sure that the **Your Coupa instance URL** field on the general tab in the Coupa
application in Okta only contains the name of the instance and not the entire login
URL.

- URL should be: `https://{your-instance-name}.coupahost.com`

- URL should not be:
`https://{your-instance-name}.coupahost.com/session/new`

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Please reach out to Coupa support if you require assistance setting up your OIDC client
in your instance.
