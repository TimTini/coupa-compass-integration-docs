---
title: "Tax Rate API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-api"
status_code: 200
fetched_at: "2026-04-09T11:59:24+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Tax Registrations API (/tax_registrations)"
  - "Tax Rate API"
---

# Tax Rate API

## Association

This resource is associated with [Tax Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/tax-line-api) and [Withholding Tax Line API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/withholding-tax-line-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Tax rate is enabled or disabled | | | true, false | yes | yes | boolean |
| country | Country where the tax code is applied | | | | yes | yes | Country |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| customer-accounting | Customer accounting | | | yes, no<br>true, false | yes | yes | boolean |
| effective-date | Date when tax rate is become active | | | | yes | yes | datetime |
| exempt | Whether Tax Rate is exempt or not | | yes | true, false | yes | yes | boolean |
| expiration-date | Date when tax rate is expiring | | | | yes | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| percentage | Tax Rate percentage | yes | yes | | yes | yes | decimal(30,6) |
| reverse-charge | Whether Tax Rate is Reverse Charge or not | | yes | true, false | yes | yes | boolean |
| tax_description | Tax rate description | | | | yes | | string(255) |
| tax-rate-type | Tax rate type | | | | yes | yes | [Tax Rate Type](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-type-api) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| out_of_scope | | | | | yes | yes | boolean |

## API Tax Rate Lookups Use New Attributes

You can now use a combination of business-relevant attributes to look up a **tax rate** when creating or updating tax lines via the **Invoices API**. This enhancement brings the API behavior in line with the CSV upload logic for tax rates.

The Invoices API now supports tax rate lookups using the following fields:

- **id**

- **tax_rate_type** (ID or description)

- **country** (ID or code)

- **percentage**

- **exempt**

- **reverse_charge**

- **out_of_scope**

- **customer_accounting**

The following table describes the valid combination rules.

| **Rule** | **Description** |
| --- | --- |
| **ID Takes Precedence and Requires Validity** | If you provide an **id** in your payload, the system will return the tax rate based only on that **id**. If the **id** is invalid, you get an error, even if other fields are correct. |
| **Require Percentage and Country** | You have to provide at least a **percentage** and a **country**. If either percentage or country is not included, the system will return an error. |
| **Non-Zero Percentage Cannot Be Exempt or Reverse Charge** | If you send a valid combination of fields, the system will try to find and return the matching tax rate. For example, if you send a non-zero percentage along with a valid country, it will look for the matching tax rate. However, if you send a non-zero percentage and also set either **exempt** = true or **reverse_charge** = true, the system will return an error, since these fields cannot be used together. |
| **0% Percentage Determines Standard or Special Rates** | If you set percentage = 0% and don’t set exempt or reverse_charge or set them both to false, the system will return the standard 0% tax rate if it exists. If you set percentage = 0% along with either **exempt** = true or **reverse_charge** = true, the system will return the corresponding exempt or reverse charge tax rate if it’s available. |
| **Require Tax Rate Type for Multiple Types** | For countries that support multiple tax rate types, if you provide the **tax_rate_type,** the system will return the tax rate matching that type. If you don’t provide it, the system will return an error. |
| **Disallow Extra/Unsupported Fields** | If your payload includes any extra fields that aren’t supported, you will get an error. |
| **Default Special Tax Attributes to False** | If you don’t provide values for **exempt**, **reverse_charge**, **out_of_scope**, or **customer_accounting**, they will be treated as false by default. |
| **ID Takes Precedence Over All Other Fields** | If you send both an **id** and a **country** code, the system will use the ID to return the tax rate. Similarly, if you send both an **id** and a **tax_rate_type** description, the ID will take precedence. An invalid **id** will always cause an error, even if other fields are valid. |

Accepted formats examples:

For **tax_rate_type**: either **id** or **description.**

```text
"tax_rate_type": {
"id": "",
"description": ""
}
```

For **country**:  either **id** or **code**

```text
"country": {
"id": "",
"code": ""
}
```

The **example** (json) below shows the **tax_rate** section from the payload.

```text
"tax-rate": {
"percentage": "10",
"country": {
"code": "MX"
},
"tax-rate-type": {
"description": "VAT"
}
}
```

The **example** (xml) below shows the **tax_rate** section from the payload.

```text
<tax-rate>
<percentage>10</percentage>
<exempt type="boolean">false</exempt>
<reverse_charge type="boolean">false</reverse_charge>
<country>
<code>MX</code>
</country>
<tax_rate_type>
<description>VAT</description>
</tax_rate_type>
</tax-rate>
```

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- If no tax rate can be found for the given input, the API will return the error: **Unable to find valid TaxRate record for tax_rate with keys {"percentage"=>"404"}. Possible keys are ["id", "code", "description", "tax_rate_type", "country", "percentage", "exempt", "reverse_charge", "out_of_scope", "customer_accounting"]. Please verify your XML.**

- For invalid percentage values like **123test** or **test123**, **123test** is converted to **123**, while **test123** becomes **0**. The behavior is the same in CSV.
