---
title: "Coupa SAML SSO Setup"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-user-authentication/coupa-saml-sso-setup"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-user-authentication/coupa-saml-sso-setup"
status_code: 200
fetched_at: "2026-04-09T12:01:09+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core User Authentication"
  - "Coupa SAML SSO Setup"
---

# Coupa SAML SSO Setup

Learn how to set up SAML SSO for your Coupa instance.

## Method

- Import initial [stage SP metadata](https://s3.amazonaws.com/sso-metadata-us-east/metadata_stg.xml) ([production SP metadata xml](https://s3.amazonaws.com/sso-metadata-us-east/metadata_prd.xml)) file into stage IdP server.

- - If the IdP does not support Metadata exchange please open the xml file to extract the information.

- Coupa's preferred setup is SP-Init-SSO. Coupa can also setup IdP-Init-SSO, IdP-Init-SSO requires IdP to send the **RelayState** parameter along with SAML request. One way to do this is add a QueryString to AssertionConsumerService in the xml ....`/sp/ACS.saml2?RelayState=https:///sessions/saml_post`. You can change the xml before creating connection.

- Complete the connection setup at IdP.

- Send the following information to Coupa:

- - Metadata: The export the metadata xml from IdP

- If the IdP does not support Metadata exchange, please provide Entity ID (a.k.a Connection ID) and X509 Certificate to verify digital signature in SAML response.

- Login URL: The IdP login page for the user. Required for IdP Initiated SSO. Read FAQ for more details.

- Logout URL: The page Coupa will display when user logout from Coupa application and their session are cleared. This can be internal page, home page or any landing page hosted by customer.

- Test User: Create a test user on IdP to test the connection.

- Coupa to import the IdP metadata and complete the connection from SP to IdP and inform customer.

- The assigned Coupa Administrator to enable users to use SAML.

- Change user settings to enable SAML authentication

- Set "Single Sign-On ID", this is same as NameID passed in SAML request to Coupa, please check with your system administrator on how the NameID is provisioned.

## Enable SSO in Coupa

- Go to https://<your_site>.coupahost.com/administration/security.

- Select **Log in using SAML**.

- Enter **Login Page URL** in the following format:

- - For SP-initiated login:

- For test/staging: https://sso-stg1.coupahost.com/sp/startSSO.ping?PartnerIdpId= <stage_IdP_entityid>&TARGET=https://<your-test_site>.coupahost.com/sessions/saml_post

- For production: https://sso-prd1.coupahost.com/sp/startSSO.ping?PartnerIdpId= <prod_IdP_entityid>&TARGET=https://<your_site>.coupahost.com/sessions/saml_post

- For IdP initiated login:

- Use your IdP login URL

- Supply the **Logout Page URL** if you would like to redirect your users upon logging out of Coupa.

- Supply the **Timeout URL**; it should be the same as your **Login page URL**.
