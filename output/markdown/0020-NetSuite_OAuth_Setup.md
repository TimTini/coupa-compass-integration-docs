---
title: "NetSuite OAuth Setup"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/netsuite-oauth-setup"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/netsuite-oauth-setup"
status_code: 200
fetched_at: "2026-04-09T11:59:05+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "OAuth 2.0 and OIDC"
  - "NetSuite OAuth Setup"
---

# NetSuite OAuth Setup

## Create an OAuth account in Coupa for NetSuite

**To set up your Coupa instance with a new connection:**

- Go to **Setup > Integrations > Oauth2/OpenID Connect Clients** and click **Create**.

- For **Grant Type** select **Client credentials.**

- Specify a Name for the Client, Login, Contact info, and Contact Email.

- Select the following scopes to enable the NetSuite bundle:

- core.common.read

- core.common.write

- core.expense.read

- core.expense.write

- core.inventory.receiving.read

- core.inventory.receiving.write

- core.invoice.read

- core.invoice.write

- core.pay.payments.read

- core.pay.payments.write

- core.pay.virtual_cards.read

- core.pay.virtual_cards.write

- core.payables.invoice.read

- core.payables.invoice.write

- core.purchase_order.read

- core.purchase_order.write

- core.supplier.read

- core.supplier.write

- core.payables.order.read

- core.payables.order.write

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Scopes are like a set of permissions set on the API key. In order to implement API permissions with OIDC, we've created several new scopes that provide access to specific functionality for the API.

You can find the list of scopes and their underlying Coupa permissions by going to the Scope management page at `/oauth2/scopes`. When you drill down into a scope, you can see the specific API permissions associated with that scope.

- Click **Save**.

Saving the client gives you values of the client Identifier and Secret which are needed to gain access to the API Scopes you have defined for it. Click Show/Hide to display and copy the Secret.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/ns-oauth-01.png)

We need an access token to be able to access APIs and it only lasts for **24 hours**, so Coupa’s recommendation is to renew the token every 20 hours (like a refresh token). With the Netsuite bundle, it's automated.

## Update to the latest version of the Coupa P2P + Expenses bundle

- Log in to NetSuite and check the client version

- Go to **Customization > SuiteBundler > Search & Install Bundles > List** form the top tool bar.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oracle-01.png)

- Search for *Coupa P2P + Expenses Bundle*.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oracle-02.png)

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

The Bundle version must be 7.0.0 or above to support OAuth

- Upgrade to the latest bundle by clicking the configuration icon () and then selecting **Update**.

The Bundle page opens.

- Set all values in the **PREFERENCE** column to **Do Not Update Deployments** since we don't want to overwrite any script deployment parameters that have already been set up.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oracle-04.png)

- Select **Update Bundle**.

The status changes to **Pending**. Wait for it to finishing updating.

It may take several minutes to update. When it's finished, a green checkmark appears.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

If the update fails, try again. Sometimes NetSuite resources aren’t immediately available and the update fails for no apparent reason.

## General observations

- This process should not overwrite any of your customization in the script deployment or alter the instance credentials.

- Please install it in your sandbox first and confirm the changes aren’t going to impact any of your current processes.

- Review the changes made in the release notes so that you are aware which scripts are being affected and why. This should allow you to better target testing.

## Configure NetSuite to use OAuth instead of API keys

- Go to **Setup > Company > General Preferences** and scroll down to **Customer Preferences**.

- Under the Coupa P2P + Expenses Bundle header, provide the OIDC client identifier and client secret from the previous section. Also include the base URL of your Coupa instance in the form of `https://{your_instance}.coupahost.com`.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oauth-01.png)

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

If any one of the above three fields are missing, NetSuite won't use OAuth to authenticate.

- To remove the API Key from your existing Coupa scripts, go to **Customization > Scripting > Scripts**.

The **Scripts** page opens.

- Under **SCRIPT FILE**, select **- All -** and under **FROM BUNDLE**, select **84306**.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oauth-02.png)

All of the Coupa P2P scripts used by the bundle displayed.

- Select the **Deployments** link for a script.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oauth-03.png)

The Script Deployments page opens.

- Select **Edit** for the deployment and then select **Parameters**.

- Blank out the value for the **COUPA API Key**. Do not change the **COUPA URL**.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oauth-04.png)

- Repeat for each Coupa script shown back in Step 5.

By removing the Coupa API Key from each script, NetSuite won't be able to use keys to access Coupa, and will now need to rely on OAuth.

## Check OAuth logging for each script during testing

- Go to **Customization > Scripting > Scripts**.

The **Scripts** page opens.

- Under **SCRIPT FILE**, select **- All -** and under **FROM BUNDLE**, select **84306**.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oauth-02.png)

All of the Coupa P2P scripts used by the bundle displayed.

- Select the **Deployments** link for a script.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/oauth-03.png)

The Script Deployments page opens.

- Select **Edit** for the deployment and then select **Execution Log**.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/logging-01.png)

Any script that can use OAuth but isn't configured yet has a deprecation notices similar to the ones shown above. These notices dissapear when you've fully implemented OAuth correctly. Then they will show an OAuth response code of 200 instead.
