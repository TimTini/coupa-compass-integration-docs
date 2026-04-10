---
title: "R39_Supply_Chain_API.json"
url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/R39/R39_Supply_Chain_API.json"
final_url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/R39/R39_Supply_Chain_API.json"
content_type: "application/json"
classification: "json_asset"
fetched_at: "2026-04-10T01:56:25+00:00"
---

# R39_Supply_Chain_API.json

```json
{
  "swagger": "2.0",
  "info": {
    "version": "",
    "title": "Coupa API",
    "description": "RESTful API that provides robust access to read, edit, or integrate your data with the Coupa platform. The [JSON](/api_docs/26.json) and [YAML](/api_docs/26.yaml) are also available.  To test with OAuth2 OAuth2AccessCode, make sure to include https://r39.coupadev.com/oauth2-redirect.html in the client's Redirect URI list"
  },
  "host": "r39.coupadev.com",
  "basePath": "/api",
  "tags": [
    {
      "name": "OrderHeaderConfirmation",
      "description": "Order Confirmations API"
    }
  ],
  "schemes": [
    "https"
  ],
  "security": [
    {
      "OAuth2AccessCode": []
    },
    {
      "OAuth2ClientCredential": []
    }
  ],
  "paths": {
    "/order_header_confirmations": {
      "get": {
        "tags": [
          "OrderHeaderConfirmation"
        ],
        "summary": "Query order confirmations",
        "description": "Query order confirmations",
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
            "description": "OrderHeaderConfirmation objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/OrderHeaderConfirmation"
              },
              "xml": {
                "name": "order-header-confirmations",
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
    "/order_header_confirmations/{id}": {
      "get": {
        "tags": [
          "OrderHeaderConfirmation"
        ],
        "summary": "Show order confirmation",
        "description": "Show order confirmation",
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
            "description": "OrderHeaderConfirmation object",
            "schema": {
              "$ref": "#/definitions/OrderHeaderConfirmation"
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
          "OrderHeaderConfirmation"
        ],
        "summary": "Update order confirmation",
        "description": "Update order confirmation",
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
            "name": "OrderHeaderConfirmation",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeaderConfirmation"
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
            "description": "OrderHeaderConfirmation object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeaderConfirmation"
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
          "OrderHeaderConfirmation"
        ],
        "summary": "Update order confirmation",
        "description": "Update order confirmation",
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
            "name": "OrderHeaderConfirmation",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/OrderHeaderConfirmation"
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
            "description": "OrderHeaderConfirmation object",
            "schema": {
              "items": {
                "$ref": "#/definitions/OrderHeaderConfirmation"
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
    "OAuth2ClientCredential": {
      "type": "oauth2",
      "flow": "application",
      "tokenUrl": "https://r39.coupadev.com/oauth2/access_tokens",
      "scopes": {
        "core.order_header_confirmations.read": "Allows to view order header confirmations",
        "core.order_header_confirmations.write": "Allows to create or modify order header confirmations"
      }
    },
    "OAuth2AccessCode": {
      "type": "oauth2",
      "flow": "accessCode",
      "authorizationUrl": "https://r39.coupadev.com/oauth2/authorizations/new",
      "tokenUrl": "https://r39.coupadev.com/oauth2/token",
      "scopes": {
        "core.order_header_confirmations.read": "Allows to view order header confirmations",
        "core.order_header_confirmations.write": "Allows to create or modify order header confirmations"
      }
    }
  },
  "definitions": {
    "Account": {
      "type": "object",
      "properties": {
        "account-type": {
          "$ref": "#/definitions/AccountType"
        },
        "account-type-id": {
          "type": "integer",
          "description": "Account Type Id",
          "format": "integer",
          "readOnly": true
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
        "account-group-type": {
          "type": "integer",
          "description": "Type",
          "format": "integer",
          "enum": [
            "1",
            "2"
          ]
        },
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
        "account-group-type",
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
          "format": "string(255)"
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
        "external-src-name": {
          "type": "string",
          "description": "External Source Name",
          "format": "string(255)"
        },
        "external-src-ref": {
          "type": "string",
          "description": "External Source Reference",
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
          "format": "string(255)"
        },
        "purposes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Purpose"
          }
        },
        "state": {
          "type": "string",
          "description": "State Name for Address",
          "format": "string(255)"
        },
        "state-iso-code": {
          "type": "string",
          "description": "ISO Code for the State",
          "format": "string(255)"
        },
        "street1": {
          "type": "string",
          "description": "Address Line 1",
          "format": "string(255)"
        },
        "street2": {
          "type": "string",
          "description": "Address Line 2",
          "format": "string(255)"
        },
        "street3": {
          "type": "string",
          "description": "Address Line 3",
          "format": "string(255)"
        },
        "street4": {
          "type": "string",
          "description": "Address Line 4",
          "format": "string(255)"
        },
        "tax-registrations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Address"
          }
        },
        "type": {
          "type": "string",
          "description": "Address type",
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
    "BillToAddress": {
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
          "format": "string(255)"
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
        "external-src-name": {
          "type": "string",
          "description": "External Source Name",
          "format": "string(255)"
        },
        "external-src-ref": {
          "type": "string",
          "description": "External Source Reference",
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
          "format": "string(10)"
        },
        "purposes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Purpose"
          }
        },
        "state": {
          "type": "string",
          "description": "State Name for Address",
          "format": "string(255)"
        },
        "state-iso-code": {
          "type": "string",
          "description": "ISO Code for the State",
          "format": "string(255)"
        },
        "street1": {
          "type": "string",
          "description": "Address Line 1",
          "format": "string(255)"
        },
        "street2": {
          "type": "string",
          "description": "Address Line 2",
          "format": "string(255)"
        },
        "street3": {
          "type": "string",
          "description": "Address Line 3",
          "format": "string(255)"
        },
        "street4": {
          "type": "string",
          "description": "Address Line 4",
          "format": "string(255)"
        },
        "tax-registrations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Address"
          }
        },
        "type": {
          "type": "string",
          "description": "Address type",
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
    "Contact": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean",
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
          "format": "string(255)"
        },
        "name-family": {
          "type": "string",
          "description": "name_family",
          "format": "string(255)"
        },
        "name-fullname": {
          "type": "string",
          "description": "name_fullname",
          "format": "string(255)",
          "readOnly": true
        },
        "name-given": {
          "type": "string",
          "description": "name_given",
          "format": "string(255)"
        },
        "name-prefix": {
          "type": "string",
          "description": "name_prefix",
          "format": "string(255)"
        },
        "name-suffix": {
          "type": "string",
          "description": "name_suffix",
          "format": "string(255)"
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
    "Country": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string",
          "description": "code",
          "format": "string(4)"
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
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
        "translated-name": {
          "type": "string",
          "description": "Translated name",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "readOnly": true
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
        }
      },
      "required": [
        "code",
        "name"
      ]
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
    "LegalEntity": {
      "type": "object",
      "properties": {
        "abbreviation": {
          "type": "string",
          "description": "Abbreviation",
          "format": "string(50)"
        },
        "accounting-method": {
          "type": "string",
          "description": "Accounting Method",
          "format": "string(7)",
          "enum": [
            "ifrs",
            "ifrs_9",
            "us_gaap"
          ]
        },
        "active": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean"
        },
        "bill-to-address": {
          "$ref": "#/definitions/BillToAddress"
        },
        "bill-to-addresses": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BillToAddress"
          }
        },
        "corporate-sector": {
          "type": "string",
          "description": "Corporate Sector",
          "format": "string(16)"
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
          "format": "string(500)"
        },
        "external-identification-company-code": {
          "type": "string",
          "description": "Company Code",
          "format": "string(11)"
        },
        "external-identification-creditor-id": {
          "type": "string",
          "description": "SEPA Creditor ID",
          "format": "string(35)"
        },
        "external-identification-ic-identifier-gl": {
          "type": "string",
          "description": "IC Identifier for GL Exports",
          "format": "string(50)"
        },
        "external-identification-lei": {
          "type": "string",
          "description": "Legal Entity Identifier",
          "format": "string(20)"
        },
        "external-identification-name-matching": {
          "type": "string",
          "description": "Deviating Name Matching",
          "format": "string(100)"
        },
        "external-identification-name-trading": {
          "type": "string",
          "description": "Deviating Name Trading",
          "format": "string(100)"
        },
        "external-identification-swift": {
          "type": "string",
          "description": "Deviating SWIFT Code",
          "format": "string(11)"
        },
        "id": {
          "type": "integer",
          "description": "Coupa Internal ID",
          "format": "integer",
          "readOnly": true
        },
        "legal-entity-address": {
          "$ref": "#/definitions/LegalEntityAddress"
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "parent": {
          "$ref": "#/definitions/LegalEntity"
        },
        "swift-code": {
          "type": "string",
          "description": "SWIFT Code",
          "format": "string(11)"
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
        "use-fx-rates-reciprocal": {
          "type": "boolean",
          "description": "Use FX rates reciprocal",
          "format": "boolean"
        }
      },
      "required": [
        "abbreviation",
        "currency",
        "name"
      ]
    },
    "LegalEntityAddress": {
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
          "format": "string(255)"
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
        "external-src-name": {
          "type": "string",
          "description": "External Source Name",
          "format": "string(255)"
        },
        "external-src-ref": {
          "type": "string",
          "description": "External Source Reference",
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
          "format": "string(10)"
        },
        "purposes": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Purpose"
          }
        },
        "state": {
          "type": "string",
          "description": "State Name for Address",
          "format": "string(255)"
        },
        "state-iso-code": {
          "type": "string",
          "description": "ISO Code for the State",
          "format": "string(255)"
        },
        "street1": {
          "type": "string",
          "description": "Address Line 1",
          "format": "string(255)"
        },
        "street2": {
          "type": "string",
          "description": "Address Line 2",
          "format": "string(255)"
        },
        "street3": {
          "type": "string",
          "description": "Address Line 3",
          "format": "string(255)"
        },
        "street4": {
          "type": "string",
          "description": "Address Line 4",
          "format": "string(255)"
        },
        "tax-registrations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Address"
          }
        },
        "type": {
          "type": "string",
          "description": "Address type",
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
    "OrderHeaderConfirmation": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Date record was created in Coupa.",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "exported": {
          "type": "boolean",
          "description": "Indicates if transaction has been exported",
          "format": "boolean",
          "readOnly": true
        },
        "external-reference-number": {
          "type": "string",
          "description": "External Reference Number",
          "format": "string(255)",
          "readOnly": true
        },
        "id": {
          "type": "integer",
          "description": "Coupa's internal ID",
          "format": "integer"
        },
        "integration-message": {
          "type": "string",
          "description": "Integration Message",
          "format": "text"
        },
        "last-exported-at": {
          "type": "string",
          "description": "Last Exported at Date",
          "format": "datetime",
          "readOnly": true
        },
        "order-header": {
          "$ref": "#/definitions/OrderHeaderConfirmation"
        },
        "order-line-confirmations": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrderLineConfirmation"
          }
        },
        "reason-insight-events": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ReasonInsightEvent"
          }
        },
        "status": {
          "type": "string",
          "description": "Order Confirmation Status",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Last Updated at Date",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "integration-message"
      ]
    },
    "OrderLineConfirmation": {
      "type": "object",
      "properties": {
        "acted-on-behalf-of-supplier": {
          "type": "boolean",
          "description": "Acted on behalf of supplier",
          "format": "boolean",
          "readOnly": true
        },
        "action": {
          "type": "string",
          "description": "Action"
        },
        "can-fulfill": {
          "type": "integer",
          "description": "Can fulfill",
          "format": "integer",
          "readOnly": true
        },
        "confirm-by-hrs": {
          "type": "number",
          "description": "Confirm by hrs",
          "format": "decimal(10,0)",
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
          "$ref": "#/definitions/OrderLineConfirmation"
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
        "item-change": {
          "type": "boolean",
          "description": "Item change",
          "format": "boolean",
          "readOnly": true
        },
        "item-record-match-found": {
          "type": "string",
          "description": "Item record match found",
          "readOnly": true
        },
        "line-num": {
          "type": "string",
          "description": "Line num",
          "readOnly": true
        },
        "manufacturer-name": {
          "type": "string",
          "description": "Manufacturer name",
          "format": "string(255)",
          "readOnly": true
        },
        "manufacturer-part-number": {
          "type": "string",
          "description": "Manufacturer part number",
          "format": "string(255)",
          "readOnly": true
        },
        "order-line": {
          "$ref": "#/definitions/OrderLineConfirmation"
        },
        "price": {
          "type": "number",
          "description": "Price",
          "format": "decimal(30,6)"
        },
        "promised-date": {
          "type": "string",
          "description": "Promised date",
          "format": "datetime",
          "readOnly": true
        },
        "promised-deliveries": {
          "type": "integer",
          "description": "Promised deliveries",
          "format": "integer",
          "readOnly": true
        },
        "quantity": {
          "type": "number",
          "description": "Quantity",
          "format": "decimal(30,6)"
        },
        "reason-insight-events": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/ReasonInsightEvent"
          }
        },
        "schedule-lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrderLineConfirmation"
          }
        },
        "source-part-num": {
          "type": "string",
          "description": "Source part num",
          "format": "string(255)",
          "readOnly": true
        },
        "status": {
          "type": "string",
          "description": "Status",
          "format": "string(255)",
          "readOnly": true
        },
        "supp-aux-part-num": {
          "type": "string",
          "description": "Supp aux part num",
          "format": "string(255)",
          "readOnly": true
        },
        "uom": {
          "$ref": "#/definitions/OrderLineConfirmation"
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
        "price",
        "quantity",
        "uom"
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
    "Purpose": {
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
        "kind": {
          "type": "string",
          "description": "Kind",
          "format": "string(255)"
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
        "kind",
        "name"
      ]
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
        },
        "user-avatar-url": {
          "type": "string",
          "description": "User avatar url",
          "readOnly": true
        },
        "user-full-name": {
          "type": "string",
          "description": "User full name",
          "readOnly": true
        }
      },
      "required": [
        "comment",
        "reason-insight"
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
        "active?": {
          "type": "boolean",
          "description": "A false value will inactivate the account making it no longer available to users.  A true value will make it active and available to users.",
          "format": "boolean",
          "readOnly": true
        },
        "aic-user": {
          "type": "boolean",
          "description": "Does the user have an AI Classification License?",
          "format": "boolean"
        },
        "aic-user?": {
          "type": "boolean",
          "description": "Does the user have an AI Classification License?",
          "format": "boolean",
          "readOnly": true
        },
        "allow-employee-payment-account-creation": {
          "type": "boolean",
          "description": "Allow the user to create an Employee Payment Account, regardless of the Employee Payment Channel.",
          "format": "boolean"
        },
        "allow-user-to-upload-invoice-from-mobile": {
          "type": "boolean",
          "description": "Allow user to upload Invoice images from Coupa Mobile to Invoice Inbox",
          "format": "boolean"
        },
        "allowed-invoice-inboxes": {
          "type": "string",
          "description": "Invoice inboxes that mobile user allowed to send invoice to",
          "format": "text",
          "readOnly": true
        },
        "analytics-user": {
          "type": "boolean",
          "description": "Does the user have an Analytics License?",
          "format": "boolean"
        },
        "analytics-user?": {
          "type": "boolean",
          "description": "Does the user have an Analytics License?",
          "format": "boolean",
          "readOnly": true
        },
        "api-user": {
          "type": "boolean",
          "description": "Is an API User?",
          "format": "boolean",
          "readOnly": true
        },
        "api-user?": {
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
        "category-planner-user": {
          "type": "boolean",
          "description": "Category Planner User",
          "format": "boolean",
          "readOnly": true
        },
        "category-planner-user?": {
          "type": "boolean",
          "description": "Does the user have a Category Planner License?",
          "format": "boolean",
          "readOnly": true
        },
        "ccw-user": {
          "type": "boolean",
          "description": "Does the user have a Contingent Workforce License?",
          "format": "boolean"
        },
        "ccw-user?": {
          "type": "boolean",
          "description": "Does the user have a Contingent Workforce License?",
          "format": "boolean",
          "readOnly": true
        },
        "clm-advanced-user": {
          "type": "boolean",
          "description": "Does the user have a Contract Lifecycle Management Advanced License?",
          "format": "boolean"
        },
        "clm-advanced-user?": {
          "type": "boolean",
          "description": "Does the user have a Contract Lifecycle Management Advanced License?",
          "format": "boolean",
          "readOnly": true
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
        "contracts-user?": {
          "type": "boolean",
          "description": "Does the user have a Contracts License?",
          "format": "boolean",
          "readOnly": true
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
        "eligible-for-virtual-cards": {
          "type": "boolean",
          "description": "Is the user eligible to manage their virtual cards?",
          "format": "boolean",
          "readOnly": true
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
        "expense-user?": {
          "type": "boolean",
          "description": "Does the user have a Expense License?",
          "format": "boolean",
          "readOnly": true
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
        "inventory-user?": {
          "type": "boolean",
          "description": "Does the user have a Inventory License?",
          "format": "boolean",
          "readOnly": true
        },
        "invoice-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "invoice-self-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "invoicing-user": {
          "type": "boolean",
          "description": "Does the user have a Invoicing License?",
          "format": "boolean"
        },
        "invoicing-user?": {
          "type": "boolean",
          "description": "Does the user have a Invoicing License?",
          "format": "boolean",
          "readOnly": true
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
        "msp-user": {
          "type": "boolean",
          "description": "Boolean flag to tell if the user is of MSP type",
          "format": "boolean",
          "readOnly": true
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
        "purchasing-user?": {
          "type": "boolean",
          "description": "Does the user have a Purchasing License?",
          "format": "boolean",
          "readOnly": true
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
        "sourcing-user?": {
          "type": "boolean",
          "description": "Does the user have a Sourcing License?",
          "format": "boolean",
          "readOnly": true
        },
        "spend-guard-user": {
          "type": "boolean",
          "description": "Does the user have a Spend Guard License?",
          "format": "boolean"
        },
        "spend-guard-user?": {
          "type": "boolean",
          "description": "Does the user have a Spend Guard License?",
          "format": "boolean",
          "readOnly": true
        },
        "sso-identifier": {
          "type": "string",
          "description": "User's Single Sign-on ID (SSO ID)",
          "format": "string(255)"
        },
        "supplier-id": {
          "type": "integer",
          "description": "Supplier Id",
          "format": "integer",
          "readOnly": true
        },
        "supplier-user": {
          "type": "boolean",
          "description": "Supplier User",
          "format": "boolean",
          "readOnly": true
        },
        "supply-chain-user": {
          "type": "boolean",
          "description": "Does the user have a Supply Chain License?",
          "format": "boolean"
        },
        "supply-chain-user?": {
          "type": "boolean",
          "description": "Does the user have a Supply Chain License?",
          "format": "boolean",
          "readOnly": true
        },
        "support-user": {
          "type": "boolean",
          "description": "Support User",
          "format": "boolean",
          "readOnly": true
        },
        "travel-user": {
          "type": "boolean",
          "description": "Does the user have a Travel License?",
          "format": "boolean"
        },
        "travel-user?": {
          "type": "boolean",
          "description": "Does the user have a Travel License?",
          "format": "boolean",
          "readOnly": true
        },
        "treasury-user": {
          "type": "boolean",
          "description": "Does the user have a Treasury License?",
          "format": "boolean"
        },
        "treasury-user?": {
          "type": "boolean",
          "description": "Does the user have a Treasury License?",
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
        "avatar-thumb-url": {
          "type": "string",
          "description": "URL for avatar thumbnail",
          "format": "string",
          "readOnly": true
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
        "avatar-thumb-url": {
          "type": "string",
          "description": "Avatar url",
          "format": "string",
          "readOnly": true
        },
        "created-at": {
          "type": "string",
          "description": "Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ",
          "format": "datetime",
          "readOnly": true
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
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
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
        "salesforce-id": {
          "type": "string",
          "description": "salesforce_id",
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
        "active": {
          "type": "boolean",
          "description": "Active",
          "format": "boolean"
        },
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
        "label": {
          "type": "string",
          "description": "Display label",
          "format": "string",
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
          "description": "Warehouse Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "warehouse-name": {
          "type": "string",
          "description": "Warehouse name",
          "format": "string",
          "readOnly": true
        }
      },
      "required": [
        "aisle"
      ]
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
    }
  }
}
```
