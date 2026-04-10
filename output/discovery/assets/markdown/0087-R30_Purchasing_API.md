---
title: "R30_Purchasing_API.json"
url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/R30/R30_Purchasing_API.json"
final_url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/R30/R30_Purchasing_API.json"
content_type: "application/json"
classification: "json_asset"
fetched_at: "2026-04-10T01:56:01+00:00"
---

# R30_Purchasing_API.json

```json
{
  "swagger": "2.0",
  "info": {
    "version": "",
    "title": "Coupa API",
    "description": "RESTful API that provides robust access to read, edit, or integrate your data with the Coupa platform. The [JSON](/api_docs/1.json) and [YAML](/api_docs/1.yaml) are also available."
  },
  "host": "r30-proc.coupadev.com",
  "basePath": "/api",
  "tags": [
    {
      "name": "InvoiceEmail",
      "description": "Invoice Emails API"
    },
    {
      "name": "OrderPadLine",
      "description": "Order Pad/List Lines API"
    },
    {
      "name": "OrderPad",
      "description": "Order Pads/Lists API"
    },
    {
      "name": "OrderHeaderChange",
      "description": "Purchase Order Changes API"
    },
    {
      "name": "SupplierItem",
      "description": "Supplier Items API"
    },
    {
      "name": "OrderHeader",
      "description": "Purchase Orders API"
    },
    {
      "name": "OrderLine",
      "description": "Purchase Order Lines API"
    },
    {
      "name": "RequisitionHeader",
      "description": "Requisitions API"
    },
    {
      "name": "LegalPaymentReceipt",
      "description": "Payment Receipts API"
    },
    {
      "name": "InvoiceHeader",
      "description": "Invoices API"
    },
    {
      "name": "Asn-Header",
      "description": "Advance Ship Notice Headers API"
    },
    {
      "name": "Asn-Line",
      "description": "Advance Ship Notice Lines API"
    },
    {
      "name": "InventoryTransaction",
      "description": "Inventory Transactions API"
    },
    {
      "name": "ContractTerm",
      "description": "Contract Terms API"
    },
    {
      "name": "Contract",
      "description": "Contracts API"
    }
  ],
  "schemes": [
    "https"
  ],
  "security": [
    {
      "internalApiKey": []
    }
  ],
  "paths": {
    "/invoice_emails": {
      "get": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Query invoice emails",
        "description": "Query invoice emails",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceEmail objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/InvoiceEmail"
              },
              "xml": {
                "name": "invoice-emails",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Create invoice email",
        "description": "Create invoice email",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceEmail",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/invoice_emails/{id}": {
      "get": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Show invoice email",
        "description": "Show invoice email",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceEmail object",
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Update invoice email",
        "description": "Update invoice email",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceEmail",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceEmail object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceEmail"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Update invoice email",
        "description": "Update invoice email",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceEmail",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceEmail object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceEmail"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/order_pads/{order_pad_id}/order_pad_lines": {
      "get": {
        "tags": [
          "OrderPadLine"
        ],
        "summary": "Query order pad lines",
        "description": "Query order pad lines",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "order_pad_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderPadLine objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/OrderPadLine"
              },
              "xml": {
                "name": "order-pad-lines",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "OrderPadLine"
        ],
        "summary": "Create order pad line",
        "description": "Create order pad line",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderPadLine",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/OrderPadLine"
            }
          },
          {
            "in": "path",
            "name": "order_pad_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/OrderPadLine"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/order_pads/{order_pad_id}/order_pad_lines/{id}": {
      "get": {
        "tags": [
          "OrderPadLine"
        ],
        "summary": "Show order pad line",
        "description": "Show order pad line",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "order_pad_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderPadLine object",
            "schema": {
              "$ref": "#/definitions/OrderPadLine"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "OrderPadLine"
        ],
        "summary": "Update order pad line",
        "description": "Update order pad line",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderPadLine",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderPadLine"
            }
          },
          {
            "in": "path",
            "name": "order_pad_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderPadLine object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderPadLine"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "OrderPadLine"
        ],
        "summary": "Update order pad line",
        "description": "Update order pad line",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderPadLine",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderPadLine"
            }
          },
          {
            "in": "path",
            "name": "order_pad_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderPadLine object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderPadLine"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/order_pads": {
      "get": {
        "tags": [
          "OrderPad"
        ],
        "summary": "Query order pads",
        "description": "Query order pads",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderPad objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/OrderPad"
              },
              "xml": {
                "name": "order-pads",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "OrderPad"
        ],
        "summary": "Create order pad",
        "description": "Create order pad",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderPad",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/OrderPad"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/OrderPad"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/order_pads/{id}": {
      "get": {
        "tags": [
          "OrderPad"
        ],
        "summary": "Show order pad",
        "description": "Show order pad",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderPad object",
            "schema": {
              "$ref": "#/definitions/OrderPad"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "OrderPad"
        ],
        "summary": "Update order pad",
        "description": "Update order pad",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderPad",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderPad"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderPad object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderPad"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "OrderPad"
        ],
        "summary": "Update order pad",
        "description": "Update order pad",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderPad",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderPad"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderPad object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderPad"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_changes/{id}/add_approver": {
      "put": {
        "tags": [
          "OrderHeaderChange"
        ],
        "summary": "Manually add an approver for an order header change",
        "description": "Manually add an approver for an order header change",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeaderChange",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeaderChange"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeaderChange object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeaderChange"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_changes/{id}/remove_approval": {
      "put": {
        "tags": [
          "OrderHeaderChange"
        ],
        "summary": "Remove an approver who was manually added",
        "description": "Remove an approver who was manually added",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeaderChange",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeaderChange"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeaderChange object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeaderChange"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_changes/{id}/submit_for_approval": {
      "put": {
        "tags": [
          "OrderHeaderChange"
        ],
        "summary": "/purchase_order_changes/{id}/submit_for_approval",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeaderChange",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeaderChange"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeaderChange object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeaderChange"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_changes": {
      "get": {
        "tags": [
          "OrderHeaderChange"
        ],
        "summary": "Query purchase order changes",
        "description": "Query purchase order changes",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeaderChange objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/OrderHeaderChange"
              },
              "xml": {
                "name": "order-header-changes",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "OrderHeaderChange"
        ],
        "summary": "Create purchase order change",
        "description": "Create purchase order change",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeaderChange",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/OrderHeaderChange"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/OrderHeaderChange"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/purchase_order_changes/{id}": {
      "get": {
        "tags": [
          "OrderHeaderChange"
        ],
        "summary": "Show purchase order change",
        "description": "Show purchase order change",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeaderChange object",
            "schema": {
              "$ref": "#/definitions/OrderHeaderChange"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "OrderHeaderChange"
        ],
        "summary": "Update purchase order change",
        "description": "Update purchase order change",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeaderChange",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeaderChange"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeaderChange object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeaderChange"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "OrderHeaderChange"
        ],
        "summary": "Update purchase order change",
        "description": "Update purchase order change",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeaderChange",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeaderChange"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeaderChange object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeaderChange"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/items/{item_id}/supplier_items": {
      "get": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Query supplier items",
        "description": "Query supplier items",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "item_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/SupplierItem"
              },
              "xml": {
                "name": "supplier-items",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Create supplier item",
        "description": "Create supplier item",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "SupplierItem",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          {
            "in": "path",
            "name": "item_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/items/{item_id}/supplier_items/{id}": {
      "get": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Show supplier item",
        "description": "Show supplier item",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "item_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Update supplier item",
        "description": "Update supplier item",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "SupplierItem",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          {
            "in": "path",
            "name": "item_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "items": {
                "$ref": "#/definitions/SupplierItem"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Update supplier item",
        "description": "Update supplier item",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "SupplierItem",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          {
            "in": "path",
            "name": "item_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "items": {
                "$ref": "#/definitions/SupplierItem"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/supplier_items/search": {
      "get": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Advanced supplier item search",
        "description": "Advanced supplier item search",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/supplier_items/catalog_item_info": {
      "get": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "/supplier_items/catalog_item_info",
        "description": "",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/supplier_items/catalog_items": {
      "get": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "/supplier_items/catalog_items",
        "description": "",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/supplier_items": {
      "get": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Query supplier items",
        "description": "Query supplier items",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/SupplierItem"
              },
              "xml": {
                "name": "supplier-items",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Create supplier item",
        "description": "Create supplier item",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "SupplierItem",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/supplier_items/{id}": {
      "get": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Show supplier item",
        "description": "Show supplier item",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Update supplier item",
        "description": "Update supplier item",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "SupplierItem",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "items": {
                "$ref": "#/definitions/SupplierItem"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "SupplierItem"
        ],
        "summary": "Update supplier item",
        "description": "Update supplier item",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "SupplierItem",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/SupplierItem"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "SupplierItem object",
            "schema": {
              "items": {
                "$ref": "#/definitions/SupplierItem"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_orders/{id}/release_from_buyer_hold": {
      "put": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Release purchase order on buyer hold",
        "description": "Release purchase order on buyer hold",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_orders/{id}/issue": {
      "put": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "IssueWithSend",
        "description": "IssueWithSend",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_orders/{id}/issue_without_send": {
      "put": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "IssueWithoutSend",
        "description": "IssueWithoutSend",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_orders/{id}/ignore_window_and_issue": {
      "put": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "IgnoreWindowsAndIssue",
        "description": "IgnoreWindowsAndIssue",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_orders/{id}/cancel": {
      "put": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Cancel",
        "description": "Cancel",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_orders/{id}/close": {
      "put": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Close",
        "description": "Close",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_orders/{id}/reopen": {
      "put": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Reopen",
        "description": "Reopen",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_orders": {
      "get": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Query purchase orders",
        "description": "Query purchase orders",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/OrderHeader"
              },
              "xml": {
                "name": "order-headers",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Create purchase order",
        "description": "Create purchase order",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/purchase_orders/{id}": {
      "get": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Show purchase order",
        "description": "Show purchase order",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Update purchase order",
        "description": "Update purchase order",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "OrderHeader"
        ],
        "summary": "Update purchase order",
        "description": "Update purchase order",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_lines/{id}/soft_close_for_receiving": {
      "put": {
        "tags": [
          "OrderLine"
        ],
        "summary": "Soft close for receiving",
        "description": "Soft close for receiving",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderLine",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderLine"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderLine object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderLine"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_lines/{id}/soft_close_for_invoicing": {
      "put": {
        "tags": [
          "OrderLine"
        ],
        "summary": "Soft close for invoicing",
        "description": "Soft close for invoicing",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderLine",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderLine"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderLine object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderLine"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_lines/{id}/reopen_for_receiving": {
      "put": {
        "tags": [
          "OrderLine"
        ],
        "summary": "Reopen for receiving",
        "description": "Reopen for receiving",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderLine",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderLine"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderLine object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderLine"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_lines/{id}/reopen_for_invoicing": {
      "put": {
        "tags": [
          "OrderLine"
        ],
        "summary": "Reopen for invoicing",
        "description": "Reopen for invoicing",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "OrderLine",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderLine"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderLine object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderLine"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_lines": {
      "get": {
        "tags": [
          "OrderLine"
        ],
        "summary": "Query purchase order lines",
        "description": "Query purchase order lines",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderLine objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/OrderLine"
              },
              "xml": {
                "name": "order-lines",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/purchase_order_lines/{id}": {
      "get": {
        "tags": [
          "OrderLine"
        ],
        "summary": "Show purchase order line",
        "description": "Show purchase order line",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "OrderLine object",
            "schema": {
              "$ref": "#/definitions/OrderLine"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "delete": {
        "tags": [
          "OrderLine"
        ],
        "summary": "Delete purchase order line",
        "description": "Delete purchase order line",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "Deleted"
          }
        }
      }
    },
    "/requisitions/{id}/add_approver": {
      "put": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Manually add an approver for a requisition",
        "description": "Manually add an approver for a requisition",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/RequisitionHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/requisitions/{id}/remove_approval": {
      "put": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Remove an approver who was manually added",
        "description": "Remove an approver who was manually added",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/RequisitionHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/requisitions/{id}/save_for_later": {
      "put": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Save For Later for API requisitions",
        "description": "Save For Later for API requisitions",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/RequisitionHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/requisitions/{id}/update_and_submit_for_approval": {
      "put": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Update requisition and submit for approval",
        "description": "Update requisition and submit for approval",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/RequisitionHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/requisitions/current_cart": {
      "get": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Send current cart for user, if there is no current cart then create and send",
        "description": "Send current cart for user, if there is no current cart then create and send",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/requisitions/submit_for_approval": {
      "post": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Create a requisition and attempt to submit it for approval / buyer action",
        "description": "Create a requisition and attempt to submit it for approval / buyer action",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/requisitions/create_as_cart": {
      "post": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Create a requisition in draft status, which will then need to be submitted manually",
        "description": "Create a requisition in draft status, which will then need to be submitted manually",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/requisitions/add_to_cart": {
      "post": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Add To Cart",
        "description": "Add To Cart",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/requisitions/mine": {
      "get": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "/requisitions/mine",
        "description": "",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/requisitions": {
      "get": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Query requisitions",
        "description": "Query requisitions",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/RequisitionHeader"
              },
              "xml": {
                "name": "requisition-headers",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Create a requisition in draft status, which will then need to be submitted manually",
        "description": "Create a requisition in draft status, which will then need to be submitted manually",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/requisitions/{id}": {
      "get": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Show requisition",
        "description": "Show requisition",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Update requisition",
        "description": "Update requisition",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/RequisitionHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Update requisition",
        "description": "Update requisition",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "RequisitionHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/RequisitionHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "RequisitionHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/RequisitionHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "delete": {
        "tags": [
          "RequisitionHeader"
        ],
        "summary": "Delete requisition",
        "description": "Delete requisition",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "Deleted"
          }
        }
      }
    },
    "/suppliers/{supplier_id}/invoice_emails": {
      "get": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Query invoice emails",
        "description": "Query invoice emails",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "supplier_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceEmail objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/InvoiceEmail"
              },
              "xml": {
                "name": "invoice-emails",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Create invoice email",
        "description": "Create invoice email",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceEmail",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          {
            "in": "path",
            "name": "supplier_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/suppliers/{supplier_id}/invoice_emails/{id}": {
      "get": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Show invoice email",
        "description": "Show invoice email",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "supplier_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceEmail object",
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Update invoice email",
        "description": "Update invoice email",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceEmail",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          {
            "in": "path",
            "name": "supplier_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceEmail object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceEmail"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "InvoiceEmail"
        ],
        "summary": "Update invoice email",
        "description": "Update invoice email",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceEmail",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceEmail"
            }
          },
          {
            "in": "path",
            "name": "supplier_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceEmail object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceEmail"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{invoice_id}/payment_receipts/{id}/retrieve_clearance_document": {
      "get": {
        "tags": [
          "LegalPaymentReceipt"
        ],
        "summary": "Retrieve/Download clearance document of payment receipt",
        "description": "Retrieve/Download clearance document of payment receipt",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "invoice_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "LegalPaymentReceipt object",
            "schema": {
              "$ref": "#/definitions/LegalPaymentReceipt"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/image_scan": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Update image scan attachment",
        "description": "Update image scan attachment",
        "consumes": [
          "multipart/form-data"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "file",
            "in": "formData",
            "required": false,
            "type": "file"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/submit": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Submit draft invoice for approval",
        "description": "Submit draft invoice for approval",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/flip_to_advance_ship_notice": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Flip invoice to Advance Ship Notice",
        "description": "Flip invoice to Advance Ship Notice",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/void": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Void an approved invoice",
        "description": "Void an approved invoice",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/retrieve_image_scan": {
      "get": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Retrieve/Download image scan",
        "description": "Retrieve/Download image scan",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/retrieve_clearance_document": {
      "get": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Retrieve/Download clearance document",
        "description": "Retrieve/Download clearance document",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/retrieve_legal_invoice_pdf": {
      "get": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Retrieve/Download legal invoice pdf",
        "description": "Retrieve/Download legal invoice pdf",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/update_line_accounts": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Update line accounts",
        "description": "Update line accounts",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/revalidate_tolerances": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Revalidate tolerances",
        "description": "Revalidate tolerances",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/bypass_approvals": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Bypass approvals",
        "description": "Bypass approvals",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/bypass_current_approval": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Bypass current approval",
        "description": "Bypass current approval",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/restart_approvals": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Restart approvals",
        "description": "Restart approvals",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/dispute": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Dispute invoice",
        "description": "Dispute invoice",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/withdraw_dispute": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Withdraw dispute",
        "description": "Withdraw dispute",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/add_approver": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Manually add an approver for an invoice",
        "description": "Manually add an approver for an invoice",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/remove_approval": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Remove an approver who was manually added",
        "description": "Remove an approver who was manually added",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}/abandon": {
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Abandon invoice",
        "description": "Abandon invoice",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices": {
      "get": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Query invoices",
        "description": "Query invoices",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              },
              "xml": {
                "name": "invoice-headers",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/invoices/{id}": {
      "get": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Show invoice",
        "description": "Show invoice",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Update invoice",
        "description": "Update invoice",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Update invoice",
        "description": "Update invoice",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InvoiceHeader",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InvoiceHeader"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InvoiceHeader object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InvoiceHeader"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "delete": {
        "tags": [
          "InvoiceHeader"
        ],
        "summary": "Delete Invoice in New status",
        "description": "Delete Invoice in New status",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "Deleted"
          }
        }
      }
    },
    "/asn/headers/receive": {
      "put": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "/asn/headers/receive",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Header",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Header object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Header"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/asn/headers/void": {
      "put": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "/asn/headers/void",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Header",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Header object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Header"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/asn/headers/{id}/receive": {
      "put": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "/asn/headers/{id}/receive",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Header",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Header object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Header"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/asn/headers/{id}/void": {
      "put": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "/asn/headers/{id}/void",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Header",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Header object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Header"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/asn/headers": {
      "get": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "Query advance ship notice header",
        "description": "Query advance ship notice header",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Header objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Asn-Header"
              },
              "xml": {
                "name": "asn-headers",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "Create advance ship notice header",
        "description": "Create advance ship notice header",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Header",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/asn/headers/{id}": {
      "get": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "Show advance ship notice header",
        "description": "Show advance ship notice header",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Header object",
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "Update advance ship notice header",
        "description": "Update advance ship notice header",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Header",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Header object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Header"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "Asn-Header"
        ],
        "summary": "Update advance ship notice header",
        "description": "Update advance ship notice header",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Header",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Header"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Header object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Header"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/asn/lines/receive": {
      "put": {
        "tags": [
          "Asn-Line"
        ],
        "summary": "/asn/lines/receive",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Line",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Line"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Line object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Line"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/asn/lines/void": {
      "put": {
        "tags": [
          "Asn-Line"
        ],
        "summary": "/asn/lines/void",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Line",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Line"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Line object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Line"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/asn/lines/{id}/receive": {
      "put": {
        "tags": [
          "Asn-Line"
        ],
        "summary": "/asn/lines/{id}/receive",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Line",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Line"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Line object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Line"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/asn/lines/{id}/void": {
      "put": {
        "tags": [
          "Asn-Line"
        ],
        "summary": "/asn/lines/{id}/void",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Asn-Line",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Asn-Line"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Asn-Line object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Asn-Line"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/inventory_transactions/{id}/void": {
      "put": {
        "tags": [
          "InventoryTransaction"
        ],
        "summary": "Perform Void action on inventory transaction",
        "description": "Perform Void action on inventory transaction",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InventoryTransaction",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InventoryTransaction"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InventoryTransaction object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InventoryTransaction"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/inventory_transactions": {
      "get": {
        "tags": [
          "InventoryTransaction"
        ],
        "summary": "Query inventory transactions",
        "description": "Query inventory transactions",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InventoryTransaction objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/InventoryTransaction"
              },
              "xml": {
                "name": "inventory-transactions",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "InventoryTransaction"
        ],
        "summary": "Create inventory transaction",
        "description": "Create inventory transaction",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InventoryTransaction",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/InventoryTransaction"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/InventoryTransaction"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/inventory_transactions/{id}": {
      "get": {
        "tags": [
          "InventoryTransaction"
        ],
        "summary": "Show inventory transaction",
        "description": "Show inventory transaction",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InventoryTransaction object",
            "schema": {
              "$ref": "#/definitions/InventoryTransaction"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "InventoryTransaction"
        ],
        "summary": "Update inventory transaction",
        "description": "Update inventory transaction",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InventoryTransaction",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InventoryTransaction"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InventoryTransaction object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InventoryTransaction"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "InventoryTransaction"
        ],
        "summary": "Update inventory transaction",
        "description": "Update inventory transaction",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "InventoryTransaction",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/InventoryTransaction"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "InventoryTransaction object",
            "schema": {
              "items": {
                "$ref": "#/definitions/InventoryTransaction"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{contract_id}/contract_terms": {
      "get": {
        "tags": [
          "ContractTerm"
        ],
        "summary": "Query contract terms",
        "description": "Query contract terms",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "contract_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "ContractTerm objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/ContractTerm"
              },
              "xml": {
                "name": "contract-terms",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "ContractTerm"
        ],
        "summary": "Create contract term",
        "description": "Create contract term",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "ContractTerm",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/ContractTerm"
            }
          },
          {
            "in": "path",
            "name": "contract_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/ContractTerm"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/contracts/{contract_id}/contract_terms/{id}": {
      "get": {
        "tags": [
          "ContractTerm"
        ],
        "summary": "Show contract term",
        "description": "Show contract term",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "contract_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "ContractTerm object",
            "schema": {
              "$ref": "#/definitions/ContractTerm"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "ContractTerm"
        ],
        "summary": "Update contract term",
        "description": "Update contract term",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "ContractTerm",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/ContractTerm"
            }
          },
          {
            "in": "path",
            "name": "contract_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "ContractTerm object",
            "schema": {
              "items": {
                "$ref": "#/definitions/ContractTerm"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "ContractTerm"
        ],
        "summary": "Update contract term",
        "description": "Update contract term",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "ContractTerm",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/ContractTerm"
            }
          },
          {
            "in": "path",
            "name": "contract_id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "ContractTerm object",
            "schema": {
              "items": {
                "$ref": "#/definitions/ContractTerm"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/retrieve_legal_agreement": {
      "get": {
        "tags": [
          "Contract"
        ],
        "summary": "Get legal legal_agreement file",
        "description": "Get legal legal_agreement file",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/legal_agreement": {
      "post": {
        "tags": [
          "Contract"
        ],
        "summary": "Add or update legal legal_agreement file",
        "description": "Add or update legal legal_agreement file",
        "consumes": [
          "multipart/form-data"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "file",
            "in": "formData",
            "required": true,
            "type": "file"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      },
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Add or update legal legal_agreement file",
        "description": "Add or update legal legal_agreement file",
        "consumes": [
          "multipart/form-data"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "file",
            "in": "formData",
            "required": false,
            "type": "file"
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/complete": {
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Moves the contract to the completed state.",
        "description": "Moves the contract to the completed state.",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/ccc_signature_created": {
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Notifies that a signature has been added in CCC.",
        "description": "Notifies that a signature has been added in CCC.",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/add_approver": {
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Manually add an approver for a contract",
        "description": "Manually add an approver for a contract",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/remove_approval": {
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Remove an approver who was manually added",
        "description": "Remove an approver who was manually added",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/submit_for_approval": {
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Submits the contract for approval.",
        "description": "Submits the contract for approval.",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/withdraw_signatures": {
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Moves contract to corresponding status after CCC withdraw_signatures.",
        "description": "Moves contract to corresponding status after CCC withdraw_signatures.",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    },
    "/contracts/{id}/create_published": {
      "post": {
        "tags": [
          "Contract"
        ],
        "summary": "/contracts/{id}/create_published",
        "description": "",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/contracts": {
      "get": {
        "tags": [
          "Contract"
        ],
        "summary": "Query contracts",
        "description": "Query contracts",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Contract"
              },
              "xml": {
                "name": "contracts",
                "wrapped": true
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "post": {
        "tags": [
          "Contract"
        ],
        "summary": "Create contract",
        "description": "Create contract",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/contracts/{id}": {
      "get": {
        "tags": [
          "Contract"
        ],
        "summary": "Show contract",
        "description": "Show contract",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "limit",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "offset",
            "type": "integer",
            "required": false
          },
          {
            "in": "query",
            "name": "order_by",
            "type": "string",
            "required": false
          },
          {
            "in": "query",
            "name": "dir",
            "type": "string",
            "required": false,
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "patch": {
        "tags": [
          "Contract"
        ],
        "summary": "Update contract",
        "description": "Update contract",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      },
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Update contract",
        "description": "Update contract",
        "consumes": [
          "application/xml",
          "application/json"
        ],
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "Contract",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/Contract"
            }
          },
          {
            "in": "path",
            "name": "id",
            "required": true,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "return_object",
            "type": "string",
            "required": false,
            "enum": [
              "limited",
              "shallow",
              "none"
            ]
          },
          {
            "in": "query",
            "name": "filter",
            "type": "string",
            "required": false
          }
        ],
        "responses": {
          "200": {
            "description": "Contract object",
            "schema": {
              "items": {
                "$ref": "#/definitions/Contract"
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    }
  },
  "securityDefinitions": {
    "internalApiKey": {
      "type": "apiKey",
      "in": "header",
      "name": "X-COUPA-API-KEY"
    }
  },
  "definitions": {
    "Account": {
      "type": "object",
      "properties": {
        "account-type": {
          "$ref": "#/definitions/AccountType"
        },
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean"
        },
        "code": {
          "type": "string",
          "description": "All segments concatenated with a hyphen ( - )",
          "format": "string(1024)",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "This is the nickname for the account.  Users can view and search against this field through the user interface.",
          "format": "string(1024)"
        },
        "segment-1": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-10": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-11": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-12": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-13": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-14": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-15": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-16": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-17": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-18": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-19": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-2": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-20": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-3": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-4": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-5": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-6": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-7": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-8": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "segment-9": {
          "type": "string",
          "description": "Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132)",
          "format": "string(100)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account-type"
      ]
    },
    "AccountGroup": {
      "type": "object",
      "properties": {
        "account-type": {
          "$ref": "#/definitions/AccountType"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(80)"
        },
        "segment-10-col": {
          "type": "string",
          "description": "segment_10_col",
          "format": "string(255)"
        },
        "segment-10-op": {
          "type": "string",
          "description": "segment_10_op",
          "format": "string(255)"
        },
        "segment-10-val": {
          "type": "string",
          "description": "segment_10_val",
          "format": "string(255)"
        },
        "segment-11-col": {
          "type": "string",
          "description": "segment_11_col",
          "format": "string(255)"
        },
        "segment-11-op": {
          "type": "string",
          "description": "segment_11_op",
          "format": "string(255)"
        },
        "segment-11-val": {
          "type": "string",
          "description": "segment_11_val",
          "format": "string(255)"
        },
        "segment-12-col": {
          "type": "string",
          "description": "segment_12_col",
          "format": "string(255)"
        },
        "segment-12-op": {
          "type": "string",
          "description": "segment_12_op",
          "format": "string(255)"
        },
        "segment-12-val": {
          "type": "string",
          "description": "segment_12_val",
          "format": "string(255)"
        },
        "segment-13-col": {
          "type": "string",
          "description": "segment_13_col",
          "format": "string(255)"
        },
        "segment-13-op": {
          "type": "string",
          "description": "segment_13_op",
          "format": "string(255)"
        },
        "segment-13-val": {
          "type": "string",
          "description": "segment_13_val",
          "format": "string(255)"
        },
        "segment-14-col": {
          "type": "string",
          "description": "segment_14_col",
          "format": "string(255)"
        },
        "segment-14-op": {
          "type": "string",
          "description": "segment_14_op",
          "format": "string(255)"
        },
        "segment-14-val": {
          "type": "string",
          "description": "segment_14_val",
          "format": "string(255)"
        },
        "segment-15-col": {
          "type": "string",
          "description": "segment_15_col",
          "format": "string(255)"
        },
        "segment-15-op": {
          "type": "string",
          "description": "segment_15_op",
          "format": "string(255)"
        },
        "segment-15-val": {
          "type": "string",
          "description": "segment_15_val",
          "format": "string(255)"
        },
        "segment-16-col": {
          "type": "string",
          "description": "segment_16_col",
          "format": "string(255)"
        },
        "segment-16-op": {
          "type": "string",
          "description": "segment_16_op",
          "format": "string(255)"
        },
        "segment-16-val": {
          "type": "string",
          "description": "segment_16_val",
          "format": "string(255)"
        },
        "segment-17-col": {
          "type": "string",
          "description": "segment_17_col",
          "format": "string(255)"
        },
        "segment-17-op": {
          "type": "string",
          "description": "segment_17_op",
          "format": "string(255)"
        },
        "segment-17-val": {
          "type": "string",
          "description": "segment_17_val",
          "format": "string(255)"
        },
        "segment-18-col": {
          "type": "string",
          "description": "segment_18_col",
          "format": "string(255)"
        },
        "segment-18-op": {
          "type": "string",
          "description": "segment_18_op",
          "format": "string(255)"
        },
        "segment-18-val": {
          "type": "string",
          "description": "segment_18_val",
          "format": "string(255)"
        },
        "segment-19-col": {
          "type": "string",
          "description": "segment_19_col",
          "format": "string(255)"
        },
        "segment-19-op": {
          "type": "string",
          "description": "segment_19_op",
          "format": "string(255)"
        },
        "segment-19-val": {
          "type": "string",
          "description": "segment_19_val",
          "format": "string(255)"
        },
        "segment-1-col": {
          "type": "string",
          "description": "segment_1_col",
          "format": "string(255)"
        },
        "segment-1-op": {
          "type": "string",
          "description": "segment_1_op",
          "format": "string(255)"
        },
        "segment-1-val": {
          "type": "string",
          "description": "segment_1_val",
          "format": "string(255)"
        },
        "segment-20-col": {
          "type": "string",
          "description": "segment_20_col",
          "format": "string(255)"
        },
        "segment-20-op": {
          "type": "string",
          "description": "segment_20_op",
          "format": "string(255)"
        },
        "segment-20-val": {
          "type": "string",
          "description": "segment_20_val",
          "format": "string(255)"
        },
        "segment-2-col": {
          "type": "string",
          "description": "segment_2_col",
          "format": "string(255)"
        },
        "segment-2-op": {
          "type": "string",
          "description": "segment_2_op",
          "format": "string(255)"
        },
        "segment-2-val": {
          "type": "string",
          "description": "segment_2_val",
          "format": "string(255)"
        },
        "segment-3-col": {
          "type": "string",
          "description": "segment_3_col",
          "format": "string(255)"
        },
        "segment-3-op": {
          "type": "string",
          "description": "segment_3_op",
          "format": "string(255)"
        },
        "segment-3-val": {
          "type": "string",
          "description": "segment_3_val",
          "format": "string(255)"
        },
        "segment-4-col": {
          "type": "string",
          "description": "segment_4_col",
          "format": "string(255)"
        },
        "segment-4-op": {
          "type": "string",
          "description": "segment_4_op",
          "format": "string(255)"
        },
        "segment-4-val": {
          "type": "string",
          "description": "segment_4_val",
          "format": "string(255)"
        },
        "segment-5-col": {
          "type": "string",
          "description": "segment_5_col",
          "format": "string(255)"
        },
        "segment-5-op": {
          "type": "string",
          "description": "segment_5_op",
          "format": "string(255)"
        },
        "segment-5-val": {
          "type": "string",
          "description": "segment_5_val",
          "format": "string(255)"
        },
        "segment-6-col": {
          "type": "string",
          "description": "segment_6_col",
          "format": "string(255)"
        },
        "segment-6-op": {
          "type": "string",
          "description": "segment_6_op",
          "format": "string(255)"
        },
        "segment-6-val": {
          "type": "string",
          "description": "segment_6_val",
          "format": "string(255)"
        },
        "segment-7-col": {
          "type": "string",
          "description": "segment_7_col",
          "format": "string(255)"
        },
        "segment-7-op": {
          "type": "string",
          "description": "segment_7_op",
          "format": "string(255)"
        },
        "segment-7-val": {
          "type": "string",
          "description": "segment_7_val",
          "format": "string(255)"
        },
        "segment-8-col": {
          "type": "string",
          "description": "segment_8_col",
          "format": "string(255)"
        },
        "segment-8-op": {
          "type": "string",
          "description": "segment_8_op",
          "format": "string(255)"
        },
        "segment-8-val": {
          "type": "string",
          "description": "segment_8_val",
          "format": "string(255)"
        },
        "segment-9-col": {
          "type": "string",
          "description": "segment_9_col",
          "format": "string(255)"
        },
        "segment-9-op": {
          "type": "string",
          "description": "segment_9_op",
          "format": "string(255)"
        },
        "segment-9-val": {
          "type": "string",
          "description": "segment_9_val",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account-type",
        "name"
      ]
    },
    "AccountType": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the chart of account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "dynamic-flag": {
          "type": "boolean",
          "description": "Boolean value for determing if account type is dynamic",
          "format": "boolean",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "legal-entity-name": {
          "type": "string",
          "description": "Legal entity or entities that are associated with this chart of accounts",
          "format": "string",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(50)"
        },
        "primary-address": {
          "$ref": "#/definitions/Address"
        },
        "primary-contact": {
          "$ref": "#/definitions/Contact"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "currency",
        "name"
      ]
    },
    "Address": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A no value will make the address inactive making it no longer available to users.  A yes value will make it active and available to users.",
          "format": "boolean"
        },
        "attention": {
          "type": "string",
          "description": "Address Default Attention Line",
          "format": "string(255)"
        },
        "business-group-name": {
          "type": "string",
          "description": "Content Group Name for Address",
          "format": "string"
        },
        "city": {
          "type": "string",
          "description": "City Name",
          "format": "string(50)"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa Internal Address ID",
          "format": "integer",
          "readOnly": true
        },
        "local-tax-number": {
          "type": "string",
          "description": "Local Tax Number",
          "format": "string(255)"
        },
        "location-code": {
          "type": "string",
          "description": "location_code",
          "format": "string(255)"
        },
        "name": {
          "type": "string",
          "description": "Address 'Nickname'",
          "format": "string(255)"
        },
        "postal-code": {
          "type": "string",
          "description": "Postal Code",
          "format": "string(50)"
        },
        "purposes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Purpose"
          }
        },
        "state": {
          "type": "string",
          "description": "State Abbreviation",
          "format": "string(50)"
        },
        "street1": {
          "type": "string",
          "description": "Address Line 1",
          "format": "string(100)"
        },
        "street2": {
          "type": "string",
          "description": "Address Line 2",
          "format": "string(100)"
        },
        "street3": {
          "type": "string",
          "description": "Address Line 3",
          "format": "string(100)"
        },
        "street4": {
          "type": "string",
          "description": "Address Line 4",
          "format": "string(100)"
        },
        "tax-registrations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/TaxRegistration"
          }
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "vat-country": {
          "$ref": "#/definitions/Country"
        },
        "vat-number": {
          "type": "string",
          "description": "VAT identification number used for value added tax purposes",
          "format": "string(255)"
        }
      },
      "required": [
        "city",
        "country",
        "local-tax-number",
        "postal-code",
        "street1"
      ]
    },
    "AdjustmentCode": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "Code",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "type": {
          "type": "string",
          "description": "Type",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "code",
        "name"
      ]
    },
    "AmountComponent": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "Amount",
          "format": "decimal(30,6)"
        },
        "amount-type": {
          "type": "string",
          "description": "Amount Type",
          "format": "string(255)",
          "enum": [
            "supplier_net_paid",
            "supplier_net_received",
            "supplier_fees",
            "msp_net_paid",
            "msp_net_received",
            "msp_fees",
            "vms_net_paid",
            "vms_net_received",
            "vms_fees"
          ]
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "source-id": {
          "type": "integer",
          "description": "Source Id",
          "format": "integer"
        },
        "source-type": {
          "type": "string",
          "description": "Source Type",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "amount",
        "amount-type",
        "currency"
      ]
    },
    "Approval": {
      "type": "object",
      "properties": {
        "approvable-id": {
          "type": "integer",
          "description": "The document ID that was approved",
          "format": "integer",
          "readOnly": true
        },
        "approvable-type": {
          "type": "string",
          "description": "The document type that was approved (requisition, purchase order, etc)",
          "format": "string(255)",
          "readOnly": true
        },
        "approval-chain-id": {
          "type": "integer",
          "description": "ID of the approval chain this approval is located in",
          "format": "integer",
          "readOnly": true
        },
        "approval-date": {
          "type": "string",
          "description": "The date the approval occurred",
          "format": "datetime",
          "readOnly": true
        },
        "approved-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "approver": {
          "description": "Approver. Can be one of multiple objects: User, ApprovalGroup",
          "readOnly": true
        },
        "approver-type": {
          "type": "string",
          "description": "The role of the approver",
          "format": "string(255)",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "delegate": {
          "description": "Delegate. Can be one of multiple objects: User, ApprovalGroup",
          "readOnly": true
        },
        "delegate-id": {
          "type": "string",
          "description": "The delegate ID that made the approval (if applicable)",
          "format": "string",
          "readOnly": true
        },
        "delegates": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/DelegateApproval"
          }
        },
        "holdable": {
          "type": "boolean",
          "description": "Hold the approval or not",
          "format": "boolean",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "note": {
          "type": "string",
          "description": "Reason for approval or reject",
          "format": "text",
          "readOnly": true
        },
        "position": {
          "type": "integer",
          "description": "The position in the approval chain this approval occurred",
          "format": "integer",
          "readOnly": true
        },
        "reasons": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ApprovalReason"
          }
        },
        "status": {
          "type": "string",
          "description": "The status of the approval (approved, escalated, rejected, etc)",
          "format": "string(50)",
          "readOnly": true
        },
        "type": {
          "type": "string",
          "description": "How the approval occured (override approval, approval chain approval, etc)",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "ApprovalGroup": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "owner": {
          "$ref": "#/definitions/ApprovalGroup"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "users": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/UserSimple"
          }
        }
      },
      "required": [
        "name"
      ]
    },
    "ApprovalLimit": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "subject": {
          "type": "string",
          "description": "subject",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "amount",
        "currency",
        "name"
      ]
    },
    "ApprovalReason": {
      "type": "object"
    },
    "Asn-Header": {
      "type": "object",
      "properties": {
        "asn-number": {
          "type": "string",
          "description": "Advanced Ship Notice Number",
          "format": "string(40)"
        },
        "bill-of-lading": {
          "type": "string",
          "description": "Detailed list of a shipment of goods used to clear customs",
          "format": "string(255)"
        },
        "carrier": {
          "type": "string",
          "description": "Shipper",
          "format": "string(255)"
        },
        "container": {
          "type": "string",
          "description": "Shipping Container number for tracking purposes",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "delivery-date": {
          "type": "string",
          "description": "Expected Delivery date when goods arrives",
          "format": "datetime"
        },
        "export-flag": {
          "type": "boolean",
          "description": "Indicates if transaction has been exported",
          "format": "boolean"
        },
        "gross-weight": {
          "type": "number",
          "description": "Gross weight of package",
          "format": "decimal(30,6)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Asn-Line"
          }
        },
        "packing-slip": {
          "type": "string",
          "description": "shipping list/manifest of goods usually inside the box",
          "format": "string(255)"
        },
        "ship-date": {
          "type": "string",
          "description": "Shipment Date",
          "format": "datetime"
        },
        "ship-method": {
          "type": "string",
          "description": "Method of shipment",
          "format": "string(255)"
        },
        "ship-note": {
          "type": "string",
          "description": "Note to shipper",
          "format": "string(255)"
        },
        "ship-to-address": {
          "$ref": "#/definitions/Address"
        },
        "ship-to-user": {
          "$ref": "#/definitions/UserSimple"
        },
        "ship-to-warehouse": {
          "$ref": "#/definitions/Warehouse"
        },
        "standard-carrier-alpha-code": {
          "type": "string",
          "description": "SCAC code to identify road transport companies",
          "format": "string(255)"
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(50)",
          "readOnly": true
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "tracking-number": {
          "type": "string",
          "description": "Tracking number of shipment",
          "format": "string(255)"
        },
        "trailer": {
          "type": "string",
          "description": "Trailer number your product will be shipping on",
          "format": "string(255)"
        },
        "uom": {
          "type": "string",
          "description": "UOM Code",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "asn-number",
        "lines",
        "ship-date",
        "ship-to-address",
        "supplier"
      ]
    },
    "Asn-Line": {
      "type": "object",
      "properties": {
        "comments": {
          "type": "string",
          "description": "Free form based comments about the shipment (e.g. hazardous)",
          "format": "string(255)"
        },
        "container": {
          "type": "string",
          "description": "Shipping Container number for tracking purposes",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "invoice-line": {
          "$ref": "#/definitions/InvoiceLine"
        },
        "item": {
          "$ref": "#/definitions/Item"
        },
        "line-num": {
          "type": "string",
          "description": "line_num",
          "format": "string(255)"
        },
        "match-reference": {
          "type": "string",
          "description": "Used for matching invoice against ASN line and receipts",
          "format": "string(255)"
        },
        "order-line": {
          "$ref": "#/definitions/OrderLine"
        },
        "quantity": {
          "type": "number",
          "description": "Shipped quantity",
          "format": "decimal(30,6)"
        },
        "received-qty": {
          "type": "number",
          "description": "Actual quantity received",
          "format": "decimal(30,6)"
        },
        "review-reason": {
          "type": "string",
          "description": "reasons - a free form text",
          "format": "string(255)",
          "readOnly": true
        },
        "soft-close-for-receiving": {
          "type": "boolean",
          "description": "Soft close PO line for Receiving",
          "format": "boolean"
        },
        "status": {
          "type": "string",
          "description": "Line status",
          "format": "string(255)",
          "enum": [
            "draft",
            "pending_receipt",
            "partially_received",
            "received",
            "error",
            "cancelled"
          ]
        },
        "supplier-aux-part-num": {
          "type": "string",
          "description": "Supplier auxiliary part number",
          "format": "text"
        },
        "supplier-part-num": {
          "type": "string",
          "description": "Supplier part number",
          "format": "string(255)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "line-num",
        "quantity",
        "received-qty"
      ]
    },
    "AssetTag": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "inventory-balance-id": {
          "type": "integer",
          "description": "inventory_balance_id",
          "format": "integer",
          "readOnly": true
        },
        "note": {
          "type": "string",
          "description": "note",
          "format": "text"
        },
        "order-line-id": {
          "type": "integer",
          "description": "order_line_id",
          "format": "integer",
          "readOnly": true
        },
        "owner": {
          "type": "string",
          "description": "owner",
          "format": "string(255)"
        },
        "received": {
          "type": "boolean",
          "description": "received",
          "format": "boolean",
          "readOnly": true
        },
        "requisition-line-id": {
          "type": "integer",
          "description": "requisition_line_id",
          "format": "integer",
          "readOnly": true
        },
        "serial-number": {
          "type": "string",
          "description": "serial number",
          "format": "string(255)"
        },
        "tag": {
          "type": "string",
          "description": "tag",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "Attachment": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "file-url": {
          "type": "string",
          "description": "URL to attached file",
          "format": "string"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "intent": {
          "type": "string",
          "description": "intent",
          "format": "string(40)"
        },
        "linked-to": {
          "type": "string",
          "description": "link to specific feature",
          "format": "string(255)"
        },
        "text": {
          "type": "string",
          "description": "text",
          "format": "text"
        },
        "type": {
          "type": "string",
          "description": "type",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "url": {
          "type": "string",
          "description": "url",
          "format": "string(255)"
        }
      }
    },
    "BulkPrice": {
      "type": "object",
      "properties": {
        "conversion-denominator": {
          "type": "number",
          "description": "UOM conversion denominator",
          "format": "decimal(30,6)"
        },
        "conversion-numerator": {
          "type": "number",
          "description": "UOM conversion numerator",
          "format": "decimal(30,6)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "price": {
          "type": "number",
          "description": "Bulk Price",
          "format": "decimal(46,20)"
        },
        "qty": {
          "type": "number",
          "description": "Bulk Price Qty",
          "format": "decimal(30,6)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        }
      },
      "required": [
        "uom"
      ]
    },
    "BusinessGroup": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(100)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "Catalog": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "Comment": {
      "type": "object",
      "properties": {
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "commentable-id": {
          "type": "integer",
          "description": "commentable_id",
          "format": "integer"
        },
        "commentable-type": {
          "type": "string",
          "description": "commentable_type",
          "format": "string(255)"
        },
        "comments": {
          "type": "string",
          "description": "comments",
          "format": "text"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "reason-code": {
          "type": "string",
          "description": "Comment reason code",
          "format": "string",
          "readOnly": true
        },
        "to-supplier": {
          "type": "string",
          "description": "to be shown to supplier?",
          "format": "tinyint(1)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "Commodity": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean",
          "enum": [
            "true",
            "false"
          ]
        },
        "category": {
          "type": "string",
          "description": "Category",
          "format": "string(255)",
          "enum": [
            "goods",
            "services"
          ]
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "deductibility": {
          "type": "string",
          "description": "Deductibility",
          "format": "string(255)",
          "enum": [
            "fully_deductible",
            "partially_deductible",
            "not_deductible"
          ]
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "parent": {
          "$ref": "#/definitions/Commodity"
        },
        "subcategory": {
          "type": "string",
          "description": "Subcategory",
          "format": "string(255)",
          "enum": [
            "raw_materials",
            "investment_goods",
            "services_exceptions"
          ]
        },
        "translated-name": {
          "type": "string",
          "description": "Translated name",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "Contact": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "email": {
          "type": "string",
          "description": "email",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name-additional": {
          "type": "string",
          "description": "name_additional",
          "format": "string(50)"
        },
        "name-family": {
          "type": "string",
          "description": "name_family",
          "format": "string(40)"
        },
        "name-fullname": {
          "type": "string",
          "description": "name_fullname",
          "format": "string(155)",
          "readOnly": true
        },
        "name-given": {
          "type": "string",
          "description": "name_given",
          "format": "string(40)"
        },
        "name-prefix": {
          "type": "string",
          "description": "name_prefix",
          "format": "string(10)"
        },
        "name-suffix": {
          "type": "string",
          "description": "name_suffix",
          "format": "string(10)"
        },
        "notes": {
          "type": "string",
          "description": "notes",
          "format": "text"
        },
        "phone-fax": {
          "$ref": "#/definitions/PhoneNumber"
        },
        "phone-mobile": {
          "$ref": "#/definitions/PhoneNumber"
        },
        "phone-work": {
          "$ref": "#/definitions/PhoneNumber"
        },
        "photo": {
          "type": "string",
          "description": "photo",
          "format": "string(255)"
        },
        "purposes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Purpose"
          }
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "Contract": {
      "type": "object",
      "properties": {
        "amended-contract-type": {
          "type": "string",
          "description": "Amended Contract Type",
          "format": "string(255)"
        },
        "auto-extend-end-date-for-renewal": {
          "type": "boolean",
          "description": "Automatically update expiry date",
          "format": "boolean"
        },
        "clma-id": {
          "type": "integer",
          "description": "Identifier for the CLMA contract details",
          "format": "integer"
        },
        "consent": {
          "type": "string",
          "description": "Notice to Consent",
          "format": "string(255)",
          "enum": [
            "",
            "notice",
            "consent",
            "not_required",
            "not_assignable"
          ]
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "contract-owner": {
          "$ref": "#/definitions/UserSimple"
        },
        "contract-parties": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ContractParty"
          }
        },
        "contract-terms": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ContractTerm"
          }
        },
        "contract-type": {
          "$ref": "#/definitions/ContractType"
        },
        "contract-type-custom-field-1": {
          "type": "string",
          "description": "Contract type custom field 1",
          "format": "string(255)"
        },
        "contract-type-custom-field-10": {
          "type": "string",
          "description": "Contract type custom field 10",
          "format": "string(255)"
        },
        "contract-type-custom-field-2": {
          "type": "string",
          "description": "Contract type custom field 2",
          "format": "string(255)"
        },
        "contract-type-custom-field-3": {
          "type": "string",
          "description": "Contract type custom field 3",
          "format": "string(255)"
        },
        "contract-type-custom-field-4": {
          "type": "string",
          "description": "Contract type custom field 4",
          "format": "string(255)"
        },
        "contract-type-custom-field-5": {
          "type": "string",
          "description": "Contract type custom field 5",
          "format": "string(255)"
        },
        "contract-type-custom-field-6": {
          "type": "string",
          "description": "Contract type custom field 6",
          "format": "string(255)"
        },
        "contract-type-custom-field-7": {
          "type": "string",
          "description": "Contract type custom field 7",
          "format": "string(255)"
        },
        "contract-type-custom-field-8": {
          "type": "string",
          "description": "Contract type custom field 8",
          "format": "string(255)"
        },
        "contract-type-custom-field-9": {
          "type": "string",
          "description": "Contract type custom field 9",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "current-approval": {
          "$ref": "#/definitions/Approval"
        },
        "default-account": {
          "$ref": "#/definitions/Account"
        },
        "department": {
          "$ref": "#/definitions/Department"
        },
        "description": {
          "type": "string",
          "description": "Descriptive notes about the contract",
          "format": "string(1024)"
        },
        "end-date": {
          "type": "string",
          "description": "Expire Date",
          "format": "datetime"
        },
        "execution-date": {
          "type": "string",
          "description": "Date when the contract is completed and legally binding",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "is-default": {
          "type": "boolean",
          "description": "Default Account for Supplier Invoice",
          "format": "boolean"
        },
        "legal-agreement-url": {
          "type": "string",
          "description": "Optional url for the legal agreement",
          "format": "string(255)"
        },
        "length-of-notice-unit": {
          "type": "string",
          "description": "Unit of Length of Notice(Days/Months/Years)",
          "format": "string(255)",
          "enum": [
            "days",
            "months",
            "years"
          ]
        },
        "length-of-notice-value": {
          "type": "string",
          "description": "Value of Length of Notice",
          "format": "string(255)"
        },
        "master-contract": {
          "$ref": "#/definitions/Contract"
        },
        "max-commit": {
          "type": "number",
          "description": "Maximum Commit Amount",
          "format": "decimal(32,4)"
        },
        "maximum-value": {
          "type": "number",
          "description": "Maximum Commit Amount",
          "format": "decimal(32,4)"
        },
        "min-commit": {
          "type": "number",
          "description": "Minimum Commit Amount",
          "format": "decimal(32,4)"
        },
        "minimum-value": {
          "type": "number",
          "description": "Minimum Commit Amount",
          "format": "decimal(32,4)"
        },
        "name": {
          "type": "string",
          "description": "Contract Name",
          "format": "string(100)"
        },
        "no-of-renewals": {
          "type": "integer",
          "description": "No of Renewals",
          "format": "integer"
        },
        "number": {
          "type": "string",
          "description": "Contract Number",
          "format": "string(50)"
        },
        "order-window-tz": {
          "type": "string",
          "description": "order_window_tz",
          "format": "string(255)",
          "enum": [
            "Africa/Abidjan",
            "Africa/Accra",
            "Africa/Addis_Ababa",
            "Africa/Algiers",
            "Africa/Asmara",
            "Africa/Asmera",
            "Africa/Bamako",
            "Africa/Bangui",
            "Africa/Banjul",
            "Africa/Bissau",
            "Africa/Blantyre",
            "Africa/Brazzaville",
            "Africa/Bujumbura",
            "Africa/Cairo",
            "Africa/Casablanca",
            "Africa/Ceuta",
            "Africa/Conakry",
            "Africa/Dakar",
            "Africa/Dar_es_Salaam",
            "Africa/Djibouti",
            "Africa/Douala",
            "Africa/El_Aaiun",
            "Africa/Freetown",
            "Africa/Gaborone",
            "Africa/Harare",
            "Africa/Johannesburg",
            "Africa/Juba",
            "Africa/Kampala",
            "Africa/Khartoum",
            "Africa/Kigali",
            "Africa/Kinshasa",
            "Africa/Lagos",
            "Africa/Libreville",
            "Africa/Lome",
            "Africa/Luanda",
            "Africa/Lubumbashi",
            "Africa/Lusaka",
            "Africa/Malabo",
            "Africa/Maputo",
            "Africa/Maseru",
            "Africa/Mbabane",
            "Africa/Mogadishu",
            "Africa/Monrovia",
            "Africa/Nairobi",
            "Africa/Ndjamena",
            "Africa/Niamey",
            "Africa/Nouakchott",
            "Africa/Ouagadougou",
            "Africa/Porto-Novo",
            "Africa/Sao_Tome",
            "Africa/Timbuktu",
            "Africa/Tripoli",
            "Africa/Tunis",
            "Africa/Windhoek",
            "America/Adak",
            "America/Anchorage",
            "America/Anguilla",
            "America/Antigua",
            "America/Araguaina",
            "America/Argentina/Buenos_Aires",
            "America/Argentina/Catamarca",
            "America/Argentina/ComodRivadavia",
            "America/Argentina/Cordoba",
            "America/Argentina/Jujuy",
            "America/Argentina/La_Rioja",
            "America/Argentina/Mendoza",
            "America/Argentina/Rio_Gallegos",
            "America/Argentina/Salta",
            "America/Argentina/San_Juan",
            "America/Argentina/San_Luis",
            "America/Argentina/Tucuman",
            "America/Argentina/Ushuaia",
            "America/Aruba",
            "America/Asuncion",
            "America/Atikokan",
            "America/Atka",
            "America/Bahia",
            "America/Bahia_Banderas",
            "America/Barbados",
            "America/Belem",
            "America/Belize",
            "America/Blanc-Sablon",
            "America/Boa_Vista",
            "America/Bogota",
            "America/Boise",
            "America/Buenos_Aires",
            "America/Cambridge_Bay",
            "America/Campo_Grande",
            "America/Cancun",
            "America/Caracas",
            "America/Catamarca",
            "America/Cayenne",
            "America/Cayman",
            "America/Chicago",
            "America/Chihuahua",
            "America/Coral_Harbour",
            "America/Cordoba",
            "America/Costa_Rica",
            "America/Creston",
            "America/Cuiaba",
            "America/Curacao",
            "America/Danmarkshavn",
            "America/Dawson",
            "America/Dawson_Creek",
            "America/Denver",
            "America/Detroit",
            "America/Dominica",
            "America/Edmonton",
            "America/Eirunepe",
            "America/El_Salvador",
            "America/Ensenada",
            "America/Fort_Nelson",
            "America/Fort_Wayne",
            "America/Fortaleza",
            "America/Glace_Bay",
            "America/Godthab",
            "America/Goose_Bay",
            "America/Grand_Turk",
            "America/Grenada",
            "America/Guadeloupe",
            "America/Guatemala",
            "America/Guayaquil",
            "America/Guyana",
            "America/Halifax",
            "America/Havana",
            "America/Hermosillo",
            "America/Indiana/Indianapolis",
            "America/Indiana/Knox",
            "America/Indiana/Marengo",
            "America/Indiana/Petersburg",
            "America/Indiana/Tell_City",
            "America/Indiana/Vevay",
            "America/Indiana/Vincennes",
            "America/Indiana/Winamac",
            "America/Indianapolis",
            "America/Inuvik",
            "America/Iqaluit",
            "America/Jamaica",
            "America/Jujuy",
            "America/Juneau",
            "America/Kentucky/Louisville",
            "America/Kentucky/Monticello",
            "America/Knox_IN",
            "America/Kralendijk",
            "America/La_Paz",
            "America/Lima",
            "America/Los_Angeles",
            "America/Louisville",
            "America/Lower_Princes",
            "America/Maceio",
            "America/Managua",
            "America/Manaus",
            "America/Marigot",
            "America/Martinique",
            "America/Matamoros",
            "America/Mazatlan",
            "America/Mendoza",
            "America/Menominee",
            "America/Merida",
            "America/Metlakatla",
            "America/Mexico_City",
            "America/Miquelon",
            "America/Moncton",
            "America/Monterrey",
            "America/Montevideo",
            "America/Montreal",
            "America/Montserrat",
            "America/Nassau",
            "America/New_York",
            "America/Nipigon",
            "America/Nome",
            "America/Noronha",
            "America/North_Dakota/Beulah",
            "America/North_Dakota/Center",
            "America/North_Dakota/New_Salem",
            "America/Nuuk",
            "America/Ojinaga",
            "America/Panama",
            "America/Pangnirtung",
            "America/Paramaribo",
            "America/Phoenix",
            "America/Port-au-Prince",
            "America/Port_of_Spain",
            "America/Porto_Acre",
            "America/Porto_Velho",
            "America/Puerto_Rico",
            "America/Punta_Arenas",
            "America/Rainy_River",
            "America/Rankin_Inlet",
            "America/Recife",
            "America/Regina",
            "America/Resolute",
            "America/Rio_Branco",
            "America/Rosario",
            "America/Santa_Isabel",
            "America/Santarem",
            "America/Santiago",
            "America/Santo_Domingo",
            "America/Sao_Paulo",
            "America/Scoresbysund",
            "America/Shiprock",
            "America/Sitka",
            "America/St_Barthelemy",
            "America/St_Johns",
            "America/St_Kitts",
            "America/St_Lucia",
            "America/St_Thomas",
            "America/St_Vincent",
            "America/Swift_Current",
            "America/Tegucigalpa",
            "America/Thule",
            "America/Thunder_Bay",
            "America/Tijuana",
            "America/Toronto",
            "America/Tortola",
            "America/Vancouver",
            "America/Virgin",
            "America/Whitehorse",
            "America/Winnipeg",
            "America/Yakutat",
            "America/Yellowknife",
            "Antarctica/Casey",
            "Antarctica/Davis",
            "Antarctica/DumontDUrville",
            "Antarctica/Macquarie",
            "Antarctica/Mawson",
            "Antarctica/McMurdo",
            "Antarctica/Palmer",
            "Antarctica/Rothera",
            "Antarctica/South_Pole",
            "Antarctica/Syowa",
            "Antarctica/Troll",
            "Antarctica/Vostok",
            "Arctic/Longyearbyen",
            "Asia/Aden",
            "Asia/Almaty",
            "Asia/Amman",
            "Asia/Anadyr",
            "Asia/Aqtau",
            "Asia/Aqtobe",
            "Asia/Ashgabat",
            "Asia/Ashkhabad",
            "Asia/Atyrau",
            "Asia/Baghdad",
            "Asia/Bahrain",
            "Asia/Baku",
            "Asia/Bangkok",
            "Asia/Barnaul",
            "Asia/Beirut",
            "Asia/Bishkek",
            "Asia/Brunei",
            "Asia/Calcutta",
            "Asia/Chita",
            "Asia/Choibalsan",
            "Asia/Chongqing",
            "Asia/Chungking",
            "Asia/Colombo",
            "Asia/Dacca",
            "Asia/Damascus",
            "Asia/Dhaka",
            "Asia/Dili",
            "Asia/Dubai",
            "Asia/Dushanbe",
            "Asia/Famagusta",
            "Asia/Gaza",
            "Asia/Harbin",
            "Asia/Hebron",
            "Asia/Ho_Chi_Minh",
            "Asia/Hong_Kong",
            "Asia/Hovd",
            "Asia/Irkutsk",
            "Asia/Istanbul",
            "Asia/Jakarta",
            "Asia/Jayapura",
            "Asia/Jerusalem",
            "Asia/Kabul",
            "Asia/Kamchatka",
            "Asia/Karachi",
            "Asia/Kashgar",
            "Asia/Kathmandu",
            "Asia/Katmandu",
            "Asia/Khandyga",
            "Asia/Kolkata",
            "Asia/Krasnoyarsk",
            "Asia/Kuala_Lumpur",
            "Asia/Kuching",
            "Asia/Kuwait",
            "Asia/Macao",
            "Asia/Macau",
            "Asia/Magadan",
            "Asia/Makassar",
            "Asia/Manila",
            "Asia/Muscat",
            "Asia/Nicosia",
            "Asia/Novokuznetsk",
            "Asia/Novosibirsk",
            "Asia/Omsk",
            "Asia/Oral",
            "Asia/Phnom_Penh",
            "Asia/Pontianak",
            "Asia/Pyongyang",
            "Asia/Qatar",
            "Asia/Qostanay",
            "Asia/Qyzylorda",
            "Asia/Rangoon",
            "Asia/Riyadh",
            "Asia/Saigon",
            "Asia/Sakhalin",
            "Asia/Samarkand",
            "Asia/Seoul",
            "Asia/Shanghai",
            "Asia/Singapore",
            "Asia/Srednekolymsk",
            "Asia/Taipei",
            "Asia/Tashkent",
            "Asia/Tbilisi",
            "Asia/Tehran",
            "Asia/Tel_Aviv",
            "Asia/Thimbu",
            "Asia/Thimphu",
            "Asia/Tokyo",
            "Asia/Tomsk",
            "Asia/Ujung_Pandang",
            "Asia/Ulaanbaatar",
            "Asia/Ulan_Bator",
            "Asia/Urumqi",
            "Asia/Ust-Nera",
            "Asia/Vientiane",
            "Asia/Vladivostok",
            "Asia/Yakutsk",
            "Asia/Yangon",
            "Asia/Yekaterinburg",
            "Asia/Yerevan",
            "Atlantic/Azores",
            "Atlantic/Bermuda",
            "Atlantic/Canary",
            "Atlantic/Cape_Verde",
            "Atlantic/Faeroe",
            "Atlantic/Faroe",
            "Atlantic/Jan_Mayen",
            "Atlantic/Madeira",
            "Atlantic/Reykjavik",
            "Atlantic/South_Georgia",
            "Atlantic/St_Helena",
            "Atlantic/Stanley",
            "Australia/ACT",
            "Australia/Adelaide",
            "Australia/Brisbane",
            "Australia/Broken_Hill",
            "Australia/Canberra",
            "Australia/Currie",
            "Australia/Darwin",
            "Australia/Eucla",
            "Australia/Hobart",
            "Australia/LHI",
            "Australia/Lindeman",
            "Australia/Lord_Howe",
            "Australia/Melbourne",
            "Australia/NSW",
            "Australia/North",
            "Australia/Perth",
            "Australia/Queensland",
            "Australia/South",
            "Australia/Sydney",
            "Australia/Tasmania",
            "Australia/Victoria",
            "Australia/West",
            "Australia/Yancowinna",
            "Brazil/Acre",
            "Brazil/DeNoronha",
            "Brazil/East",
            "Brazil/West",
            "CET",
            "CST6CDT",
            "Canada/Atlantic",
            "Canada/Central",
            "Canada/Eastern",
            "Canada/Mountain",
            "Canada/Newfoundland",
            "Canada/Pacific",
            "Canada/Saskatchewan",
            "Canada/Yukon",
            "Chile/Continental",
            "Chile/EasterIsland",
            "Cuba",
            "EET",
            "EST",
            "EST5EDT",
            "Egypt",
            "Eire",
            "Etc/GMT",
            "Etc/GMT+0",
            "Etc/GMT+1",
            "Etc/GMT+10",
            "Etc/GMT+11",
            "Etc/GMT+12",
            "Etc/GMT+2",
            "Etc/GMT+3",
            "Etc/GMT+4",
            "Etc/GMT+5",
            "Etc/GMT+6",
            "Etc/GMT+7",
            "Etc/GMT+8",
            "Etc/GMT+9",
            "Etc/GMT-0",
            "Etc/GMT-1",
            "Etc/GMT-10",
            "Etc/GMT-11",
            "Etc/GMT-12",
            "Etc/GMT-13",
            "Etc/GMT-14",
            "Etc/GMT-2",
            "Etc/GMT-3",
            "Etc/GMT-4",
            "Etc/GMT-5",
            "Etc/GMT-6",
            "Etc/GMT-7",
            "Etc/GMT-8",
            "Etc/GMT-9",
            "Etc/GMT0",
            "Etc/Greenwich",
            "Etc/UCT",
            "Etc/UTC",
            "Etc/Universal",
            "Etc/Zulu",
            "Europe/Amsterdam",
            "Europe/Andorra",
            "Europe/Astrakhan",
            "Europe/Athens",
            "Europe/Belfast",
            "Europe/Belgrade",
            "Europe/Berlin",
            "Europe/Bratislava",
            "Europe/Brussels",
            "Europe/Bucharest",
            "Europe/Budapest",
            "Europe/Busingen",
            "Europe/Chisinau",
            "Europe/Copenhagen",
            "Europe/Dublin",
            "Europe/Gibraltar",
            "Europe/Guernsey",
            "Europe/Helsinki",
            "Europe/Isle_of_Man",
            "Europe/Istanbul",
            "Europe/Jersey",
            "Europe/Kaliningrad",
            "Europe/Kiev",
            "Europe/Kirov",
            "Europe/Lisbon",
            "Europe/Ljubljana",
            "Europe/London",
            "Europe/Luxembourg",
            "Europe/Madrid",
            "Europe/Malta",
            "Europe/Mariehamn",
            "Europe/Minsk",
            "Europe/Monaco",
            "Europe/Moscow",
            "Europe/Nicosia",
            "Europe/Oslo",
            "Europe/Paris",
            "Europe/Podgorica",
            "Europe/Prague",
            "Europe/Riga",
            "Europe/Rome",
            "Europe/Samara",
            "Europe/San_Marino",
            "Europe/Sarajevo",
            "Europe/Saratov",
            "Europe/Simferopol",
            "Europe/Skopje",
            "Europe/Sofia",
            "Europe/Stockholm",
            "Europe/Tallinn",
            "Europe/Tirane",
            "Europe/Tiraspol",
            "Europe/Ulyanovsk",
            "Europe/Uzhgorod",
            "Europe/Vaduz",
            "Europe/Vatican",
            "Europe/Vienna",
            "Europe/Vilnius",
            "Europe/Volgograd",
            "Europe/Warsaw",
            "Europe/Zagreb",
            "Europe/Zaporozhye",
            "Europe/Zurich",
            "Factory",
            "GB",
            "GB-Eire",
            "GMT",
            "GMT+0",
            "GMT-0",
            "GMT0",
            "Greenwich",
            "HST",
            "Hongkong",
            "Iceland",
            "Indian/Antananarivo",
            "Indian/Chagos",
            "Indian/Christmas",
            "Indian/Cocos",
            "Indian/Comoro",
            "Indian/Kerguelen",
            "Indian/Mahe",
            "Indian/Maldives",
            "Indian/Mauritius",
            "Indian/Mayotte",
            "Indian/Reunion",
            "Iran",
            "Israel",
            "Jamaica",
            "Japan",
            "Kwajalein",
            "Libya",
            "MET",
            "MST",
            "MST7MDT",
            "Mexico/BajaNorte",
            "Mexico/BajaSur",
            "Mexico/General",
            "NZ",
            "NZ-CHAT",
            "Navajo",
            "PRC",
            "PST8PDT",
            "Pacific/Apia",
            "Pacific/Auckland",
            "Pacific/Bougainville",
            "Pacific/Chatham",
            "Pacific/Chuuk",
            "Pacific/Easter",
            "Pacific/Efate",
            "Pacific/Enderbury",
            "Pacific/Fakaofo",
            "Pacific/Fiji",
            "Pacific/Funafuti",
            "Pacific/Galapagos",
            "Pacific/Gambier",
            "Pacific/Guadalcanal",
            "Pacific/Guam",
            "Pacific/Honolulu",
            "Pacific/Johnston",
            "Pacific/Kiritimati",
            "Pacific/Kosrae",
            "Pacific/Kwajalein",
            "Pacific/Majuro",
            "Pacific/Marquesas",
            "Pacific/Midway",
            "Pacific/Nauru",
            "Pacific/Niue",
            "Pacific/Norfolk",
            "Pacific/Noumea",
            "Pacific/Pago_Pago",
            "Pacific/Palau",
            "Pacific/Pitcairn",
            "Pacific/Pohnpei",
            "Pacific/Ponape",
            "Pacific/Port_Moresby",
            "Pacific/Rarotonga",
            "Pacific/Saipan",
            "Pacific/Samoa",
            "Pacific/Tahiti",
            "Pacific/Tarawa",
            "Pacific/Tongatapu",
            "Pacific/Truk",
            "Pacific/Wake",
            "Pacific/Wallis",
            "Pacific/Yap",
            "Poland",
            "Portugal",
            "ROC",
            "ROK",
            "Singapore",
            "SystemV/AST4",
            "SystemV/AST4ADT",
            "SystemV/CST6",
            "SystemV/CST6CDT",
            "SystemV/EST5",
            "SystemV/EST5EDT",
            "SystemV/HST10",
            "SystemV/MST7",
            "SystemV/MST7MDT",
            "SystemV/PST8",
            "SystemV/PST8PDT",
            "SystemV/YST9",
            "SystemV/YST9YDT",
            "Turkey",
            "UCT",
            "US/Alaska",
            "US/Aleutian",
            "US/Arizona",
            "US/Central",
            "US/East-Indiana",
            "US/Eastern",
            "US/Hawaii",
            "US/Indiana-Starke",
            "US/Michigan",
            "US/Mountain",
            "US/Pacific",
            "US/Samoa",
            "UTC",
            "Universal",
            "W-SU",
            "WET",
            "Zulu",
            "International Date Line West",
            "American Samoa",
            "Midway Island",
            "Hawaii",
            "Alaska",
            "Pacific Time (US & Canada)",
            "Tijuana",
            "Arizona",
            "Chihuahua",
            "Mazatlan",
            "Mountain Time (US & Canada)",
            "Central America",
            "Central Time (US & Canada)",
            "Guadalajara",
            "Mexico City",
            "Monterrey",
            "Saskatchewan",
            "Bogota",
            "Eastern Time (US & Canada)",
            "Indiana (East)",
            "Lima",
            "Quito",
            "Atlantic Time (Canada)",
            "Caracas",
            "Georgetown",
            "La Paz",
            "Puerto Rico",
            "Santiago",
            "Newfoundland",
            "Brasilia",
            "Buenos Aires",
            "Greenland",
            "Montevideo",
            "Mid-Atlantic",
            "Azores",
            "Cape Verde Is.",
            "Edinburgh",
            "Lisbon",
            "London",
            "Monrovia",
            "Amsterdam",
            "Belgrade",
            "Berlin",
            "Bern",
            "Bratislava",
            "Brussels",
            "Budapest",
            "Casablanca",
            "Copenhagen",
            "Dublin",
            "Ljubljana",
            "Madrid",
            "Paris",
            "Prague",
            "Rome",
            "Sarajevo",
            "Skopje",
            "Stockholm",
            "Vienna",
            "Warsaw",
            "West Central Africa",
            "Zagreb",
            "Zurich",
            "Athens",
            "Bucharest",
            "Cairo",
            "Harare",
            "Helsinki",
            "Jerusalem",
            "Kaliningrad",
            "Kyiv",
            "Pretoria",
            "Riga",
            "Sofia",
            "Tallinn",
            "Vilnius",
            "Baghdad",
            "Istanbul",
            "Kuwait",
            "Minsk",
            "Moscow",
            "Nairobi",
            "Riyadh",
            "St. Petersburg",
            "Volgograd",
            "Tehran",
            "Abu Dhabi",
            "Baku",
            "Muscat",
            "Samara",
            "Tbilisi",
            "Yerevan",
            "Kabul",
            "Ekaterinburg",
            "Islamabad",
            "Karachi",
            "Tashkent",
            "Chennai",
            "Kolkata",
            "Mumbai",
            "New Delhi",
            "Sri Jayawardenepura",
            "Kathmandu",
            "Almaty",
            "Astana",
            "Dhaka",
            "Urumqi",
            "Rangoon",
            "Bangkok",
            "Hanoi",
            "Jakarta",
            "Krasnoyarsk",
            "Novosibirsk",
            "Beijing",
            "Chongqing",
            "Hong Kong",
            "Irkutsk",
            "Kuala Lumpur",
            "Perth",
            "Taipei",
            "Ulaanbaatar",
            "Osaka",
            "Sapporo",
            "Seoul",
            "Tokyo",
            "Yakutsk",
            "Adelaide",
            "Darwin",
            "Brisbane",
            "Canberra",
            "Guam",
            "Hobart",
            "Melbourne",
            "Port Moresby",
            "Sydney",
            "Vladivostok",
            "Magadan",
            "New Caledonia",
            "Solomon Is.",
            "Srednekolymsk",
            "Auckland",
            "Fiji",
            "Kamchatka",
            "Marshall Is.",
            "Wellington",
            "Chatham Is.",
            "Nuku'alofa",
            "Samoa",
            "Tokelau Is."
          ]
        },
        "parent": {
          "$ref": "#/definitions/Contract"
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "po-message": {
          "type": "string",
          "description": "Order Windows PO Message",
          "format": "string(255)"
        },
        "preferred": {
          "type": "boolean",
          "description": "Indicate preferred contract for supplier",
          "format": "boolean"
        },
        "proxy-supplier-id": {
          "type": "integer",
          "description": "Identifier for a proxy supplier",
          "format": "integer"
        },
        "published-date": {
          "type": "string",
          "description": "Date when the contract was published",
          "format": "datetime"
        },
        "quote-response-id": {
          "type": "integer",
          "description": "Id of Quote Response",
          "format": "integer",
          "readOnly": true
        },
        "reason-insight-events": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ReasonInsightEvent"
          }
        },
        "renewal-length-unit": {
          "type": "string",
          "description": "Unit of Renewal Length(Days/Months/Years)",
          "format": "string(255)",
          "enum": [
            "days",
            "months",
            "years"
          ]
        },
        "renewal-length-value": {
          "type": "integer",
          "description": "Value of Renewal Length",
          "format": "integer"
        },
        "requisition-message": {
          "type": "string",
          "description": "Order Windows Requisition Message",
          "format": "string(255)"
        },
        "savings-pct": {
          "type": "number",
          "description": "Savings Achieved through Contracts Pricing",
          "format": "decimal(20,2)"
        },
        "schedule": {
          "$ref": "#/definitions/OrderWindow"
        },
        "shipping-term": {
          "$ref": "#/definitions/ShippingTerm"
        },
        "source": {
          "type": "string",
          "description": "The URL to the source of contract creation",
          "format": "string",
          "readOnly": true
        },
        "source-id": {
          "type": "string",
          "description": "The source id of contract creation",
          "format": "string(255)"
        },
        "source-type": {
          "type": "string",
          "description": "The source type of contract creation",
          "format": "string(255)"
        },
        "start-date": {
          "type": "string",
          "description": "Start Date",
          "format": "datetime"
        },
        "status": {
          "type": "string",
          "description": "Status of the Contract",
          "format": "string(50)"
        },
        "stop-spend-based-on-max-value": {
          "type": "string",
          "description": "Stop Spend Based On Max Value",
          "format": "string(255)",
          "enum": [
            "yes",
            "no"
          ]
        },
        "strict-invoicing-rules": {
          "type": "boolean",
          "description": "Strict Invoicing Rules",
          "format": "boolean"
        },
        "submitter": {
          "$ref": "#/definitions/UserSimple"
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "supplier-account": {
          "type": "string",
          "description": "Supplier Account Number",
          "format": "string(255)"
        },
        "supplier-invoiceable": {
          "type": "boolean",
          "description": "Supplier Can Invoice Directly",
          "format": "boolean"
        },
        "taggings": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Tagging"
          }
        },
        "tags": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Tag"
          }
        },
        "term-type": {
          "type": "string",
          "description": "Term type",
          "format": "string(255)",
          "enum": [
            "fixed",
            "auto_renew",
            "perpetual"
          ]
        },
        "terminated": {
          "type": "boolean",
          "description": "Terminated",
          "format": "boolean"
        },
        "termination-notice": {
          "type": "string",
          "description": "Termination Notice",
          "format": "string(255)",
          "enum": [
            "yes",
            "no"
          ]
        },
        "termination-notice-length-unit": {
          "type": "string",
          "description": "Unit of Termination Notice Length(Days/Months/Years)",
          "format": "string(255)",
          "enum": [
            "days",
            "months",
            "years"
          ]
        },
        "termination-notice-length-value": {
          "type": "integer",
          "description": "Value of Termination Notice Length",
          "format": "integer"
        },
        "terms": {
          "type": "string",
          "description": "terms",
          "format": "text"
        },
        "type": {
          "type": "string",
          "description": "Hierarchy type",
          "format": "string",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "use-order-windows": {
          "type": "boolean",
          "description": "Use Order Windows",
          "format": "boolean"
        },
        "used-for-buying": {
          "type": "boolean",
          "description": "Used for Buying",
          "format": "boolean"
        },
        "version": {
          "type": "integer",
          "description": "version",
          "format": "integer"
        }
      },
      "required": [
        "content-groups",
        "name",
        "no-of-renewals",
        "number",
        "reason-insight-events",
        "renewal-length-unit",
        "renewal-length-value",
        "status",
        "supplier"
      ]
    },
    "ContractParty": {
      "type": "object",
      "properties": {
        "bill-to-address": {
          "$ref": "#/definitions/Address"
        },
        "business-name": {
          "type": "string",
          "description": "Business Name",
          "format": "string(255)"
        },
        "clma-id": {
          "type": "integer",
          "description": "CLM Advanced Counterparty Identifier",
          "format": "integer"
        },
        "contact-name": {
          "type": "string",
          "description": "Contact Name",
          "format": "string(255)"
        },
        "contact-title": {
          "type": "string",
          "description": "Contact Title",
          "format": "string(255)"
        },
        "counterparty-role": {
          "type": "string",
          "description": "Counterparty Role",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "email": {
          "type": "string",
          "description": "Email",
          "format": "string(255)"
        },
        "entity-name": {
          "type": "string",
          "description": "Entity Name",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "mail-to-address": {
          "$ref": "#/definitions/Address"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "entity-name"
      ]
    },
    "ContractTerm": {
      "type": "object",
      "properties": {
        "contract-term-type": {
          "type": "string",
          "description": "contract term type",
          "format": "string",
          "enum": [
            "PerOrderContractTerm",
            "TotalQtyContractTerm",
            "TotalAmtContractTerm",
            "PriceRangeContractTerm"
          ]
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "tier-10-disc-pct": {
          "type": "number",
          "description": "tier_10_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-10-upper-bound": {
          "type": "number",
          "description": "tier_10_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-11-disc-pct": {
          "type": "number",
          "description": "tier_11_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-11-upper-bound": {
          "type": "number",
          "description": "tier_11_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-12-disc-pct": {
          "type": "number",
          "description": "tier_12_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-12-upper-bound": {
          "type": "number",
          "description": "tier_12_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-13-disc-pct": {
          "type": "number",
          "description": "tier_13_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-13-upper-bound": {
          "type": "number",
          "description": "tier_13_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-14-disc-pct": {
          "type": "number",
          "description": "tier_14_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-14-upper-bound": {
          "type": "number",
          "description": "tier_14_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-15-disc-pct": {
          "type": "number",
          "description": "tier_15_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-15-upper-bound": {
          "type": "number",
          "description": "tier_15_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-16-disc-pct": {
          "type": "number",
          "description": "tier_16_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-16-upper-bound": {
          "type": "number",
          "description": "tier_16_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-17-disc-pct": {
          "type": "number",
          "description": "tier_17_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-17-upper-bound": {
          "type": "number",
          "description": "tier_17_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-18-disc-pct": {
          "type": "number",
          "description": "tier_18_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-18-upper-bound": {
          "type": "number",
          "description": "tier_18_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-19-disc-pct": {
          "type": "number",
          "description": "tier_19_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-19-upper-bound": {
          "type": "number",
          "description": "tier_19_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-1-disc-pct": {
          "type": "number",
          "description": "tier_1_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-1-upper-bound": {
          "type": "number",
          "description": "tier_1_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-20-disc-pct": {
          "type": "number",
          "description": "tier_20_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-20-upper-bound": {
          "type": "number",
          "description": "tier_20_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-2-disc-pct": {
          "type": "number",
          "description": "tier_2_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-2-upper-bound": {
          "type": "number",
          "description": "tier_2_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-3-disc-pct": {
          "type": "number",
          "description": "tier_3_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-3-upper-bound": {
          "type": "number",
          "description": "tier_3_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-4-disc-pct": {
          "type": "number",
          "description": "tier_4_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-4-upper-bound": {
          "type": "number",
          "description": "tier_4_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-5-disc-pct": {
          "type": "number",
          "description": "tier_5_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-5-upper-bound": {
          "type": "number",
          "description": "tier_5_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-6-disc-pct": {
          "type": "number",
          "description": "tier_6_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-6-upper-bound": {
          "type": "number",
          "description": "tier_6_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-7-disc-pct": {
          "type": "number",
          "description": "tier_7_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-7-upper-bound": {
          "type": "number",
          "description": "tier_7_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-8-disc-pct": {
          "type": "number",
          "description": "tier_8_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-8-upper-bound": {
          "type": "number",
          "description": "tier_8_upper_bound",
          "format": "decimal(30,4)"
        },
        "tier-9-disc-pct": {
          "type": "number",
          "description": "tier_9_disc_pct",
          "format": "decimal(30,4)"
        },
        "tier-9-upper-bound": {
          "type": "number",
          "description": "tier_9_upper_bound",
          "format": "decimal(30,4)"
        },
        "type": {
          "type": "string",
          "description": "type",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "use-pct-discounts": {
          "type": "boolean",
          "description": "use_pct_discounts",
          "format": "boolean"
        }
      },
      "required": [
        "name",
        "tier-1-upper-bound"
      ]
    },
    "ContractType": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "text"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "Country": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(4)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(100)"
        }
      },
      "required": [
        "code"
      ]
    },
    "Currency": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(6)"
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "decimals": {
          "type": "integer",
          "description": "Decimal precision",
          "format": "integer",
          "readOnly": true
        },
        "enabled": {
          "type": "boolean",
          "description": "Enabled",
          "format": "boolean"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(100)"
        },
        "symbol": {
          "type": "string",
          "description": "symbol",
          "format": "string(10)"
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "code",
        "name"
      ]
    },
    "CustomerSupportContact": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "email": {
          "type": "string",
          "description": "Email",
          "readOnly": true
        },
        "fullname": {
          "type": "string",
          "description": "Fullname",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "purposes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Purpose"
          }
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "user-id": {
          "type": "integer",
          "description": "User",
          "format": "integer"
        }
      },
      "required": [
        "user-id"
      ]
    },
    "DelegateApproval": {
      "type": "object",
      "properties": {
        "approvable-id": {
          "type": "integer",
          "description": "approvable_id",
          "format": "integer",
          "readOnly": true
        },
        "approvable-type": {
          "type": "string",
          "description": "approvable_type",
          "format": "string(255)",
          "readOnly": true
        },
        "approval-chain-id": {
          "type": "integer",
          "description": "approval_chain_id",
          "format": "integer",
          "readOnly": true
        },
        "approval-date": {
          "type": "string",
          "description": "approval_date",
          "format": "datetime",
          "readOnly": true
        },
        "approved-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "approver": {
          "type": "string",
          "description": "approver",
          "readOnly": true
        },
        "approver-type": {
          "type": "string",
          "description": "The role of the approver",
          "format": "string(255)",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "delegate": {
          "type": "string",
          "description": "delegate",
          "readOnly": true
        },
        "delegate-id": {
          "type": "string",
          "description": "The delegate ID that made the approval (if applicable)",
          "format": "string",
          "readOnly": true
        },
        "delegates": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/DelegateApproval"
          }
        },
        "holdable": {
          "type": "boolean",
          "description": "Hold the approval or not",
          "format": "boolean",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "note": {
          "type": "string",
          "description": "note",
          "format": "text",
          "readOnly": true
        },
        "position": {
          "type": "integer",
          "description": "position",
          "format": "integer",
          "readOnly": true
        },
        "reasons": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ApprovalReason"
          }
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(50)",
          "readOnly": true
        },
        "type": {
          "type": "string",
          "description": "type",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "Department": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Control whether the Department is Active or Inactive",
          "format": "boolean",
          "enum": [
            "true",
            "false"
          ]
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Department Name",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "DisputeReason": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "Code",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "text"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "code",
        "description"
      ]
    },
    "DiversityAssociation": {
      "type": "object",
      "properties": {
        "country": {
          "$ref": "#/definitions/Country"
        },
        "country-id": {
          "type": "integer",
          "description": "Country",
          "format": "integer"
        },
        "created-at": {
          "type": "string",
          "description": "Created Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "diversity-category": {
          "$ref": "#/definitions/DiversityCategory"
        },
        "diversity-category-id": {
          "type": "integer",
          "description": "Diversity category",
          "format": "integer"
        },
        "id": {
          "type": "integer",
          "description": "Diversity Association ID",
          "format": "integer"
        },
        "sim-diversity-certificate-artifacts": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/SimDiversityCertificateArtifact"
          }
        },
        "updated-at": {
          "type": "string",
          "description": "Last Updated Date and Time",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "country-id",
        "diversity-category-id"
      ]
    },
    "DiversityCategory": {
      "type": "object",
      "properties": {
        "category": {
          "type": "string",
          "description": "Category",
          "readOnly": true
        },
        "code": {
          "type": "string",
          "description": "Code",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer"
        },
        "parent-category": {
          "type": "string",
          "description": "Parent Category",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "code"
      ]
    },
    "DiversityCertificationAgency": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "Code",
          "format": "string(255)",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)",
          "readOnly": true
        },
        "region-type": {
          "type": "string",
          "description": "Region type",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      }
    },
    "EasyFormResponse": {
      "type": "object",
      "properties": {
        "approvals": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Approval"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "easy-form-id": {
          "type": "integer",
          "description": "Easy form ID associated with this easy form response",
          "format": "integer"
        },
        "easy-form-widget-responses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/EasyFormWidgetResponse"
          }
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name of the easy form response",
          "format": "string(255)",
          "readOnly": true
        },
        "requested-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "status": {
          "type": "string",
          "description": "Status of the easy form response",
          "format": "string(255)",
          "readOnly": true
        },
        "subject": {
          "description": "Object associated with this easy form response. Can be one of multiple objects: InvoiceHeader, InvoiceLine, SupplierInformation, User",
          "readOnly": true
        },
        "submitted-at": {
          "type": "string",
          "description": "The date/time the response was submitted in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "easy-form-id"
      ]
    },
    "EasyFormWidgetResponse": {
      "type": "object",
      "properties": {
        "answer": {
          "type": "string",
          "description": "Answer"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "easy-form-id": {
          "type": "integer",
          "description": "Easy form ID associated with this easy form response",
          "format": "integer"
        },
        "easy-form-response-id": {
          "type": "integer",
          "description": "Easy form response ID associated with this widget",
          "format": "integer"
        },
        "easy-form-widget-id": {
          "type": "integer",
          "description": "Easy form widget ID associated with this widget response",
          "format": "integer"
        },
        "encrypted-answer": {
          "type": "string",
          "description": "The answer for widget response",
          "readOnly": true
        },
        "field-name": {
          "type": "string",
          "description": "Field name",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "type": {
          "type": "string",
          "description": "Type of widget response",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "widget-label": {
          "type": "string",
          "description": "User name for widget",
          "readOnly": true
        },
        "widget-type": {
          "type": "string",
          "description": "Type of widget",
          "readOnly": true
        }
      },
      "required": [
        "easy-form-id",
        "easy-form-response-id",
        "easy-form-widget-id"
      ]
    },
    "Enterprise": {
      "type": "object",
      "properties": {
        "active-flag": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean"
        },
        "code": {
          "type": "string",
          "description": "Code",
          "format": "string(6)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(100)"
        },
        "system-flag": {
          "type": "boolean",
          "description": "System",
          "format": "boolean",
          "readOnly": true
        },
        "tax-coding-enabled": {
          "type": "string",
          "description": "Tax Coding Enabled",
          "format": "string"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "vendor-remit-to-required": {
          "type": "string",
          "description": "Vendor Remit-To Required",
          "format": "string"
        }
      },
      "required": [
        "code",
        "name"
      ]
    },
    "ExtraLineAttributes-OrderLineAttribute": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "end-date": {
          "type": "string",
          "description": "End date",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "manager": {
          "$ref": "#/definitions/UserSimple"
        },
        "start-date": {
          "type": "string",
          "description": "Start date",
          "format": "datetime"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "work-confirmer-email": {
          "type": "string",
          "description": "Work confirmer email",
          "format": "string(255)"
        }
      }
    },
    "ExtraLineAttributes-OrderLineChangeAttribute": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "end-date": {
          "type": "string",
          "description": "End date",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "manager": {
          "$ref": "#/definitions/UserSimple"
        },
        "start-date": {
          "type": "string",
          "description": "Start date",
          "format": "datetime"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "work-confirmer-email": {
          "type": "string",
          "description": "Work confirmer email",
          "format": "string(255)"
        }
      }
    },
    "ExtraLineAttributes-RequisitionLineAttribute": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "end-date": {
          "type": "string",
          "description": "End date",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "manager": {
          "$ref": "#/definitions/UserSimple"
        },
        "start-date": {
          "type": "string",
          "description": "Start date",
          "format": "datetime"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "work-confirmer-email": {
          "type": "string",
          "description": "Work confirmer email",
          "format": "string(255)"
        }
      }
    },
    "Flow": {
      "type": "object"
    },
    "Form": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "form-type": {
          "type": "string",
          "description": "form_type",
          "format": "string(255)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(100)"
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(50)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "FormResponse": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "InboundInvoice": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "InspectionCode": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "code"
      ]
    },
    "Integration": {
      "type": "object",
      "properties": {
        "business-object": {
          "type": "string",
          "description": "Business Object",
          "format": "string(255)"
        },
        "code": {
          "type": "string",
          "description": "Unique Integration Code",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "direction": {
          "type": "string",
          "description": "Direction",
          "format": "string(255)",
          "enum": [
            "to_coupa",
            "from_coupa"
          ]
        },
        "end-system": {
          "type": "string",
          "description": "End System",
          "format": "string(255)"
        },
        "end-system-type": {
          "type": "string",
          "description": "End System Type",
          "format": "string(255)",
          "enum": [
            "payroll",
            "erp",
            "hr",
            "third_party_partner",
            "third_party_vendor",
            "other",
            "internal"
          ]
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "integration-type": {
          "type": "string",
          "description": "Type of integration",
          "format": "string(255)",
          "enum": [
            "flat_file",
            "api",
            "corporate_credit_card_file",
            "json",
            "xml"
          ]
        },
        "name": {
          "type": "string",
          "description": "Integration Name",
          "format": "string(255)"
        },
        "standard": {
          "type": "boolean",
          "description": "Standard",
          "format": "boolean",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "business-object",
        "code",
        "direction",
        "end-system",
        "end-system-type",
        "name"
      ]
    },
    "IntegrationError": {
      "type": "object",
      "properties": {
        "contact-alert-type": {
          "type": "string",
          "description": "contact_alert_type",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime"
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "creation-method": {
          "type": "string",
          "description": "creation_method",
          "format": "string(255)"
        },
        "document-id": {
          "type": "integer",
          "description": "document_id",
          "format": "integer"
        },
        "document-revision": {
          "type": "integer",
          "description": "document_revision",
          "format": "integer"
        },
        "document-status": {
          "type": "string",
          "description": "document_status",
          "format": "string(255)"
        },
        "document-type": {
          "type": "string",
          "description": "document_type",
          "format": "string(255)",
          "enum": [
            "ContingentWorkOrderHeader",
            "ExternalOrderHeader",
            "OrderHeader",
            "InventoryTransaction",
            "InvoiceHeader",
            "ExpenseReport",
            "RequisitionHeader",
            "Account",
            "Supplier",
            "User",
            "Address",
            "RemitToAddress",
            "Contract",
            "ExchangeRate",
            "Invoice",
            "Requisition",
            "Payment",
            "ApprovalChain",
            "LookupValue",
            "Item",
            "SupplierInformation",
            "Asn::Header",
            "AccountValidationRule"
          ]
        },
        "external-id": {
          "type": "string",
          "description": "external_id",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "integration": {
          "$ref": "#/definitions/Integration"
        },
        "integration-filename": {
          "type": "string",
          "description": "filename that is associated with integration error",
          "format": "string(255)"
        },
        "integration-run-id": {
          "type": "integer",
          "description": "Integration Run ID",
          "format": "integer"
        },
        "resolved": {
          "type": "boolean",
          "description": "True if this error is resolved",
          "format": "boolean",
          "readOnly": true
        },
        "responses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/IntegrationRecordResponse"
          }
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime"
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "contact-alert-type",
        "integration-run-id"
      ]
    },
    "IntegrationHistoryRecord": {
      "type": "object",
      "properties": {
        "contact-alert-type": {
          "type": "string",
          "description": "contact_alert_type",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime"
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "creation-method": {
          "type": "string",
          "description": "creation_method",
          "format": "string(255)"
        },
        "document-id": {
          "type": "integer",
          "description": "document_id",
          "format": "integer"
        },
        "document-revision": {
          "type": "integer",
          "description": "document_revision",
          "format": "integer"
        },
        "document-status": {
          "type": "string",
          "description": "document_status",
          "format": "string(255)"
        },
        "document-type": {
          "type": "string",
          "description": "document_type",
          "format": "string(255)",
          "enum": [
            "ContingentWorkOrderHeader",
            "ExternalOrderHeader",
            "OrderHeader",
            "InventoryTransaction",
            "InvoiceHeader",
            "ExpenseReport",
            "RequisitionHeader",
            "Account",
            "Supplier",
            "User",
            "Address",
            "RemitToAddress",
            "Contract",
            "ExchangeRate",
            "Invoice",
            "Requisition",
            "Payment",
            "ApprovalChain",
            "LookupValue",
            "Item",
            "SupplierInformation",
            "Asn::Header",
            "AccountValidationRule"
          ]
        },
        "external-id": {
          "type": "string",
          "description": "external_id",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "integration": {
          "$ref": "#/definitions/Integration"
        },
        "integration-filename": {
          "type": "string",
          "description": "Filename for bulk import/export",
          "format": "string(255)",
          "readOnly": true
        },
        "integration-run": {
          "$ref": "#/definitions/IntegrationRun"
        },
        "integration-run-id": {
          "type": "integer",
          "description": "Unique identifier for integration run",
          "format": "integer",
          "readOnly": true
        },
        "resolved": {
          "type": "boolean",
          "description": "True if this record is resolved",
          "format": "boolean",
          "readOnly": true
        },
        "responses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/IntegrationRecordResponse"
          }
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "contact-alert-type",
        "document-id",
        "document-type"
      ]
    },
    "IntegrationRecordResponse": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "response-code": {
          "type": "string",
          "description": "response_code",
          "format": "string(255)"
        },
        "response-message": {
          "type": "string",
          "description": "response_message",
          "format": "text"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "IntegrationRun": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "end-time": {
          "type": "string",
          "description": "end_time",
          "format": "datetime"
        },
        "flow": {
          "$ref": "#/definitions/Flow"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "integration": {
          "$ref": "#/definitions/Integration"
        },
        "integration-errors": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/IntegrationError"
          }
        },
        "records-processed": {
          "type": "integer",
          "description": "records_processed",
          "format": "integer"
        },
        "start-time": {
          "type": "string",
          "description": "start_time",
          "format": "datetime"
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(255)",
          "readOnly": true
        },
        "total-records": {
          "type": "integer",
          "description": "total_records",
          "format": "integer"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "integration"
      ]
    },
    "InventoryLot": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "expiration-date": {
          "type": "string",
          "description": "Expiration date",
          "format": "date"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "item-id": {
          "type": "integer",
          "description": "Item",
          "format": "integer"
        },
        "number": {
          "type": "string",
          "description": "Number",
          "format": "string(256)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "expiration-date",
        "number"
      ]
    },
    "InventoryOrganization": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "fulfillment-type": {
          "type": "string",
          "description": "Fulfillment type",
          "format": "string(255)",
          "enum": [
            "manual",
            "automatic"
          ]
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "warehouses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Warehouse"
          }
        }
      },
      "required": [
        "currency",
        "fulfillment-type"
      ]
    },
    "InventoryTransaction": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "account-allocations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InventoryTxnAllocation"
          }
        },
        "asn-header": {
          "$ref": "#/definitions/Asn-Header"
        },
        "asn-line": {
          "$ref": "#/definitions/Asn-Line"
        },
        "asset-tags": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AssetTag"
          }
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "barcode": {
          "type": "string",
          "description": "Barcode Value",
          "format": "string(255)"
        },
        "comments": {
          "type": "string",
          "description": "Comments for voiding transaction",
          "format": "text",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Time of Inventory Transaction Creation",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "current-integration-history-records": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/IntegrationHistoryRecord"
          }
        },
        "exported": {
          "type": "boolean",
          "description": "Indicates if transaction has been exported",
          "format": "boolean"
        },
        "from-warehouse": {
          "$ref": "#/definitions/Warehouse"
        },
        "from-warehouse-location": {
          "$ref": "#/definitions/WarehouseLocation"
        },
        "id": {
          "type": "integer",
          "description": "Coupa's Internal Inventory Transaction ID",
          "format": "integer",
          "readOnly": true
        },
        "inspection-code": {
          "$ref": "#/definitions/InspectionCode"
        },
        "inventory-transaction-lots": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InventoryTransactionLot"
          }
        },
        "inventory-transaction-valuations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InventoryTransactionValuation"
          }
        },
        "item": {
          "$ref": "#/definitions/Item"
        },
        "last-exported-at": {
          "type": "string",
          "description": "Date and time transaction was last exported in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "match-reference": {
          "type": "string",
          "description": "Three-way match attribute to connect with Receipt and ASN Line",
          "format": "string(255)"
        },
        "order-line": {
          "$ref": "#/definitions/OrderLine"
        },
        "original-transaction": {
          "$ref": "#/definitions/InventoryTransaction"
        },
        "original-transaction-id": {
          "type": "integer",
          "description": "N/A",
          "format": "integer",
          "readOnly": true
        },
        "price": {
          "type": "number",
          "description": "Item Price",
          "format": "decimal(30,6)"
        },
        "quantity": {
          "type": "number",
          "description": "Receipt Quantity",
          "format": "decimal(30,6)"
        },
        "reason-insight": {
          "$ref": "#/definitions/ReasonInsight"
        },
        "receipt": {
          "$ref": "#/definitions/Receipt"
        },
        "receipts-batch-id": {
          "type": "integer",
          "description": "Receipts Batch ID",
          "format": "integer",
          "readOnly": true
        },
        "received-weight": {
          "type": "number",
          "description": "Inventory Transaction Received Weight",
          "format": "decimal(30,6)"
        },
        "receiving-form-response": {
          "$ref": "#/definitions/FormResponse"
        },
        "rfid-tag": {
          "type": "string",
          "description": "RFID Tag Value",
          "format": "string(255)"
        },
        "soft-close-for-receiving": {
          "type": "boolean",
          "description": "Soft close PO line for Receiving",
          "format": "boolean"
        },
        "status": {
          "type": "string",
          "description": "Inventory Transaction Status",
          "format": "string(255)",
          "readOnly": true
        },
        "to-warehouse": {
          "$ref": "#/definitions/Warehouse"
        },
        "to-warehouse-location": {
          "$ref": "#/definitions/WarehouseLocation"
        },
        "total": {
          "type": "number",
          "description": "Receipt Total",
          "format": "decimal(30,6)"
        },
        "transaction-date": {
          "type": "string",
          "description": "Actual date of transaction",
          "format": "datetime"
        },
        "type": {
          "type": "string",
          "description": "Inventory Transaction Type",
          "format": "string(255)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "updated-at": {
          "type": "string",
          "description": "Time of Inventory Transaction Updation",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "voided-value": {
          "type": "number",
          "description": "Total quantity/amount that was voided",
          "format": "decimal(30,6)",
          "readOnly": true
        }
      },
      "required": [
        "rfid-tag",
        "type"
      ]
    },
    "InventoryTransactionLot": {
      "type": "object",
      "properties": {
        "adjustment-code": {
          "$ref": "#/definitions/AdjustmentCode"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "inventory-lot": {
          "$ref": "#/definitions/InventoryLot"
        },
        "inventory-lot-id": {
          "type": "integer",
          "description": "Inventory lot",
          "format": "integer"
        },
        "quantity": {
          "type": "number",
          "description": "Quantity",
          "format": "decimal(32,4)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "uom-id": {
          "type": "integer",
          "description": "Uom",
          "format": "integer"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "inventory-lot",
        "quantity",
        "uom"
      ]
    },
    "InventoryTransactionValuation": {
      "type": "object",
      "properties": {
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "inventory-transaction-id": {
          "type": "integer",
          "description": "inventory transaction id",
          "format": "integer",
          "readOnly": true
        },
        "price": {
          "type": "number",
          "description": "price",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "quantity": {
          "type": "number",
          "description": "quantity",
          "format": "decimal(30,6)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        }
      },
      "required": [
        "quantity",
        "uom"
      ]
    },
    "InventoryTxnAllocation": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "pct": {
          "type": "number",
          "description": "pct",
          "format": "decimal(16,10)"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account",
        "pct"
      ]
    },
    "Invoice-FailedTolerance": {
      "type": "object",
      "properties": {
        "account-type-id": {
          "type": "integer",
          "description": "Account type",
          "format": "integer",
          "readOnly": true
        },
        "breach-amount": {
          "type": "string",
          "description": "Breach amount",
          "format": "string(255)",
          "readOnly": true
        },
        "breach-detail-1": {
          "type": "string",
          "description": "Breach detail 1",
          "format": "string(255)",
          "readOnly": true
        },
        "breach-detail-2": {
          "type": "string",
          "description": "Breach detail 2",
          "format": "string(255)",
          "readOnly": true
        },
        "breach-detail-3": {
          "type": "string",
          "description": "Breach detail 3",
          "format": "string(255)",
          "readOnly": true
        },
        "breach-detail-4": {
          "type": "string",
          "description": "Breach detail 4",
          "format": "string(255)",
          "readOnly": true
        },
        "breach-limit": {
          "type": "string",
          "description": "Breach limit",
          "format": "string(255)",
          "readOnly": true
        },
        "code": {
          "type": "string",
          "description": "Code",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "failable-id": {
          "type": "integer",
          "description": "Failable",
          "format": "integer",
          "readOnly": true
        },
        "failable-type": {
          "type": "string",
          "description": "Failable type",
          "format": "string(255)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "resolution-strategy": {
          "type": "string",
          "description": "Resolution strategy",
          "format": "string(25)",
          "readOnly": true
        },
        "resolved": {
          "type": "boolean",
          "description": "Resolved",
          "format": "boolean"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "code"
      ]
    },
    "Invoice-ReconciliationLine": {
      "type": "object",
      "properties": {
        "adjustment-date": {
          "type": "string",
          "description": "Adjustment date",
          "format": "datetime"
        },
        "amount": {
          "type": "number",
          "description": "Amount",
          "format": "decimal(46,20)"
        },
        "amount-paid": {
          "type": "number",
          "description": "Amount paid",
          "format": "decimal(46,20)",
          "readOnly": true
        },
        "category": {
          "type": "string",
          "description": "Category",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "note": {
          "type": "string",
          "description": "Note",
          "format": "string(255)"
        },
        "notes": {
          "type": "string",
          "description": "Notes",
          "format": "string(255)",
          "readOnly": true
        },
        "payable-id": {
          "type": "integer",
          "description": "Payable",
          "format": "integer"
        },
        "payable-type": {
          "type": "string",
          "description": "Payable type",
          "format": "string",
          "readOnly": true
        },
        "payment-date": {
          "type": "string",
          "description": "Payment date",
          "format": "datetime",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "InvoiceCharge": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "account-allocations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InvoiceChargeAllocation"
          }
        },
        "accounting-total": {
          "type": "number",
          "description": "Accounting total",
          "format": "decimal(30,4)",
          "readOnly": true
        },
        "accounting-total-currency": {
          "$ref": "#/definitions/Currency"
        },
        "billing-note": {
          "type": "string",
          "description": "Billing note",
          "format": "text"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "string(1550)"
        },
        "distributed": {
          "type": "boolean",
          "description": "Distributed",
          "format": "boolean"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "line-num": {
          "type": "integer",
          "description": "Line num",
          "format": "integer"
        },
        "pct": {
          "type": "number",
          "description": "Pct",
          "format": "decimal(16,10)"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "tax-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/TaxLine"
          }
        },
        "total": {
          "type": "number",
          "description": "Total",
          "format": "decimal"
        },
        "type": {
          "type": "string",
          "description": "Type",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account"
      ]
    },
    "InvoiceChargeAllocation": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "amount": {
          "type": "number",
          "description": "dollar amount for this allocation",
          "format": "decimal(30,4)"
        },
        "billing-note": {
          "type": "string",
          "description": "Billing note",
          "format": "text"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "pct": {
          "type": "number",
          "description": "percent",
          "format": "decimal(16,10)"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account",
        "pct"
      ]
    },
    "InvoiceEmail": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "email": {
          "type": "string",
          "description": "email",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "send-notification": {
          "type": "string",
          "description": "Send Email added notification to supplier",
          "format": "string"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "email"
      ]
    },
    "InvoiceHeader": {
      "type": "object",
      "properties": {
        "abandon-reason": {
          "$ref": "#/definitions/ReasonInsight"
        },
        "account-type": {
          "$ref": "#/definitions/AccountType"
        },
        "advance-payment-received-amount": {
          "type": "number",
          "description": "Amount of advance payment received",
          "format": "decimal(30,4)"
        },
        "amount-due": {
          "type": "number",
          "description": "Amount due to the supplier - Invoice Total without withholding and customer accounting taxes",
          "format": "decimal",
          "readOnly": true
        },
        "amount-due-less-discount": {
          "type": "number",
          "description": "Amount due after applying the discount",
          "format": "decimal",
          "readOnly": true
        },
        "amount-of-advance-payment": {
          "type": "number",
          "description": "Amount Of Advance Payment",
          "format": "decimal(46,20)",
          "readOnly": true
        },
        "approvals": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Approval"
          }
        },
        "archive-entity-id": {
          "type": "integer",
          "description": "Archive Entity Id",
          "format": "integer",
          "readOnly": true
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "bill-to-address": {
          "$ref": "#/definitions/Address"
        },
        "buyer-tax-registration": {
          "$ref": "#/definitions/TaxRegistration"
        },
        "canceled": {
          "type": "boolean",
          "description": "Indicates if transaction has been canceled",
          "format": "boolean",
          "readOnly": true
        },
        "cash-accounting-scheme-reference": {
          "type": "string",
          "description": "Note if using cash accounting scheme",
          "format": "string(255)"
        },
        "cash-register-operator": {
          "type": "string",
          "description": "Cash Register Operator",
          "format": "string(255)"
        },
        "clearance-document": {
          "type": "string",
          "description": "Clearance document attachment file name. Accessible via /retrieve_clearance_document",
          "format": "string",
          "readOnly": true
        },
        "comments": {
          "type": "string",
          "description": "comments",
          "format": "string(255)"
        },
        "compliant": {
          "type": "boolean",
          "description": "Invoice compliance indicator",
          "format": "boolean",
          "readOnly": true
        },
        "confirmation": {
          "type": "string",
          "description": "Confirmation",
          "format": "string(255)",
          "readOnly": true
        },
        "content-validation": {
          "type": "boolean",
          "description": "Invoice Content Validation Indicator",
          "format": "boolean",
          "readOnly": true
        },
        "contract": {
          "$ref": "#/definitions/Contract"
        },
        "correct-value-of-supply": {
          "type": "number",
          "description": "Correct Value of Supply",
          "format": "decimal(46,20)"
        },
        "coupa-accelerate-status": {
          "type": "string",
          "description": "Status indicating whether the invoice has discount payment terms via Static Discounting",
          "format": "string(40)",
          "readOnly": true,
          "enum": [
            "accelerated"
          ]
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "credit-note-differences-with-original-invoice": {
          "type": "number",
          "description": "Credit Note Differences With Original Invoice",
          "format": "decimal(30,4)"
        },
        "credit-reason": {
          "type": "string",
          "description": "The reason of creating the credit",
          "format": "string(255)"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "current-integration-history-records": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/IntegrationHistoryRecord"
          }
        },
        "customer-accounting-tax": {
          "type": "number",
          "description": "Customer accounting tax",
          "format": "decimal",
          "readOnly": true
        },
        "customer-accounting-tax-less-discount": {
          "type": "number",
          "description": "Customer accounting tax after applying the discount",
          "format": "decimal",
          "readOnly": true
        },
        "customs-declaration-date": {
          "type": "string",
          "description": "Customs Declaration Date",
          "format": "datetime"
        },
        "customs-declaration-number": {
          "type": "string",
          "description": "Customs Declaration Number",
          "format": "string(60)"
        },
        "customs-office": {
          "type": "string",
          "description": "Customs Office",
          "format": "text"
        },
        "date-of-discovery-of-facts-decisive-for-correction": {
          "type": "string",
          "description": "Date of Discovery of Facts Decisive for Correction",
          "format": "datetime"
        },
        "date-received": {
          "type": "string",
          "description": "Date Received in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "delivery-date": {
          "type": "string",
          "description": "Date of Supply",
          "format": "datetime"
        },
        "delivery-number": {
          "type": "string",
          "description": "Delivery Number",
          "format": "string(255)"
        },
        "destination-country": {
          "$ref": "#/definitions/Country"
        },
        "discount-amount": {
          "type": "number",
          "description": "Discount Amount provided by supplier",
          "format": "decimal(32,4)"
        },
        "discount-due-date": {
          "type": "string",
          "description": "Discount Due Date calculated based on the discount payment terms",
          "format": "datetime",
          "readOnly": true
        },
        "discount-percent": {
          "type": "number",
          "description": "Discount %",
          "format": "float"
        },
        "dispute-method": {
          "type": "string",
          "description": "Dispute Method",
          "format": "string(10)",
          "readOnly": true
        },
        "dispute-reasons": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/DisputeReason"
          }
        },
        "document-type": {
          "type": "string",
          "description": "Invoice or Credit Note",
          "format": "string",
          "readOnly": true
        },
        "early-payment-provisions": {
          "type": "string",
          "description": "Early payment incentives (This field has been deprecated)",
          "format": "string(255)"
        },
        "endorsement-on-invoices": {
          "type": "string",
          "description": "Endorsement On Invoices",
          "format": "string(255)"
        },
        "exchange-rate": {
          "type": "number",
          "description": "Exchange Rate",
          "format": "decimal(30,9)"
        },
        "exported": {
          "type": "boolean",
          "description": "Indicates if transaction has been exported",
          "format": "boolean",
          "readOnly": true
        },
        "failed-tolerances": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Invoice-FailedTolerance"
          }
        },
        "folio-number": {
          "type": "string",
          "description": "Folio Number",
          "format": "string(20)",
          "readOnly": true
        },
        "form-of-payment": {
          "type": "string",
          "description": "Payment Form",
          "format": "string(10)",
          "readOnly": true
        },
        "freight-type": {
          "type": "string",
          "description": "Freight Type",
          "format": "string(255)"
        },
        "gross-total": {
          "type": "number",
          "description": "Gross Total",
          "format": "decimal",
          "readOnly": true
        },
        "gross-total-less-discount": {
          "type": "number",
          "description": "Invoice total after applying the discount",
          "format": "decimal",
          "readOnly": true
        },
        "handling-amount": {
          "type": "number",
          "description": "Handling amount",
          "format": "decimal(32,4)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "image-scan": {
          "type": "string",
          "description": "Invoice Image Scan attachment filename",
          "format": "string(255)",
          "readOnly": true
        },
        "image-scan-url": {
          "type": "string",
          "description": "Invoice Image Scan URL. Must begin with 'http://' or 'https://'.",
          "format": "string(255)",
          "readOnly": true
        },
        "inbound-invoice": {
          "$ref": "#/definitions/InboundInvoice"
        },
        "inbox-name": {
          "type": "string",
          "description": "Inbox Name",
          "format": "string",
          "readOnly": true
        },
        "internal-note": {
          "type": "string",
          "description": "Internal Note",
          "format": "text"
        },
        "invoice-charges": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InvoiceCharge"
          }
        },
        "invoice-date": {
          "type": "string",
          "description": "Date of Invoice",
          "format": "datetime"
        },
        "invoice-from-address": {
          "$ref": "#/definitions/SupplierRemitTo"
        },
        "invoice-issuance-time": {
          "type": "string",
          "description": "Invoice Issuance Time",
          "format": "string(255)"
        },
        "invoice-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InvoiceLine"
          }
        },
        "invoice-number": {
          "type": "string",
          "description": "Invoice number",
          "format": "string(40)"
        },
        "invoice-payment-receipts": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InvoicePaymentReceipt"
          }
        },
        "invoice-reference-number": {
          "type": "string",
          "description": "Invoice Reference Number (IRN)",
          "format": "string(255)"
        },
        "is-credit-note": {
          "type": "boolean",
          "description": "Document Type Credit Note",
          "format": "boolean"
        },
        "issuance-place": {
          "type": "string",
          "description": "Issuance Place",
          "format": "string(255)",
          "readOnly": true
        },
        "last-exported-at": {
          "type": "string",
          "description": "Date and time transaction was last exported in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "late-payment-penalties": {
          "type": "string",
          "description": "Late Payment Penalties",
          "format": "string(255)"
        },
        "legal-destination-country": {
          "$ref": "#/definitions/Country"
        },
        "line-level-taxation": {
          "type": "boolean",
          "description": "Flag indicating whether taxes are provided at line level in this invoice",
          "format": "boolean"
        },
        "lock-version-key": {
          "type": "integer",
          "description": "Lock Version",
          "format": "integer",
          "readOnly": true
        },
        "margin-scheme": {
          "type": "string",
          "description": "Reason for using margin scheme",
          "format": "string(255)"
        },
        "means-of-payment": {
          "type": "string",
          "description": "Means Of Payment",
          "format": "string(255)"
        },
        "misc-amount": {
          "type": "number",
          "description": "Miscellaneous Amount",
          "format": "decimal(32,4)"
        },
        "municipal-tax-number": {
          "type": "string",
          "description": "Municipality Tax ID Number",
          "format": "string(255)"
        },
        "national-enrollment-of-conveyor": {
          "type": "string",
          "description": "National Enrollment of Conveyor",
          "format": "string(255)"
        },
        "nature-of-operation": {
          "type": "string",
          "description": "Nature of Operation",
          "format": "string(255)"
        },
        "net-due-date": {
          "type": "string",
          "description": "Net Due Date calculated based on the net payment terms",
          "format": "datetime",
          "readOnly": true
        },
        "net-total-less-discount": {
          "type": "number",
          "description": "Net total after applying the discount",
          "format": "decimal",
          "readOnly": true
        },
        "new-means-of-transport": {
          "type": "string",
          "description": "New Means Of Transport",
          "format": "string(255)"
        },
        "origin-country": {
          "$ref": "#/definitions/Country"
        },
        "origin-currency-gross": {
          "type": "number",
          "description": "Local Currency Gross",
          "format": "decimal(32,4)"
        },
        "origin-currency-net": {
          "type": "number",
          "description": "Local Currency Net",
          "format": "decimal(32,4)"
        },
        "original-invoice-date": {
          "type": "string",
          "description": "Original invoice date used in case of a Credit Note",
          "format": "datetime"
        },
        "original-invoice-number": {
          "type": "string",
          "description": "Original invoice number used in case of a Credit Note",
          "format": "string(40)"
        },
        "original-value-of-supply": {
          "type": "number",
          "description": "Original Value of Supply",
          "format": "decimal(46,20)"
        },
        "paid": {
          "type": "boolean",
          "description": "Paid",
          "format": "boolean"
        },
        "payment-agreement-notes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ReasonInsight"
          }
        },
        "payment-channel": {
          "type": "string",
          "description": "How the invoice payment will be handled - ERP (default), Coupa Pay Virtual Card, Coupa Pay Invoice Payment",
          "format": "string(40)",
          "readOnly": true
        },
        "payment-date": {
          "type": "string",
          "description": "Date of payment for invoice",
          "format": "datetime"
        },
        "payment-method": {
          "type": "string",
          "description": "Payment Method",
          "format": "string(10)",
          "readOnly": true
        },
        "payment-notes": {
          "type": "string",
          "description": "Notes included with payment for invoice",
          "format": "text"
        },
        "payment-order-number": {
          "type": "string",
          "description": "Payment Order Number",
          "format": "string(255)"
        },
        "payment-order-reference": {
          "type": "string",
          "description": "Payment Order Reference",
          "format": "string(255)"
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "payments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Invoice-ReconciliationLine"
          }
        },
        "place-of-issuance": {
          "type": "string",
          "description": "Place Of Issuance",
          "format": "string(255)"
        },
        "place-of-supply": {
          "type": "string",
          "description": "Place Of Supply",
          "format": "string(255)"
        },
        "pre-payment-date": {
          "type": "string",
          "description": "Pre-Payment Date",
          "format": "datetime"
        },
        "protocol-number": {
          "type": "string",
          "description": "Protocol Number",
          "format": "string(255)"
        },
        "reconciliation-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Invoice-ReconciliationLine"
          }
        },
        "remit-to-address": {
          "$ref": "#/definitions/RemitToAddress"
        },
        "requested-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "requester-email": {
          "type": "string",
          "description": "Requester Email",
          "format": "string"
        },
        "requester-lookup-name": {
          "type": "string",
          "description": "Requester Lookup Name",
          "format": "string"
        },
        "requester-name": {
          "type": "string",
          "description": "Requester Fullname",
          "format": "string"
        },
        "reverse-charge-reference": {
          "type": "string",
          "description": "Reverse Charge Reference",
          "format": "string(255)"
        },
        "security-code-of-issuer": {
          "type": "string",
          "description": "Security Code Of Issuer",
          "format": "string(255)"
        },
        "self-billing-reference": {
          "type": "string",
          "description": "Self billing reference on the invoice",
          "format": "string(191)"
        },
        "sender-email": {
          "type": "string",
          "description": "Sender Email",
          "format": "string",
          "readOnly": true
        },
        "serial-code-of-fiscal-invoice": {
          "type": "string",
          "description": "Serial Code of Fiscal Invoice",
          "format": "string(255)"
        },
        "series": {
          "type": "string",
          "description": "Series",
          "format": "string(30)",
          "readOnly": true
        },
        "ship-from-address": {
          "$ref": "#/definitions/SupplierRemitTo"
        },
        "ship-to-address": {
          "$ref": "#/definitions/Address"
        },
        "shipping-amount": {
          "type": "number",
          "description": "Shipping Amount",
          "format": "decimal(32,4)"
        },
        "shipping-term": {
          "$ref": "#/definitions/ShippingTerm"
        },
        "show-tax-information": {
          "type": "boolean",
          "description": "Show tax information in the invoice",
          "format": "boolean",
          "readOnly": true
        },
        "signed-qr-code": {
          "type": "string",
          "description": "Signed QR Code",
          "format": "text"
        },
        "split-payment-mechanism": {
          "type": "boolean",
          "description": "Split Payment Mechanism",
          "format": "boolean"
        },
        "state-tax-number": {
          "type": "string",
          "description": "State Tax ID Number",
          "format": "string(255)"
        },
        "state-tax-number-for-substitute-taxpayer": {
          "type": "string",
          "description": "State Tax ID Number for Substitute Taxpayer",
          "format": "string(255)"
        },
        "status": {
          "type": "string",
          "description": "Invoice Status",
          "format": "string(50)",
          "readOnly": true
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "supplier-created": {
          "type": "string",
          "description": "Supplier created indicator for invoice",
          "format": "true",
          "readOnly": true
        },
        "supplier-invoice-issuer-name": {
          "type": "string",
          "description": "Supplier Invoice Issuer Name",
          "format": "string(255)"
        },
        "supplier-invoice-reviewer-name": {
          "type": "string",
          "description": "Supplier Invoice Reviewer Name",
          "format": "string(255)"
        },
        "supplier-note": {
          "type": "string",
          "description": "Note provided by supplier",
          "format": "text"
        },
        "supplier-payment-collector-name": {
          "type": "string",
          "description": "Supplier Payment Collector Name",
          "format": "string(255)"
        },
        "supplier-remit-to": {
          "$ref": "#/definitions/SupplierRemitTo"
        },
        "supplier-tax-registration": {
          "$ref": "#/definitions/TaxRegistration"
        },
        "supplier-total": {
          "type": "number",
          "description": "Supplier Total",
          "format": "decimal",
          "readOnly": true
        },
        "taggings": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Tagging"
          }
        },
        "tags": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Tag"
          }
        },
        "tax-amount": {
          "type": "number",
          "description": "Tax amount (not used if tax is provided at line level)",
          "format": "decimal"
        },
        "tax-amount-engine": {
          "type": "number",
          "description": "Tax amount calculated by either Coupa Native or External Tax Engine based on configuration",
          "format": "decimal",
          "readOnly": true
        },
        "tax-code": {
          "type": "string",
          "description": "Tax code (not used if tax is provided at line level)",
          "format": "string(255)"
        },
        "tax-code-engine": {
          "type": "string",
          "description": "Tax code returned by External Tax Engine based on configuration",
          "format": "string",
          "readOnly": true
        },
        "tax-due-to-supplier": {
          "type": "number",
          "description": "Tax due to the supplier",
          "format": "decimal",
          "readOnly": true
        },
        "tax-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/TaxLine"
          }
        },
        "tax-rate": {
          "type": "number",
          "description": "Tax rate (not used if tax is provided at line level)",
          "format": "float"
        },
        "tax-rate-engine": {
          "type": "number",
          "description": "Tax rate returned by External Tax Engine based on configuration",
          "format": "decimal",
          "readOnly": true
        },
        "taxes-in-origin-country-currency": {
          "type": "number",
          "description": "Local Currency Tax",
          "format": "decimal(32,4)"
        },
        "tcs-tax-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/TcsTaxLine"
          }
        },
        "tolerance-failures": {
          "type": "string",
          "description": "Tolerance Failure",
          "format": "string(512)",
          "readOnly": true
        },
        "total-taxes-less-discount": {
          "type": "number",
          "description": "Total taxes after applying the discount",
          "format": "decimal",
          "readOnly": true
        },
        "total-with-taxes": {
          "type": "number",
          "description": "Total with taxes",
          "format": "decimal",
          "readOnly": true
        },
        "transaction-notification-date": {
          "type": "string",
          "description": "Transaction Notification Date",
          "format": "datetime",
          "readOnly": true
        },
        "transaction-uuid": {
          "type": "string",
          "description": "Transaction UUID",
          "format": "string(50)",
          "readOnly": true
        },
        "type-of-document": {
          "type": "string",
          "description": "Type of Document",
          "format": "string(255)"
        },
        "type-of-operation": {
          "type": "string",
          "description": "Type of Operation",
          "format": "string(255)"
        },
        "type-of-receipt": {
          "type": "string",
          "description": "Type of Receipt",
          "format": "string(10)",
          "readOnly": true
        },
        "type-of-relationship": {
          "type": "string",
          "description": "Type of Relationship",
          "format": "string(10)"
        },
        "unique-identification-code-of-cash-receipt": {
          "type": "string",
          "description": "Unique Identification Code Of Cash Receipt",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "use-of-invoice": {
          "type": "string",
          "description": "Use of the Invoice",
          "format": "string(10)",
          "readOnly": true
        },
        "vehicle-license-plate": {
          "type": "string",
          "description": "Vehicle License Plate",
          "format": "string(255)"
        },
        "verification-code": {
          "type": "string",
          "description": "Verification Code",
          "format": "string(255)"
        },
        "volume-amount": {
          "type": "string",
          "description": "Volume Amount",
          "format": "string(255)"
        },
        "volume-brand": {
          "type": "string",
          "description": "Volume Brand",
          "format": "string(255)"
        },
        "volume-gross-weight": {
          "type": "string",
          "description": "Volume Gross Weight",
          "format": "string(255)"
        },
        "volume-liquid-weight": {
          "type": "string",
          "description": "Volume Liquid Weight",
          "format": "string(255)"
        },
        "volume-numbering": {
          "type": "string",
          "description": "Volume Numbering",
          "format": "string(255)"
        },
        "volume-type": {
          "type": "string",
          "description": "Volume Type",
          "format": "string(255)"
        },
        "withholding-tax-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/WithholdingTaxLine"
          }
        },
        "withholding-tax-override": {
          "type": "number",
          "description": "Withholding Tax Override",
          "format": "decimal(30,3)",
          "readOnly": true
        }
      },
      "required": [
        "account-type",
        "bill-to-address",
        "buyer-tax-registration",
        "invoice-date",
        "invoice-from-address",
        "invoice-number",
        "line-level-taxation",
        "origin-currency-gross",
        "origin-currency-net",
        "original-invoice-date",
        "original-invoice-number",
        "remit-to-address",
        "ship-from-address",
        "supplier-remit-to",
        "supplier-tax-registration",
        "taxes-in-origin-country-currency"
      ]
    },
    "InvoiceLine": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "account-allocations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InvoiceLineAllocation"
          }
        },
        "accounting-total": {
          "type": "number",
          "description": "accounting_total",
          "format": "decimal(46,20)",
          "readOnly": true
        },
        "accounting-total-currency": {
          "$ref": "#/definitions/Currency"
        },
        "adjustment-type": {
          "type": "string",
          "description": "Adjustment Type",
          "format": "string(255)",
          "enum": [
            "price",
            "quantity",
            "other"
          ]
        },
        "billing-note": {
          "type": "string",
          "description": "Billing note",
          "format": "text"
        },
        "bulk-price": {
          "$ref": "#/definitions/BulkPrice"
        },
        "category": {
          "type": "string",
          "description": "Category"
        },
        "classification-of-goods": {
          "type": "string",
          "description": "Classification of Goods",
          "format": "string(255)"
        },
        "commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "company-uom": {
          "type": "string",
          "description": "Company UOM",
          "format": "string(255)",
          "readOnly": true
        },
        "contract": {
          "$ref": "#/definitions/Contract"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "customs-declaration-number": {
          "type": "string",
          "description": "Customs Declaration Number",
          "format": "string(255)",
          "readOnly": true
        },
        "deductibility": {
          "type": "string",
          "description": "Deductibility"
        },
        "delivery-note-number": {
          "type": "string",
          "description": "Delivery Note Number",
          "format": "string(255)"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(1550)"
        },
        "discount-amount": {
          "type": "number",
          "description": "Discount Amount",
          "format": "decimal(30,3)",
          "readOnly": true
        },
        "failed-tolerances": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Invoice-FailedTolerance"
          }
        },
        "fiscal-code": {
          "type": "string",
          "description": "Fiscal Code",
          "format": "string(255)"
        },
        "handling-distribution-total": {
          "type": "number",
          "description": "Handling distribution total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "hsn-sac-code": {
          "type": "string",
          "description": "HSN/SAC",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "item": {
          "$ref": "#/definitions/Item"
        },
        "item-barcode": {
          "type": "string",
          "description": "Item Barcode",
          "format": "string(255)"
        },
        "line-num": {
          "type": "integer",
          "description": "line_num",
          "format": "integer"
        },
        "line-type": {
          "type": "string",
          "description": "line type"
        },
        "match-reference": {
          "type": "string",
          "description": "Three-way match attribute to connect with Receipt and ASN Line",
          "format": "string(255)"
        },
        "misc-distribution-total": {
          "type": "number",
          "description": "Misc distribution total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "municipality-taxation-code": {
          "type": "string",
          "description": "Municipality Taxation Code",
          "format": "string(255)"
        },
        "net-weight": {
          "type": "number",
          "description": "net_weight",
          "format": "decimal(30,6)"
        },
        "order-header-num": {
          "type": "string",
          "description": "order_header_num",
          "readOnly": true
        },
        "order-line-commodity": {
          "type": "string",
          "description": "order_line_commodity",
          "readOnly": true
        },
        "order-line-custom-fields": {
          "type": "string",
          "description": "order_line_custom_fields",
          "readOnly": true
        },
        "order-line-id": {
          "type": "integer",
          "description": "order_line_id",
          "format": "integer"
        },
        "order-line-num": {
          "type": "string",
          "description": "order_line_num",
          "readOnly": true
        },
        "order-line-source-part-num": {
          "type": "string",
          "description": "Supplier part number on the respective order line",
          "readOnly": true
        },
        "original-date-of-supply": {
          "type": "string",
          "description": "Original Date of Supply",
          "format": "datetime"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "po-number": {
          "type": "string",
          "description": "Po number",
          "readOnly": true
        },
        "price": {
          "type": "number",
          "description": "price",
          "format": "decimal(46,20)"
        },
        "price-per-uom": {
          "type": "number",
          "description": "price_per_uom",
          "format": "decimal(30,6)"
        },
        "property-tax-account": {
          "type": "string",
          "description": "Property Tax Account",
          "format": "string(255)",
          "readOnly": true
        },
        "quantity": {
          "type": "number",
          "description": "quantity",
          "format": "decimal(30,6)"
        },
        "shipping-distribution-total": {
          "type": "number",
          "description": "Shipping distribution total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "source-part-num": {
          "type": "string",
          "description": "Source part num",
          "format": "string(255)"
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(255)",
          "readOnly": true
        },
        "subcategory": {
          "type": "string",
          "description": "Subcategory"
        },
        "supp-aux-part-num": {
          "type": "string",
          "description": "Supp aux part num",
          "format": "text"
        },
        "taggings": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Tagging"
          }
        },
        "tags": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Tag"
          }
        },
        "tax-amount": {
          "type": "number",
          "description": "tax_amount",
          "format": "decimal"
        },
        "tax-amount-engine": {
          "type": "string",
          "description": "Tax amount calculated by either Coupa Native or External Tax Engine based on configuration",
          "readOnly": true
        },
        "tax-code": {
          "$ref": "#/definitions/TaxCode"
        },
        "tax-code-engine": {
          "type": "string",
          "description": "Tax code returned by External Tax Engine based on configuration",
          "readOnly": true
        },
        "tax-description": {
          "type": "string",
          "description": "tax_description",
          "readOnly": true
        },
        "tax-distribution-total": {
          "type": "number",
          "description": "Tax distribution total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "tax-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/TaxLine"
          }
        },
        "tax-location": {
          "type": "string",
          "description": "tax_location",
          "readOnly": true
        },
        "tax-rate": {
          "type": "string",
          "description": "tax_rate"
        },
        "tax-rate-engine": {
          "type": "string",
          "description": "Tax rate returned by External Tax Engine based on configuration",
          "readOnly": true
        },
        "tax-supply-date": {
          "type": "string",
          "description": "tax_supply_date",
          "readOnly": true
        },
        "total": {
          "type": "number",
          "description": "total",
          "format": "decimal(46,20)",
          "readOnly": true
        },
        "type": {
          "type": "string",
          "description": "type",
          "format": "string(100)"
        },
        "unspsc": {
          "type": "string",
          "description": "UNSPSC",
          "format": "string(255)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "weight-uom": {
          "$ref": "#/definitions/Uom"
        },
        "withholding-tax-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/WithholdingTaxLine"
          }
        }
      },
      "required": [
        "description",
        "price"
      ]
    },
    "InvoiceLineAllocation": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "billing-note": {
          "type": "string",
          "description": "Billing note",
          "format": "text"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "handling-distribution-total": {
          "type": "number",
          "description": "Handling distribution total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "misc-distribution-total": {
          "type": "number",
          "description": "Misc distribution total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "pct": {
          "type": "number",
          "description": "pct",
          "format": "decimal(16,10)"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "shipping-distribution-total": {
          "type": "number",
          "description": "Shipping distribution total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "tax-distribution-total": {
          "type": "number",
          "description": "Tax distribution total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account",
        "pct"
      ]
    },
    "InvoicePaymentReceipt": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "Payed amount",
          "format": "decimal(32,6)",
          "readOnly": true
        },
        "clearance-document": {
          "type": "string",
          "description": "File name of payment receipt's clearance document.  Accessible via api/invoices/:id/payment_receipts/:uuid/retrieve_clearance_document",
          "format": "string",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "document-uuid": {
          "type": "string",
          "description": "Document UUID",
          "format": "string(255)",
          "readOnly": true
        },
        "exchange-rate": {
          "type": "number",
          "description": "Exchange rate",
          "format": "decimal(32,6)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "legal-payment-receipt": {
          "$ref": "#/definitions/LegalPaymentReceipt"
        },
        "payment-method": {
          "type": "string",
          "description": "Payment method",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      }
    },
    "Item": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Is the item given for this supplier & contract active? and if NOT then DELETE",
          "format": "boolean"
        },
        "allow-partial-quantity": {
          "type": "boolean",
          "description": "Allow partial quantity in cycle counts",
          "format": "boolean",
          "readOnly": true
        },
        "commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "connect-item-id": {
          "type": "integer",
          "description": "connect_item_id",
          "format": "integer"
        },
        "consumption-quantity": {
          "type": "integer",
          "description": "consumption_quantity",
          "format": "integer"
        },
        "consumption-uom": {
          "$ref": "#/definitions/Uom"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Item desciption",
          "format": "text"
        },
        "external-image-url": {
          "type": "string",
          "description": "External image URL for item image",
          "format": "string",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "image-url": {
          "type": "string",
          "description": "URL for item image (will be copied into Coupa on item create/update)",
          "format": "string"
        },
        "inventory-lot-expiration-type": {
          "type": "string",
          "description": "Lot expiration type",
          "format": "string",
          "readOnly": true
        },
        "inventory-lot-tracking-enabled": {
          "type": "boolean",
          "description": "Enable lot tracking",
          "format": "boolean",
          "readOnly": true
        },
        "item-number": {
          "type": "string",
          "description": "Unique item number",
          "format": "string(255)"
        },
        "item-type": {
          "type": "string",
          "description": "Item Type",
          "format": "string"
        },
        "manufacturer-name": {
          "type": "string",
          "description": "Manufacturer name",
          "format": "string(255)"
        },
        "manufacturer-part-number": {
          "type": "string",
          "description": "Manufacturer part number",
          "format": "string(255)"
        },
        "name": {
          "type": "string",
          "description": "Item name",
          "format": "string(255)"
        },
        "net-weight": {
          "type": "number",
          "description": "net_weight",
          "format": "decimal(30,6)"
        },
        "net-weight-uom": {
          "$ref": "#/definitions/Uom"
        },
        "pack-qty": {
          "type": "number",
          "description": "Total items in a pack",
          "format": "decimal(30,6)"
        },
        "pack-uom": {
          "$ref": "#/definitions/Uom"
        },
        "pack-uom-id": {
          "type": "integer",
          "description": "Pack UOM ID",
          "format": "integer"
        },
        "pack-weight": {
          "type": "number",
          "description": "Total weight of a pack",
          "format": "decimal(30,6)"
        },
        "receive-catch-weight": {
          "type": "boolean",
          "description": "Receive item as a catch weight (pack)",
          "format": "boolean"
        },
        "receiving-form": {
          "$ref": "#/definitions/Form"
        },
        "reorder-alerts": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ReorderAlert"
          }
        },
        "reorder-point": {
          "type": "number",
          "description": "reorder_point",
          "format": "float"
        },
        "require-asset-tag": {
          "type": "boolean",
          "description": "Require asset tag",
          "format": "boolean",
          "readOnly": true
        },
        "require-inspection": {
          "type": "boolean",
          "description": "Require inspection",
          "format": "boolean",
          "readOnly": true
        },
        "storage-quantity": {
          "type": "integer",
          "description": "storage_quantity",
          "format": "integer"
        },
        "storage-uom": {
          "$ref": "#/definitions/Uom"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "use-pack-weight": {
          "type": "boolean",
          "description": "Item is a pack of items",
          "format": "boolean"
        }
      },
      "required": [
        "description",
        "manufacturer-name",
        "name",
        "net-weight",
        "pack-qty",
        "pack-uom-id",
        "pack-weight"
      ]
    },
    "Language": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "Code",
          "format": "string(12)"
        },
        "id": {
          "type": "integer",
          "description": "Id",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(100)",
          "readOnly": true
        }
      },
      "required": [
        "code"
      ]
    },
    "LegalEntity": {
      "type": "object",
      "properties": {
        "bill-to-address": {
          "type": "string",
          "description": "Bill to address",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "LegalPaymentReceipt": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "Total amount which was payed",
          "format": "decimal(32,6)",
          "readOnly": true
        },
        "buyer-bank-name": {
          "type": "string",
          "description": "Buyer bank name",
          "format": "string(255)",
          "readOnly": true
        },
        "buyer-bank-reference": {
          "type": "string",
          "description": "Buyer bank reference",
          "format": "string(255)",
          "readOnly": true
        },
        "buyer-tax-number": {
          "type": "string",
          "description": "Buyer tax registration number",
          "format": "string(255)",
          "readOnly": true
        },
        "check-number": {
          "type": "string",
          "description": "Identification number of payment receipt",
          "format": "string(255)",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "document-date": {
          "type": "string",
          "description": "Date payment receipt was created",
          "format": "datetime",
          "readOnly": true,
          "enum": [
            "YYYY-MM-DDTHH:MM:SS+HH:MM"
          ]
        },
        "form-of-payment": {
          "type": "string",
          "description": "Form of payment",
          "format": "string(255)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "payment-received-date": {
          "type": "string",
          "description": "Date payment receipt was received",
          "format": "datetime",
          "readOnly": true,
          "enum": [
            "YYYY-MM-DDTHH:MM:SS+HH:MM"
          ]
        },
        "supplier-bank-reference": {
          "type": "string",
          "description": "Supplier bank reference",
          "format": "string(255)",
          "readOnly": true
        },
        "supplier-tax-number": {
          "type": "string",
          "description": "Supplier tax registration number",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "uuid": {
          "type": "string",
          "description": "UUID of payment receipt document",
          "format": "string(255)",
          "readOnly": true
        }
      }
    },
    "OnlineStore": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "login": {
          "type": "string",
          "description": "login",
          "format": "string(255)"
        },
        "password": {
          "type": "string",
          "description": "password"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "url": {
          "type": "string",
          "description": "url",
          "format": "string(255)"
        }
      },
      "required": [
        "url"
      ]
    },
    "OrderHeader": {
      "type": "object",
      "properties": {
        "acknowledged-at": {
          "type": "string",
          "description": "acknowledged_at",
          "format": "datetime",
          "readOnly": true
        },
        "acknowledged-flag": {
          "type": "boolean",
          "description": "Has PO been acknowledged by Supplier?",
          "format": "boolean"
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "change-type": {
          "type": "string",
          "description": "Last type of change on PO, it represents whether PO was changed through change request or through revise",
          "format": "string(255)",
          "readOnly": true,
          "enum": [
            "change",
            "revision"
          ]
        },
        "classification": {
          "type": "string",
          "description": "Classification",
          "format": "string(255)",
          "enum": [
            "msp",
            "supplier",
            "vms"
          ]
        },
        "coupa-accelerate-status": {
          "type": "string",
          "description": "Status indicating whether the invoice has discount payment terms via Static Discounting",
          "format": "string(255)",
          "readOnly": true,
          "enum": [
            "accelerated"
          ]
        },
        "created-at": {
          "type": "string",
          "description": "Date record was created in Coupa.",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "current-integration-history-records": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/IntegrationHistoryRecord"
          }
        },
        "exported": {
          "type": "boolean",
          "description": "Indicates if transaction has been exported",
          "format": "boolean",
          "readOnly": true
        },
        "hide-price": {
          "$ref": "#/definitions/OrderHeader"
        },
        "id": {
          "type": "integer",
          "description": "Coupa's internal ID",
          "format": "integer",
          "readOnly": true
        },
        "internal-revision": {
          "type": "integer",
          "description": "Internal Revision Number - Increases each time a change is made to a PO whether that change is internal or causes the PO to be resent to the supplier.",
          "format": "integer",
          "readOnly": true
        },
        "invoice-stop": {
          "type": "boolean",
          "description": "Invoice Stop flag",
          "format": "boolean",
          "readOnly": true
        },
        "last-exported-at": {
          "type": "string",
          "description": "Date and time transaction was last exported in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "milestones": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-Milestone"
          }
        },
        "order-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrderLine"
          }
        },
        "payment-method": {
          "type": "string",
          "description": "payment_method",
          "format": "string(255)"
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "pcard": {
          "$ref": "#/definitions/Pcard"
        },
        "po-number": {
          "type": "string",
          "description": "PO Number",
          "format": "string(20)"
        },
        "price-hidden": {
          "type": "boolean",
          "description": "Hide Price from supplier. True or False",
          "format": "boolean",
          "readOnly": true
        },
        "reason-insight-events": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ReasonInsightEvent"
          }
        },
        "recurring-rules": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-RecurringRule"
          }
        },
        "requester": {
          "$ref": "#/definitions/UserSimple"
        },
        "requisition-header": {
          "$ref": "#/definitions/RequisitionHeader"
        },
        "ship-to-address": {
          "$ref": "#/definitions/Address"
        },
        "ship-to-attention": {
          "type": "string",
          "description": "Ship to attention",
          "format": "string(255)"
        },
        "ship-to-user": {
          "$ref": "#/definitions/UserSimple"
        },
        "shipping-term": {
          "$ref": "#/definitions/ShippingTerm"
        },
        "status": {
          "type": "string",
          "description": "PO Status",
          "format": "string(50)",
          "readOnly": true
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "supplier-site": {
          "$ref": "#/definitions/SupplierSite"
        },
        "transmission-emails": {
          "type": "string",
          "description": "Tranmission Email comma seperated list",
          "format": "text"
        },
        "transmission-method-override": {
          "type": "string",
          "description": "Transmission Method Override",
          "format": "string(30)",
          "enum": [
            "supplier_default",
            "email",
            "do_not_transmit"
          ]
        },
        "transmission-status": {
          "type": "string",
          "description": "Transmission Status",
          "format": "string",
          "readOnly": true,
          "enum": [
            "created",
            "deferred",
            "deferred_processing",
            "pending_manual",
            "pending_manual_cancel",
            "awaiting_online_purchase",
            "scheduled_for_email",
            "sent_via_email",
            "scheduled_for_cxml",
            "scheduled_for_xml",
            "sent_via_cxml",
            "sent_via_xml",
            "sent_manually",
            "purchased_online",
            "transmission_failure"
          ]
        },
        "type": {
          "type": "string",
          "description": "Type of Order",
          "format": "string(255)",
          "enum": [
            "ExternalOrderHeader"
          ]
        },
        "updated-at": {
          "type": "string",
          "description": "Last Updated at Date",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "version": {
          "type": "integer",
          "description": "PO Supplier Version Number - Increase each time a PO is changed and triggers a resend to the supplier.",
          "format": "integer"
        }
      },
      "required": [
        "order-lines",
        "po-number",
        "ship-to-address",
        "ship-to-user",
        "supplier"
      ]
    },
    "OrderHeaderChange": {
      "type": "object",
      "properties": {
        "acknowledged-at": {
          "type": "string",
          "description": "acknowledged_at",
          "format": "date",
          "readOnly": true
        },
        "approvals": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Approval"
          }
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "current-approval": {
          "$ref": "#/definitions/Approval"
        },
        "department": {
          "$ref": "#/definitions/Department"
        },
        "exported": {
          "type": "boolean",
          "description": "Indicates if transaction has been exported",
          "format": "boolean",
          "readOnly": true
        },
        "hide-price": {
          "$ref": "#/definitions/OrderHeaderChange"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "justification": {
          "type": "string",
          "description": "justification",
          "format": "string",
          "readOnly": true
        },
        "milestones": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-Milestone"
          }
        },
        "order-header-id": {
          "type": "integer",
          "description": "id of the order that is being changed",
          "format": "integer"
        },
        "order-line-changes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrderLineChange"
          }
        },
        "payment-method": {
          "type": "string",
          "description": "payment_method",
          "format": "string(255)"
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "pcard": {
          "$ref": "#/definitions/Pcard"
        },
        "po-number": {
          "type": "string",
          "description": "PO Number",
          "format": "string(20)",
          "readOnly": true
        },
        "price-hidden": {
          "type": "boolean",
          "description": "Hide Price from supplier. True or False",
          "format": "boolean",
          "readOnly": true
        },
        "reason-insight-event": {
          "$ref": "#/definitions/ReasonInsightEvent"
        },
        "recurring-rules": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-RecurringRule"
          }
        },
        "reject-reason": {
          "$ref": "#/definitions/Comment"
        },
        "requester": {
          "$ref": "#/definitions/UserSimple"
        },
        "requisition-header-id": {
          "type": "integer",
          "description": "requisition_header_id",
          "format": "integer",
          "readOnly": true
        },
        "ship-to-address": {
          "$ref": "#/definitions/Address"
        },
        "ship-to-attention": {
          "type": "string",
          "description": "Attention user for the PO",
          "format": "string(255)"
        },
        "ship-to-user": {
          "$ref": "#/definitions/UserSimple"
        },
        "shipping-term": {
          "$ref": "#/definitions/ShippingTerm"
        },
        "status": {
          "type": "string",
          "description": "PO Status",
          "format": "string(255)",
          "readOnly": true
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "supplier-initiated": {
          "type": "boolean",
          "description": "Was this change initiated by a supplier. True or False",
          "format": "boolean",
          "readOnly": true
        },
        "supplier-site": {
          "$ref": "#/definitions/SupplierSite"
        },
        "transmission-emails": {
          "type": "string",
          "description": "Tranmission Email comma seperated list",
          "format": "text"
        },
        "transmission-method-override": {
          "type": "string",
          "description": "Transmission Method Override",
          "format": "string(30)",
          "enum": [
            "supplier_default",
            "email",
            "do_not_transmit"
          ]
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "version": {
          "type": "integer",
          "description": "PO Supplier Version Number - Increase each time a PO is changed and triggers a resend to the supplier.",
          "format": "integer",
          "readOnly": true
        }
      },
      "required": [
        "reason-insight-event"
      ]
    },
    "OrderLine": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "account-allocations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrderLineAllocation"
          }
        },
        "accounting-total": {
          "type": "number",
          "description": "accounting_total",
          "format": "decimal(32,4)"
        },
        "accounting-total-currency": {
          "$ref": "#/definitions/Currency"
        },
        "amount-components": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AmountComponent"
          }
        },
        "asset-tags": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AssetTag"
          }
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "bulk-price": {
          "$ref": "#/definitions/BulkPrice"
        },
        "commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "contract": {
          "$ref": "#/definitions/Contract"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "department": {
          "$ref": "#/definitions/Department"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "easy-form-response-id": {
          "$ref": "#/definitions/EasyFormResponse"
        },
        "external-reference-number": {
          "type": "string",
          "description": "External Reference Number",
          "format": "string(255)"
        },
        "external-reference-type": {
          "type": "string",
          "description": "External Reference Type",
          "format": "string(255)",
          "enum": [
            "staff_augmentation",
            "sow_project"
          ]
        },
        "extra-line-attribute": {
          "$ref": "#/definitions/ExtraLineAttributes-OrderLineAttribute"
        },
        "form-response": {
          "$ref": "#/definitions/FormResponse"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "invoice-stop": {
          "type": "boolean",
          "description": "Invoice Stop flag",
          "format": "boolean",
          "readOnly": true
        },
        "invoiced": {
          "type": "number",
          "description": "invoiced",
          "format": "decimal(32,6)"
        },
        "item": {
          "$ref": "#/definitions/Item"
        },
        "line-num": {
          "type": "string",
          "description": "line_num",
          "format": "string(255)"
        },
        "manufacturer-name": {
          "type": "string",
          "description": "Manufacturer Name",
          "format": "string(255)"
        },
        "manufacturer-part-number": {
          "type": "string",
          "description": "Manufacturer Part Number",
          "format": "string(255)"
        },
        "match-type": {
          "type": "string",
          "description": "Match type",
          "format": "string(255)",
          "enum": [
            "direct_matching",
            "3-way-fifo",
            "3-way",
            "2-way",
            "none"
          ]
        },
        "milestones": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-Milestone"
          }
        },
        "minimum-order-quantity": {
          "type": "number",
          "description": "Minimum order quantity",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "need-by-date": {
          "type": "string",
          "description": "need_by_date",
          "format": "datetime"
        },
        "order-header-id": {
          "type": "integer",
          "description": "order_header_id",
          "format": "integer"
        },
        "order-header-number": {
          "type": "string",
          "description": "PO Number",
          "format": "string",
          "readOnly": true
        },
        "order-increment": {
          "type": "number",
          "description": "Order increment",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "price": {
          "type": "number",
          "description": "price",
          "format": "decimal(30,6)"
        },
        "quantity": {
          "type": "number",
          "description": "quantity",
          "format": "decimal(30,6)"
        },
        "receipt-approval-required": {
          "type": "boolean",
          "description": "Receipt approval required",
          "format": "boolean",
          "readOnly": true
        },
        "receipt-required": {
          "type": "boolean",
          "description": "receipt_required",
          "format": "boolean"
        },
        "received": {
          "type": "string",
          "description": "Quantity/Amount received",
          "format": "string"
        },
        "receiving-warehouse": {
          "$ref": "#/definitions/Warehouse"
        },
        "recurring-rules": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-RecurringRule"
          }
        },
        "reporting-total": {
          "type": "number",
          "description": "reporting_total",
          "format": "decimal(32,4)"
        },
        "requester": {
          "$ref": "#/definitions/UserSimple"
        },
        "requisition-line-id": {
          "type": "string",
          "description": "Requisition Line Id",
          "format": "string",
          "readOnly": true
        },
        "rfq-easy-form-response-id": {
          "$ref": "#/definitions/EasyFormResponse"
        },
        "rfq-form-response": {
          "$ref": "#/definitions/FormResponse"
        },
        "savings-pct": {
          "type": "number",
          "description": "savings_pct",
          "format": "decimal(8,2)"
        },
        "service-type": {
          "type": "string",
          "description": "Service type",
          "format": "string",
          "readOnly": true
        },
        "source-part-num": {
          "type": "string",
          "description": "source_part_num",
          "format": "string(255)"
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(50)"
        },
        "sub-line-num": {
          "type": "integer",
          "description": "sub_line_num",
          "format": "integer"
        },
        "supp-aux-part-num": {
          "type": "string",
          "description": "supp_aux_part_num",
          "format": "text"
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "supplier-order-number": {
          "type": "string",
          "description": "supplier_order_number",
          "format": "string(255)"
        },
        "supplier-site-id": {
          "type": "integer",
          "description": "supplier site id",
          "format": "integer",
          "readOnly": true
        },
        "third-party-supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "total": {
          "type": "number",
          "description": "total",
          "format": "decimal(32,4)"
        },
        "type": {
          "type": "string",
          "description": "type",
          "format": "string(100)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "version": {
          "type": "integer",
          "description": "version",
          "format": "integer"
        }
      },
      "required": [
        "account",
        "currency",
        "description",
        "external-reference-number",
        "price"
      ]
    },
    "OrderLineAllocation": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "pct": {
          "type": "number",
          "description": "pct",
          "format": "decimal(16,10)"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account",
        "pct"
      ]
    },
    "OrderLineChange": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "account-allocations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrderLineChangeAllocation"
          }
        },
        "asset-tags": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AssetTag"
          }
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "contract": {
          "$ref": "#/definitions/Contract"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "department": {
          "$ref": "#/definitions/Department"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "easy-form-response-id": {
          "type": "string",
          "description": "Easy Form Response Id",
          "readOnly": true
        },
        "extra-line-attribute": {
          "$ref": "#/definitions/ExtraLineAttributes-OrderLineChangeAttribute"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "item": {
          "$ref": "#/definitions/Item"
        },
        "line-num": {
          "type": "string",
          "description": "line_num",
          "format": "string(255)",
          "readOnly": true
        },
        "manufacturer-name": {
          "type": "string",
          "description": "Manufacturer Name",
          "format": "string(255)"
        },
        "manufacturer-part-number": {
          "type": "string",
          "description": "Manufacturer Part Number",
          "format": "string(255)"
        },
        "milestones": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-Milestone"
          }
        },
        "minimum-order-quantity": {
          "type": "number",
          "description": "Minimum order quantity",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "need-by-date": {
          "type": "string",
          "description": "need_by_date",
          "format": "datetime"
        },
        "order-header-change-id": {
          "type": "integer",
          "description": "order_header_change_id",
          "format": "integer",
          "readOnly": true
        },
        "order-increment": {
          "type": "number",
          "description": "Order increment",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "order-line-id": {
          "type": "integer",
          "description": "order_line_id",
          "format": "integer"
        },
        "pending-delete": {
          "type": "boolean",
          "description": "Pending delete",
          "format": "boolean"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "price": {
          "type": "number",
          "description": "price",
          "format": "decimal(30,6)"
        },
        "quantity": {
          "type": "number",
          "description": "quantity",
          "format": "decimal(30,6)"
        },
        "recurring-rules": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-RecurringRule"
          }
        },
        "savings-pct": {
          "type": "number",
          "description": "savings_pct",
          "format": "decimal(8,2)"
        },
        "service-type": {
          "type": "string",
          "description": "Service type",
          "readOnly": true
        },
        "source-part-num": {
          "type": "string",
          "description": "Source part num",
          "format": "string(255)"
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "total": {
          "type": "number",
          "description": "total",
          "format": "decimal(30,4)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "account",
        "currency",
        "description",
        "price",
        "quantity",
        "total"
      ]
    },
    "OrderLineChangeAllocation": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "pct": {
          "type": "number",
          "description": "pct",
          "format": "decimal(16,10)"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account",
        "pct"
      ]
    },
    "OrderPad": {
      "type": "object",
      "properties": {
        "add-all-items": {
          "type": "boolean",
          "description": "Flag indicating to add all items",
          "format": "boolean"
        },
        "any-supplier": {
          "type": "boolean",
          "description": "any_supplier",
          "format": "boolean"
        },
        "base-value": {
          "type": "number",
          "description": "base_value",
          "format": "decimal(10,0)"
        },
        "base-value-currency": {
          "$ref": "#/definitions/Currency"
        },
        "business-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "locked": {
          "type": "boolean",
          "description": "locked",
          "format": "boolean"
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "order-pad-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrderPadLine"
          }
        },
        "order-pad-sections": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrderPadSection"
          }
        },
        "suppliers": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Supplier"
          }
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "use-base-value": {
          "type": "boolean",
          "description": "use_base_value",
          "format": "boolean"
        }
      },
      "required": [
        "base-value",
        "name"
      ]
    },
    "OrderPadLine": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(30,6)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "item": {
          "$ref": "#/definitions/Item"
        },
        "key-item": {
          "type": "boolean",
          "description": "key_item",
          "format": "boolean"
        },
        "order-amount-method": {
          "type": "string",
          "description": "order_amount_method",
          "format": "string(255)",
          "enum": [
            "amount",
            "par"
          ]
        },
        "order-pad-section": {
          "$ref": "#/definitions/OrderPadSection"
        },
        "par-level": {
          "type": "number",
          "description": "par_level",
          "format": "decimal(10,2)"
        },
        "position": {
          "type": "integer",
          "description": "position",
          "format": "integer"
        },
        "supplier-id": {
          "type": "integer",
          "description": "supplier_id",
          "format": "integer"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "item",
        "order-amount-method",
        "supplier-id"
      ]
    },
    "OrderPadSection": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "position": {
          "type": "integer",
          "description": "position",
          "format": "integer"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "name"
      ]
    },
    "OrderWindow": {
      "type": "object"
    },
    "PaymentTerm": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean",
          "enum": [
            "true"
          ]
        },
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(255)"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "days-for-discount-payment": {
          "type": "integer",
          "description": "days_for_discount_payment",
          "format": "integer"
        },
        "days-for-net-payment": {
          "type": "integer",
          "description": "days_for_net_payment",
          "format": "integer"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "discount-cutoff-day": {
          "type": "integer",
          "description": "Document before this day are eligible for discount else they will fall into the next month",
          "format": "integer"
        },
        "discount-due-day": {
          "type": "integer",
          "description": "This field is used to calculate the document's discount due date.",
          "format": "integer"
        },
        "discount-due-month": {
          "type": "integer",
          "description": "This field is used to calculate the document's discount due date along with the discount due day.",
          "format": "integer"
        },
        "discount-rate": {
          "type": "number",
          "description": "discount_rate",
          "format": "float"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "net-cutoff-day": {
          "type": "integer",
          "description": "This helps to determine payment due date if the document should be counted against this month or next",
          "format": "integer"
        },
        "net-due-day": {
          "type": "integer",
          "description": "This helps to determine the document's payment due date",
          "format": "integer"
        },
        "net-due-month": {
          "type": "integer",
          "description": "This helps to determine the document's payment due date",
          "format": "integer"
        },
        "type": {
          "type": "string",
          "description": "Type can be either DaysAfterNetPaymentTerm or SpecificDayPaymentTerm",
          "format": "string(50)",
          "enum": [
            "DaysAfterNetPaymentTerm",
            "SpecificDayPaymentTerm"
          ]
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "code",
        "discount-due-day",
        "discount-due-month",
        "net-due-day",
        "net-due-month",
        "type"
      ]
    },
    "Pcard": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "cvv": {
          "type": "string",
          "description": "cvv",
          "readOnly": true
        },
        "expiry": {
          "type": "string",
          "description": "expiry",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "nickname": {
          "type": "string",
          "description": "nickname",
          "format": "string(255)"
        },
        "number": {
          "type": "string",
          "description": "number",
          "format": "string"
        },
        "shared": {
          "type": "boolean",
          "description": "shared",
          "format": "boolean"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "expiry",
        "name",
        "number"
      ]
    },
    "Period": {
      "type": "object",
      "properties": {
        "account-type": {
          "$ref": "#/definitions/AccountType"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime"
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "end-date": {
          "type": "string",
          "description": "end_date",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer"
        },
        "is-open": {
          "type": "boolean",
          "description": "is_open",
          "format": "boolean"
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(100)"
        },
        "segment-1": {
          "type": "boolean",
          "description": "segment_1",
          "format": "boolean"
        },
        "segment-10": {
          "type": "boolean",
          "description": "segment_10",
          "format": "boolean"
        },
        "segment-11": {
          "type": "boolean",
          "description": "segment_11",
          "format": "boolean"
        },
        "segment-12": {
          "type": "boolean",
          "description": "segment_12",
          "format": "boolean"
        },
        "segment-13": {
          "type": "boolean",
          "description": "segment_13",
          "format": "boolean"
        },
        "segment-14": {
          "type": "boolean",
          "description": "segment_14",
          "format": "boolean"
        },
        "segment-15": {
          "type": "boolean",
          "description": "segment_15",
          "format": "boolean"
        },
        "segment-16": {
          "type": "boolean",
          "description": "segment_16",
          "format": "boolean"
        },
        "segment-17": {
          "type": "boolean",
          "description": "segment_17",
          "format": "boolean"
        },
        "segment-18": {
          "type": "boolean",
          "description": "segment_18",
          "format": "boolean"
        },
        "segment-19": {
          "type": "boolean",
          "description": "segment_19",
          "format": "boolean"
        },
        "segment-2": {
          "type": "boolean",
          "description": "segment_2",
          "format": "boolean"
        },
        "segment-20": {
          "type": "boolean",
          "description": "segment_20",
          "format": "boolean"
        },
        "segment-3": {
          "type": "boolean",
          "description": "segment_3",
          "format": "boolean"
        },
        "segment-4": {
          "type": "boolean",
          "description": "segment_4",
          "format": "boolean"
        },
        "segment-5": {
          "type": "boolean",
          "description": "segment_5",
          "format": "boolean"
        },
        "segment-6": {
          "type": "boolean",
          "description": "segment_6",
          "format": "boolean"
        },
        "segment-7": {
          "type": "boolean",
          "description": "segment_7",
          "format": "boolean"
        },
        "segment-8": {
          "type": "boolean",
          "description": "segment_8",
          "format": "boolean"
        },
        "segment-9": {
          "type": "boolean",
          "description": "segment_9",
          "format": "boolean"
        },
        "start-date": {
          "type": "string",
          "description": "start_date",
          "format": "datetime"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime"
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "end-date",
        "name",
        "start-date"
      ]
    },
    "PhoneNumber": {
      "type": "object",
      "properties": {
        "area-code": {
          "type": "string",
          "description": "area_code",
          "format": "string(255)",
          "readOnly": true
        },
        "country-code": {
          "type": "string",
          "description": "country_code",
          "format": "string(255)",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "extension": {
          "type": "string",
          "description": "extension",
          "format": "string(255)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "number": {
          "type": "string",
          "description": "number",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "Procurement-Milestone": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "Amount",
          "format": "decimal(30,6)"
        },
        "amount-type": {
          "type": "integer",
          "description": "Amount type",
          "format": "integer"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "text"
        },
        "due-date": {
          "type": "string",
          "description": "Due date",
          "format": "date"
        },
        "external-reference-code": {
          "type": "string",
          "description": "External reference code",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "last-exported-at": {
          "type": "string",
          "description": "Last exported at",
          "format": "datetime"
        },
        "parent-milestone-id": {
          "type": "integer",
          "description": "Parent milestone",
          "format": "integer",
          "readOnly": true
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "pending-delete": {
          "type": "boolean",
          "description": "Pending delete",
          "format": "boolean"
        },
        "percent": {
          "type": "number",
          "description": "Percent",
          "format": "decimal(30,6)"
        },
        "recurring-rule-id": {
          "type": "integer",
          "description": "Recurring rule",
          "format": "integer",
          "readOnly": true
        },
        "status": {
          "type": "string",
          "description": "Status",
          "format": "string(255)",
          "readOnly": true
        },
        "type": {
          "type": "string",
          "description": "Type",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "amount-type"
      ]
    },
    "Procurement-RecurringRule": {
      "type": "object",
      "properties": {
        "accounting-amount-currency": {
          "$ref": "#/definitions/Currency"
        },
        "accounting-amount-per-occurrence": {
          "type": "number",
          "description": "Accounting amount per occurrence",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "amount-per-occurrence": {
          "type": "number",
          "description": "Amount per occurrence",
          "format": "decimal(30,6)"
        },
        "amount-type": {
          "type": "string",
          "description": "Amount type",
          "format": "string(255)",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "text",
          "readOnly": true
        },
        "end-date": {
          "type": "string",
          "description": "End date",
          "format": "datetime",
          "readOnly": true
        },
        "frequency": {
          "type": "integer",
          "description": "Frequency",
          "format": "integer"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "interval": {
          "type": "integer",
          "description": "Interval",
          "format": "integer",
          "readOnly": true,
          "enum": [
            "weekly",
            "monthly"
          ]
        },
        "number-of-occurrences": {
          "type": "integer",
          "description": "Number of occurrences",
          "format": "integer",
          "readOnly": true
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "reporting-amount-per-occurrence": {
          "type": "number",
          "description": "Reporting amount per occurrence",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "start-date": {
          "type": "string",
          "description": "Start date",
          "format": "datetime",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "amount-per-occurrence",
        "frequency"
      ]
    },
    "PunchoutSite": {
      "type": "object",
      "properties": {
        "contract-id": {
          "type": "integer",
          "description": "Contract",
          "format": "integer"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "string(255)",
          "readOnly": true
        },
        "disable-cert-verify": {
          "type": "boolean",
          "description": "Disable cert verify",
          "format": "boolean"
        },
        "domain": {
          "type": "string",
          "description": "domain",
          "format": "string"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "identity": {
          "type": "string",
          "description": "identity",
          "format": "string"
        },
        "is-from-coupa-checkout": {
          "type": "boolean",
          "description": "is_from_coupa_checkout",
          "format": "boolean"
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "protocol": {
          "type": "string",
          "description": "protocol",
          "format": "string"
        },
        "secret": {
          "type": "string",
          "description": "secret",
          "format": "string"
        },
        "sender-domain": {
          "type": "string",
          "description": "sender_domain",
          "format": "string"
        },
        "sender-identity": {
          "type": "string",
          "description": "sender_identity",
          "format": "string"
        },
        "ssl-version": {
          "type": "string",
          "description": "Ssl version",
          "format": "string(255)"
        },
        "supplier-id": {
          "type": "integer",
          "description": "supplier_id",
          "format": "integer"
        },
        "supports-edit": {
          "type": "boolean",
          "description": "supports_edit",
          "format": "boolean"
        },
        "supports-inspect": {
          "type": "boolean",
          "description": "supports_inspect",
          "format": "boolean"
        },
        "title": {
          "type": "string",
          "description": "Title",
          "format": "string",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "url": {
          "type": "string",
          "description": "url",
          "format": "string"
        }
      },
      "required": [
        "contract-id",
        "domain",
        "identity",
        "name",
        "protocol",
        "secret",
        "sender-domain",
        "sender-identity",
        "url"
      ]
    },
    "Purpose": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      }
    },
    "ReasonInsight": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "Code",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "reason-type": {
          "type": "string",
          "description": "Reason type",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "code",
        "description",
        "reason-type"
      ]
    },
    "ReasonInsightEvent": {
      "type": "object",
      "properties": {
        "comment": {
          "type": "string",
          "description": "comment",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "eventable-id": {
          "type": "integer",
          "description": "Eventable",
          "format": "integer"
        },
        "eventable-type": {
          "type": "string",
          "description": "Eventable type",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "reason-insight": {
          "$ref": "#/definitions/ReasonInsight"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "comment",
        "reason-insight"
      ]
    },
    "Receipt": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "exported": {
          "type": "boolean",
          "description": "Indicates if transaction has been exported",
          "format": "boolean",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "inventory-transaction": {
          "$ref": "#/definitions/InventoryTransaction"
        },
        "quantity": {
          "type": "number",
          "description": "quantity",
          "format": "decimal(30,6)"
        },
        "receipt-date": {
          "type": "string",
          "description": "receipt_date",
          "format": "datetime"
        },
        "receivable": {
          "type": "string",
          "description": "receivable",
          "readOnly": true
        },
        "receivable-id": {
          "type": "integer",
          "description": "receivable_id",
          "format": "integer"
        },
        "receivable-type": {
          "type": "string",
          "description": "receivable_type",
          "format": "string(255)"
        },
        "total": {
          "type": "number",
          "description": "total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "unit-price": {
          "type": "number",
          "description": "line item price",
          "format": "decimal(30,6)"
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "receipt-date"
      ]
    },
    "RegisteredCompany": {
      "type": "object",
      "properties": {
        "authorized-person-address": {
          "type": "string",
          "description": "Authorized Person Address",
          "format": "string(255)",
          "readOnly": true
        },
        "authorized-person-name": {
          "type": "string",
          "description": "Authorized Person Name",
          "format": "string(255)",
          "readOnly": true
        },
        "authorized-person-vat-id": {
          "type": "string",
          "description": "Authorized Person Vat Id",
          "format": "string(255)",
          "readOnly": true
        },
        "chairman-of-the-board": {
          "type": "string",
          "description": "Chairman of the Board",
          "format": "string(255)",
          "readOnly": true
        },
        "commercial-register-number": {
          "type": "string",
          "description": "Commercial Register & Number",
          "format": "string(255)",
          "readOnly": true
        },
        "company-in-examinership": {
          "type": "boolean",
          "description": "Company in examinership",
          "format": "boolean",
          "readOnly": true
        },
        "company-is-being-wound-up": {
          "type": "boolean",
          "description": "Company is being wound up",
          "format": "boolean",
          "readOnly": true
        },
        "company-receiver-appointed": {
          "type": "boolean",
          "description": "Receiver of the property of a company has been appointed",
          "format": "boolean",
          "readOnly": true
        },
        "company-registration-number": {
          "type": "string",
          "description": "Company Registration Number",
          "format": "string(20)",
          "readOnly": true
        },
        "company-type": {
          "type": "string",
          "description": "Type of Company",
          "format": "string(255)",
          "readOnly": true
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "court-of-registration": {
          "type": "string",
          "description": "Court of Registration",
          "format": "string(255)",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "date-of-registration": {
          "type": "string",
          "description": "Date of Registration",
          "format": "date",
          "readOnly": true
        },
        "file-reference-number": {
          "type": "string",
          "description": "File Reference No.",
          "format": "string(255)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "issued-share-capital": {
          "type": "number",
          "description": "Unpaid Share Capital",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "legal-type": {
          "type": "string",
          "description": "Legal Type of Company",
          "format": "string(255)",
          "readOnly": true
        },
        "liable-company": {
          "type": "string",
          "description": "Liable Company",
          "format": "string(255)",
          "readOnly": true
        },
        "license-number": {
          "type": "string",
          "description": "License Number",
          "format": "string(255)",
          "readOnly": true
        },
        "liquidation-remark": {
          "type": "string",
          "description": "Remark if Company in Liquidation",
          "format": "string(255)",
          "readOnly": true
        },
        "liquidator-name": {
          "type": "string",
          "description": "Liquidator Name",
          "format": "string(255)",
          "readOnly": true
        },
        "managing-directors": {
          "type": "string",
          "description": "Managing Directors",
          "format": "string(255)",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Registered company legal name",
          "format": "string(255)"
        },
        "number-of-issued-stocks": {
          "type": "integer",
          "description": "Number of Issued Stocks",
          "format": "integer",
          "readOnly": true
        },
        "permanent-account-number": {
          "type": "string",
          "description": "Permanent account number",
          "format": "string(255)",
          "readOnly": true
        },
        "permit-date": {
          "type": "string",
          "description": "Permit Date",
          "format": "string(255)",
          "readOnly": true
        },
        "permit-number": {
          "type": "string",
          "description": "Permit Number",
          "format": "string(255)",
          "readOnly": true
        },
        "place-of-registration": {
          "type": "string",
          "description": "Place of Registration",
          "format": "string(255)",
          "readOnly": true
        },
        "preference-agreement": {
          "type": "string",
          "description": "Preference Agreement",
          "format": "string(255)",
          "readOnly": true
        },
        "register-legal-entities": {
          "type": "string",
          "description": "Register Legal Entities",
          "format": "string(255)",
          "readOnly": true
        },
        "registered-seat": {
          "type": "string",
          "description": "Registered Seat",
          "format": "string(255)",
          "readOnly": true
        },
        "registration-authority": {
          "type": "string",
          "description": "QST Registration Number",
          "format": "string(255)",
          "readOnly": true
        },
        "share-capital": {
          "type": "string",
          "description": "Share Capital",
          "format": "string(255)",
          "readOnly": true
        },
        "sole-registration-code": {
          "type": "string",
          "description": "Sole Registration Code",
          "format": "string(255)",
          "readOnly": true
        },
        "supplier-phone-number": {
          "type": "string",
          "description": "Supplier Telephone Number",
          "format": "string(255)",
          "readOnly": true
        },
        "tax-regime": {
          "type": "string",
          "description": "Tax Regime",
          "format": "string(255)",
          "readOnly": true
        },
        "unique-shareholder": {
          "type": "string",
          "description": "Unique Shareholder",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        }
      },
      "required": [
        "country",
        "name"
      ]
    },
    "RemitToAddress": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A no value will make the address inactive making it no longer available to users.  A yes value will make it active and available to users.",
          "format": "boolean"
        },
        "city": {
          "type": "string",
          "description": "City Name",
          "format": "string(50)"
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "external-src-name": {
          "type": "string",
          "description": "Name of the source system.",
          "format": "string(255)"
        },
        "external-src-ref": {
          "type": "string",
          "description": "Reference number from source system.",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa Internal Address ID",
          "format": "integer",
          "readOnly": true
        },
        "local-tax-number": {
          "type": "string",
          "description": "Local Tax Number",
          "format": "string(255)"
        },
        "name": {
          "type": "string",
          "description": "Address 'Nickname'",
          "format": "string(255)"
        },
        "postal-code": {
          "type": "string",
          "description": "Postal Code",
          "format": "string(50)"
        },
        "remit-to-code": {
          "type": "string",
          "description": "Remit To Code (if a Supplier address)",
          "format": "string(255)"
        },
        "state": {
          "type": "string",
          "description": "State Abbreviation",
          "format": "string(50)"
        },
        "street1": {
          "type": "string",
          "description": "Address Line 1",
          "format": "string(100)"
        },
        "street2": {
          "type": "string",
          "description": "Address Line 2",
          "format": "string(100)"
        },
        "tax-registrations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/TaxRegistration"
          }
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "vat-country": {
          "$ref": "#/definitions/Country"
        },
        "vat-number": {
          "type": "string",
          "description": "VAT identification number used for value added tax purposes",
          "format": "string(255)"
        }
      },
      "required": [
        "city",
        "country",
        "local-tax-number",
        "postal-code",
        "remit-to-code",
        "street1"
      ]
    },
    "ReorderAlert": {
      "type": "object"
    },
    "ReqLineAllocation": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "pct": {
          "type": "number",
          "description": "pct",
          "format": "decimal(16,10)"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "account",
        "pct"
      ]
    },
    "RequisitionHeader": {
      "type": "object",
      "properties": {
        "approvals": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Approval"
          }
        },
        "approver": {
          "$ref": "#/definitions/UserSimple"
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "buyer-note": {
          "type": "string",
          "description": "Any comments or notes from the Buyer",
          "format": "text"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "type": "string",
          "description": "Currency Code",
          "format": "USD",
          "readOnly": true
        },
        "current-approval": {
          "$ref": "#/definitions/Approval"
        },
        "department": {
          "$ref": "#/definitions/Department"
        },
        "exported": {
          "type": "boolean",
          "description": "Indicates if transaction has been exported",
          "format": "boolean",
          "readOnly": true
        },
        "external-po-reference": {
          "type": "string",
          "description": "External PO reference that allows customers to supply PO numbers that would override auto generated PO numbers",
          "format": "string(255)"
        },
        "hide-price": {
          "$ref": "#/definitions/RequisitionHeader"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "justification": {
          "type": "string",
          "description": "Requisition Justification Comments",
          "format": "text"
        },
        "line-count": {
          "type": "integer",
          "description": "Requisition Header Line Count",
          "format": "integer",
          "readOnly": true
        },
        "milestones": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-Milestone"
          }
        },
        "mobile-currency": {
          "type": "string",
          "description": "Default currency used",
          "format": "USD",
          "readOnly": true
        },
        "mobile-total": {
          "type": "number",
          "description": "total",
          "format": "decimal",
          "readOnly": true
        },
        "need-by-date": {
          "type": "string",
          "description": "Item Need By Date",
          "format": "datetime"
        },
        "pcard": {
          "$ref": "#/definitions/Pcard"
        },
        "price-hidden": {
          "type": "boolean",
          "description": "Hide price from supplier. True or False",
          "format": "boolean",
          "readOnly": true
        },
        "receiving-warehouse-id": {
          "type": "integer",
          "description": "Receiving Warehouse ID",
          "format": "integer"
        },
        "recurring-rules": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-RecurringRule"
          }
        },
        "reject-reason-comment": {
          "type": "string",
          "description": "last reject reason comment",
          "format": "string",
          "readOnly": true
        },
        "requested-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "requester": {
          "$ref": "#/definitions/UserSimple"
        },
        "requisition-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/RequisitionLine"
          }
        },
        "ship-to-address": {
          "$ref": "#/definitions/Address"
        },
        "ship-to-attention": {
          "type": "string",
          "description": "Ship to Address Attention",
          "format": "string(255)"
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(50)"
        },
        "submitted-at": {
          "type": "string",
          "description": "submitted_at",
          "format": "datetime",
          "readOnly": true
        },
        "total": {
          "type": "number",
          "description": "Total in own currency",
          "format": "decimal",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "requested-by",
        "requester",
        "requisition-lines",
        "ship-to-address",
        "status"
      ]
    },
    "RequisitionLine": {
      "type": "object",
      "properties": {
        "account": {
          "$ref": "#/definitions/Account"
        },
        "account-allocations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ReqLineAllocation"
          }
        },
        "asset-tags": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AssetTag"
          }
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "contract": {
          "$ref": "#/definitions/Contract"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "easy-form-response-id": {
          "type": "string",
          "description": "Easy Form Response Id",
          "readOnly": true
        },
        "extra-line-attribute": {
          "$ref": "#/definitions/ExtraLineAttributes-RequisitionLineAttribute"
        },
        "form-response": {
          "$ref": "#/definitions/FormResponse"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "item": {
          "$ref": "#/definitions/Item"
        },
        "line-num": {
          "type": "integer",
          "description": "line_num",
          "format": "integer"
        },
        "line-type": {
          "type": "string",
          "description": "line type",
          "format": "string",
          "enum": [
            "RequisitionQuantityLine",
            "RequisitionAmountLine"
          ]
        },
        "manufacturer-name": {
          "type": "string",
          "description": "Manufacturer Name",
          "format": "string(255)"
        },
        "manufacturer-part-number": {
          "type": "string",
          "description": "Manufacturer Part Number",
          "format": "string(255)"
        },
        "milestones": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-Milestone"
          }
        },
        "minimum-order-quantity": {
          "type": "number",
          "description": "Minimum order quantity",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "need-by-date": {
          "type": "string",
          "description": "need_by_date",
          "format": "datetime"
        },
        "order-increment": {
          "type": "number",
          "description": "Order increment",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "order-line-id": {
          "type": "integer",
          "description": "order_line_id",
          "format": "integer",
          "readOnly": true
        },
        "order-pad-line": {
          "$ref": "#/definitions/OrderPadLine"
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "period": {
          "$ref": "#/definitions/Period"
        },
        "punchout-site": {
          "$ref": "#/definitions/PunchoutSite"
        },
        "quantity": {
          "type": "number",
          "description": "quantity",
          "format": "decimal(30,6)"
        },
        "realtime-extension": {
          "$ref": "#/definitions/RequisitionLine-RealtimeExtension"
        },
        "receipt-required": {
          "type": "boolean",
          "description": "receipt_required",
          "format": "boolean"
        },
        "recurring-rules": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Procurement-RecurringRule"
          }
        },
        "service-type": {
          "type": "string",
          "description": "Service type",
          "readOnly": true
        },
        "shipping-term": {
          "$ref": "#/definitions/ShippingTerm"
        },
        "source": {
          "type": "string",
          "description": "Source",
          "format": "string(255)"
        },
        "source-details": {
          "type": "string",
          "description": "Source Details",
          "format": "string(255)"
        },
        "source-part-num": {
          "type": "string",
          "description": "source_part_num",
          "format": "string(255)"
        },
        "source-type": {
          "type": "string",
          "description": "source type",
          "format": "string",
          "readOnly": true
        },
        "status": {
          "type": "string",
          "description": "transaction status",
          "format": "string(50)",
          "readOnly": true
        },
        "sub-line-num": {
          "type": "integer",
          "description": "sub_line_num",
          "format": "integer",
          "readOnly": true
        },
        "supp-aux-part-num": {
          "type": "string",
          "description": "supp_aux_part_num",
          "format": "text",
          "readOnly": true
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "supplier-site": {
          "$ref": "#/definitions/SupplierSite"
        },
        "supplier-site-id": {
          "type": "integer",
          "description": "Supplier site",
          "format": "integer"
        },
        "total": {
          "type": "number",
          "description": "total",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "transmission-emails": {
          "type": "string",
          "description": "Transmission emails",
          "format": "text"
        },
        "transmission-method-override": {
          "type": "string",
          "description": "Transmission method override",
          "format": "string(30)",
          "enum": [
            "supplier_default",
            "email",
            "do_not_transmit"
          ]
        },
        "unit-price": {
          "type": "number",
          "description": "line item price",
          "format": "decimal"
        },
        "unspsc-code": {
          "type": "string",
          "description": "UNSPSC code",
          "format": "string(255)",
          "readOnly": true
        },
        "uom": {
          "$ref": "#/definitions/Uom"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "description",
        "item"
      ]
    },
    "RequisitionLine-RealtimeExtension": {
      "type": "object",
      "properties": {
        "async-status": {
          "type": "string",
          "description": "Async status",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "error-code": {
          "type": "string",
          "description": "Error code",
          "format": "string(255)",
          "enum": [
            "un_authorized",
            "service_error",
            "timed_out",
            "out_of_stock",
            "item_not_found",
            "agent_failure",
            "registration_error",
            "has_more_options",
            "check_out_options_reqd",
            "uom_not_available",
            "unknown"
          ]
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "realtime-item-key": {
          "type": "string",
          "description": "Realtime item key",
          "format": "string(255)"
        },
        "requisition-line-id": {
          "type": "integer",
          "description": "Requisition line",
          "format": "integer"
        },
        "show-error-warning": {
          "type": "boolean",
          "description": "Show error warning",
          "format": "boolean",
          "readOnly": true
        },
        "translated-error-message": {
          "type": "string",
          "description": "Translated error message",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "async-status",
        "realtime-item-key",
        "requisition-line-id"
      ]
    },
    "Role": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "omnipotent": {
          "type": "boolean",
          "description": "omnipotent",
          "format": "boolean"
        },
        "system-role": {
          "type": "boolean",
          "description": "system_role",
          "format": "boolean"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "ShippingTerm": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean",
          "enum": [
            "true"
          ]
        },
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(255)"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "text"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "code"
      ]
    },
    "SimDiversityCertificateArtifact": {
      "type": "object",
      "properties": {
        "agency": {
          "$ref": "#/definitions/DiversityCertificationAgency"
        },
        "agency-id": {
          "type": "integer",
          "description": "Agency",
          "format": "integer"
        },
        "created-at": {
          "type": "string",
          "description": "Created Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "string(255)"
        },
        "effective-date": {
          "type": "string",
          "description": "Attachment Effective Date",
          "format": "datetime"
        },
        "expiry-date": {
          "type": "string",
          "description": "Attachment Expiration Date",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Artifact/Attachment ID",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Last Updated Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "Supplier": {
      "type": "object",
      "properties": {
        "account-number": {
          "type": "string",
          "description": "Account number",
          "format": "string(255)"
        },
        "allow-change-requests": {
          "type": "integer",
          "description": "Allows suppliers to create change requests from CSP",
          "format": "integer"
        },
        "allow-csp-access-without-two-factor": {
          "type": "boolean",
          "description": "Allows supplier to access Customer's data from CSP without Two Factor",
          "format": "boolean"
        },
        "allow-cxml-invoicing": {
          "type": "boolean",
          "description": "Allow cXML invoicing for Supplier",
          "format": "boolean"
        },
        "allow-inv-choose-billing-account": {
          "type": "boolean",
          "description": "allow_inv_choose_billing_account",
          "format": "boolean"
        },
        "allow-inv-from-connect": {
          "type": "boolean",
          "description": "If yes, then the supplier can create invoices against their POs or Contracts in CSP",
          "format": "boolean"
        },
        "allow-inv-no-backing-doc-from-connect": {
          "type": "boolean",
          "description": "If yes, then the supplier can create invoices without a backing PO or Contract in CSP.",
          "format": "boolean"
        },
        "allow-inv-unbacked-lines-from-connect": {
          "type": "boolean",
          "description": "If yes, then the supplier can create unbacked invoices without a backing PO or Contract in CSP.",
          "format": "boolean"
        },
        "business-entity-id": {
          "type": "integer",
          "description": "Business Entity",
          "format": "integer"
        },
        "buyer-hold": {
          "type": "boolean",
          "description": "Hold all POs for buyer review",
          "format": "boolean"
        },
        "commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "contacts": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Contact"
          }
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "corporate-url": {
          "type": "string",
          "description": "corporate_url",
          "format": "string(255)"
        },
        "coupa-connect-secret": {
          "type": "string",
          "description": "coupa_connect_secret",
          "format": "string(255)",
          "readOnly": true
        },
        "coupa-pay-financing-only": {
          "type": "boolean",
          "description": "Only pay financed invoices via Coupa Pay",
          "format": "boolean"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "customer-support-contacts": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/CustomerSupportContact"
          }
        },
        "cxml-domain": {
          "type": "string",
          "description": "\"From\" , our domain",
          "format": "string"
        },
        "cxml-http-password": {
          "type": "string",
          "description": "Password required to access the Supplier's online store",
          "format": "string(255)"
        },
        "cxml-http-username": {
          "type": "string",
          "description": "User name required to access the Supplier's online store",
          "format": "string"
        },
        "cxml-identity": {
          "type": "string",
          "description": "\"From\", our identity",
          "format": "string"
        },
        "cxml-invoice-buyer-domain": {
          "type": "string",
          "description": "Buyer Domain for cXML Invoicing",
          "format": "string"
        },
        "cxml-invoice-buyer-identity": {
          "type": "string",
          "description": "Buyer Identity for cXML Invoicing",
          "format": "string"
        },
        "cxml-invoice-secret": {
          "type": "string",
          "description": "Secret Key for cXML Invoicing Authentication",
          "format": "string"
        },
        "cxml-invoice-supplier-domain": {
          "type": "string",
          "description": "Supplier Domain for cXML Invoicing",
          "format": "string"
        },
        "cxml-invoice-supplier-identity": {
          "type": "string",
          "description": "Supplier Identity for cXML Invoicing",
          "format": "string"
        },
        "cxml-protocol": {
          "type": "string",
          "description": "Transmission protocol",
          "format": "string"
        },
        "cxml-secret": {
          "type": "string",
          "description": "Shared secret",
          "format": "string"
        },
        "cxml-ssl-version": {
          "type": "string",
          "description": "Specify the SSL version used for cXML communication with the supplier",
          "format": "string"
        },
        "cxml-supplier-domain": {
          "type": "string",
          "description": "\"To\", supplier domain",
          "format": "string"
        },
        "cxml-supplier-identity": {
          "type": "string",
          "description": "\"To\", supplier identity",
          "format": "string"
        },
        "cxml-url": {
          "type": "string",
          "description": "URL where POs are sent if PO transmission is \"cxml\"",
          "format": "string"
        },
        "dd-settings": {
          "type": "string",
          "description": "Dynamic Discounting Settings whitelisted for supplier",
          "format": "string"
        },
        "default-locale": {
          "type": "string",
          "description": "Default Locale for sending emails to this supplier",
          "format": "string(255)"
        },
        "disable-cert-verify": {
          "type": "boolean",
          "description": "Specify whether to ignore SSL certificate mismatch errors",
          "format": "boolean"
        },
        "display-name": {
          "type": "string",
          "description": "display_name",
          "format": "string(255)"
        },
        "diversities": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/DiversityAssociation"
          }
        },
        "duns": {
          "type": "string",
          "description": "Supplier DUNS number",
          "format": "string"
        },
        "enterprise": {
          "$ref": "#/definitions/Enterprise"
        },
        "hold-invoices-for-ap-review": {
          "type": "boolean",
          "description": "Prevent invoices from this supplier from being approved before AP reviews them.",
          "format": "boolean"
        },
        "id": {
          "type": "integer",
          "description": "Coupa Internal ID",
          "format": "integer",
          "readOnly": true
        },
        "integration-contacts": {
          "type": "string",
          "description": "Supplier user integration contacts",
          "format": "string",
          "readOnly": true
        },
        "invoice-emails": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InvoiceEmail"
          }
        },
        "invoice-matching-level": {
          "type": "string",
          "description": "Invoice matching level",
          "format": "string(255)",
          "enum": [
            "2-way",
            "3-way",
            "3-way-direct",
            "none"
          ]
        },
        "name": {
          "type": "string",
          "description": "Supplier name",
          "format": "string(100)"
        },
        "number": {
          "type": "string",
          "description": "Supplier number",
          "format": "string(255)"
        },
        "on-hold": {
          "type": "boolean",
          "description": "Supplier On Hold",
          "format": "boolean"
        },
        "online-store": {
          "$ref": "#/definitions/OnlineStore"
        },
        "parent": {
          "$ref": "#/definitions/Supplier"
        },
        "payment-method": {
          "type": "string",
          "description": "Default payment method, selectable from drop down",
          "format": "string(255)"
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "payment-term-id": {
          "type": "integer",
          "description": "Payment Term ID",
          "format": "integer"
        },
        "payment-terms": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/PaymentTerm"
          }
        },
        "po-change-method": {
          "type": "string",
          "description": "Purchase order change transmission method",
          "format": "string(255)",
          "enum": [
            "cxml",
            "xml",
            "email",
            "prompt",
            "mark_as_sent",
            "buy_online"
          ]
        },
        "po-email": {
          "type": "string",
          "description": "Email where POs are sent if PO transmission is \"email\"",
          "format": "string(255)"
        },
        "po-method": {
          "type": "string",
          "description": "Purchase order transmission method",
          "format": "string(255)",
          "enum": [
            "cxml",
            "xml",
            "email",
            "prompt",
            "mark_as_sent",
            "buy_online"
          ]
        },
        "preferred-commodities": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Commodity"
          }
        },
        "primary-address": {
          "$ref": "#/definitions/SupplierAddress"
        },
        "primary-contact": {
          "$ref": "#/definitions/Contact"
        },
        "remit-to-addresses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/RemitToAddress"
          }
        },
        "restricted-account-types": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AccountType"
          }
        },
        "savings-pct": {
          "type": "number",
          "description": "Savings for using this supplier",
          "format": "decimal(8,2)"
        },
        "scf-configs": {
          "type": "string",
          "description": "Supply Chain Finance Configurations whitelisted for supplier",
          "format": "string"
        },
        "send-invoices-to-approvals": {
          "type": "boolean",
          "description": "If yes, then invoices will all be sent thru approvals, regardless of total amount.",
          "format": "boolean"
        },
        "shipping-term": {
          "$ref": "#/definitions/ShippingTerm"
        },
        "status": {
          "type": "string",
          "description": "Supplier status",
          "format": "string(20)"
        },
        "storefront-url": {
          "type": "string",
          "description": "Supplier website",
          "format": "string(255)"
        },
        "supplier-addresses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/SupplierAddress"
          }
        },
        "supplier-sites": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/SupplierSite"
          }
        },
        "taggings": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Tagging"
          }
        },
        "tax-code": {
          "$ref": "#/definitions/TaxCode"
        },
        "tax-id": {
          "type": "string",
          "description": "Supplier DUNS number",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "website": {
          "type": "string",
          "description": "Supplier website",
          "format": "string(255)"
        },
        "whitelist-dd": {
          "type": "boolean",
          "description": "Whitelist suppliers for Dynamic Discounting",
          "format": "boolean"
        }
      },
      "required": [
        "enterprise",
        "name",
        "online-store",
        "payment-method",
        "primary-address",
        "primary-contact"
      ]
    },
    "SupplierAddress": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A no value will make the address inactive making it no longer available to users.  A yes value will make it active and available to users.",
          "format": "boolean"
        },
        "attention": {
          "type": "string",
          "description": "Address Default Attention Line",
          "format": "string(255)"
        },
        "business-group-name": {
          "type": "string",
          "description": "Content Group Name for Address",
          "format": "string"
        },
        "city": {
          "type": "string",
          "description": "City Name",
          "format": "string(50)"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa Internal Address ID",
          "format": "integer",
          "readOnly": true
        },
        "local-tax-number": {
          "type": "string",
          "description": "Local Tax Number",
          "format": "string(255)"
        },
        "location-code": {
          "type": "string",
          "description": "location_code",
          "format": "string(255)"
        },
        "name": {
          "type": "string",
          "description": "Address 'Nickname'",
          "format": "string(255)"
        },
        "postal-code": {
          "type": "string",
          "description": "Postal Code",
          "format": "string(50)"
        },
        "purposes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Purpose"
          }
        },
        "state": {
          "type": "string",
          "description": "State Abbreviation",
          "format": "string(50)"
        },
        "street1": {
          "type": "string",
          "description": "Address Line 1",
          "format": "string(100)"
        },
        "street2": {
          "type": "string",
          "description": "Address Line 2",
          "format": "string(100)"
        },
        "street3": {
          "type": "string",
          "description": "Address Line 3",
          "format": "string(100)"
        },
        "street4": {
          "type": "string",
          "description": "Address Line 4",
          "format": "string(100)"
        },
        "tax-registrations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/TaxRegistration"
          }
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "vat-country": {
          "$ref": "#/definitions/Country"
        },
        "vat-number": {
          "type": "string",
          "description": "VAT identification number used for value added tax purposes",
          "format": "string(255)"
        }
      },
      "required": [
        "city",
        "country",
        "local-tax-number",
        "postal-code",
        "street1"
      ]
    },
    "SupplierInformation": {
      "type": "object",
      "properties": {
        "allow-cxml-invoicing": {
          "type": "boolean",
          "description": "Allow cXML Invoicing",
          "format": "boolean",
          "readOnly": true
        },
        "allow-inv-choose-billing-account": {
          "type": "boolean",
          "description": "Allow Choosing Billing Account in Invoicing",
          "format": "boolean",
          "readOnly": true
        },
        "allow-inv-from-connect": {
          "type": "boolean",
          "description": "Allow Invoicing from Connect",
          "format": "boolean",
          "readOnly": true
        },
        "allow-inv-no-backing-doc-from-connect": {
          "type": "boolean",
          "description": "Allow Invoicing with no Backing Doc from Connect",
          "format": "boolean",
          "readOnly": true
        },
        "allow-inv-unbacked-lines-from-connect": {
          "type": "boolean",
          "description": "Allow Invoicing with Unbacked Lines from Connect",
          "format": "boolean",
          "readOnly": true
        },
        "backend-system-catalog": {
          "type": "string",
          "description": "Backend System Used for Catalog Management",
          "format": "string(255)",
          "enum": [
            "CatBase",
            "Elastic",
            "iPartner Product Suite",
            "Claritum",
            "Contalog",
            "CatalognTime",
            "Advizia",
            "Aravo",
            "MatrixCMX",
            "SigmaCommerce"
          ]
        },
        "backend-system-invoicing": {
          "type": "string",
          "description": "Backend System Used for Invoice",
          "format": "string(255)",
          "enum": [
            "SAP",
            "Oracle"
          ]
        },
        "buyer-hold": {
          "type": "boolean",
          "description": "Hold POs for buyer review",
          "format": "boolean"
        },
        "buyer-id": {
          "type": "integer",
          "description": "Buyer ID",
          "format": "integer"
        },
        "comment": {
          "type": "string",
          "description": "Comment Text",
          "format": "text"
        },
        "comment-source": {
          "type": "string",
          "description": "Comment Source",
          "format": "string(255)"
        },
        "commodity-id": {
          "type": "integer",
          "description": "Commodity ID",
          "format": "integer",
          "readOnly": true
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "country-of-operation": {
          "$ref": "#/definitions/Country"
        },
        "country-of-operation-id": {
          "type": "integer",
          "description": "Country of Operation ID",
          "format": "integer"
        },
        "created-at": {
          "type": "string",
          "description": "SIM Record Create Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency-id": {
          "type": "integer",
          "description": "Currency ID",
          "format": "integer"
        },
        "cxml-domain": {
          "type": "string",
          "description": "cXML Domain",
          "format": "string"
        },
        "cxml-http-username": {
          "type": "string",
          "description": "cXML HTTP Username",
          "format": "string"
        },
        "cxml-identity": {
          "type": "string",
          "description": "cXML Identity",
          "format": "string"
        },
        "cxml-protocol": {
          "type": "string",
          "description": "cXML Protocol",
          "format": "string"
        },
        "cxml-secret": {
          "type": "string",
          "description": "cXML Secret",
          "format": "string"
        },
        "cxml-ssl-version": {
          "type": "string",
          "description": "cXML SSL Version",
          "format": "string"
        },
        "cxml-supplier-domain": {
          "type": "string",
          "description": "cXML Supplier Domain",
          "format": "string"
        },
        "cxml-supplier-identity": {
          "type": "string",
          "description": "cXML Supplier Identity",
          "format": "string"
        },
        "cxml-url": {
          "type": "string",
          "description": "cXML URL",
          "format": "string"
        },
        "default-commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "default-commodity-id": {
          "type": "integer",
          "description": "Default Commodity",
          "format": "integer"
        },
        "default-invoice-email": {
          "type": "string",
          "description": "Default Invoice Email",
          "format": "string(255)",
          "readOnly": true
        },
        "disable-cert-verify": {
          "type": "boolean",
          "description": "Disable Cert Verify",
          "format": "boolean"
        },
        "display-name": {
          "type": "string",
          "description": "Supplier Display Name",
          "format": "string(255)"
        },
        "diversities": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/DiversityAssociation"
          }
        },
        "duns-number": {
          "type": "string",
          "description": "Dun and Bradstreet Number",
          "format": "string"
        },
        "duplicate-exists": {
          "type": "boolean",
          "description": "Duplicate Exists",
          "format": "boolean"
        },
        "estimated-spend-amount": {
          "type": "number",
          "description": "Estimate Spend Amount",
          "format": "decimal(30,4)"
        },
        "fed-reportable": {
          "type": "boolean",
          "description": "Federal Tax Reportable Indicator",
          "format": "boolean"
        },
        "federal-tax-num": {
          "type": "string",
          "description": "Federal Tax ID Number",
          "format": "string(255)"
        },
        "goods-services-provided": {
          "type": "string",
          "description": "Goods and Services Provided",
          "format": "string(255)"
        },
        "govt-agency-interaction": {
          "type": "string",
          "description": "Government Agency Interaction Explanation",
          "format": "text"
        },
        "govt-agency-interaction-indicator": {
          "type": "boolean",
          "description": "Government Agency Interaction Indicator",
          "format": "boolean"
        },
        "govt-allegation-fraud-bribery": {
          "type": "string",
          "description": "Supplier policy for government allegations of fraud and bribery",
          "format": "string(255)"
        },
        "govt-allegation-fraud-bribery-indicator": {
          "type": "boolean",
          "description": "Does the supplier have a policy for government allegations of fraud and bribery?",
          "format": "boolean"
        },
        "hold-invoices-for-ap-review": {
          "type": "boolean",
          "description": "Hold Invoices for AP Review",
          "format": "boolean",
          "readOnly": true
        },
        "hold-payment": {
          "type": "string",
          "description": "Hold Payment",
          "format": "string"
        },
        "hold-payment-indicator": {
          "type": "boolean",
          "description": "Hold Payment Indicator",
          "format": "boolean"
        },
        "id": {
          "type": "integer",
          "description": "SIM ID",
          "format": "integer",
          "readOnly": true
        },
        "inbound-invoice-domain": {
          "type": "string",
          "description": "Inbound Invoice Email Domain",
          "format": "string(255)",
          "readOnly": true
        },
        "inco-terms": {
          "type": "string",
          "description": "Inco Terms",
          "format": "string(255)",
          "enum": [
            "EXW",
            "FCA",
            "CPT",
            "CIP",
            "DAT",
            "DAP",
            "DDP",
            "FAS",
            "FOB",
            "CFR",
            "CIF",
            "DPU"
          ]
        },
        "income-type": {
          "type": "string",
          "description": "Income Type",
          "format": "string"
        },
        "industry": {
          "type": "string",
          "description": "Primary Industry of Supplier",
          "format": "string(255)"
        },
        "intl-other-explanation": {
          "type": "string",
          "description": "International Tax Classification Explanation",
          "format": "text"
        },
        "intl-tax-classification": {
          "type": "string",
          "description": "International Tax Classification",
          "format": "string"
        },
        "intl-tax-num": {
          "type": "string",
          "description": "International Tax Number",
          "format": "string"
        },
        "invoice-amount-limit": {
          "type": "string",
          "description": "Invoice Amount Limit",
          "format": "text"
        },
        "invoice-inbound-emails": {
          "type": "string",
          "description": "Invoice Inbound Emails",
          "format": "text",
          "readOnly": true
        },
        "invoice-matching-level": {
          "type": "string",
          "description": "Invoice Matching Level",
          "format": "string(255)",
          "readOnly": true
        },
        "last-exported-at": {
          "type": "string",
          "description": "Last Exported Flag",
          "format": "datetime",
          "readOnly": true
        },
        "logo-content-type": {
          "type": "string",
          "description": "Logo content type",
          "format": "string(255)",
          "readOnly": true
        },
        "logo-file-name": {
          "type": "string",
          "description": "Logo file name",
          "format": "string(255)",
          "readOnly": true
        },
        "logo-file-size": {
          "type": "integer",
          "description": "Logo file size",
          "format": "integer",
          "readOnly": true
        },
        "logo-updated-at": {
          "type": "string",
          "description": "Logo updated at",
          "format": "datetime",
          "readOnly": true
        },
        "minority-indicator": {
          "type": "boolean",
          "description": "MWBE Indicator",
          "format": "boolean"
        },
        "minority-type-id": {
          "type": "integer",
          "description": "Minority Type",
          "format": "integer",
          "enum": [
            "1",
            "2",
            "3",
            "4"
          ]
        },
        "name": {
          "type": "string",
          "description": "Supplier name",
          "format": "string(100)"
        },
        "organization-type": {
          "type": "string",
          "description": "Organization Type",
          "format": "string(255)",
          "enum": [
            "Corporation",
            "Foreign Corporation",
            "Individual",
            "Foreign Individual",
            "Partnership",
            "Foreign Partnership"
          ]
        },
        "parent-company-name": {
          "type": "string",
          "description": "Parent Company Name",
          "format": "string(255)"
        },
        "pay-group": {
          "type": "string",
          "description": "Pay Group",
          "format": "string"
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "payment-term-id": {
          "type": "integer",
          "description": "Payment Term",
          "format": "integer"
        },
        "payment-terms-id": {
          "type": "integer",
          "description": "Payment Term",
          "format": "integer"
        },
        "po-change-method": {
          "type": "string",
          "description": "PO Change Method",
          "format": "string(255)",
          "enum": [
            "cxml",
            "xml",
            "email",
            "prompt",
            "mark_as_sent",
            "buy_online"
          ]
        },
        "po-email": {
          "type": "string",
          "description": "PO Email",
          "format": "string(255)"
        },
        "po-method": {
          "type": "string",
          "description": "PO Method",
          "format": "string(255)",
          "enum": [
            "cxml",
            "xml",
            "email",
            "prompt",
            "mark_as_sent",
            "buy_online"
          ]
        },
        "policy-for-bribery-corruption": {
          "type": "string",
          "description": "Supplier policy for bribery and corruption",
          "format": "text"
        },
        "policy-for-bribery-corruption-indicator": {
          "type": "boolean",
          "description": "Does the supplier have a policy for bribery and corruption?",
          "format": "boolean"
        },
        "preferred-currency": {
          "$ref": "#/definitions/Currency"
        },
        "preferred-currency-id": {
          "type": "integer",
          "description": "Default Currency ID",
          "format": "integer"
        },
        "preferred-language": {
          "$ref": "#/definitions/Language"
        },
        "preferred-language-id": {
          "type": "integer",
          "description": "Preferred Language ID",
          "format": "integer"
        },
        "savings-pct": {
          "type": "number",
          "description": "Savings Percentage",
          "format": "decimal(8,2)",
          "readOnly": true
        },
        "send-invoices-to-approvals": {
          "type": "boolean",
          "description": "Send Invoices to Approvals",
          "format": "boolean",
          "readOnly": true
        },
        "separate-remit-to": {
          "type": "boolean",
          "description": "Separate Remit To",
          "format": "boolean"
        },
        "shipping-term-id": {
          "type": "integer",
          "description": "Shipping Term ID",
          "format": "integer",
          "readOnly": true
        },
        "social-security-number": {
          "type": "string",
          "description": "Social Security Number",
          "format": "string",
          "readOnly": true
        },
        "status": {
          "type": "string",
          "description": "Status",
          "format": "string(255)"
        },
        "supplier-id": {
          "type": "integer",
          "description": "Supplier ID",
          "format": "integer"
        },
        "supplier-information-addresses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/SupplierInformationAddress"
          }
        },
        "supplier-information-artifacts": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/SupplierInformationArtifact"
          }
        },
        "supplier-information-contacts": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/SupplierInformationContact"
          }
        },
        "supplier-name": {
          "type": "string",
          "description": "Supplier Name",
          "format": "string(255)"
        },
        "supplier-number": {
          "type": "string",
          "description": "Supplier Number",
          "format": "string(255)"
        },
        "supplier-region": {
          "type": "string",
          "description": "Supplier Region",
          "format": "string(255)",
          "enum": [
            "AMER",
            "EMEA",
            "APAC",
            "Japan"
          ]
        },
        "tax-classification": {
          "type": "string",
          "description": "US Tax Classification",
          "format": "string"
        },
        "tax-code-id": {
          "type": "integer",
          "description": "Tax Code ID",
          "format": "integer"
        },
        "tax-exempt-other-explanation": {
          "type": "string",
          "description": "Tax Exempt Explanation",
          "format": "string"
        },
        "tax-region": {
          "type": "string",
          "description": "Tax Region",
          "format": "string"
        },
        "third-party-interaction": {
          "type": "string",
          "description": "Supplier policy for Third Party Interactions",
          "format": "text"
        },
        "third-party-interaction-indicator": {
          "type": "boolean",
          "description": "Supplier has a policy for its Third Party Interactions?",
          "format": "boolean"
        },
        "updated-at": {
          "type": "string",
          "description": "SIM Record Updated Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "user-id": {
          "type": "integer",
          "description": "User ID",
          "format": "integer"
        },
        "website": {
          "type": "string",
          "description": "Website",
          "format": "string(255)",
          "readOnly": true
        }
      },
      "required": [
        "name",
        "status"
      ]
    },
    "SupplierInformationAddress": {
      "type": "object",
      "properties": {
        "account-type-item": {
          "type": "string",
          "description": "Bank Account Type"
        },
        "active": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean"
        },
        "address-name": {
          "type": "string",
          "description": "Address Name",
          "format": "string(255)"
        },
        "bank-account-number": {
          "type": "string",
          "description": "Bank Account Number"
        },
        "bank-address": {
          "type": "string",
          "description": "Bank Address"
        },
        "bank-city": {
          "type": "string",
          "description": "Bank City"
        },
        "bank-code": {
          "type": "string",
          "description": "Bank Code"
        },
        "bank-country": {
          "$ref": "#/definitions/Country"
        },
        "bank-fax-phone": {
          "type": "string",
          "description": "Bank Fax"
        },
        "bank-name": {
          "type": "string",
          "description": "Bank Name"
        },
        "bank-postal-code": {
          "type": "string",
          "description": "Bank Postal Code"
        },
        "bank-routing-number": {
          "type": "string",
          "description": "Bank Account Routing Number"
        },
        "bank-state-region": {
          "type": "string",
          "description": "Bank State"
        },
        "bank-work-phone": {
          "type": "string",
          "description": "Bank Work Phone"
        },
        "bic": {
          "type": "string",
          "description": "BIC"
        },
        "bic-routing-code": {
          "type": "string",
          "description": "BIC Routing Code"
        },
        "bsb-number": {
          "type": "string",
          "description": "BSB Number (Australian Routing Code)"
        },
        "city": {
          "type": "string",
          "description": "City",
          "format": "string(255)"
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Created Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "csp-rta-id": {
          "type": "integer",
          "description": "Coupa Supplier Portal Remit-to Address ID",
          "format": "integer",
          "readOnly": true
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "iban-number": {
          "type": "string",
          "description": "IBAN Number"
        },
        "id": {
          "type": "integer",
          "description": "Address ID",
          "format": "integer",
          "readOnly": true
        },
        "ifsc": {
          "type": "string",
          "description": "IFSC"
        },
        "intermediary-bank-name": {
          "type": "string",
          "description": "Intermediary Bank Name"
        },
        "international-bank-account-number": {
          "type": "string",
          "description": "International Bank Account Number (IBAN)"
        },
        "kind": {
          "type": "string",
          "description": "Address Type",
          "format": "string(255)",
          "enum": [
            "RTA",
            "User",
            "Primary"
          ]
        },
        "location-code": {
          "type": "string",
          "description": "Remit To Location Code / Address ID / Key",
          "format": "string(255)"
        },
        "name-on-bank-account": {
          "type": "string",
          "description": "Name on Bank Account"
        },
        "payment-method-item": {
          "type": "string",
          "description": "Payment Method",
          "format": "string(255)",
          "enum": [
            "tran",
            "cash",
            "cred",
            "pcard"
          ]
        },
        "po-box": {
          "type": "string",
          "description": "PO Box",
          "format": "string(255)"
        },
        "po-box-postal-code": {
          "type": "string",
          "description": "PO Box Postal Code",
          "format": "string(255)"
        },
        "postal-code": {
          "type": "string",
          "description": "Postal Code",
          "format": "string(255)"
        },
        "sort-code": {
          "type": "string",
          "description": "Sort Code"
        },
        "state-region": {
          "type": "string",
          "description": "State",
          "format": "string(255)"
        },
        "street-address": {
          "type": "string",
          "description": "Street Address 1",
          "format": "string(255)"
        },
        "street-address2": {
          "type": "string",
          "description": "Street Address 2",
          "format": "string(255)"
        },
        "supplier-information-id": {
          "type": "integer",
          "description": "Supplier information",
          "format": "integer",
          "readOnly": true
        },
        "swift-code": {
          "type": "string",
          "description": "SWIFT Code"
        },
        "transit-number-and-institution-number": {
          "type": "string",
          "description": "Transit Number And Institution Number"
        },
        "updated-at": {
          "type": "string",
          "description": "Last Updated Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "kind"
      ]
    },
    "SupplierInformationArtifact": {
      "type": "object",
      "properties": {
        "agency": {
          "type": "string",
          "description": "Agency",
          "readOnly": true
        },
        "artifact-meta-type": {
          "type": "string",
          "description": "Artifact/Attachment Sub-Type",
          "format": "string(255)"
        },
        "artifact-type": {
          "type": "string",
          "description": "Artifact/Attachment Type",
          "format": "string(255)"
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Created Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "string(255)"
        },
        "effective-date": {
          "type": "string",
          "description": "Attachment Effective Date",
          "format": "datetime"
        },
        "expiry-date": {
          "type": "string",
          "description": "Attachment Expiration Date",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Artifact/Attachment ID",
          "format": "integer",
          "readOnly": true
        },
        "supplier-id": {
          "type": "string",
          "description": "Supplier ID",
          "format": "string(255)"
        },
        "supplier-information-id": {
          "type": "integer",
          "description": "SIM ID",
          "format": "integer",
          "readOnly": true
        },
        "type": {
          "type": "string",
          "description": "Type",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Last Updated Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "SupplierInformationContact": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Created Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "email": {
          "type": "string",
          "description": "Email Address",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Contact ID",
          "format": "integer",
          "readOnly": true
        },
        "kind": {
          "type": "string",
          "description": "Contract Kind/Type",
          "format": "string(255)",
          "enum": [
            "Primary",
            "Sales",
            "PO Delivery",
            "Account_Receivable"
          ]
        },
        "name-additional": {
          "type": "string",
          "description": "Name Additional",
          "format": "string(255)"
        },
        "name-family": {
          "type": "string",
          "description": "Last Name/Family Name",
          "format": "string(255)"
        },
        "name-fullname": {
          "type": "string",
          "description": "Full Name",
          "format": "string(255)"
        },
        "name-given": {
          "type": "string",
          "description": "Given/First Name",
          "format": "string(255)"
        },
        "name-prefix": {
          "type": "string",
          "description": "Name Prefix",
          "format": "string(255)"
        },
        "name-suffix": {
          "type": "string",
          "description": "Name Suffix",
          "format": "string(255)"
        },
        "notes": {
          "type": "string",
          "description": "Contact Notes",
          "format": "string(255)"
        },
        "phone-fax": {
          "$ref": "#/definitions/PhoneNumber"
        },
        "phone-mobile": {
          "$ref": "#/definitions/PhoneNumber"
        },
        "phone-work": {
          "$ref": "#/definitions/PhoneNumber"
        },
        "supplier-information-id": {
          "type": "integer",
          "description": "Supplier information",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Last Updated Date and Time",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "kind"
      ]
    },
    "SupplierItem": {
      "type": "object",
      "properties": {
        "availability": {
          "type": "string",
          "description": "Availability",
          "format": "string(255)",
          "enum": [
            "in_stock",
            "out_of_stock",
            "backordered"
          ]
        },
        "availability-date": {
          "type": "string",
          "description": "Availability Date",
          "format": "datetime"
        },
        "catalog": {
          "$ref": "#/definitions/Catalog"
        },
        "contract": {
          "$ref": "#/definitions/Contract"
        },
        "contract-term": {
          "$ref": "#/definitions/ContractTerm"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "is-coupa-advantage": {
          "type": "boolean",
          "description": "Is Coupa Advantage",
          "format": "boolean",
          "readOnly": true
        },
        "item": {
          "$ref": "#/definitions/Item"
        },
        "lead-time": {
          "type": "integer",
          "description": "lead_time",
          "format": "integer"
        },
        "manufacturer": {
          "type": "string",
          "description": "manufacturer",
          "format": "string(255)"
        },
        "minimum-order-quantity": {
          "type": "number",
          "description": "minimum_order_quantity",
          "format": "decimal(30,6)"
        },
        "order-increment": {
          "type": "number",
          "description": "order_increment",
          "format": "decimal(30,6)"
        },
        "preferred": {
          "type": "boolean",
          "description": "Indicates preferred supplier for this item",
          "format": "boolean"
        },
        "price": {
          "type": "number",
          "description": "price",
          "format": "decimal"
        },
        "price-change": {
          "type": "number",
          "description": "price_change",
          "format": "float"
        },
        "price-tier-1": {
          "type": "number",
          "description": "price_tier_1",
          "format": "decimal(30,6)"
        },
        "price-tier-10": {
          "type": "number",
          "description": "price_tier_10",
          "format": "decimal(30,6)"
        },
        "price-tier-11": {
          "type": "number",
          "description": "price_tier_11",
          "format": "decimal(30,6)"
        },
        "price-tier-12": {
          "type": "number",
          "description": "price_tier_12",
          "format": "decimal(30,6)"
        },
        "price-tier-13": {
          "type": "number",
          "description": "price_tier_13",
          "format": "decimal(30,6)"
        },
        "price-tier-14": {
          "type": "number",
          "description": "price_tier_14",
          "format": "decimal(30,6)"
        },
        "price-tier-15": {
          "type": "number",
          "description": "price_tier_15",
          "format": "decimal(30,6)"
        },
        "price-tier-16": {
          "type": "number",
          "description": "price_tier_16",
          "format": "decimal(30,6)"
        },
        "price-tier-17": {
          "type": "number",
          "description": "price_tier_17",
          "format": "decimal(30,6)"
        },
        "price-tier-18": {
          "type": "number",
          "description": "price_tier_18",
          "format": "decimal(30,6)"
        },
        "price-tier-19": {
          "type": "number",
          "description": "price_tier_19",
          "format": "decimal(30,6)"
        },
        "price-tier-2": {
          "type": "number",
          "description": "price_tier_2",
          "format": "decimal(30,6)"
        },
        "price-tier-20": {
          "type": "number",
          "description": "price_tier_20",
          "format": "decimal(30,6)"
        },
        "price-tier-3": {
          "type": "number",
          "description": "price_tier_3",
          "format": "decimal(30,6)"
        },
        "price-tier-4": {
          "type": "number",
          "description": "price_tier_4",
          "format": "decimal(30,6)"
        },
        "price-tier-5": {
          "type": "number",
          "description": "price_tier_5",
          "format": "decimal(30,6)"
        },
        "price-tier-6": {
          "type": "number",
          "description": "price_tier_6",
          "format": "decimal(30,6)"
        },
        "price-tier-7": {
          "type": "number",
          "description": "price_tier_7",
          "format": "decimal(30,6)"
        },
        "price-tier-8": {
          "type": "number",
          "description": "price_tier_8",
          "format": "decimal(30,6)"
        },
        "price-tier-9": {
          "type": "number",
          "description": "price_tier_9",
          "format": "decimal(30,6)"
        },
        "savings-pct": {
          "type": "number",
          "description": "savings_pct",
          "format": "decimal(8,2)"
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
        },
        "supplier-aux-part-num": {
          "type": "string",
          "description": "supplier_aux_part_num",
          "format": "string(255)"
        },
        "supplier-part-num": {
          "type": "string",
          "description": "supplier_part_num",
          "format": "string(255)"
        },
        "unspsc-code": {
          "type": "string",
          "description": "UNSPSC code",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "supplier",
        "supplier-part-num"
      ]
    },
    "SupplierRemitTo": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "City",
          "format": "string(255)"
        },
        "company-registration-number": {
          "type": "string",
          "description": "Company Registration Number",
          "readOnly": true
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "disclosure": {
          "type": "string",
          "description": "Disclosure",
          "format": "text",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)",
          "readOnly": true
        },
        "postal-code": {
          "type": "string",
          "description": "Postal Code",
          "format": "string(255)"
        },
        "preferred-language": {
          "type": "string",
          "description": "Preferred Language",
          "format": "string(255)",
          "readOnly": true
        },
        "registered-company": {
          "$ref": "#/definitions/RegisteredCompany"
        },
        "remit-to-code": {
          "type": "string",
          "description": "Remit to code",
          "format": "string(255)"
        },
        "state": {
          "type": "string",
          "description": "State",
          "format": "string(255)"
        },
        "street1": {
          "type": "string",
          "description": "Street 1",
          "format": "string(255)"
        },
        "street2": {
          "type": "string",
          "description": "Street 2",
          "format": "string(255)"
        },
        "supplier-name": {
          "type": "string",
          "description": "Supplier Name",
          "readOnly": true
        },
        "tax-number": {
          "type": "string",
          "description": "Tax Number",
          "format": "string(255)"
        },
        "tax-prefix": {
          "type": "string",
          "description": "Tax Prefix",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "validated-source": {
          "type": "string",
          "description": "Validated source",
          "format": "string(50)",
          "readOnly": true
        }
      },
      "required": [
        "city",
        "postal-code",
        "street1",
        "tax-number"
      ]
    },
    "SupplierSite": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "true if the site is active",
          "format": "boolean"
        },
        "allow-change-requests": {
          "type": "integer",
          "description": "Allows suppliers to create change requests from CSP",
          "format": "integer"
        },
        "buyer-hold": {
          "type": "boolean",
          "description": "Hold all POs for buyer review",
          "format": "boolean"
        },
        "code": {
          "type": "string",
          "description": "supplier_code",
          "format": "string(20)"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "cxml-domain": {
          "type": "string",
          "description": "\"From\" , our domain",
          "format": "string(255)"
        },
        "cxml-http-username": {
          "type": "string",
          "description": "User name required to access the Supplier's online store",
          "format": "string(255)"
        },
        "cxml-identity": {
          "type": "string",
          "description": "\"From\", our identity",
          "format": "string(255)"
        },
        "cxml-protocol": {
          "type": "string",
          "description": "Transmission protocol",
          "format": "string(255)"
        },
        "cxml-secret": {
          "type": "string",
          "description": "Shared secret",
          "format": "string(255)"
        },
        "cxml-ssl-version": {
          "type": "string",
          "description": "Specify the SSL version used for cXML communication with the supplier",
          "format": "string(255)"
        },
        "cxml-supplier-domain": {
          "type": "string",
          "description": "\"To\", supplier domain",
          "format": "string(255)"
        },
        "cxml-supplier-identity": {
          "type": "string",
          "description": "\"To\", supplier identity",
          "format": "string(255)"
        },
        "cxml-url": {
          "type": "string",
          "description": "URL where POs are sent if PO transmission is \"cxml\"",
          "format": "string(255)"
        },
        "default-locale": {
          "type": "string",
          "description": "Default Locale for sending emails to this supplier site",
          "format": "string(255)"
        },
        "disable-cert-verify": {
          "type": "boolean",
          "description": "Specify whether to ignore SSL certificate mismatch errors",
          "format": "boolean"
        },
        "id": {
          "type": "integer",
          "description": "Coupa Internal ID",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Supplier name",
          "format": "string(255)"
        },
        "payment-term": {
          "$ref": "#/definitions/PaymentTerm"
        },
        "po-change-method": {
          "type": "string",
          "description": "Purchase order change transmission method",
          "format": "string(255)",
          "enum": [
            "cxml",
            "xml",
            "email",
            "prompt",
            "mark_as_sent",
            "buy_online"
          ]
        },
        "po-email": {
          "type": "string",
          "description": "Email where POs are sent if PO transmission is \"email\"",
          "format": "string(255)"
        },
        "po-method": {
          "type": "string",
          "description": "Purchase order transmission method",
          "format": "string(255)",
          "enum": [
            "cxml",
            "xml",
            "email",
            "prompt",
            "mark_as_sent",
            "buy_online"
          ]
        },
        "remit-to-addresses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/RemitToAddress"
          }
        },
        "shipping-term": {
          "$ref": "#/definitions/ShippingTerm"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "code",
        "cxml-domain",
        "cxml-identity",
        "cxml-protocol",
        "cxml-secret",
        "cxml-supplier-domain",
        "cxml-supplier-identity",
        "cxml-url",
        "name",
        "po-email"
      ]
    },
    "Tag": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(30)"
        },
        "system-tag": {
          "type": "boolean",
          "description": "System tag",
          "format": "boolean"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "Tagging": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Tagging active state",
          "format": "boolean"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description on the Tag on an Object (Tags on different objects can have different descriptions)",
          "format": "text"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "tag": {
          "$ref": "#/definitions/Tag"
        }
      }
    },
    "TaxCode": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Tax code is enabled or disabled",
          "format": "boolean"
        },
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(255)"
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "effective-date": {
          "type": "string",
          "description": "Date when tax code is become active",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "percentage": {
          "type": "number",
          "description": "percentage",
          "format": "float"
        },
        "tax-rate": {
          "$ref": "#/definitions/TaxRate"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "code",
        "country",
        "percentage"
      ]
    },
    "TaxLine": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "amount-engine": {
          "type": "number",
          "description": "Amount calculated by either Coupa Native or External Tax Engine based on configuration",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "base": {
          "type": "number",
          "description": "Base to Calculate Tax",
          "format": "decimal(30,4)"
        },
        "basis": {
          "type": "number",
          "description": "Supplier Withholding Base Suggestion",
          "format": "decimal(30,6)"
        },
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(255)",
          "readOnly": true
        },
        "code-engine": {
          "type": "string",
          "description": "Code returned by External Tax Engine based on configuration",
          "format": "string(255)",
          "readOnly": true
        },
        "code-id": {
          "type": "integer",
          "description": "code_id",
          "format": "integer"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Tax Reference",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer"
        },
        "kind-of-factor": {
          "type": "string",
          "description": "Kind of Factor",
          "format": "string(255)",
          "readOnly": true
        },
        "nature-of-tax": {
          "type": "string",
          "description": "Kind of Tax",
          "format": "string(255)"
        },
        "product-tax-classification": {
          "type": "string",
          "description": "Product Tax Classification",
          "format": "string(255)"
        },
        "rate": {
          "type": "number",
          "description": "rate",
          "format": "float"
        },
        "rate-engine": {
          "type": "number",
          "description": "Rate returned by External Tax Engine based on configuration",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "supplier-rate": {
          "type": "number",
          "description": "Supplier Withholding Rate Suggestion",
          "format": "decimal(30,4)"
        },
        "tax-code": {
          "$ref": "#/definitions/TaxCode"
        },
        "tax-rate": {
          "$ref": "#/definitions/TaxRate"
        },
        "tax-rate-type": {
          "$ref": "#/definitions/TaxRateType"
        },
        "taxable-amount": {
          "type": "number",
          "description": "Amount",
          "format": "decimal(32,4)"
        },
        "type": {
          "type": "string",
          "description": "WithholdingTaxLine, TcsTaxLine or TaxLine",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "withholding-amount": {
          "type": "number",
          "description": "Withholding Amount",
          "format": "decimal(30,4)"
        }
      }
    },
    "TaxRate": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Tax rate is enabled or disabled",
          "format": "boolean"
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "customer-accounting": {
          "type": "boolean",
          "description": "Customer accounting",
          "format": "boolean"
        },
        "effective-date": {
          "type": "string",
          "description": "Date when tax rate is become active",
          "format": "datetime"
        },
        "exempt": {
          "type": "boolean",
          "description": "Whether Tax Rate is exempt or not",
          "format": "boolean"
        },
        "expiration-date": {
          "type": "string",
          "description": "Date when tax rate is expiring",
          "format": "datetime"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "out-of-scope": {
          "type": "boolean",
          "description": "Out of scope",
          "format": "boolean"
        },
        "percentage": {
          "type": "number",
          "description": "Tax Rate percentage",
          "format": "decimal(30,6)"
        },
        "reverse-charge": {
          "type": "boolean",
          "description": "Whether Tax Rate is Reverse Charge or not",
          "format": "boolean"
        },
        "tax-description": {
          "type": "string",
          "description": "Tax Rate Description",
          "format": "string(255)"
        },
        "tax-rate-type": {
          "$ref": "#/definitions/TaxRateType"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "percentage"
      ]
    },
    "TaxRateType": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean",
          "readOnly": true
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description of the tax rate type",
          "format": "string(255)"
        },
        "effective-date": {
          "type": "string",
          "description": "Effective date",
          "format": "datetime",
          "readOnly": true
        },
        "expiration-date": {
          "type": "string",
          "description": "Expiration date",
          "format": "datetime",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      }
    },
    "TaxRegistration": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Tax code is enabled or disabled",
          "format": "boolean"
        },
        "country": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "fiscal-representative": {
          "description": "Fiscal representative who is locally established and who is in general held jointly and severally liable with the tax payer for the payment of the vat to the tax authorities. Can be one of multiple objects: RemitToAddress, TaxRegistration",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "local": {
          "type": "boolean",
          "description": "True if tax registration cannot be used for cross-border invoices",
          "format": "boolean"
        },
        "number": {
          "type": "string",
          "description": "Tax Registration number",
          "format": "string(47)"
        },
        "owner-id": {
          "type": "integer",
          "description": "Coupa unique identifier of the object associated with this tax registration",
          "format": "integer"
        },
        "owner-type": {
          "type": "string",
          "description": "Type of the owning object",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "country",
        "number"
      ]
    },
    "TcsTaxLine": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "amount-engine": {
          "type": "number",
          "description": "Amount calculated by either Coupa Native or External Tax Engine based on configuration",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "base": {
          "type": "number",
          "description": "Base to Calculate Tax",
          "format": "decimal(30,4)"
        },
        "basis": {
          "type": "number",
          "description": "Supplier Withholding Base Suggestion",
          "format": "decimal(30,6)"
        },
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(255)",
          "readOnly": true
        },
        "code-engine": {
          "type": "string",
          "description": "Code returned by External Tax Engine based on configuration",
          "format": "string(255)",
          "readOnly": true
        },
        "code-id": {
          "type": "integer",
          "description": "code_id",
          "format": "integer"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Tax Reference",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer"
        },
        "kind-of-factor": {
          "type": "string",
          "description": "Kind of Factor",
          "format": "string(255)",
          "readOnly": true
        },
        "nature-of-tax": {
          "type": "string",
          "description": "Kind of Tax",
          "format": "string(255)"
        },
        "product-tax-classification": {
          "type": "string",
          "description": "Product Tax Classification",
          "format": "string(255)"
        },
        "rate": {
          "type": "number",
          "description": "rate",
          "format": "float"
        },
        "rate-engine": {
          "type": "number",
          "description": "Rate returned by External Tax Engine based on configuration",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "supplier-rate": {
          "type": "number",
          "description": "Supplier Withholding Rate Suggestion",
          "format": "decimal(30,4)"
        },
        "tax-code": {
          "$ref": "#/definitions/TaxCode"
        },
        "tax-rate": {
          "$ref": "#/definitions/TaxRate"
        },
        "tax-rate-type": {
          "$ref": "#/definitions/TaxRateType"
        },
        "taxable-amount": {
          "type": "number",
          "description": "Amount",
          "format": "decimal(32,4)"
        },
        "type": {
          "type": "string",
          "description": "WithholdingTaxLine, TcsTaxLine or TaxLine",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "withholding-amount": {
          "type": "number",
          "description": "Withholding Amount",
          "format": "decimal(30,4)"
        }
      }
    },
    "Uom": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean"
        },
        "allowable-precision": {
          "type": "integer",
          "description": "allowable_precision",
          "format": "integer"
        },
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(6)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(100)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "allowable-precision",
        "code",
        "name"
      ]
    },
    "User": {
      "type": "object",
      "properties": {
        "account-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AccountGroup"
          }
        },
        "account-security-type": {
          "type": "integer",
          "description": "account_security_type",
          "format": "integer"
        },
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean"
        },
        "aic-user": {
          "type": "boolean",
          "description": "Does the user have an AI Classification License?",
          "format": "boolean"
        },
        "allow-employee-payment-account-creation": {
          "type": "boolean",
          "description": "Allow the user to create an Employee Payment Account, regardless of the Employee Payment Channel.",
          "format": "boolean"
        },
        "analytics-user": {
          "type": "boolean",
          "description": "Does the user have an Analytics License?",
          "format": "boolean"
        },
        "api-user": {
          "type": "boolean",
          "description": "Is an API User?",
          "format": "boolean",
          "readOnly": true
        },
        "approval-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/UserGroup"
          }
        },
        "approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "authentication-method": {
          "type": "string",
          "description": "What Authentication Method will be used (Coupa_Credentials, LDAP, SAML)?",
          "format": "string(255)"
        },
        "avatar-thumb-url": {
          "type": "string",
          "description": "Avatar url",
          "format": "string",
          "readOnly": true
        },
        "business-function": {
          "type": "string",
          "description": "The employee's main job role in your company, e.g. Sales, Executive, Administrative, Managerial, etc.",
          "format": "string(255)"
        },
        "business-group-security-type": {
          "type": "integer",
          "description": "business_group_security_type",
          "format": "integer",
          "enum": [
            "0",
            "1"
          ]
        },
        "can-expense-for": {
          "$ref": "#/definitions/UserSimple"
        },
        "ccw-user": {
          "type": "boolean",
          "description": "Does the user have a Contingent Workforce License?",
          "format": "boolean"
        },
        "clm-advanced-user": {
          "type": "boolean",
          "description": "Does the user have a Contract Lifecycle Management Advanced License?",
          "format": "boolean"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "contract-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "contract-self-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "contracts-user": {
          "type": "boolean",
          "description": "Does the user have a Contracts License?",
          "format": "boolean"
        },
        "country-of-residence": {
          "$ref": "#/definitions/Country"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "default-account": {
          "$ref": "#/definitions/Account"
        },
        "default-account-type": {
          "$ref": "#/definitions/AccountType"
        },
        "default-address": {
          "$ref": "#/definitions/Address"
        },
        "default-currency": {
          "$ref": "#/definitions/Currency"
        },
        "default-locale": {
          "type": "string",
          "description": "Default locale",
          "format": "string(10)"
        },
        "department": {
          "$ref": "#/definitions/Department"
        },
        "edit-invoice-on-quick-entry": {
          "type": "boolean",
          "description": "Edit invoice button routes user to fast entry screen",
          "format": "boolean"
        },
        "email": {
          "type": "string",
          "description": "email",
          "format": "string(255)"
        },
        "employee-number": {
          "type": "string",
          "description": "employee number",
          "format": "string(255)"
        },
        "employee-payment-channel": {
          "type": "string",
          "description": "Determine how expenses will be paid to the employee. 'ERP' per default and can be switched to 'CoupaPay' if instance allows it.",
          "format": "string(255)"
        },
        "escalation-threshold": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "expense-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "expense-self-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "expense-user": {
          "type": "boolean",
          "description": "Does the user have a Expense License?",
          "format": "boolean"
        },
        "expenses-delegated-to": {
          "$ref": "#/definitions/UserSimple"
        },
        "firstname": {
          "type": "string",
          "description": "first name",
          "format": "string(40)"
        },
        "fullname": {
          "type": "string",
          "description": "full name",
          "format": "string(255)",
          "readOnly": true
        },
        "generate-password-and-notify": {
          "type": "string",
          "description": "Set to Yes if you want the system to invite the user to the system and have them set up their password",
          "format": "string",
          "enum": [
            "Yes",
            "No"
          ]
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "inventory-organizations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InventoryOrganization"
          }
        },
        "inventory-user": {
          "type": "boolean",
          "description": "Does the user have a Inventory License?",
          "format": "boolean"
        },
        "invoice-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "invoice-self-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "lastname": {
          "type": "string",
          "description": "last name",
          "format": "string(40)"
        },
        "legal-entity": {
          "$ref": "#/definitions/LegalEntity"
        },
        "login": {
          "type": "string",
          "description": "login",
          "format": "string(255)"
        },
        "manager": {
          "$ref": "#/definitions/UserSimple"
        },
        "mention-name": {
          "type": "string",
          "description": "Mention Name",
          "format": "string(255)"
        },
        "middlename": {
          "type": "string",
          "description": "middle name",
          "format": "string(255)"
        },
        "password": {
          "type": "string",
          "description": "Changed password",
          "format": "string"
        },
        "pcard": {
          "$ref": "#/definitions/Pcard"
        },
        "phone-mobile": {
          "$ref": "#/definitions/PhoneNumber"
        },
        "phone-work": {
          "$ref": "#/definitions/PhoneNumber"
        },
        "purchasing-user": {
          "type": "boolean",
          "description": "Does the user have a Purchasing License?",
          "format": "boolean"
        },
        "requisition-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "requisition-self-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "risk-assess-user": {
          "type": "boolean",
          "description": "Does the user have a Risk Assess License?",
          "format": "boolean"
        },
        "roles": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Role"
          }
        },
        "salesforce-enabled": {
          "type": "boolean",
          "description": "salesforce_enabled",
          "format": "boolean"
        },
        "salesforce-id": {
          "type": "string",
          "description": "salesforce_id",
          "format": "string(255)"
        },
        "self-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "seniority-level": {
          "type": "string",
          "description": "The employee's job grade or band in your company's hierarchy.",
          "format": "string(255)"
        },
        "sourcing-user": {
          "type": "boolean",
          "description": "Does the user have a Sourcing License?",
          "format": "boolean"
        },
        "spend-guard-user": {
          "type": "boolean",
          "description": "Does the user have a Spend Guard License?",
          "format": "boolean"
        },
        "sso-identifier": {
          "type": "string",
          "description": "User's Single Sign-on ID (SSO ID)",
          "format": "string(255)"
        },
        "supply-chain-user": {
          "type": "boolean",
          "description": "Does the user have a Supply Chain License?",
          "format": "boolean"
        },
        "travel-user": {
          "type": "boolean",
          "description": "Does the user have a Travel License?",
          "format": "boolean"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "user-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/UserGroup"
          }
        },
        "work-confirmation-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "working-warehouses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Warehouse"
          }
        }
      },
      "required": [
        "email",
        "firstname",
        "lastname",
        "login",
        "salesforce-id"
      ]
    },
    "UserGroup": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean"
        },
        "can-approve": {
          "type": "boolean",
          "description": "User group has the ability to be an approver",
          "format": "boolean"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Description",
          "format": "text"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "mention-name": {
          "type": "string",
          "description": "Mention name",
          "format": "string(255)",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "open": {
          "type": "boolean",
          "description": "User group is open for everyone to join or owner must invite others",
          "format": "boolean"
        },
        "owner": {
          "$ref": "#/definitions/UserGroup"
        },
        "type": {
          "type": "string",
          "description": "Blank for Groups, Project for Projects",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "users": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/UserSimple"
          }
        }
      },
      "required": [
        "name"
      ]
    },
    "UserSimple": {
      "type": "object",
      "properties": {
        "account-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/AccountGroup"
          }
        },
        "account-security-type": {
          "type": "integer",
          "description": "account_security_type",
          "format": "integer"
        },
        "active": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean"
        },
        "aic-user": {
          "type": "boolean",
          "description": "Does the user have an AI Classification License?",
          "format": "boolean"
        },
        "allow-employee-payment-account-creation": {
          "type": "boolean",
          "description": "Allow the user to create an Employee Payment Account, regardless of the Employee Payment Channel.",
          "format": "boolean"
        },
        "analytics-user": {
          "type": "boolean",
          "description": "Does the user have an Analytics License?",
          "format": "boolean"
        },
        "api-user": {
          "type": "boolean",
          "description": "Is an API User?",
          "format": "boolean",
          "readOnly": true
        },
        "approval-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/UserGroup"
          }
        },
        "authentication-method": {
          "type": "string",
          "description": "What Authentication Method will be used (Coupa_Credentials, LDAP, SAML)?",
          "format": "string(255)"
        },
        "avatar-thumb-url": {
          "type": "string",
          "description": "Avatar url",
          "format": "string",
          "readOnly": true
        },
        "business-function": {
          "type": "string",
          "description": "The employee's main job role in your company, e.g. Sales, Executive, Administrative, Managerial, etc.",
          "format": "string(255)"
        },
        "business-group-security-type": {
          "type": "integer",
          "description": "business_group_security_type",
          "format": "integer",
          "enum": [
            "0",
            "1"
          ]
        },
        "ccw-user": {
          "type": "boolean",
          "description": "Does the user have a Contingent Workforce License?",
          "format": "boolean"
        },
        "clm-advanced-user": {
          "type": "boolean",
          "description": "Does the user have a Contract Lifecycle Management Advanced License?",
          "format": "boolean"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "contracts-user": {
          "type": "boolean",
          "description": "Does the user have a Contracts License?",
          "format": "boolean"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "default-locale": {
          "type": "string",
          "description": "Default locale",
          "format": "string(10)"
        },
        "edit-invoice-on-quick-entry": {
          "type": "boolean",
          "description": "Edit invoice button routes user to fast entry screen",
          "format": "boolean"
        },
        "email": {
          "type": "string",
          "description": "email",
          "format": "string(255)"
        },
        "employee-number": {
          "type": "string",
          "description": "employee number",
          "format": "string(255)"
        },
        "employee-payment-channel": {
          "type": "string",
          "description": "Determine how expenses will be paid to the employee. 'ERP' per default and can be switched to 'CoupaPay' if instance allows it.",
          "format": "string(255)"
        },
        "expense-user": {
          "type": "boolean",
          "description": "Does the user have a Expense License?",
          "format": "boolean"
        },
        "firstname": {
          "type": "string",
          "description": "first name",
          "format": "string(40)"
        },
        "fullname": {
          "type": "string",
          "description": "full name",
          "format": "string(255)",
          "readOnly": true
        },
        "generate-password-and-notify": {
          "type": "string",
          "description": "Set to Yes if you want the system to invite the user to the system and have them set up their password",
          "format": "string",
          "enum": [
            "Yes",
            "No"
          ]
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "inventory-organizations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InventoryOrganization"
          }
        },
        "inventory-user": {
          "type": "boolean",
          "description": "Does the user have a Inventory License?",
          "format": "boolean"
        },
        "lastname": {
          "type": "string",
          "description": "last name",
          "format": "string(40)"
        },
        "login": {
          "type": "string",
          "description": "login",
          "format": "string(255)"
        },
        "mention-name": {
          "type": "string",
          "description": "Mention Name",
          "format": "string(255)"
        },
        "middlename": {
          "type": "string",
          "description": "middle name",
          "format": "string(255)"
        },
        "password": {
          "type": "string",
          "description": "Changed password",
          "format": "string"
        },
        "purchasing-user": {
          "type": "boolean",
          "description": "Does the user have a Purchasing License?",
          "format": "boolean"
        },
        "risk-assess-user": {
          "type": "boolean",
          "description": "Does the user have a Risk Assess License?",
          "format": "boolean"
        },
        "roles": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Role"
          }
        },
        "salesforce-enabled": {
          "type": "boolean",
          "description": "salesforce_enabled",
          "format": "boolean"
        },
        "salesforce-id": {
          "type": "string",
          "description": "salesforce_id",
          "format": "string(255)"
        },
        "seniority-level": {
          "type": "string",
          "description": "The employee's job grade or band in your company's hierarchy.",
          "format": "string(255)"
        },
        "sourcing-user": {
          "type": "boolean",
          "description": "Does the user have a Sourcing License?",
          "format": "boolean"
        },
        "spend-guard-user": {
          "type": "boolean",
          "description": "Does the user have a Spend Guard License?",
          "format": "boolean"
        },
        "sso-identifier": {
          "type": "string",
          "description": "User's Single Sign-on ID (SSO ID)",
          "format": "string(255)"
        },
        "supply-chain-user": {
          "type": "boolean",
          "description": "Does the user have a Supply Chain License?",
          "format": "boolean"
        },
        "travel-user": {
          "type": "boolean",
          "description": "Does the user have a Travel License?",
          "format": "boolean"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "user-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/UserGroup"
          }
        },
        "working-warehouses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Warehouse"
          }
        }
      },
      "required": [
        "email",
        "firstname",
        "lastname",
        "login",
        "salesforce-id"
      ]
    },
    "Warehouse": {
      "type": "object",
      "properties": {
        "active-flag": {
          "type": "boolean",
          "description": "active_flag",
          "format": "boolean"
        },
        "address": {
          "$ref": "#/definitions/Address"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "warehouse-locations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/WarehouseLocation"
          }
        },
        "warehouse-type": {
          "$ref": "#/definitions/WarehouseType"
        }
      },
      "required": [
        "address",
        "currency",
        "description",
        "name",
        "warehouse-type"
      ]
    },
    "WarehouseLocation": {
      "type": "object",
      "properties": {
        "aisle": {
          "type": "string",
          "description": "aisle",
          "format": "string(255)"
        },
        "bin": {
          "type": "string",
          "description": "bin",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "level": {
          "type": "string",
          "description": "level",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "warehouse-id": {
          "type": "integer",
          "description": "Warehouse",
          "format": "integer",
          "readOnly": true
        },
        "warehouse-name": {
          "type": "string",
          "description": "Warehouse name",
          "readOnly": true
        }
      }
    },
    "WarehouseType": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "description",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "name": {
          "type": "string",
          "description": "name",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "description",
        "name"
      ]
    },
    "WithholdingTaxLine": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "number",
          "description": "amount",
          "format": "decimal(32,4)"
        },
        "amount-engine": {
          "type": "number",
          "description": "Amount calculated by either Coupa Native or External Tax Engine based on configuration",
          "format": "decimal(32,4)",
          "readOnly": true
        },
        "base": {
          "type": "number",
          "description": "Base to Calculate Tax",
          "format": "decimal(30,4)"
        },
        "basis": {
          "type": "number",
          "description": "Supplier Withholding Base Suggestion",
          "format": "decimal(30,6)"
        },
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(255)",
          "readOnly": true
        },
        "code-engine": {
          "type": "string",
          "description": "Code returned by External Tax Engine based on configuration",
          "format": "string(255)",
          "readOnly": true
        },
        "code-id": {
          "type": "integer",
          "description": "code_id",
          "format": "integer"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "description": {
          "type": "string",
          "description": "Tax Reference",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer"
        },
        "kind-of-factor": {
          "type": "string",
          "description": "Kind of Factor",
          "format": "string(255)",
          "readOnly": true
        },
        "nature-of-tax": {
          "type": "string",
          "description": "Kind of Tax",
          "format": "string(255)"
        },
        "product-tax-classification": {
          "type": "string",
          "description": "Product Tax Classification",
          "format": "string(255)"
        },
        "rate": {
          "type": "number",
          "description": "rate",
          "format": "float"
        },
        "rate-engine": {
          "type": "number",
          "description": "Rate returned by External Tax Engine based on configuration",
          "format": "decimal(30,6)",
          "readOnly": true
        },
        "supplier-rate": {
          "type": "number",
          "description": "Supplier Withholding Rate Suggestion",
          "format": "decimal(30,4)"
        },
        "tax-code": {
          "$ref": "#/definitions/TaxCode"
        },
        "tax-rate": {
          "$ref": "#/definitions/TaxRate"
        },
        "tax-rate-type": {
          "$ref": "#/definitions/TaxRateType"
        },
        "taxable-amount": {
          "type": "number",
          "description": "Amount",
          "format": "decimal(32,4)"
        },
        "type": {
          "type": "string",
          "description": "WithholdingTaxLine, TcsTaxLine or TaxLine",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "withholding-amount": {
          "type": "number",
          "description": "Withholding Amount",
          "format": "decimal(30,4)"
        }
      }
    }
  }
}
```
