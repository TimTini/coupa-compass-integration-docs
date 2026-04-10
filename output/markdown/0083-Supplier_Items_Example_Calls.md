---
title: "Supplier Items Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/supplier-items-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/supplier-items-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:21+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
  - "Supplier Items Example Calls"
---

# Supplier Items Example Calls

## Create Supplier Item

Here's an example where catalog item 'Turkey' with id=1 already exists in Coupa. We are
posting to api/supplier_items to associate catalog item turkey to supplier Saladino's OG and
marking it as
preferred.

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier-item>
<price type="decimal">2.00</price>
<supplier-part-num>99847490</supplier-part-num>
<preferred>true</preferred>
<currency>
<id type="integer">1</id>
<code>USD</code>
</currency>
<supplier>
<number>DC05</number>
</supplier>
<item>
<id type="integer">1</id>
<name>Turkey</name>
</item>
<contract>
<name>Saladino's OG 15</name>
</contract>
</supplier-item>
```
