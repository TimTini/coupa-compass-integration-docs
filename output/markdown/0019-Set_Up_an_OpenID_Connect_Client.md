---
title: "Set Up an OpenID Connect Client"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/set-up-an-openid-connect-client"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/set-up-an-openid-connect-client"
status_code: 200
fetched_at: "2026-04-09T11:59:05+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "OAuth 2.0 and OIDC"
  - "Set Up an OpenID Connect Client"
---

# Set Up an OpenID Connect Client

Configure an OpenID Connect (OIDC) OAuth client to authenticate your users.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

API keys are deprecated. You must transition any existing keys to OAuth clients and revoke the keys under **Setup > API Keys**. This transition only affects customer-created API integrations to the Coupa Core platform, and does not not affect applications such as Treasury, CSO, Supply Chain Design & Planning.

## Create an OAuth client and assign scopes

- Navigate to **Setup > Oauth2/OpenID Connect Clients** (/oauth2/clients).

- Click **Create**.

- Select **Client Credentials** in the **Grant type** dropdown.

- Complete the fields and select the scopes (access permissions) the Client needs.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

If you want to give a client access to all API endpoints and operations, you will need to add all scopes to that client.

- Once you save the client, note the client credentials: **Identifier**, **Secret**, **Oidc Scopes**.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oath_client_info.jpg)

## Generate access token

Send a request to the OAuth client using an HTTP client like Postman in order to generate an access token. You can also send a cURL request using your terminal.

- If using the terminal, use the command line to perform a Curl POST:

```text
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "client_id=
<CLIENT_ID>
&grant_type=client_credentials&scope=
<SPACE_SEPARATED_LIST_OF_SCOPES>
&client_secret=
<CLIENT_SECRET>
"
https://<INSTANCE_DOMAIN>/oauth2/token
```

- If using an HTTP Client like Postman or another REST Client, configure an OAuth2/OIDC Client connection to use the Coupa API.

- Select **POST**.

- Set the URL to the instance name where you defined the Client above. For example: https://{your_instance_address}/oauth2/token.

- Set the headers key value for Content-Type = `application/x-www-form-urlencoded`

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/Content-Type_POST_example.png)

- In the POST body set the following values:

- **client_id** = <Your Client Identifier value>

- **grant_type** = `client_credentials`

- **scope** = <Copy/paste all the scopes that you selected in Client credentials setup without the comma.>

- **client_secret** = <Copy/paste the **Coupa Client Secret** value> ![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/POST_body_settings.png)

- Click **Send**. The POST response has the `access_token` that was generated to authorize API calls within the defined scope for the next 24 hours ( `expires_in` 86,399 seconds).

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/POST_response_example.png)

- Copy your `access_token` value from the response body and use it as the **Token value** in **Authorization** headers for your Coupa API calls within the scope you defined for this Client connection.

- Create a new tab to make API calls to GET, POST, or PUT etc. and in the **Authorization** part of the request builder define the ‘TYPE’ = OAuth 2.0.

- Paste the `access_token` as the **Token** field value.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/Token_field_value_example.png)

- Go to **Headers** and enter a value of `application/xml` or `application/json` in the **Accept key** field. Define the other request parameters according to the call and the interface you are attempting to use.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/Accept_key_field_example.png)

- Click **Send**. With that `access_token` set in the **Authorization** header you can make GET, PUT or POST calls to the Client scopes you defined for that connection.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/Successful_request_example.png)

## Build Middleware script/flow for token creation and refresh every 20 hours

Depending on the middleware, configurations may vary. However, it is important to ensure that all integrations using Coupa API keys are updated to use the OAuth token. To generate and refresh this token, a new script/flow might need to be created to ensure this is updated every 20 hours. Most of the adapters in the middlewares will refresh the token automatically once the setup is done.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Warning:

Changing the scopes in a Client will impact the token generation script/adapter since these are passed in the token generation request.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/Flow_example.png)

## Update Integrations to use new token generated by script

All existing integrations must adopt the OAuth connection and use the token generated by the new script/flow. This can be done in phases, for example, where master data integrations are transitioned first followed by transactional data integrations at a later stage.
