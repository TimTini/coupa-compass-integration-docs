---
title: "Sample Requests/Responses - XML vs JSON"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/sample-requestsresponses-xml-vs-json"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/sample-requestsresponses-xml-vs-json"
status_code: 200
fetched_at: "2026-04-09T11:59:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Get Started with the API"
  - "Sample Requests/Responses - XML vs JSON"
---

# Sample Requests/Responses - XML vs JSON

Below are examples of JSON and XML requests and responses, using the User object as an
example. The responses can be long, so use the table of contents below to skip to the desired
sections.

## User List

url: [http://dashmaster17-0.coupadev.com/api/users?limit=2](http://dashmaster17-0.coupadev.com/api/users?limit=2)

method: GET

## JSON response

```text
[
{	 "id": 771,
"created-at": "2016-11-08T11:28:50+02:00",
"updated-at": "2016-11-09T16:35:40+02:00",
"login": "testuser1",
"email": "adf@gmail.com",
"purchasing-user": true,
"expense-user": false,
"sourcing-user": false,
"inventory-user": false,
"employee-number": "",
"firstname": "text",
"lastname": "abc",
"fullname": "text abc",
"api-user": false,
"active": true,
"salesforce-id": null,
"account-security-type": 0,
"authentication-method": "coupa_credentials",
"sso-identifier": "899",
"default-locale": "en",
"business-group-security-type": 1,
"edit-invoice-on-quick-entry": false,
"avatar-thumb-url": null,
"mention-name": "text12",
"gpo-entity": "",
"radio-button-test": null,
"subsidary": "",
"function": "",
"seg3default": "",
"phone-work": null,
"phone-mobile": null,
"roles": [
{			 "id": 2,
"created-at": "2011-08-05T19:46:31+03:00",
"updated-at": "2011-08-05T19:46:31+03:00",
"name": "Admin",
"description": "Full system access to setup and maintain the application",
"omnipotent": true,
"system-role": true,
"updated-by": {				 "id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"created-by": null
},
{			 "id": 3,
"created-at": "2011-08-05T19:46:31+03:00",
"updated-at": "2011-08-05T19:46:31+03:00",
"name": "User",
"description": "Standard role for all users who need to create and/or approve requisitions",
"omnipotent": false,
"system-role": true,
"updated-by": {				 "id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"created-by": null
}	 ],
"manager": {		 "id": 629,
"login": "gunab",
"firstname": "gunab",
"lastname": "buyer",
"employee-number": "",
"email": "catestit8@gmail.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-11-01T17:07:03+02:00",
"updated-at": "2016-11-09T09:40:36+02:00"
},
"default-address": null,
"default-account": null,
"default-account-type": null,
"default-currency": {		 "id": 1,
"code": "USD",
"decimals": 2,
"updated-by": {			 "id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-16T01:05:17+03:00",
"updated-at": "2016-03-30T12:35:20+03:00"
}	 },
"pcard": null,
"department": null,
"requisition-approval-limit": {		 "id": 35,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED",
"amount": "0.00",
"subject": "requisition_header",
"currency": {			 "id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null
},
"created-by": {			 "id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"expense-approval-limit": {
"id": 36,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED (2)",
"amount": "0.00",
"subject": "expense_report",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"invoice-approval-limit": {
"id": 37,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED (3)",
"amount": "0.00",
"subject": "invoice_header",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null
},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"requisition-self-approval-limit": {
"id": 35,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED",
"amount": "0.00",
"subject": "requisition_header",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"expense-self-approval-limit": {
"id": 36,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED (2)",
"amount": "0.00",
"subject": "expense_report",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"expenses-delegated-to": [],
"can-expense-for": [],
"content-groups": [],
"account-groups": [],
"approval-groups": [],
"working-warehouses": [],
"inventory-organizations": [],
"created-by": {
"id": 224,
"login": "sneha.latha@coupa.com",
"firstname": "Sneha",
"lastname": "Latha",
"employee-number": null,
"email": "sneha.latha@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-12T09:20:37+03:00",
"updated-at": "2016-11-14T09:21:00+02:00"
},
"updated-by": {
"id": 228,
"login": "kuppusamy.sekaran@coupa.com",
"firstname": "Kuppusamy",
"lastname": "Sekaran",
"employee-number": null,
"email": "kuppusamy.sekaran@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-12T11:42:59+03:00",
"updated-at": "2016-11-14T10:59:24+02:00"
},
"custom-field-8": null,
"custom-field-7": null,
"username1": null

},
{
"id": 808,
"created-at": "2016-11-10T02:55:30+02:00",
"updated-at": "2016-11-11T00:52:43+02:00",
"login": "pfiuser1",
"email": "aditya+r17-pfiuser@coupa.com",
"purchasing-user": true,
"expense-user": false,
"sourcing-user": false,
"inventory-user": false,
"employee-number": "",
"firstname": "PFI",
"lastname": "User",
"fullname": "PFI User",
"api-user": false,
"active": true,
"salesforce-id": null,
"account-security-type": 0,
"authentication-method": "coupa_credentials",
"sso-identifier": "pfiuser1",
"default-locale": "en",
"business-group-security-type": 0,
"edit-invoice-on-quick-entry": false,
"avatar-thumb-url": null,
"mention-name": "pfiuser",
"gpo-entity": "",
"radio-button-test": null,
"subsidary": "",
"function": "",
"seg3default": "",
"phone-work": null,
"phone-mobile": null,
"roles": [

{
"id": 3,
"created-at": "2011-08-05T19:46:31+03:00",
"updated-at": "2011-08-05T19:46:31+03:00",
"name": "User",
"description": "Standard role for all users who need to create and/or approve requisitions",
"omnipotent": false,
"system-role": true,
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"created-by": null

},
{
"id": 10153,
"created-at": "2016-11-11T00:52:22+02:00",
"updated-at": "2016-11-11T00:52:22+02:00",
"name": "Analytics Only",
"description": "",
"omnipotent": false,
"system-role": false,
"updated-by": {
"id": 475,
"login": "justin.mehta@coupa.com",
"firstname": "Justin",
"lastname": "Mehta",
"employee-number": null,
"email": "justin.mehta@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-20T20:55:27+03:00",
"updated-at": "2016-11-14T09:56:55+02:00"
},
"created-by": {
"id": 475,
"login": "justin.mehta@coupa.com",
"firstname": "Justin",
"lastname": "Mehta",
"employee-number": null,
"email": "justin.mehta@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-20T20:55:27+03:00",
"updated-at": "2016-11-14T09:56:55+02:00"
}
}
],
"manager": null,
"default-address": null,
"default-account": null,
"default-account-type": null,
"default-currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"pcard": null,
"department": null,
"requisition-approval-limit": {
"id": 35,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED",
"amount": "0.00",
"subject": "requisition_header",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"expense-approval-limit": {
"id": 36,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED (2)",
"amount": "0.00",
"subject": "expense_report",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"invoice-approval-limit": {
"id": 37,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED (3)",
"amount": "0.00",
"subject": "invoice_header",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"requisition-self-approval-limit": {
"id": 35,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED",
"amount": "0.00",
"subject": "requisition_header",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"expense-self-approval-limit": {
"id": 36,
"created-at": "2016-04-01T09:08:38+03:00",
"updated-at": "2016-04-01T09:08:38+03:00",
"name": "0.00 AED (2)",
"amount": "0.00",
"subject": "expense_report",
"currency": {
"id": 156,
"code": "AED",
"decimals": 2,
"updated-by": null

},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"expenses-delegated-to": [],
"can-expense-for": [],
"content-groups": [],
"account-groups": [],
"approval-groups": [],
"working-warehouses": [],
"inventory-organizations": [],
"created-by": {
"id": 390,
"login": "aditya.mandavilli@coupa.com",
"firstname": "Aditya",
"lastname": "Mandavilli",
"employee-number": null,
"email": "aditya.mandavilli@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-17T20:24:54+03:00",
"updated-at": "2016-11-14T01:40:08+02:00"
},
"updated-by": {
"id": 475,
"login": "justin.mehta@coupa.com",
"firstname": "Justin",
"lastname": "Mehta",
"employee-number": null,
"email": "justin.mehta@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-20T20:55:27+03:00",
"updated-at": "2016-11-14T09:56:55+02:00"
},
"custom-field-8": null,
"custom-field-7": null,
"username1": null
}
]
```

## XML Response

```text
<?xml version="1.0" encoding="UTF-8"?><users type="array">
<user>
<id type="integer">771</id>
<created-at type="dateTime">2016-11-08T11:28:50+02:00</created-at>
<updated-at type="dateTime">2016-11-09T16:35:40+02:00</updated-at>
<login>testuser1</login>
<email>adf@gmail.com</email>
<purchasing-user type="boolean">true</purchasing-user>
<expense-user type="boolean">false</expense-user>
<sourcing-user type="boolean">false</sourcing-user>
<inventory-user type="boolean">false</inventory-user>
<employee-number />
<firstname>text</firstname>
<lastname>abc</lastname>
<fullname>text abc</fullname>
<api-user type="boolean">false</api-user>
<active type="boolean">true</active>
<salesforce-id nil="true" />
<account-security-type type="integer">0</account-security-type>
<authentication-method type="symbol">coupa_credentials</authentication-method>
<sso-identifier>899</sso-identifier>
<default-locale>en</default-locale>
<business-group-security-type type="integer">1</business-group-security-type>
<edit-invoice-on-quick-entry type="boolean">false</edit-invoice-on-quick-entry>
<avatar-thumb-url nil="true" />
<mention-name>text12</mention-name>
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
<roles type="array">
<role>
<id type="integer">2</id>
<created-at type="dateTime">2011-08-05T19:46:31+03:00</created-at>
<updated-at type="dateTime">2011-08-05T19:46:31+03:00</updated-at>
<name>Admin</name>
<description>Full system access to setup and maintain the application</description>
<omnipotent type="boolean">true</omnipotent>
<system-role type="boolean">true</system-role>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</role>
<role>
<id type="integer">3</id>
<created-at type="dateTime">2011-08-05T19:46:31+03:00</created-at>
<updated-at type="dateTime">2011-08-05T19:46:31+03:00</updated-at>
<name>User</name>
<description>Standard role for all users who need to create and/or approve requisitions</description>
<omnipotent type="boolean">false</omnipotent>
<system-role type="boolean">true</system-role>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</role>
</roles>
<manager>
<id type="integer">629</id>
<login>gunab</login>
<email>catestit8@gmail.com</email>
<employee-number />
<firstname>gunab</firstname>
<lastname>buyer</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</manager>
<default-currency>
<id type="integer">1</id>
<code>USD</code>
<decimals type="integer">2</decimals>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true" />
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</default-currency>
<requisition-approval-limit>
<id type="integer">35</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED</name>
<amount type="decimal">0.00</amount>
<subject>requisition_header</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</requisition-approval-limit>
<expense-approval-limit>
<id type="integer">36</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED (2)</name>
<amount type="decimal">0.00</amount>
<subject>expense_report</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</expense-approval-limit>
<invoice-approval-limit>
<id type="integer">37</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED (3)</name>
<amount type="decimal">0.00</amount>
<subject>invoice_header</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</invoice-approval-limit>
<requisition-self-approval-limit>
<id type="integer">35</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED</name>
<amount type="decimal">0.00</amount>
<subject>requisition_header</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</requisition-self-approval-limit>
<expense-self-approval-limit>
<id type="integer">36</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED (2)</name>
<amount type="decimal">0.00</amount>
<subject>expense_report</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</expense-self-approval-limit>
<expenses-delegated-to type="array" />
<can-expense-for type="array" />
<content-groups type="array" />
<account-groups type="array" />
<approval-groups type="array" />
<working-warehouses type="array" />
<inventory-organizations type="array" />
<created-by>
<id type="integer">224</id>
<login>sneha.latha@coupa.com</login>
<email>sneha.latha@coupa.com</email>
<employee-number nil="true" />
<firstname>Sneha</firstname>
<lastname>Latha</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">228</id>
<login>kuppusamy.sekaran@coupa.com</login>
<email>kuppusamy.sekaran@coupa.com</email>
<employee-number nil="true" />
<firstname>Kuppusamy</firstname>
<lastname>Sekaran</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</user>
<user>
<id type="integer">808</id>
<created-at type="dateTime">2016-11-10T02:55:30+02:00</created-at>
<updated-at type="dateTime">2016-11-11T00:52:43+02:00</updated-at>
<login>pfiuser1</login>
<email>aditya+r17-pfiuser@coupa.com</email>
<purchasing-user type="boolean">true</purchasing-user>
<expense-user type="boolean">false</expense-user>
<sourcing-user type="boolean">false</sourcing-user>
<inventory-user type="boolean">false</inventory-user>
<employee-number />
<firstname>PFI</firstname>
<lastname>User</lastname>
<fullname>PFI User</fullname>
<api-user type="boolean">false</api-user>
<active type="boolean">true</active>
<salesforce-id nil="true" />
<account-security-type type="integer">0</account-security-type>
<authentication-method type="symbol">coupa_credentials</authentication-method>
<sso-identifier>pfiuser1</sso-identifier>
<default-locale>en</default-locale>
<business-group-security-type type="integer">0</business-group-security-type>
<edit-invoice-on-quick-entry type="boolean">false</edit-invoice-on-quick-entry>
<avatar-thumb-url nil="true" />
<mention-name>pfiuser</mention-name>
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
<roles type="array">
<role>
<id type="integer">3</id>
<created-at type="dateTime">2011-08-05T19:46:31+03:00</created-at>
<updated-at type="dateTime">2011-08-05T19:46:31+03:00</updated-at>
<name>User</name>
<description>Standard role for all users who need to create and / or approve requisitions</description>
<omnipotent type="boolean">false</omnipotent>
<system-role type="boolean">true</system-role>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</role>
<role>
<id type="integer">10153</id>
<created-at type="dateTime">2016-11-11T00:52:22+02:00</created-at>
<updated-at type="dateTime">2016-11-11T00:52:22+02:00</updated-at>
<name>Analytics Only</name>
<description />
<omnipotent type="boolean">false</omnipotent>
<system-role type="boolean">false</system-role>
<created-by>
<id type="integer">475</id>
<login>justin.mehta@coupa.com</login>
<email>justin.mehta@coupa.com</email>
<employee-number nil="true" />
<firstname>Justin</firstname>
<lastname>Mehta</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">475</id>
<login>justin.mehta@coupa.com</login>
<email>justin.mehta@coupa.com</email>
<employee-number nil="true" />
<firstname>Justin</firstname>
<lastname>Mehta</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</role>
</roles>
<default-currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</default-currency>
<requisition-approval-limit>
<id type="integer">35</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED</name>
<amount type="decimal">0.00</amount>
<subject>requisition_header</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</requisition-approval-limit>
<expense-approval-limit>
<id type="integer">36</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED (2)</name>
<amount type="decimal">0.00</amount>
<subject>expense_report</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</expense-approval-limit>
<invoice-approval-limit>
<id type="integer">37</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED (3)</name>
<amount type="decimal">0.00</amount>
<subject>invoice_header</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</invoice-approval-limit>
<requisition-self-approval-limit>
<id type="integer">35</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED</name>
<amount type="decimal">0.00</amount>
<subject>requisition_header</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</requisition-self-approval-limit>
<expense-self-approval-limit>
<id type="integer">36</id>
<created-at type="dateTime">2016-04-01T09:08:38+03:00</created-at>
<updated-at type="dateTime">2016-04-01T09:08:38+03:00</updated-at>
<name>0.00 AED (2)</name>
<amount type="decimal">0.00</amount>
<subject>expense_report</subject>
<currency>
<id type="integer">156</id>
<code>AED</code>
<decimals type="integer">2</decimals>
</currency>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</expense-self-approval-limit>
<expenses-delegated-to type="array" />
<can-expense-for type="array" />
<content-groups type="array" />
<account-groups type="array" />
<approval-groups type="array" />
<working-warehouses type="array" />
<inventory-organizations type="array" />
<created-by>
<id type="integer">390</id>
<login>aditya.mandavilli@coupa.com</login>
<email>aditya.mandavilli@coupa.com</email>
<employee-number nil="true" />
<firstname>Aditya</firstname>
<lastname>Mandavilli</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</created-by>
<updated-by>
<id type="integer">475</id>
<login>justin.mehta@coupa.com</login>
<email>justin.mehta@coupa.com</email>
<employee-number nil="true" />
<firstname>Justin</firstname>
<lastname>Mehta</lastname>
<salesforce-id nil="true" />
<avatar-thumb-url nil="true" />
<custom-field-8 />
<custom-field-7 />
<gpo-entity />
<radio-button-test />
<subsidary />
<function />
<seg3default />
<username1 />
</updated-by>
</user></users>
```

## User Show

url: [http://dashmaster17-0.coupadev.com/api/users/5](http://dashmaster17-0.coupadev.com/api/users/5)

method: GET

## JSON Response

```text
{
"id": 5,
"created-at": "2008-10-27T22:54:10+02:00",
"updated-at": "2013-04-19T22:02:26+03:00",
"login": "tkennedy",
"email": "upgrade+tk@coupa.com",
"purchasing-user": true,
"expense-user": false,
"sourcing-user": false,
"inventory-user": false,
"employee-number": "",
"firstname": "Tommy (Sales Lead)",
"lastname": "Kennedy",
"fullname": "Tommy (Sales Lead) Kennedy",
"api-user": false,
"active": true,
"salesforce-id": null,
"account-security-type": 0,
"authentication-method": "coupa_credentials",
"sso-identifier": "",
"default-locale": null,
"business-group-security-type": 1,
"edit-invoice-on-quick-entry": false,
"avatar-thumb-url": null,
"mention-name": "tommy(saleslead)kennedy",
"gpo-entity": "",
"radio-button-test": null,
"subsidary": null,
"function": null,
"seg3default": null,
"phone-work": {
"id": 5,
"created-at": "2008-10-27T22:54:10+02:00",
"updated-at": "2012-12-14T00:27:57+02:00",
"country-code": "1",
"area-code": "650",
"number": "5856306",
"extension": null,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"phone-mobile": {
"id": 30,
"created-at": "2008-10-28T19:59:47+02:00",
"updated-at": "2012-12-14T00:27:57+02:00",
"country-code": "1",
"area-code": "650",
"number": "5856306",
"extension": null,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"roles": [
{
"id": 3,
"created-at": "2011-08-05T19:46:31+03:00",
"updated-at": "2011-08-05T19:46:31+03:00",
"name": "User",
"description": "Standard role for all users who need to create and/or approve requisitions",
"omnipotent": false,
"system-role": true,
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
{
"id": 8,
"created-at": "2011-08-05T19:46:31+03:00",
"updated-at": "2012-07-31T19:40:04+03:00",
"name": "Edit Requisition as Approver",
"description": "Adds ability to edit a requisition when you are approving it",
"omnipotent": false,
"system-role": true,
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
}
],
"manager": {
"id": 4,
"login": "sjones",
"firstname": "Sally (Sales VP)",
"lastname": "Jones",
"employee-number": "",
"email": "upgradet+sj@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2008-10-27T22:54:10+02:00",
"updated-at": "2016-10-21T21:47:04+03:00"
},
"default-address": {
"id": 16,
"created-at": "2008-10-27T22:00:19+02:00",
"updated-at": "2016-11-10T07:42:35+02:00",
"name": "HQ",
"location-code": null,
"street1": "28 Nevada Blvd",
"street2": "",
"city": "Laughlin",
"state": "NV",
"postal-code": "89028",
"attention": "",
"active": true,
"business-group-name": "Everyone",
"vat-number": null,
"local-tax-number": null,
"country": {
"id": 223,
"code": "US",
"name": "United States"
},
"vat-country": null,
"content-groups": [
{
"id": 1,
"created-at": "2006-08-28T05:40:04+03:00",
"updated-at": "2015-08-17T11:07:10+03:00",
"name": "Everyone",
"description": "All users can see documents assigned to this group",
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-16T01:05:17+03:00",
"updated-at": "2016-03-30T12:35:20+03:00"
}
}
],
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 157,
"login": "vijayashree.christopher@coupa.com",
"firstname": "vijayashree",
"lastname": "Christopher",
"employee-number": null,
"email": "vijayashree.christopher@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-11T08:02:51+03:00",
"updated-at": "2016-11-14T08:43:47+02:00"
}
},
"default-account": {
"id": null,
"created-at": null,
"updated-at": null,
"name": null,
"code": "SF-Sales-Indirect",
"active": true,
"segment-1": "SF",
"segment-2": "Sales",
"segment-3": "Indirect",
"segment-4": null,
"segment-5": null,
"segment-6": null,
"segment-7": null,
"segment-8": null,
"segment-9": null,
"segment-10": null,
"segment-11": null,
"segment-12": null,
"segment-13": null,
"segment-14": null,
"segment-15": null,
"segment-16": null,
"segment-17": null,
"segment-18": null,
"segment-19": null,
"segment-20": null,
"account-type": {
"id": 1,
"created-at": "2008-10-27T22:10:01+02:00",
"updated-at": "2016-11-08T20:56:40+02:00",
"name": "Ace Corporate",
"active": true,
"currency": {
"id": 1,
"code": "USD",
"decimals": 2,
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-16T01:05:17+03:00",
"updated-at": "2016-03-30T12:35:20+03:00"
}
},
"primary-contact": {
"id": 14,
"created-at": "2008-10-27T22:10:01+02:00",
"updated-at": "2016-11-08T20:56:40+02:00",
"email": "upgrade@coupa.com",
"name-prefix": null,
"name-suffix": null,
"name-additional": null,
"name-given": "xxx",
"name-family": "yyy",
"name-fullname": null,
"notes": null,
"phone-work": null,
"phone-mobile": null,
"phone-fax": null,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 195,
"login": "tim.durkin@coupa.com",
"firstname": "Timothy",
"lastname": "Durkin",
"employee-number": null,
"email": "tim.durkin@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-11T19:30:34+03:00",
"updated-at": "2016-11-10T18:18:36+02:00"
}
},
"primary-address": {
"id": 184,
"created-at": "2008-10-27T22:10:01+02:00",
"updated-at": "2016-11-08T20:56:40+02:00",
"name": "xxx yyy",
"location-code": null,
"street1": "2 W 5th Ave",
"street2": "Suite 300",
"city": "San Mateo",
"state": "CA",
"postal-code": "94404",
"attention": null,
"active": true,
"business-group-name": null,
"vat-number": "465456645",
"local-tax-number": "",
"country": {
"id": 22,
"code": "BE",
"name": "Belgium"
},
"vat-country": {
"id": 223,
"code": "US",
"name": "United States"
},
"content-groups": [],
"created-by": {
"id": 122,
"login": "matthew.otzwirk@coupa.com",
"firstname": "Matthew",
"lastname": "Otzwirk",
"employee-number": null,
"email": "matthew.otzwirk@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-04-27T20:54:43+03:00",
"updated-at": "2016-11-09T23:23:32+02:00"
},
"updated-by": {
"id": 195,
"login": "tim.durkin@coupa.com",
"firstname": "Timothy",
"lastname": "Durkin",
"employee-number": null,
"email": "tim.durkin@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-11T19:30:34+03:00",
"updated-at": "2016-11-10T18:18:36+02:00"
}
},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 195,
"login": "tim.durkin@coupa.com",
"firstname": "Timothy",
"lastname": "Durkin",
"employee-number": null,
"email": "tim.durkin@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-11T19:30:34+03:00",
"updated-at": "2016-11-10T18:18:36+02:00"
}
}
},
"default-account-type": {
"id": 1,
"created-at": "2008-10-27T22:10:01+02:00",
"updated-at": "2016-11-08T20:56:40+02:00",
"name": "Ace Corporate",
"active": true,
"currency": {
"id": 1,
"code": "USD",
"decimals": 2,
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-16T01:05:17+03:00",
"updated-at": "2016-03-30T12:35:20+03:00"
}
},
"primary-contact": {
"id": 14,
"created-at": "2008-10-27T22:10:01+02:00",
"updated-at": "2016-11-08T20:56:40+02:00",
"email": "upgrade@coupa.com",
"name-prefix": null,
"name-suffix": null,
"name-additional": null,
"name-given": "xxx",
"name-family": "yyy",
"name-fullname": null,
"notes": null,
"phone-work": null,
"phone-mobile": null,
"phone-fax": null,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 195,
"login": "tim.durkin@coupa.com",
"firstname": "Timothy",
"lastname": "Durkin",
"employee-number": null,
"email": "tim.durkin@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-11T19:30:34+03:00",
"updated-at": "2016-11-10T18:18:36+02:00"
}
},
"primary-address": {
"id": 184,
"created-at": "2008-10-27T22:10:01+02:00",
"updated-at": "2016-11-08T20:56:40+02:00",
"name": "xxx yyy",
"location-code": null,
"street1": "2 W 5th Ave",
"street2": "Suite 300",
"city": "San Mateo",
"state": "CA",
"postal-code": "94404",
"attention": null,
"active": true,
"business-group-name": null,
"vat-number": "465456645",
"local-tax-number": "",
"country": {
"id": 22,
"code": "BE",
"name": "Belgium"
},
"vat-country": {
"id": 223,
"code": "US",
"name": "United States"
},
"content-groups": [],
"created-by": {
"id": 122,
"login": "matthew.otzwirk@coupa.com",
"firstname": "Matthew",
"lastname": "Otzwirk",
"employee-number": null,
"email": "matthew.otzwirk@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-04-27T20:54:43+03:00",
"updated-at": "2016-11-09T23:23:32+02:00"
},
"updated-by": {
"id": 195,
"login": "tim.durkin@coupa.com",
"firstname": "Timothy",
"lastname": "Durkin",
"employee-number": null,
"email": "tim.durkin@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-11T19:30:34+03:00",
"updated-at": "2016-11-10T18:18:36+02:00"
}
},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 195,
"login": "tim.durkin@coupa.com",
"firstname": "Timothy",
"lastname": "Durkin",
"employee-number": null,
"email": "tim.durkin@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-11T19:30:34+03:00",
"updated-at": "2016-11-10T18:18:36+02:00"
}
},
"default-currency": {
"id": 1,
"code": "USD",
"decimals": 2,
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-16T01:05:17+03:00",
"updated-at": "2016-03-30T12:35:20+03:00"
}
},
"department": {
"id": 2,
"created-at": "2008-10-27T22:00:53+02:00",
"updated-at": "2010-03-24T06:03:22+02:00",
"name": "Sales",
"active": true,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
},
"expenses-delegated-to": [],
"can-expense-for": [],
"content-groups": [],
"account-groups": [],
"approval-groups": [],
"working-warehouses": [],
"inventory-organizations": [],
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T16:01:34+02:00",
"updated-at": "2016-10-28T11:14:12+03:00"
}
}
```

## XML response

```text
<?xml version="1.0" encoding="UTF-8"?>
<user>
<id type="integer">5</id>
<created-at type="dateTime">2008-10-27T22:54:10+02:00</created-at>
<updated-at type="dateTime">2013-04-19T22:02:26+03:00</updated-at>
<login>tkennedy</login>
<email>upgrade+tk@coupa.com</email>
<purchasing-user type="boolean">true</purchasing-user>
<expense-user type="boolean">false</expense-user>
<sourcing-user type="boolean">false</sourcing-user>
<inventory-user type="boolean">false</inventory-user>
<employee-number></employee-number>
<firstname>Tommy (Sales Lead)</firstname>
<lastname>Kennedy</lastname>
<fullname>Tommy (Sales Lead) Kennedy</fullname>
<api-user type="boolean">false</api-user>
<active type="boolean">true</active>
<salesforce-id nil="true"/>
<account-security-type type="integer">0</account-security-type>
<authentication-method type="symbol">coupa_credentials</authentication-method>
<sso-identifier></sso-identifier>
<default-locale nil="true"/>
<business-group-security-type type="integer">1</business-group-security-type>
<edit-invoice-on-quick-entry type="boolean">false</edit-invoice-on-quick-entry>
<avatar-thumb-url nil="true"/>
<mention-name>tommy(saleslead)kennedy</mention-name>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
<phone-work>
<id type="integer">5</id>
<created-at type="dateTime">2008-10-27T22:54:10+02:00</created-at>
<updated-at type="dateTime">2012-12-14T00:27:57+02:00</updated-at>
<country-code>1</country-code>
<area-code>650</area-code>
<number>5856306</number>
<extension nil="true"/>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</phone-work>
<phone-mobile>
<id type="integer">30</id>
<created-at type="dateTime">2008-10-28T19:59:47+02:00</created-at>
<updated-at type="dateTime">2012-12-14T00:27:57+02:00</updated-at>
<country-code>1</country-code>
<area-code>650</area-code>
<number>5856306</number>
<extension nil="true"/>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</phone-mobile>
<roles type="array">
<role>
<id type="integer">3</id>
<created-at type="dateTime">2011-08-05T19:46:31+03:00</created-at>
<updated-at type="dateTime">2011-08-05T19:46:31+03:00</updated-at>
<name>User</name>
<description>Standard role for all users who need to create and/or approve requisitions</description>
<omnipotent type="boolean">false</omnipotent>
<system-role type="boolean">true</system-role>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</role>
<role>
<id type="integer">8</id>
<created-at type="dateTime">2011-08-05T19:46:31+03:00</created-at>
<updated-at type="dateTime">2012-07-31T19:40:04+03:00</updated-at>
<name>Edit Requisition as Approver</name>
<description>Adds ability to edit a requisition when you are approving it</description>
<omnipotent type="boolean">false</omnipotent>
<system-role type="boolean">true</system-role>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</role>
</roles>
<manager>
<id type="integer">4</id>
<login>sjones</login>
<email>upgradet+sj@coupa.com</email>
<employee-number></employee-number>
<firstname>Sally (Sales VP)</firstname>
<lastname>Jones</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</manager>
<default-address>
<id type="integer">16</id>
<created-at type="dateTime">2008-10-27T22:00:19+02:00</created-at>
<updated-at type="dateTime">2016-11-10T07:42:35+02:00</updated-at>
<name>HQ</name>
<location-code nil="true"/>
<street1>28 Nevada Blvd</street1>
<street2></street2>
<city>Laughlin</city>
<state>NV</state>
<postal-code>89028</postal-code>
<attention></attention>
<active type="boolean">true</active>
<business-group-name>Everyone</business-group-name>
<vat-number nil="true"/>
<local-tax-number nil="true"/>
<country>
<id type="integer">223</id>
<code>US</code>
<name>United States</name>
</country>
<content-groups type="array">
<content-group>
<id type="integer">1</id>
<created-at type="dateTime">2006-08-28T05:40:04+03:00</created-at>
<updated-at type="dateTime">2015-08-17T11:07:10+03:00</updated-at>
<name>Everyone</name>
<description>All users can see documents assigned to this group</description>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</content-group>
</content-groups>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">157</id>
<login>vijayashree.christopher@coupa.com</login>
<email>vijayashree.christopher@coupa.com</email>
<employee-number nil="true"/>
<firstname>vijayashree</firstname>
<lastname>Christopher</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</default-address>
<default-account>
<id nil="true"/>
<created-at nil="true"/>
<updated-at nil="true"/>
<name nil="true"/>
<code>SF-Sales-Indirect</code>
<active type="boolean">true</active>
<segment-1>SF</segment-1>
<segment-2>Sales</segment-2>
<segment-3>Indirect</segment-3>
<segment-4 nil="true"/>
<segment-5 nil="true"/>
<segment-6 nil="true"/>
<segment-7 nil="true"/>
<segment-8 nil="true"/>
<segment-9 nil="true"/>
<segment-10 nil="true"/>
<segment-11 nil="true"/>
<segment-12 nil="true"/>
<segment-13 nil="true"/>
<segment-14 nil="true"/>
<segment-15 nil="true"/>
<segment-16 nil="true"/>
<segment-17 nil="true"/>
<segment-18 nil="true"/>
<segment-19 nil="true"/>
<segment-20 nil="true"/>
<account-type>
<id type="integer">1</id>
<created-at type="dateTime">2008-10-27T22:10:01+02:00</created-at>
<updated-at type="dateTime">2016-11-08T20:56:40+02:00</updated-at>
<name>Ace Corporate</name>
<active type="boolean">true</active>
<currency>
<id type="integer">1</id>
<code>USD</code>
<decimals type="integer">2</decimals>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</currency>
<primary-contact>
<id type="integer">14</id>
<created-at type="dateTime">2008-10-27T22:10:01+02:00</created-at>
<updated-at type="dateTime">2016-11-08T20:56:40+02:00</updated-at>
<email>upgrade@coupa.com</email>
<name-prefix nil="true"/>
<name-suffix nil="true"/>
<name-additional nil="true"/>
<name-given>xxx</name-given>
<name-family>yyy</name-family>
<name-fullname nil="true"/>
<notes nil="true"/>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">195</id>
<login>tim.durkin@coupa.com</login>
<email>tim.durkin@coupa.com</email>
<employee-number nil="true"/>
<firstname>Timothy</firstname>
<lastname>Durkin</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</primary-contact>
<primary-address>
<id type="integer">184</id>
<created-at type="dateTime">2008-10-27T22:10:01+02:00</created-at>
<updated-at type="dateTime">2016-11-08T20:56:40+02:00</updated-at>
<name>xxx yyy</name>
<location-code nil="true"/>
<street1>2 W 5th Ave</street1>
<street2>Suite 300</street2>
<city>San Mateo</city>
<state>CA</state>
<postal-code>94404</postal-code>
<attention nil="true"/>
<active type="boolean">true</active>
<business-group-name nil="true"/>
<vat-number>465456645</vat-number>
<local-tax-number></local-tax-number>
<country>
<id type="integer">22</id>
<code>BE</code>
<name>Belgium</name>
</country>
<vat-country>
<id type="integer">223</id>
<code>US</code>
<name>United States</name>
</vat-country>
<content-groups type="array"/>
<created-by>
<id type="integer">122</id>
<login>matthew.otzwirk@coupa.com</login>
<email>matthew.otzwirk@coupa.com</email>
<employee-number nil="true"/>
<firstname>Matthew</firstname>
<lastname>Otzwirk</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">195</id>
<login>tim.durkin@coupa.com</login>
<email>tim.durkin@coupa.com</email>
<employee-number nil="true"/>
<firstname>Timothy</firstname>
<lastname>Durkin</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</primary-address>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">195</id>
<login>tim.durkin@coupa.com</login>
<email>tim.durkin@coupa.com</email>
<employee-number nil="true"/>
<firstname>Timothy</firstname>
<lastname>Durkin</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</account-type>
</default-account>
<default-account-type>
<id type="integer">1</id>
<created-at type="dateTime">2008-10-27T22:10:01+02:00</created-at>
<updated-at type="dateTime">2016-11-08T20:56:40+02:00</updated-at>
<name>Ace Corporate</name>
<active type="boolean">true</active>
<currency>
<id type="integer">1</id>
<code>USD</code>
<decimals type="integer">2</decimals>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</currency>
<primary-contact>
<id type="integer">14</id>
<created-at type="dateTime">2008-10-27T22:10:01+02:00</created-at>
<updated-at type="dateTime">2016-11-08T20:56:40+02:00</updated-at>
<email>upgrade@coupa.com</email>
<name-prefix nil="true"/>
<name-suffix nil="true"/>
<name-additional nil="true"/>
<name-given>xxx</name-given>
<name-family>yyy</name-family>
<name-fullname nil="true"/>
<notes nil="true"/>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">195</id>
<login>tim.durkin@coupa.com</login>
<email>tim.durkin@coupa.com</email>
<employee-number nil="true"/>
<firstname>Timothy</firstname>
<lastname>Durkin</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</primary-contact>
<primary-address>
<id type="integer">184</id>
<created-at type="dateTime">2008-10-27T22:10:01+02:00</created-at>
<updated-at type="dateTime">2016-11-08T20:56:40+02:00</updated-at>
<name>xxx yyy</name>
<location-code nil="true"/>
<street1>2 W 5th Ave</street1>
<street2>Suite 300</street2>
<city>San Mateo</city>
<state>CA</state>
<postal-code>94404</postal-code>
<attention nil="true"/>
<active type="boolean">true</active>
<business-group-name nil="true"/>
<vat-number>465456645</vat-number>
<local-tax-number></local-tax-number>
<country>
<id type="integer">22</id>
<code>BE</code>
<name>Belgium</name>
</country>
<vat-country>
<id type="integer">223</id>
<code>US</code>
<name>United States</name>
</vat-country>
<content-groups type="array"/>
<created-by>
<id type="integer">122</id>
<login>matthew.otzwirk@coupa.com</login>
<email>matthew.otzwirk@coupa.com</email>
<employee-number nil="true"/>
<firstname>Matthew</firstname>
<lastname>Otzwirk</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">195</id>
<login>tim.durkin@coupa.com</login>
<email>tim.durkin@coupa.com</email>
<employee-number nil="true"/>
<firstname>Timothy</firstname>
<lastname>Durkin</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</primary-address>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">195</id>
<login>tim.durkin@coupa.com</login>
<email>tim.durkin@coupa.com</email>
<employee-number nil="true"/>
<firstname>Timothy</firstname>
<lastname>Durkin</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</default-account-type>
<default-currency>
<id type="integer">1</id>
<code>USD</code>
<decimals type="integer">2</decimals>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</default-currency>
<department>
<id type="integer">2</id>
<created-at type="dateTime">2008-10-27T22:00:53+02:00</created-at>
<updated-at type="dateTime">2010-03-24T06:03:22+02:00</updated-at>
<name>Sales</name>
<active type="boolean">true</active>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</department>
<expenses-delegated-to type="array"/>
<can-expense-for type="array"/>
<content-groups type="array"/>
<account-groups type="array"/>
<approval-groups type="array"/>
<working-warehouses type="array"/>
<inventory-organizations type="array"/>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<custom-field-8></custom-field-8>
<custom-field-7></custom-field-7>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</user>
```

## User Create

url: /api/users

method: POST

## JSON request

```text
{
"login": "test1@coupa.com",
"email": "test1@coupa.com",
"purchasing-user": true,
"firstname": "test1",
"lastname": "user1"
}
```

## JSON response

```text
{
"id": 606,
"created-at": "2016-11-14T11:53:40-08:00",
"updated-at": "2016-11-14T11:53:40-08:00",
"login": "test1@coupa.com",
"email": "test1@coupa.com",
"purchasing-user": true,
"expense-user": false,
"sourcing-user": false,
"inventory-user": false,
"employee-number": null,
"firstname": "test1",
"lastname": "user1",
"fullname": "test1 user1",
"api-user": false,
"active": true,
"salesforce-id": null,
"account-security-type": 0,
"authentication-method": "coupa_credentials",
"sso-identifier": null,
"default-locale": null,
"business-group-security-type": null,
"edit-invoice-on-quick-entry": false,
"avatar-thumb-url": null,
"mention-name": "test1user1",
"gpo-entity": null,
"radio-button-test": null,
"subsidary": null,
"function": null,
"seg3default": null,
"roles": [
{
"id": 3,
"created-at": "2011-08-05T09:46:31-07:00",
"updated-at": "2011-08-05T09:46:31-07:00",
"name": "User",
"description": "Standard role for all users who need to create and/or approve requisitions",
"omnipotent": false,
"system-role": true,
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
}
}
],
"expenses-delegated-to": [],
"can-expense-for": [],
"content-groups": [],
"account-groups": [],
"approval-groups": [],
"working-warehouses": [],
"inventory-organizations": [],
"created-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-15T15:05:17-07:00",
"updated-at": "2016-03-30T02:35:20-07:00"
},
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-15T15:05:17-07:00",
"updated-at": "2016-03-30T02:35:20-07:00"
}
}
```

## XML request

```text
<user>
<login>test2@coupa.com</login>
<email>test2@coupa.com</email>
<purchasing-user>true</purchasing-user>
<firstname>test2</firstname>
<lastname>user2</lastname>
</user>
```

## XML response

```text
<?xml version="1.0" encoding="UTF-8"?>
<user>
<id type="integer">607</id>
<created-at type="dateTime">2016-11-14T11:58:38-08:00</created-at>
<updated-at type="dateTime">2016-11-14T11:58:38-08:00</updated-at>
<login>test2@coupa.com</login>
<email>test2@coupa.com</email>
<purchasing-user type="boolean">true</purchasing-user>
<expense-user type="boolean">false</expense-user>
<sourcing-user type="boolean">false</sourcing-user>
<inventory-user type="boolean">false</inventory-user>
<employee-number nil="true"/>
<firstname>test2</firstname>
<lastname>user2</lastname>
<fullname>test2 user2</fullname>
<api-user type="boolean">false</api-user>
<active type="boolean">true</active>
<salesforce-id nil="true"/>
<account-security-type type="integer">0</account-security-type>
<authentication-method type="symbol">coupa_credentials</authentication-method>
<sso-identifier nil="true"/>
<default-locale nil="true"/>
<business-group-security-type nil="true"/>
<edit-invoice-on-quick-entry type="boolean">false</edit-invoice-on-quick-entry>
<avatar-thumb-url nil="true"/>
<mention-name>test2user2</mention-name>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
<roles type="array">
<role>
<id type="integer">3</id>
<created-at type="dateTime">2011-08-05T09:46:31-07:00</created-at>
<updated-at type="dateTime">2011-08-05T09:46:31-07:00</updated-at>
<name>User</name>
<description>Standard role for all users who need to create and/or approve requisitions</description>
<omnipotent type="boolean">false</omnipotent>
<system-role type="boolean">true</system-role>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</role>
</roles>
<expenses-delegated-to type="array"/>
<can-expense-for type="array"/>
<content-groups type="array"/>
<account-groups type="array"/>
<approval-groups type="array"/>
<working-warehouses type="array"/>
<inventory-organizations type="array"/>
<created-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</user>
```

## User Create with Errors

url: /api/users

method: POST

## JSON request

```text
{
"login": "test1@coupa.com",
"email": "test1@coupa.com",
"purchasing-user": true,
"firstname": "test1",
"lastname": "user1"
}
```

## JSON response

```text
{
"errors": {
"user": [
"Login has already been taken",
"Email has already been taken"
]
}
}
```

## XML request

```text
<user>
<login>test1@coupa.com</login>
<email>test1@coupa.com</email>
<purchasing-user>true</purchasing-user>
<firstname>test1</firstname>
<lastname>user1</lastname>
</user>
```

## XML response

```text
<?xml version="1.0" encoding="UTF-8"?>
<errors>
<error>
<![CDATA[Login has already been taken]]>
</error>
<error>
<![CDATA[Email has already been taken]]>
</error>
</errors>
```

## User Update

url: /api/users/5

method: PUT

## JSON request

```text
{
"firstname": "test2",
"lastname": "user2"
}
```

## JSON response

```text
{
"id": 5,
"created-at": "2008-10-27T13:54:10-07:00",
"updated-at": "2016-11-15T06:45:11-08:00",
"login": "tkennedy",
"email": "upgrade+tk@coupa.com",
"purchasing-user": true,
"expense-user": false,
"sourcing-user": false,
"inventory-user": false,
"employee-number": "",
"firstname": "test2",
"lastname": "user2",
"fullname": "test2 user2",
"api-user": false,
"active": true,
"salesforce-id": null,
"account-security-type": 0,
"authentication-method": "coupa_credentials",
"sso-identifier": "",
"default-locale": null,
"business-group-security-type": 1,
"edit-invoice-on-quick-entry": false,
"avatar-thumb-url": null,
"mention-name": "tommy(saleslead)kennedy",
"gpo-entity": "",
"radio-button-test": null,
"subsidary": null,
"function": null,
"seg3default": null,
"phone-work": {
"id": 5,
"created-at": "2008-10-27T13:54:10-07:00",
"updated-at": "2012-12-13T14:27:57-08:00",
"country-code": "1",
"area-code": "650",
"number": "5856306",
"extension": null,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
}
},
"phone-mobile": {
"id": 30,
"created-at": "2008-10-28T10:59:47-07:00",
"updated-at": "2012-12-13T14:27:57-08:00",
"country-code": "1",
"area-code": "650",
"number": "5856306",
"extension": null,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
}
},
"roles": [
{
"id": 3,
"created-at": "2011-08-05T09:46:31-07:00",
"updated-at": "2011-08-05T09:46:31-07:00",
"name": "User",
"description": "Standard role for all users who need to create and/or approve requisitions",
"omnipotent": false,
"system-role": true,
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
}
},
{
"id": 8,
"created-at": "2011-08-05T09:46:31-07:00",
"updated-at": "2012-07-31T09:40:04-07:00",
"name": "Edit Requisition as Approver",
"description": "Adds ability to edit a requisition when you are approving it",
"omnipotent": false,
"system-role": true,
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
}
}
],
"manager": {
"id": 4,
"login": "sjones",
"firstname": "Sally (Sales VP)",
"lastname": "Jones",
"employee-number": "",
"email": "upgradet+sj@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2008-10-27T13:54:10-07:00",
"updated-at": "2016-10-21T11:47:04-07:00"
},
"default-address": {
"id": 16,
"created-at": "2008-10-27T13:00:19-07:00",
"updated-at": "2009-07-11T13:33:25-07:00",
"name": "HQ",
"location-code": null,
"street1": "28 Nevada Blvd",
"street2": "",
"city": "Laughlin",
"state": "NV",
"postal-code": "89028",
"attention": "",
"active": true,
"business-group-name": "Everyone",
"vat-number": null,
"local-tax-number": null,
"country": {
"id": 223,
"code": "US",
"name": "United States"
},
"vat-country": null,
"content-groups": [
{
"id": 1,
"created-at": "2006-08-27T19:40:04-07:00",
"updated-at": "2015-08-17T01:07:10-07:00",
"name": "Everyone",
"description": "All users can see documents assigned to this group",
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-15T15:05:17-07:00",
"updated-at": "2016-03-30T02:35:20-07:00"
}
}
],
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
},
"updated-by": {
"id": 16,
"login": "krhine",
"firstname": "Kevin",
"lastname": "Rhine",
"employee-number": "",
"email": "kevin.rhine@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2009-02-23T17:28:34-08:00",
"updated-at": "2016-10-23T22:53:46-07:00"
}
},
"default-account": {
"id": null,
"created-at": null,
"updated-at": null,
"name": null,
"code": "SF-Sales-Indirect",
"active": true,
"segment-1": "SF",
"segment-2": "Sales",
"segment-3": "Indirect",
"segment-4": null,
"segment-5": null,
"segment-6": null,
"segment-7": null,
"segment-8": null,
"segment-9": null,
"segment-10": null,
"segment-11": null,
"segment-12": null,
"segment-13": null,
"segment-14": null,
"segment-15": null,
"segment-16": null,
"segment-17": null,
"segment-18": null,
"segment-19": null,
"segment-20": null,
"account-type": {
"id": 1,
"created-at": "2008-10-27T13:10:01-07:00",
"updated-at": "2016-10-27T02:38:59-07:00",
"name": "Ace Corporate",
"active": true,
"currency": {
"id": 1,
"code": "USD",
"decimals": 2,
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-15T15:05:17-07:00",
"updated-at": "2016-03-30T02:35:20-07:00"
}
},
"primary-contact": {
"id": 14,
"created-at": "2008-10-27T13:10:01-07:00",
"updated-at": "2016-10-12T14:35:18-07:00",
"email": "upgrade@coupa.com",
"name-prefix": null,
"name-suffix": null,
"name-additional": null,
"name-given": "xxx",
"name-family": "yyy",
"name-fullname": null,
"notes": null,
"phone-work": null,
"phone-mobile": null,
"phone-fax": null,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
},
"updated-by": {
"id": 122,
"login": "matthew.otzwirk@coupa.com",
"firstname": "Matthew",
"lastname": "Otzwirk",
"employee-number": null,
"email": "matthew.otzwirk@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-04-27T10:54:43-07:00",
"updated-at": "2016-10-27T09:30:21-07:00"
}
},
"primary-address": {
"id": 184,
"created-at": "2008-10-27T13:10:01-07:00",
"updated-at": "2016-03-17T01:35:36-07:00",
"name": "xxx yyy",
"location-code": null,
"street1": "2 W 5th Ave",
"street2": "Suite 300",
"city": "San Mateo",
"state": "CA",
"postal-code": "94404",
"attention": null,
"active": true,
"business-group-name": null,
"vat-number": "465456645",
"local-tax-number": "",
"country": {
"id": 22,
"code": "BE",
"name": "Belgium"
},
"vat-country": {
"id": 223,
"code": "US",
"name": "United States"
},
"content-groups": [],
"created-by": {
"id": 122,
"login": "matthew.otzwirk@coupa.com",
"firstname": "Matthew",
"lastname": "Otzwirk",
"employee-number": null,
"email": "matthew.otzwirk@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-04-27T10:54:43-07:00",
"updated-at": "2016-10-27T09:30:21-07:00"
},
"updated-by": {
"id": 122,
"login": "matthew.otzwirk@coupa.com",
"firstname": "Matthew",
"lastname": "Otzwirk",
"employee-number": null,
"email": "matthew.otzwirk@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-04-27T10:54:43-07:00",
"updated-at": "2016-10-27T09:30:21-07:00"
}
},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
},
"updated-by": {
"id": 147,
"login": "sourabh.pataskar@coupa.com",
"firstname": "Sourabh",
"lastname": "Pataskar",
"employee-number": null,
"email": "sourabh.pataskar@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-10T03:15:04-07:00",
"updated-at": "2016-10-27T02:36:52-07:00"
}
}
},
"default-account-type": {
"id": 1,
"created-at": "2008-10-27T13:10:01-07:00",
"updated-at": "2016-10-27T02:38:59-07:00",
"name": "Ace Corporate",
"active": true,
"currency": {
"id": 1,
"code": "USD",
"decimals": 2,
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-15T15:05:17-07:00",
"updated-at": "2016-03-30T02:35:20-07:00"
}
},
"primary-contact": {
"id": 14,
"created-at": "2008-10-27T13:10:01-07:00",
"updated-at": "2016-10-12T14:35:18-07:00",
"email": "upgrade@coupa.com",
"name-prefix": null,
"name-suffix": null,
"name-additional": null,
"name-given": "xxx",
"name-family": "yyy",
"name-fullname": null,
"notes": null,
"phone-work": null,
"phone-mobile": null,
"phone-fax": null,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
},
"updated-by": {
"id": 122,
"login": "matthew.otzwirk@coupa.com",
"firstname": "Matthew",
"lastname": "Otzwirk",
"employee-number": null,
"email": "matthew.otzwirk@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-04-27T10:54:43-07:00",
"updated-at": "2016-10-27T09:30:21-07:00"
}
},
"primary-address": {
"id": 184,
"created-at": "2008-10-27T13:10:01-07:00",
"updated-at": "2016-03-17T01:35:36-07:00",
"name": "xxx yyy",
"location-code": null,
"street1": "2 W 5th Ave",
"street2": "Suite 300",
"city": "San Mateo",
"state": "CA",
"postal-code": "94404",
"attention": null,
"active": true,
"business-group-name": null,
"vat-number": "465456645",
"local-tax-number": "",
"country": {
"id": 22,
"code": "BE",
"name": "Belgium"
},
"vat-country": {
"id": 223,
"code": "US",
"name": "United States"
},
"content-groups": [],
"created-by": {
"id": 122,
"login": "matthew.otzwirk@coupa.com",
"firstname": "Matthew",
"lastname": "Otzwirk",
"employee-number": null,
"email": "matthew.otzwirk@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-04-27T10:54:43-07:00",
"updated-at": "2016-10-27T09:30:21-07:00"
},
"updated-by": {
"id": 122,
"login": "matthew.otzwirk@coupa.com",
"firstname": "Matthew",
"lastname": "Otzwirk",
"employee-number": null,
"email": "matthew.otzwirk@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-04-27T10:54:43-07:00",
"updated-at": "2016-10-27T09:30:21-07:00"
}
},
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
},
"updated-by": {
"id": 147,
"login": "sourabh.pataskar@coupa.com",
"firstname": "Sourabh",
"lastname": "Pataskar",
"employee-number": null,
"email": "sourabh.pataskar@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2016-10-10T03:15:04-07:00",
"updated-at": "2016-10-27T02:36:52-07:00"
}
},
"default-currency": {
"id": 1,
"code": "USD",
"decimals": 2,
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-15T15:05:17-07:00",
"updated-at": "2016-03-30T02:35:20-07:00"
}
},
"department": {
"id": 2,
"created-at": "2008-10-27T13:00:53-07:00",
"updated-at": "2010-03-23T21:03:22-07:00",
"name": "Sales",
"active": true,
"created-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"firstname": "Coupa",
"lastname": "Support",
"employee-number": "",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2006-02-16T06:01:34-08:00",
"updated-at": "2016-11-14T11:52:00-08:00"
}
},
"expenses-delegated-to": [],
"can-expense-for": [],
"content-groups": [],
"account-groups": [],
"approval-groups": [],
"working-warehouses": [],
"inventory-organizations": [],
"updated-by": {
"id": 80,
"login": "learnapi",
"firstname": "API",
"lastname": "API",
"employee-number": null,
"email": "learnapi@learnapi.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"created-at": "2013-05-15T15:05:17-07:00",
"updated-at": "2016-03-30T02:35:20-07:00"
}
}
```

## XML request

```text
<user>
<firstname>test2</firstname>
<lastname>user2</lastname>
</user>
```

## XML response

```text
<?xml version="1.0" encoding="UTF-8"?>
<user>
<id type="integer">5</id>
<created-at type="dateTime">2008-10-27T13:54:10-07:00</created-at>
<updated-at type="dateTime">2016-11-15T06:45:11-08:00</updated-at>
<login>tkennedy</login>
<email>upgrade+tk@coupa.com</email>
<purchasing-user type="boolean">true</purchasing-user>
<expense-user type="boolean">false</expense-user>
<sourcing-user type="boolean">false</sourcing-user>
<inventory-user type="boolean">false</inventory-user>
<employee-number></employee-number>
<firstname>test2</firstname>
<lastname>user2</lastname>
<fullname>test2 user2</fullname>
<api-user type="boolean">false</api-user>
<active type="boolean">true</active>
<salesforce-id nil="true"/>
<account-security-type type="integer">0</account-security-type>
<authentication-method type="symbol">coupa_credentials</authentication-method>
<sso-identifier></sso-identifier>
<default-locale nil="true"/>
<business-group-security-type type="integer">1</business-group-security-type>
<edit-invoice-on-quick-entry type="boolean">false</edit-invoice-on-quick-entry>
<avatar-thumb-url nil="true"/>
<mention-name>tommy(saleslead)kennedy</mention-name>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
<phone-work>
<id type="integer">5</id>
<created-at type="dateTime">2008-10-27T13:54:10-07:00</created-at>
<updated-at type="dateTime">2012-12-13T14:27:57-08:00</updated-at>
<country-code>1</country-code>
<area-code>650</area-code>
<number>5856306</number>
<extension nil="true"/>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</phone-work>
<phone-mobile>
<id type="integer">30</id>
<created-at type="dateTime">2008-10-28T10:59:47-07:00</created-at>
<updated-at type="dateTime">2012-12-13T14:27:57-08:00</updated-at>
<country-code>1</country-code>
<area-code>650</area-code>
<number>5856306</number>
<extension nil="true"/>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</phone-mobile>
<roles type="array">
<role>
<id type="integer">3</id>
<created-at type="dateTime">2011-08-05T09:46:31-07:00</created-at>
<updated-at type="dateTime">2011-08-05T09:46:31-07:00</updated-at>
<name>User</name>
<description>Standard role for all users who need to create and/or approve requisitions</description>
<omnipotent type="boolean">false</omnipotent>
<system-role type="boolean">true</system-role>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</role>
<role>
<id type="integer">8</id>
<created-at type="dateTime">2011-08-05T09:46:31-07:00</created-at>
<updated-at type="dateTime">2012-07-31T09:40:04-07:00</updated-at>
<name>Edit Requisition as Approver</name>
<description>Adds ability to edit a requisition when you are approving it</description>
<omnipotent type="boolean">false</omnipotent>
<system-role type="boolean">true</system-role>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</role>
</roles>
<manager>
<id type="integer">4</id>
<login>sjones</login>
<email>upgradet+sj@coupa.com</email>
<employee-number></employee-number>
<firstname>Sally (Sales VP)</firstname>
<lastname>Jones</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</manager>
<default-address>
<id type="integer">16</id>
<created-at type="dateTime">2008-10-27T13:00:19-07:00</created-at>
<updated-at type="dateTime">2009-07-11T13:33:25-07:00</updated-at>
<name>HQ</name>
<location-code nil="true"/>
<street1>28 Nevada Blvd</street1>
<street2></street2>
<city>Laughlin</city>
<state>NV</state>
<postal-code>89028</postal-code>
<attention></attention>
<active type="boolean">true</active>
<business-group-name>Everyone</business-group-name>
<vat-number nil="true"/>
<local-tax-number nil="true"/>
<country>
<id type="integer">223</id>
<code>US</code>
<name>United States</name>
</country>
<content-groups type="array">
<content-group>
<id type="integer">1</id>
<created-at type="dateTime">2006-08-27T19:40:04-07:00</created-at>
<updated-at type="dateTime">2015-08-17T01:07:10-07:00</updated-at>
<name>Everyone</name>
<description>All users can see documents assigned to this group</description>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</content-group>
</content-groups>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">16</id>
<login>krhine</login>
<email>kevin.rhine@coupa.com</email>
<employee-number></employee-number>
<firstname>Kevin</firstname>
<lastname>Rhine</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</default-address>
<default-account>
<id nil="true"/>
<created-at nil="true"/>
<updated-at nil="true"/>
<name nil="true"/>
<code>SF-Sales-Indirect</code>
<active type="boolean">true</active>
<segment-1>SF</segment-1>
<segment-2>Sales</segment-2>
<segment-3>Indirect</segment-3>
<segment-4 nil="true"/>
<segment-5 nil="true"/>
<segment-6 nil="true"/>
<segment-7 nil="true"/>
<segment-8 nil="true"/>
<segment-9 nil="true"/>
<segment-10 nil="true"/>
<segment-11 nil="true"/>
<segment-12 nil="true"/>
<segment-13 nil="true"/>
<segment-14 nil="true"/>
<segment-15 nil="true"/>
<segment-16 nil="true"/>
<segment-17 nil="true"/>
<segment-18 nil="true"/>
<segment-19 nil="true"/>
<segment-20 nil="true"/>
<account-type>
<id type="integer">1</id>
<created-at type="dateTime">2008-10-27T13:10:01-07:00</created-at>
<updated-at type="dateTime">2016-10-27T02:38:59-07:00</updated-at>
<name>Ace Corporate</name>
<active type="boolean">true</active>
<currency>
<id type="integer">1</id>
<code>USD</code>
<decimals type="integer">2</decimals>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</currency>
<primary-contact>
<id type="integer">14</id>
<created-at type="dateTime">2008-10-27T13:10:01-07:00</created-at>
<updated-at type="dateTime">2016-10-12T14:35:18-07:00</updated-at>
<email>upgrade@coupa.com</email>
<name-prefix nil="true"/>
<name-suffix nil="true"/>
<name-additional nil="true"/>
<name-given>xxx</name-given>
<name-family>yyy</name-family>
<name-fullname nil="true"/>
<notes nil="true"/>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">122</id>
<login>matthew.otzwirk@coupa.com</login>
<email>matthew.otzwirk@coupa.com</email>
<employee-number nil="true"/>
<firstname>Matthew</firstname>
<lastname>Otzwirk</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</primary-contact>
<primary-address>
<id type="integer">184</id>
<created-at type="dateTime">2008-10-27T13:10:01-07:00</created-at>
<updated-at type="dateTime">2016-03-17T01:35:36-07:00</updated-at>
<name>xxx yyy</name>
<location-code nil="true"/>
<street1>2 W 5th Ave</street1>
<street2>Suite 300</street2>
<city>San Mateo</city>
<state>CA</state>
<postal-code>94404</postal-code>
<attention nil="true"/>
<active type="boolean">true</active>
<business-group-name nil="true"/>
<vat-number>465456645</vat-number>
<local-tax-number></local-tax-number>
<country>
<id type="integer">22</id>
<code>BE</code>
<name>Belgium</name>
</country>
<vat-country>
<id type="integer">223</id>
<code>US</code>
<name>United States</name>
</vat-country>
<content-groups type="array"/>
<created-by>
<id type="integer">122</id>
<login>matthew.otzwirk@coupa.com</login>
<email>matthew.otzwirk@coupa.com</email>
<employee-number nil="true"/>
<firstname>Matthew</firstname>
<lastname>Otzwirk</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">122</id>
<login>matthew.otzwirk@coupa.com</login>
<email>matthew.otzwirk@coupa.com</email>
<employee-number nil="true"/>
<firstname>Matthew</firstname>
<lastname>Otzwirk</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</primary-address>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">147</id>
<login>sourabh.pataskar@coupa.com</login>
<email>sourabh.pataskar@coupa.com</email>
<employee-number nil="true"/>
<firstname>Sourabh</firstname>
<lastname>Pataskar</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</account-type>
</default-account>
<default-account-type>
<id type="integer">1</id>
<created-at type="dateTime">2008-10-27T13:10:01-07:00</created-at>
<updated-at type="dateTime">2016-10-27T02:38:59-07:00</updated-at>
<name>Ace Corporate</name>
<active type="boolean">true</active>
<currency>
<id type="integer">1</id>
<code>USD</code>
<decimals type="integer">2</decimals>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</currency>
<primary-contact>
<id type="integer">14</id>
<created-at type="dateTime">2008-10-27T13:10:01-07:00</created-at>
<updated-at type="dateTime">2016-10-12T14:35:18-07:00</updated-at>
<email>upgrade@coupa.com</email>
<name-prefix nil="true"/>
<name-suffix nil="true"/>
<name-additional nil="true"/>
<name-given>xxx</name-given>
<name-family>yyy</name-family>
<name-fullname nil="true"/>
<notes nil="true"/>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">122</id>
<login>matthew.otzwirk@coupa.com</login>
<email>matthew.otzwirk@coupa.com</email>
<employee-number nil="true"/>
<firstname>Matthew</firstname>
<lastname>Otzwirk</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</primary-contact>
<primary-address>
<id type="integer">184</id>
<created-at type="dateTime">2008-10-27T13:10:01-07:00</created-at>
<updated-at type="dateTime">2016-03-17T01:35:36-07:00</updated-at>
<name>xxx yyy</name>
<location-code nil="true"/>
<street1>2 W 5th Ave</street1>
<street2>Suite 300</street2>
<city>San Mateo</city>
<state>CA</state>
<postal-code>94404</postal-code>
<attention nil="true"/>
<active type="boolean">true</active>
<business-group-name nil="true"/>
<vat-number>465456645</vat-number>
<local-tax-number></local-tax-number>
<country>
<id type="integer">22</id>
<code>BE</code>
<name>Belgium</name>
</country>
<vat-country>
<id type="integer">223</id>
<code>US</code>
<name>United States</name>
</vat-country>
<content-groups type="array"/>
<created-by>
<id type="integer">122</id>
<login>matthew.otzwirk@coupa.com</login>
<email>matthew.otzwirk@coupa.com</email>
<employee-number nil="true"/>
<firstname>Matthew</firstname>
<lastname>Otzwirk</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">122</id>
<login>matthew.otzwirk@coupa.com</login>
<email>matthew.otzwirk@coupa.com</email>
<employee-number nil="true"/>
<firstname>Matthew</firstname>
<lastname>Otzwirk</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</primary-address>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">147</id>
<login>sourabh.pataskar@coupa.com</login>
<email>sourabh.pataskar@coupa.com</email>
<employee-number nil="true"/>
<firstname>Sourabh</firstname>
<lastname>Pataskar</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</default-account-type>
<default-currency>
<id type="integer">1</id>
<code>USD</code>
<decimals type="integer">2</decimals>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</default-currency>
<department>
<id type="integer">2</id>
<created-at type="dateTime">2008-10-27T13:00:53-07:00</created-at>
<updated-at type="dateTime">2010-03-23T21:03:22-07:00</updated-at>
<name>Sales</name>
<active type="boolean">true</active>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade+coupasupport@coupa.com</email>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</department>
<expenses-delegated-to type="array"/>
<can-expense-for type="array"/>
<content-groups type="array"/>
<account-groups type="array"/>
<approval-groups type="array"/>
<working-warehouses type="array"/>
<inventory-organizations type="array"/>
<updated-by>
<id type="integer">80</id>
<login>learnapi</login>
<email>learnapi@learnapi.com</email>
<employee-number nil="true"/>
<firstname>API</firstname>
<lastname>API</lastname>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<radio-button-test></radio-button-test>
<subsidary></subsidary>
<function></function>
<seg3default></seg3default>
<username1></username1>
</updated-by>
</user>
```
