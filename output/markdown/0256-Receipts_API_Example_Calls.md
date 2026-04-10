---
title: "Receipts API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/receipts-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/receipts-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:58+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Receipts API"
  - "Receipts API Example Calls"
---

# Receipts API Example Calls

## Receipt GET (Query)

In this example, we queried for a single receipt with an ID of 296.

We did a GET to the URL:

```text
https://<instanceburl>/api/receiving_transactions/6
```

or

```text
https://<instance url>/api/receiving_transactions?id=6
```

Here is the response matching the search criteria:

```text
<?xml version="1.0" encoding="UTF-8"?>
<inventory-transaction>
<barcode type="string">4433</barcode>
<created-at type="datetime">2010-12-06T10:21:07-08:00</created-at>
<id type="integer">296</id>
<price type="decimal">1000.00</price>
<quantity type="float">1.0</quantity>
<rfid-tag type="string">3344</rfid-tag>
<total type="decimal">1000.00</total>
<type type="string">InventoryReceipt</type>
<status type="string">created</status>
<updated-at type="datetime">2010-12-06T10:21:07-08:00</updated-at>
<exported type="boolean">false</exported>
<account>
<active type="boolean">true</active>
<code>SF-Marketing-Assets</code>
<id type="integer">14</id>
<name>San Francisco -Marketing, Assets</name>
<segment-1>SF</segment-1>
<segment-10 />
<segment-11 />
<segment-12 />
<segment-13 />
<segment-14 />
<segment-15 />
<segment-16 />
<segment-17 />
<segment-18 />
<segment-19 />
<segment-2>Marketing</segment-2>
<segment-20 />
<segment-3>Assets</segment-3>
<segment-4 />
<segment-5 />
<segment-6 />
<segment-7 />
<segment-8 />
<segment-9 />
<account-type>
<id type="integer">1</id>
<name>Ace Corporate</name>
</account-type>
</account>
<order-line>
<accounting-total type="decimal">1000.00</accounting-total>
<created-at type="datetime">2010-12-06T10:16:12-08:00</created-at>
<description>Gabe's Test Item</description>
<id type="integer">2949</id>
<invoiced type="float">0.0</invoiced>
<line-num type="integer">1</line-num>
<need-by-date type="datetime">2010-12-10T00:00:00-08:00</need-by-date>
<order-header-id type="integer">2079</order-header-id>
<price type="decimal">1000.00</price>
<quantity type="float">1.0</quantity>
<received type="float">1.0</received>
<source-part-num>9999</source-part-num>
<status>received</status>
<sub-line-num type="integer" />
<supp-aux-part-num />
<total type="decimal">1000.00</total>
<type>OrderQuantityLine</type>
<updated-at type="datetime">2010-12-06T10:21:08-08:00</updated-at>
<version type="integer" />
<account>
<active type="boolean">true</active>
<code>SF-Marketing-Assets</code>
<id type="integer">14</id>
<name>San Francisco -Marketing, Assets</name>
<segment-1>SF</segment-1>
<segment-10 />
<segment-11 />
<segment-12 />
<segment-13 />
<segment-14 />
<segment-15 />
<segment-16 />
<segment-17 />
<segment-18 />
<segment-19 />
<segment-2>Marketing</segment-2>
<segment-20 />
<segment-3>Assets</segment-3>
<segment-4 />
<segment-5 />
<segment-6 />
<segment-7 />
<segment-8 />
<segment-9 />
<account-type>
<id type="integer">1</id>
<name>Ace Corporate</name>
</account-type>
</account>
<accounting-total-currency>
<code>USD</code>
<id type="integer">1</id>
</accounting-total-currency>
<currency>
<code>USD</code>
<id type="integer">1</id>
</currency>
<commodity>
<active type="boolean">true</active>
<created-at type="datetime">2008-10-28T17:13:45Z</created-at>
<id type="integer">8</id>
<name>Software</name>
<updated-at type="datetime">2009-08-14T16:34:54Z</updated-at>
<created-by>
<email>upgrade@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<id type="integer">1</id>
<lastname>Support</lastname>
<login>coupasupport</login>
</created-by>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
</commodity>
<item>
<id type="integer">47</id>
<active type="boolean">true</active>
<created-at type="datetime">2010-11-29T13:16:11-08:00</created-at>
<description>Gabe's Test Description</description>
<item-number>12345</item-number>
<name>Gabe's Test Item</name>
<updated-at type="datetime">2010-12-02T15:16:09-08:00</updated-at>
<commodity>
<active type="boolean">true</active>
<created-at type="datetime">2008-10-28T17:13:45Z</created-at>
<id type="integer">8</id>
<name>Software</name>
<updated-at type="datetime">2009-08-14T16:34:54Z</updated-at>
<created-by>
<email>upgrade@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<id type="integer">1</id>
<lastname>Support</lastname>
<login>coupasupport</login>
</created-by>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
</commodity>
<user>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</user>
<uom>
<code>EA</code>
<id type="integer">1</id>
</uom>
<user>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</user>
<reorder-alerts>
<reorder-alert>
<created-at type="datetime">2010-11-29T21:16:11Z</created-at>
<created-by type="integer">Kyle Eisner</created-by>
<id type="integer">2</id>
<item-id type="integer">47</item-id>
<quantity type="float">50.0</quantity>
<updated-at type="datetime">2010-11-29T21:16:11Z</updated-at>
<updated-by type="integer">Kyle Eisner</updated-by>
<user-id type="integer">47</user-id>
<warehouse-id type="integer">3</warehouse-id>
</reorder-alert>
</reorder-alerts>
</item>
<created-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</created-by>
<supplier>
<id type="integer">18</id>
<name>Lenovo</name>
<number nil="true" />
<primary-contact>
<email>upgrade@coupa.com</email>
<id type="integer">19</id>
<name-additional nil="true" />
<name-family>Arnaud</name-family>
<name-fullname nil="true" />
<name-given>Jacqueline</name-given>
<name-prefix nil="true" />
<name-suffix nil="true" />
<notes nil="true" />
<phone-work>
<area-code>650</area-code>
<country-code>1</country-code>
<extension nil="true" />
<number>5856306</number>
</phone-work>
<phone-mobile>
<area-code>650</area-code>
<country-code>1</country-code>
<extension nil="true" />
<number>5856306</number>
</phone-mobile>
<phone-fax>
<area-code>650</area-code>
<country-code>1</country-code>
<extension nil="true" />
<number>5856306</number>
</phone-fax>
</primary-contact>
<primary-address>
<attention nil="true" />
<city>San Mateo</city>
<id type="integer">25</id>
<name>Lenovo</name>
<postal-code>94402</postal-code>
<state>CA</state>
<street1>451 D Street</street1>
<street2 />
<country>
<code>US</code>
<id type="integer">223</id>
<name>United States</name>
</country>
</primary-address>
</supplier>
<uom>
<code>EA</code>
<id type="integer">1</id>
</uom>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
<asset-tags />
<attachments>
<attachment>
<id>325</id>
<intent>Supplier</intent>
<type>AttachmentFile</type>
<url>http://</url>
<text />
<file>https://s3.amazonaws.com/paperclip.coupahost.com/gabedemo.coupahost.com/attachment_files/files/79/original/asset_tag_template.csv</file>
<created-at>2010-12-06T10:16:12-08:00</created-at>
<updated-at>2010-12-06T10:16:12-08:00</updated-at>
</attachment>
</attachments>
</order-line>
<created-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</created-by>
<inspection-code>
<code>Fail</code>
<created-at type="datetime">2008-10-27T21:33:24Z</created-at>
<description />
<id type="integer">2</id>
<updated-at type="datetime">2008-10-27T21:33:24Z</updated-at>
<created-by>
<email>upgrade@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<id type="integer">1</id>
<lastname>Support</lastname>
<login>coupasupport</login>
</created-by>
<updated-by>
<email>upgrade@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<id type="integer">1</id>
<lastname>Support</lastname>
<login>coupasupport</login>
</updated-by>
</inspection-code>
<item>
<id type="integer">47</id>
<active type="boolean">true</active>
<created-at type="datetime">2010-11-29T13:16:11-08:00</created-at>
<description>Gabe's Test Description</description>
<item-number>12345</item-number>
<name>Gabe's Test Item</name>
<updated-at type="datetime">2010-12-02T15:16:09-08:00</updated-at>
<commodity>
<active type="boolean">true</active>
<created-at type="datetime">2008-10-28T17:13:45Z</created-at>
<id type="integer">8</id>
<name>Software</name>
<updated-at type="datetime">2009-08-14T16:34:54Z</updated-at>
<created-by>
<email>upgrade@coupa.com</email>
<employee-number />
<firstname>Coupa</firstname>
<id type="integer">1</id>
<lastname>Support</lastname>
<login>coupasupport</login>
</created-by>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
</commodity>
<user>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</user>
<uom>
<code>EA</code>
<id type="integer">1</id>
</uom>
<user>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</user>
<reorder-alerts>
<reorder-alert>
<created-at type="datetime">2010-11-29T21:16:11Z</created-at>
<created-by type="integer">Kyle Eisner</created-by>
<id type="integer">2</id>
<item-id type="integer">47</item-id>
<quantity type="float">50.0</quantity>
<updated-at type="datetime">2010-11-29T21:16:11Z</updated-at>
<updated-by type="integer">Kyle Eisner</updated-by>
<user-id type="integer">47</user-id>
<warehouse-id type="integer">3</warehouse-id>
</reorder-alert>
</reorder-alerts>
</item>
<to-warehouse-location>
<aisle>First</aisle>
<bin>Top</bin>
<created-at type="datetime">2010-12-02T23:08:03Z</created-at>
<id type="integer">8</id>
<level>3</level>
<updated-at type="datetime">2010-12-02T23:29:28Z</updated-at>
<created-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</created-by>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
<warehouse>
<active-flag type="boolean">true</active-flag>
<created-at type="datetime">2010-12-02T23:08:03Z</created-at>
<description>SF Stockroom</description>
<id type="integer">7</id>
<name>SF Stockroom</name>
<updated-at type="datetime">2010-12-02T23:08:03Z</updated-at>
<address>
<attention />
<city>San Francisco</city>
<id type="integer">87</id>
<name>SF Stockroom</name>
<postal-code>112211</postal-code>
<state />
<street1>123 Stockton</street1>
<street2 />
<country>
<code>US</code>
<id type="integer">223</id>
<name>United States</name>
</country>
</address>
<created-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</created-by>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
<warehouse-type>
<created-at type="datetime">2010-12-02T23:06:08Z</created-at>
<description>Stockroom</description>
<id type="integer">3</id>
<name>Stockroom</name>
<updated-at type="datetime">2010-12-02T23:06:08Z</updated-at>
<created-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</created-by>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
</warehouse-type>
</warehouse>
</to-warehouse-location>
<uom>
<code>EA</code>
<id type="integer">1</id>
</uom>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
<asset-tags>
<asset-tag>
<created-at type="datetime">2010-12-06T18:21:07Z</created-at>
<id type="integer">32</id>
<inventory-balance-id type="integer">29</inventory-balance-id>
<order-line-id type="integer" nil="true" />
<received type="boolean">true</received>
<requisition-line-id type="integer" nil="true" />
<tag>12121212</tag>
<updated-at type="datetime">2010-12-06T18:21:08Z</updated-at>
<created-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</created-by>
<updated-by>
<email>upgrade+ke@coupa.com</email>
<employee-number />
<firstname>Kyle</firstname>
<id type="integer">16</id>
<lastname>Eisner</lastname>
<login>administrator</login>
</updated-by>
</asset-tag>
</asset-tags>
<attachments />
</inventory-transaction>
```

## Receipt Create

In this example we are creating a Receiving Transaction.

We posted it to the URL:
`https://.coupahost.com/api/receiving_transactions`. This
created the receipt.

```text
<?xml version="1.0" encoding="UTF-8"?>
<inventory-transaction>
<barcode>4433</barcode>
<price>1000.00</price>
<quantity>1.0</quantity>
<rfid-tag>3344</rfid-tag>
<type type="string">InventoryReceipt</type>
<account>
<code>SF-Marketing-Assets</code>
<id type="integer">14</id>
</account>
<order-line>
<id>2949</id>
<line-num>1</line-num>
<order-header-id>2079</order-header-id>
</order-line>
<inspection-code>
<code>Fail</code>
<description />
<id type="integer">2</id>
</inspection-code>
<item>
<id type="integer">47</id>
<item-number>12345</item-number>
</item>
<to-warehouse>
<id type="integer">7</id>
</to-warehouse>
<to-warehouse-location>
<id type="integer">8</id>
</to-warehouse-location>
<uom>
<code>EA</code>
<id type="integer">1</id>
</uom>
<attachments />
</inventory-transaction>
```

## GET Receiving Transactions Options

Here are more examples of how to use the Receiving Transactions API to query and get the
result set you want.

This query will return all receipts that have been received:

```text
https://<instance url>/api/receiving_transactions?type=InventoryReceipt&order-line[status]=received
```

This query will return all receipts with a line description that contains "Adobe Acrobat
Professional":

```text
https://<instance url>/api/receiving_transactions?type=InventoryReceipt&order-line[description][contains]=Adobe+Acrobat+Professional
```

This query will return all receipts for the account SF-IT-Assets :

```text
https://<instance url>/api/receiving_transactions?type=InventoryReceipt&account[code]=SF-IT-Assets
```

This query will return all receipts that were created after January 1, 2010 12:00:00:

```text
https://<instance url>/api/receiving_transactions?type=InventoryReceipt&order-line[created-at][gt]=2010-01-01T12:00:00
```

This query will return all receipts for the Chart of Accounts Ace Corporate:

```text
https://<instance url>/api/receiving_transactions?type=InventoryReceipt&account[account-type][name]=Ace+Corporate
```

This query will return all receipts created by the login name of administrator:

```text
https://<instance url>/api/receiving_transactions?type=InventoryReceipt&order-line[created-by][login]=administrator
```

## Return Requests API examples

Return a single return request by submitting a GET request:

- Method: GET

- Endpoint: `https:///api/return_requests/10`

This query returns the following payload:

```text
<?xml version="1.0" encoding="UTF-8"?>
<return-request>
<id type="integer">10</id>
<created-at type="dateTime">2022-04-19T01:48:05-07:00</created-at>
<updated-at type="dateTime">2022-04-19T01:49:06-07:00</updated-at>
<rma></rma>
<number>10</number>
<status>created</status>
<address>
<id type="integer">1410</id>
<created-at type="dateTime">2022-04-19T01:49:02-07:00</created-at>
<updated-at type="dateTime">2023-01-03T01:52:16-08:00</updated-at>
<name>test</name>
<location-code nil="true"/>
<street1>test</street1>
<street2 nil="true"/>
<city>test</city>
<state nil="true"/>
<state-iso-code nil="true"/>
<postal-code>111111</postal-code>
<attention nil="true"/>
<active type="boolean">true</active>
<business-group-name nil="true"/>
<vat-number nil="true"/>
<local-tax-number nil="true"/>
<type>SupplierReturnAddress</type>
<country>
<id type="integer">99</id>
<code>IN</code>
<name>India</name>
</country>
<vat-country nil="true"/>
<content-groups type="array"/>
<purposes type="array"/>
<tax-registrations type="array"/>
<created-by>
<id type="integer">261</id>
<login>harold.sheen@coupa.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">264</id>
<login>sheen</login>
<employee-number></employee-number>
<firstname>harold</firstname>
<lastname>sheen</lastname>
<fullname>harold sheen</fullname>
<email>harold@demo.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<custom-fields nil="true"/>
</updated-by>
</address>
<lines type="array">
<line>
<id type="integer">10</id>
<created-at type="dateTime">2022-04-19T01:48:05-07:00</created-at>
<updated-at type="dateTime">2022-04-19T01:49:06-07:00</updated-at>
<source-transaction-id type="integer">736</source-transaction-id>
<quantity type="decimal">3.0</quantity>
<price type="decimal">425.00</price>
<weight nil="true"/>
<inventory-transaction-id type="integer">738</inventory-transaction-id>
<warehouse>
<id type="integer">6</id>
<created-at type="dateTime">2009-08-20T11:31:47-07:00</created-at>
<updated-at type="dateTime">2022-06-28T07:46:01-07:00</updated-at>
<active-flag type="boolean">true</active-flag>
<description>Virtual Location to Track Assets Assigned to Employees</description>
<name>Employee Use</name>
<currency>
<id type="integer">1</id>
<code>USD</code>
<decimals type="integer">2</decimals>
</currency>
<address>
<id type="integer">68</id>
<created-at type="dateTime">2009-08-20T11:31:47-07:00</created-at>
<updated-at type="dateTime">2022-06-28T07:46:01-07:00</updated-at>
<name></name>
<location-code nil="true"/>
<street1>38 Market Street</street1>
<street2></street2>
<city>San Francisco</city>
<state>CA</state>
<state-iso-code nil="true"/>
<postal-code>97104</postal-code>
<attention></attention>
<active type="boolean">true</active>
<business-group-name nil="true"/>
<vat-number nil="true"/>
<local-tax-number nil="true"/>
<type nil="true"/>
<country>
<id type="integer">223</id>
<code>US</code>
<name>United States</name>
</country>
<vat-country nil="true"/>
<content-groups type="array"/>
<purposes type="array"/>
<tax-registrations type="array"/>
<created-by>
<id type="integer">16</id>
<login>kline</login>
<employee-number></employee-number>
<firstname>Kevin</firstname>
<lastname>Kline</lastname>
<fullname>Kevin Kline</fullname>
<email>kevin.kline@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">261</id>
<login>harold.sheen@coupa.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@coupa.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</updated-by>
</address>
<warehouse-type>
<id type="integer">2</id>
<created-at type="dateTime">2008-10-27T14:30:18-07:00</created-at>
<updated-at type="dateTime">2008-10-27T14:30:18-07:00</updated-at>
<name>Closet</name>
<description>Closet</description>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<fullname>Coupa Support</fullname>
<email>upgrade+coupasupport@coupa.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<fullname>Coupa Support</fullname>
<email>upgrade+coupasupport@coupa.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</updated-by>
</warehouse-type>
<warehouse-locations type="array">
<warehouse-location>
<id type="integer">6</id>
<created-at type="dateTime">2009-08-20T11:31:47-07:00</created-at>
<updated-at type="dateTime">2022-06-28T07:46:01-07:00</updated-at>
<aisle>1</aisle>
<bin>1</bin>
<level>2</level>
<warehouse-id type="integer">6</warehouse-id>
<warehouse-name>Employee Use</warehouse-name>
<label>1-1-2</label>
<created-by>
<id type="integer">16</id>
<login>krhine</login>
<employee-number></employee-number>
<firstname>Kevin</firstname>
<lastname>kline</lastname>
<fullname>Kevin Kline</fullname>
<email>kevin.kline@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">261</id>
<login>harold.sheen@coupa.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</updated-by>
</warehouse-location>
<warehouse-location>
<id type="integer">15</id>
<created-at type="dateTime">2022-06-28T07:46:01-07:00</created-at>
<updated-at type="dateTime">2022-06-28T07:46:01-07:00</updated-at>
<aisle>2</aisle>
<bin>3</bin>
<level>4</level>
<warehouse-id type="integer">6</warehouse-id>
<warehouse-name>Employee Use</warehouse-name>
<label>2-3-4</label>
<created-by>
<id type="integer">261</id>
<login>harold.sheen@company.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">261</id>
<login>harold.sheen@coupa.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</updated-by>
</warehouse-location>
</warehouse-locations>
<created-by>
<id type="integer">16</id>
<login>krhine</login>
<employee-number></employee-number>
<firstname>Kevin</firstname>
<lastname>Kline</lastname>
<fullname>Kevin Kline</fullname>
<email>kevin.kline@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">261</id>
<login>harold.sheen@company.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</updated-by>
<custom-fields>
<type></type>
</custom-fields>
</warehouse>
<warehouse-location>
<id type="integer">6</id>
<created-at type="dateTime">2009-08-20T11:31:47-07:00</created-at>
<updated-at type="dateTime">2022-06-28T07:46:01-07:00</updated-at>
<aisle>1</aisle>
<bin>1</bin>
<level>2</level>
<warehouse-id type="integer">6</warehouse-id>
<warehouse-name>Employee Use</warehouse-name>
<label>1-1-2</label>
<created-by>
<id type="integer">16</id>
<login>krhine</login>
<employee-number></employee-number>
<firstname>Kevin</firstname>
<lastname>Rhine</lastname>
<fullname>Kevin Rhine</fullname>
<email>kevin.rhine@coupa.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity></gpo-entity>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">261</id>
<login>harold.sheen@company.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</updated-by>
</warehouse-location>
<reason-insight>
<id type="integer">17</id>
<created-at type="dateTime">2018-01-16T04:01:34-08:00</created-at>
<updated-at type="dateTime">2018-01-16T04:01:34-08:00</updated-at>
<reason-type>Returns</reason-type>
<code>Damaged Item</code>
<description>Item in damaged condition</description>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<fullname>Coupa Support</fullname>
<email>upgrade+coupasupport@coupa.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<employee-number></employee-number>
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<fullname>Coupa Support</fullname>
<email>upgrade+coupasupport@coupa.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</updated-by>
</reason-insight>
</line>
</lines>
<created-by>
<id type="integer">261</id>
<login>harold.sheen@company.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</created-by>
<updated-by>
<id type="integer">261</id>
<login>harold.sheen@company.com</login>
<employee-number nil="true"/>
<firstname>Harold</firstname>
<lastname>Sheen</lastname>
<fullname>Harold Sheen</fullname>
<email>harold.sheen@company.com</email>
<salesforce-id nil="true"/>
<avatar-thumb-url nil="true"/>
<gpo-entity nil="true"/>
<custom-fields nil="true"/>
</updated-by>
</return-request>
```

Create a return request:

- Method: POST

- Endpoint: `https:///api/return_requests`

We've included the following payload in the request body:

```text
<return-request>
<number>1234</number>
<rma>return1234</rma>
<address><id>1</id></address>
<lines type="array">
<line>
<source-transaction-id>894</source-transaction-id>
<quantity>5</quantity>
</line>
</lines>
</return-request>
```
