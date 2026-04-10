---
title: "R26_Sourcing_API.json"
url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/R26/R26_Sourcing_API.json"
final_url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/R26/R26_Sourcing_API.json"
content_type: "application/json"
classification: "json_asset"
fetched_at: "2026-04-10T01:55:54+00:00"
---

# R26_Sourcing_API.json

```json
{
  "swagger": "2.0",
  "info": {
    "version": "",
    "title": "Coupa API",
    "description": "RESTful API that provides robust access to read, edit, or integrate your data with the Coupa platform. The [JSON](/api_docs/3.json) and [YAML](/api_docs/3.yaml) are also available."
  },
  "host": "r26.coupadev.com",
  "basePath": "/api",
  "tags": [
    {
      "name": "QuoteRequest",
      "description": "QuoteRequests API"
    },
    {
      "name": "QuoteResponse",
      "description": "QuoteResponses API"
    },
    {
      "name": "QuoteSupplier",
      "description": "QuoteSuppliers API"
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
    "/quote_requests/{id}/go_to_production": {
      "patch": {
        "tags": [
          "QuoteRequest"
        ],
        "summary": "Submit event to production",
        "description": "Submit event to production",
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
            "name": "QuoteRequest",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/QuoteRequest"
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
            "description": "QuoteRequest object",
            "schema": {
              "items": {
                "$ref": "#/definitions/QuoteRequest"
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
    "/quote_requests/{id}/go_to_test": {
      "patch": {
        "tags": [
          "QuoteRequest"
        ],
        "summary": "Submit event to production as tests event",
        "description": "Submit event to production as tests event",
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
            "name": "QuoteRequest",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/QuoteRequest"
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
            "description": "QuoteRequest object",
            "schema": {
              "items": {
                "$ref": "#/definitions/QuoteRequest"
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
    "/quote_requests/{id}/end_event": {
      "patch": {
        "tags": [
          "QuoteRequest"
        ],
        "summary": "End production event",
        "description": "End production event",
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
            "name": "QuoteRequest",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/QuoteRequest"
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
            "description": "QuoteRequest object",
            "schema": {
              "items": {
                "$ref": "#/definitions/QuoteRequest"
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
    "/quote_requests/create_from_source": {
      "post": {
        "tags": [
          "QuoteRequest"
        ],
        "summary": "Create Sourcing event from Requisition, Contract, Catalog, Order pad, Order lines, Invoice lines and items",
        "description": "Create Sourcing event from Requisition, Contract, Catalog, Order pad, Order lines, Invoice lines and items",
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
            "name": "QuoteRequest",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/QuoteRequest"
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
              "$ref": "#/definitions/QuoteRequest"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/quote_requests/{quote_request_id}/quote_responses": {
      "get": {
        "tags": [
          "QuoteResponse"
        ],
        "summary": "Get all responses of specific Sourcing event",
        "description": "Get all responses of specific Sourcing event",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "quote_request_id",
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
            "description": "QuoteResponse objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/QuoteResponse"
              },
              "xml": {
                "name": "quote-responses",
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
    "/quote_requests": {
      "get": {
        "tags": [
          "QuoteRequest"
        ],
        "summary": "Returns all Sourcing events",
        "description": "Returns all Sourcing events",
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
            "description": "QuoteRequest objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/QuoteRequest"
              },
              "xml": {
                "name": "quote-requests",
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
          "QuoteRequest"
        ],
        "summary": "Create a Sourcing event",
        "description": "Create a Sourcing event",
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
            "name": "QuoteRequest",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/QuoteRequest"
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
              "$ref": "#/definitions/QuoteRequest"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/quote_requests/{id}": {
      "get": {
        "tags": [
          "QuoteRequest"
        ],
        "summary": "Get information about the particular event",
        "description": "Get information about the particular event",
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
            "description": "QuoteRequest object",
            "schema": {
              "$ref": "#/definitions/QuoteRequest"
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
          "QuoteRequest"
        ],
        "summary": "Update a Sourcing event",
        "description": "Update a Sourcing event",
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
            "name": "QuoteRequest",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/QuoteRequest"
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
            "description": "QuoteRequest object",
            "schema": {
              "items": {
                "$ref": "#/definitions/QuoteRequest"
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
          "QuoteRequest"
        ],
        "summary": "Update a Sourcing event",
        "description": "Update a Sourcing event",
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
            "name": "QuoteRequest",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/QuoteRequest"
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
            "description": "QuoteRequest object",
            "schema": {
              "items": {
                "$ref": "#/definitions/QuoteRequest"
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
    "/quote_suppliers/{id}": {
      "get": {
        "tags": [
          "QuoteSupplier"
        ],
        "summary": "Get information about the quote supplier",
        "description": "Get information about the quote supplier",
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
            "description": "QuoteSupplier object",
            "schema": {
              "$ref": "#/definitions/QuoteSupplier"
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
    "/quote_responses/{id}/award": {
      "post": {
        "tags": [
          "QuoteResponse"
        ],
        "summary": "Award the quote response",
        "description": "Award the quote response",
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
            "name": "QuoteResponse",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/QuoteResponse"
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
              "$ref": "#/definitions/QuoteResponse"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      },
      "delete": {
        "tags": [
          "QuoteResponse"
        ],
        "summary": "Remove award from the quote response",
        "description": "Remove award from the quote response",
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
    "/quote_responses": {
      "get": {
        "tags": [
          "QuoteResponse"
        ],
        "summary": "Get all responses of specific Sourcing event",
        "description": "Get all responses of specific Sourcing event",
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
            "description": "QuoteResponse objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/QuoteResponse"
              },
              "xml": {
                "name": "quote-responses",
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
    "/quote_responses/{id}": {
      "get": {
        "tags": [
          "QuoteResponse"
        ],
        "summary": "Get information about the particular response",
        "description": "Get information about the particular response",
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
            "description": "QuoteResponse object",
            "schema": {
              "$ref": "#/definitions/QuoteResponse"
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
          "QuoteResponse"
        ],
        "summary": "Update a quote response",
        "description": "Update a quote response",
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
            "name": "QuoteResponse",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/QuoteResponse"
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
            "description": "QuoteResponse object",
            "schema": {
              "items": {
                "$ref": "#/definitions/QuoteResponse"
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
          "QuoteResponse"
        ],
        "summary": "Update a quote response",
        "description": "Update a quote response",
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
            "name": "QuoteResponse",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/QuoteResponse"
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
            "description": "QuoteResponse object",
            "schema": {
              "items": {
                "$ref": "#/definitions/QuoteResponse"
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
      }
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
    "EasyForm": {
      "type": "object",
      "properties": {
        "auto-apply": {
          "type": "boolean",
          "description": "Auto apply",
          "format": "boolean",
          "readOnly": true
        },
        "auto-approve": {
          "type": "boolean",
          "description": "Auto approve",
          "format": "boolean",
          "readOnly": true
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "created-at": {
          "type": "string",
          "description": "Created at",
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
        "easy-form-widgets": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/EasyFormWidget"
          }
        },
        "id": {
          "type": "integer",
          "description": "Id",
          "format": "integer",
          "readOnly": true
        },
        "image": {
          "type": "string",
          "description": "Image",
          "format": "na.png",
          "readOnly": true
        },
        "model": {
          "type": "string",
          "description": "Model",
          "format": "string(255)"
        },
        "model-scope": {
          "type": "string",
          "description": "Model scope",
          "format": "string(255)"
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "owner": {
          "type": "string",
          "description": "Owner",
          "readOnly": true
        },
        "status": {
          "type": "string",
          "description": "Status",
          "format": "string(255)",
          "readOnly": true
        },
        "updated-at": {
          "type": "string",
          "description": "Updated at",
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
    "EasyFormWidget": {
      "type": "object",
      "properties": {
        "backing-attribute": {
          "type": "string",
          "description": "Backing attribute",
          "format": "string(255)"
        },
        "created-at": {
          "type": "string",
          "description": "Created at",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "date-value": {
          "type": "string",
          "description": "Date value",
          "format": "datetime"
        },
        "easy-form-id": {
          "type": "integer",
          "description": "Easy form",
          "format": "integer"
        },
        "encrypted": {
          "type": "boolean",
          "description": "Encrypted",
          "format": "boolean",
          "readOnly": true
        },
        "field-name": {
          "type": "string",
          "description": "Field name",
          "format": "string(255)"
        },
        "hint": {
          "type": "string",
          "description": "Hint",
          "format": "string(255)"
        },
        "id": {
          "type": "integer",
          "description": "Id",
          "format": "integer",
          "readOnly": true
        },
        "position": {
          "type": "integer",
          "description": "Position",
          "format": "integer"
        },
        "prompt": {
          "type": "string",
          "description": "Prompt",
          "format": "text"
        },
        "required": {
          "type": "boolean",
          "description": "Required",
          "format": "boolean",
          "readOnly": true
        },
        "rules": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/EasyFormWidgetRule"
          }
        },
        "type": {
          "type": "string",
          "description": "Type",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Updated at",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "value": {
          "type": "string",
          "description": "Value",
          "format": "text"
        }
      },
      "required": [
        "field-name"
      ]
    },
    "EasyFormWidgetRule": {
      "type": "object",
      "properties": {
        "created-at": {
          "type": "string",
          "description": "Created at",
          "format": "datetime",
          "readOnly": true
        },
        "created-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "easy-form-widget-id": {
          "type": "integer",
          "description": "Easy form widget",
          "format": "integer"
        },
        "id": {
          "type": "integer",
          "description": "Id",
          "format": "integer",
          "readOnly": true
        },
        "parameters": {
          "type": "string",
          "description": "Parameters",
          "format": "text"
        },
        "type": {
          "type": "string",
          "description": "Type",
          "format": "string(255)"
        },
        "updated-at": {
          "type": "string",
          "description": "Updated at",
          "format": "datetime",
          "readOnly": true
        },
        "updated-by": {
          "$ref": "#/definitions/UserSimple"
        },
        "value": {
          "type": "string",
          "description": "Value",
          "format": "string(255)"
        }
      },
      "required": [
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
          "description": "Tax Coding Enabled"
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
          "description": "Vendor Remit-To Required"
        }
      },
      "required": [
        "code",
        "name"
      ]
    },
    "ExtraLineAttributes-QuoteRequestLineAttribute": {
      "type": "object",
      "properties": {
        "completed": {
          "type": "boolean",
          "description": "Completed",
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
        "manager-id": {
          "type": "integer",
          "description": "Manager",
          "format": "integer"
        },
        "start-date": {
          "type": "string",
          "description": "Start date",
          "format": "datetime"
        },
        "type": {
          "type": "string",
          "description": "Type",
          "format": "string(255)",
          "enum": [
            "ExtraLineAttributes::ResourceRequisitionLineAttribute",
            "ExtraLineAttributes::ResourceRequisitionLineTemplateAttribute",
            "ExtraLineAttributes::ResourceOrderLineAttribute",
            "ExtraLineAttributes::ResourceOrderLineChangeAttribute",
            "ExtraLineAttributes::ResourceOrderLineVersionAttribute",
            "ExtraLineAttributes::ResourceInvoiceLineAttribute",
            "ExtraLineAttributes::ResourceQuoteRequestLineAttribute",
            "ExtraLineAttributes::DeliverableRequisitionLineAttribute",
            "ExtraLineAttributes::DeliverableRequisitionLineTemplateAttribute",
            "ExtraLineAttributes::DeliverableOrderLineAttribute",
            "ExtraLineAttributes::DeliverableOrderLineChangeAttribute",
            "ExtraLineAttributes::DeliverableOrderLineVersionAttribute",
            "ExtraLineAttributes::DeliverableInvoiceLineAttribute",
            "ExtraLineAttributes::DeliverableQuoteRequestLineAttribute",
            "ExtraLineAttributes::MilestoneRequisitionLineAttribute",
            "ExtraLineAttributes::MilestoneOrderLineAttribute",
            "ExtraLineAttributes::MilestoneOrderLineChangeAttribute",
            "ExtraLineAttributes::MilestoneOrderLineVersionAttribute",
            "ExtraLineAttributes::MilestoneInvoiceLineAttribute",
            "ExtraLineAttributes::MilestoneQuoteRequestLineAttribute"
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
        },
        "work-confirmer-email": {
          "type": "string",
          "description": "Work confirmer email",
          "format": "string(255)"
        }
      }
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
          "type": "boolean",
          "description": "Send Email added notification to supplier",
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
        "email"
      ]
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
          "description": "number"
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
    "QuoteRequest": {
      "type": "object",
      "properties": {
        "allow-award-individual-line-items": {
          "type": "boolean",
          "description": "Ability to award individual line items",
          "format": "boolean"
        },
        "allow-multiple-response": {
          "type": "boolean",
          "description": "Allow multiple responses from one supplier",
          "format": "boolean"
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "automatic-bid-unsealing": {
          "type": "boolean",
          "description": "If checked, bids will be unsealed automatically",
          "format": "boolean",
          "enum": [
            "true",
            "false"
          ]
        },
        "base-price-calculation-method": {
          "type": "integer",
          "description": "Base price calculation method ('average_of_supplier_responses', 'lowest_supplier_response_in_prebid' or 'manually_enter_base_prices') allows to understand the method by which the base price will be calculated",
          "format": "integer"
        },
        "business-partners": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/QuoteRequestsUser"
          }
        },
        "comments": {
          "type": "string",
          "description": "Comments",
          "format": "text"
        },
        "commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "content-groups": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/BusinessGroup"
          }
        },
        "cost-avoidance": {
          "type": "number",
          "description": "Cost avoidance",
          "format": "decimal(30,4)"
        },
        "currency": {
          "$ref": "#/definitions/Currency"
        },
        "description": {
          "type": "string",
          "description": "Event name",
          "format": "text"
        },
        "easy-forms": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/EasyForm"
          }
        },
        "end-time": {
          "type": "string",
          "description": "Time when event should end, format: %m/%d/%y %I:%M %p %z",
          "format": "datetime"
        },
        "event-type": {
          "type": "string",
          "description": "Type of event",
          "format": "string(255)"
        },
        "forms": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Form"
          }
        },
        "lines": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/QuoteRequestLine"
          }
        },
        "lots": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/QuoteRequestsLot"
          }
        },
        "negotiated-savings": {
          "type": "number",
          "description": "Alias of savings to be used as a key in API",
          "format": "decimal(32,4)"
        },
        "planned-savings": {
          "type": "number",
          "description": "Planned savings",
          "format": "decimal(30,6)"
        },
        "quote-request-attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/QuoteRequestAttachment"
          }
        },
        "quote-suppliers": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/QuoteSupplier"
          }
        },
        "sealed-bids": {
          "type": "boolean",
          "description": "If checked, bids will be sealed",
          "format": "boolean"
        },
        "sealing-type": {
          "type": "integer",
          "description": "Sealing type ('one_step_unsealing' or 'two_steps_unsealing') should be selected when Unseal Manually option is chosen",
          "format": "integer",
          "enum": [
            "one_step_unsealing",
            "two_steps_unsealing"
          ]
        },
        "start-on-submit": {
          "type": "boolean",
          "description": "Flag that indicates whether to start event on submit or not",
          "format": "boolean"
        },
        "start-time": {
          "type": "string",
          "description": "Time when event should start, format: %m/%d/%y %I:%M %p %z",
          "format": "datetime"
        },
        "tags": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Tag"
          }
        },
        "timezone": {
          "type": "string",
          "description": "Event timezone",
          "format": "string(255)"
        }
      },
      "required": [
        "event-type"
      ]
    },
    "QuoteRequestAttachment": {
      "type": "object",
      "properties": {
        "allow-to-respond": {
          "type": "boolean",
          "description": "Allow to respond",
          "format": "boolean"
        },
        "attachments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Attachment"
          }
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer"
        },
        "instruction": {
          "type": "string",
          "description": "Instruction",
          "format": "text"
        },
        "name": {
          "type": "string",
          "description": "Name",
          "format": "string(255)"
        },
        "response-required": {
          "type": "boolean",
          "description": "Response required",
          "format": "boolean"
        }
      }
    },
    "QuoteRequestLine": {
      "type": "object",
      "properties": {
        "commodity": {
          "$ref": "#/definitions/Commodity"
        },
        "creatable-from-id": {
          "type": "integer",
          "description": "Creatable from",
          "format": "integer",
          "readOnly": true
        },
        "creatable-from-type": {
          "type": "string",
          "description": "Creatable from type",
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
        "description": {
          "type": "string",
          "description": "Line description",
          "format": "string(255)"
        },
        "easy-form": {
          "$ref": "#/definitions/EasyForm"
        },
        "extra-line-attribute": {
          "$ref": "#/definitions/ExtraLineAttributes-QuoteRequestLineAttribute"
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "manually-entered-base-price": {
          "type": "boolean",
          "description": "Manually entered base price",
          "format": "boolean"
        },
        "need-by-date": {
          "type": "string",
          "description": "Date by which the line item is required",
          "format": "datetime"
        },
        "price-amount": {
          "type": "number",
          "description": "Price",
          "format": "decimal(30,6)"
        },
        "price-currency": {
          "$ref": "#/definitions/Currency"
        },
        "quantity": {
          "type": "number",
          "description": "Quantity",
          "format": "decimal(30,6)"
        },
        "reporting-price-amount": {
          "type": "number",
          "description": "Line reporting price",
          "format": "decimal(30,6)"
        },
        "request-details": {
          "type": "string",
          "description": "Request details",
          "readOnly": true
        },
        "type": {
          "type": "string",
          "description": "Type of line",
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
        "weight": {
          "type": "integer",
          "description": "Weight",
          "format": "integer"
        }
      },
      "required": [
        "type"
      ]
    },
    "QuoteRequestsLot": {
      "type": "object",
      "properties": {
        "expected-quantity": {
          "type": "integer",
          "description": "Quantity of lots we want",
          "format": "integer"
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
            "$ref": "#/definitions/QuoteRequestLine"
          }
        },
        "name": {
          "type": "string",
          "description": "Name of the lot",
          "format": "string(255)"
        }
      }
    },
    "QuoteRequestsUser": {
      "type": "object",
      "properties": {
        "attitude": {
          "type": "string",
          "description": "Attitude",
          "format": "string(255)",
          "enum": [
            "creator",
            "owner",
            "watcher",
            "evaluator"
          ]
        },
        "id": {
          "type": "integer",
          "description": "Coupa unique identifier",
          "format": "integer",
          "readOnly": true
        },
        "user-id": {
          "type": "integer",
          "description": "User",
          "format": "integer"
        }
      }
    },
    "QuoteResponse": {
      "type": "object",
      "properties": {
        "comments": {
          "type": "string",
          "description": "comments",
          "format": "text",
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
        "position": {
          "type": "integer",
          "description": "position",
          "format": "integer",
          "readOnly": true
        },
        "quote-request-id": {
          "type": "integer",
          "description": "quote_request_id",
          "format": "integer",
          "readOnly": true
        },
        "quote-supplier": {
          "$ref": "#/definitions/QuoteSupplier"
        },
        "state": {
          "type": "string",
          "description": "state",
          "format": "string(255)",
          "readOnly": true
        },
        "submitted-at": {
          "type": "string",
          "description": "submitted_at",
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
        }
      },
      "required": [
        "quote-supplier",
        "submitted-at"
      ]
    },
    "QuoteSupplier": {
      "type": "object",
      "properties": {
        "contact-name": {
          "type": "string",
          "description": "Quote supplier contact name",
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
        "display-name": {
          "type": "string",
          "description": "Name that we display to buyer",
          "format": "string(255)"
        },
        "email": {
          "type": "string",
          "description": "Quote supplier email",
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
          "description": " Quote supplier name",
          "format": "string(255)"
        },
        "supplier": {
          "$ref": "#/definitions/Supplier"
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
        "contact-name",
        "email",
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
        "cxml-http-password": {
          "type": "string",
          "description": "Password required to access the Supplier's online store",
          "format": "string"
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
        "cxml-invoice-buyer-domain": {
          "type": "string",
          "description": "Buyer Domain for cXML Invoicing",
          "format": "string(255)"
        },
        "cxml-invoice-buyer-identity": {
          "type": "string",
          "description": "Buyer Identity for cXML Invoicing",
          "format": "string(255)"
        },
        "cxml-invoice-secret": {
          "type": "string",
          "description": "Secret Key for cXML Invoicing Authentication",
          "format": "string(255)"
        },
        "cxml-invoice-supplier-domain": {
          "type": "string",
          "description": "Supplier Domain for cXML Invoicing",
          "format": "string(255)"
        },
        "cxml-invoice-supplier-identity": {
          "type": "string",
          "description": "Supplier Identity for cXML Invoicing",
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
          "format": "string(940)"
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
        "duns": {
          "type": "string",
          "description": "Supplier DUNS number",
          "format": "string(255)"
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
          "format": "IntegrationContact",
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
          "format": "draft"
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
        "cxml-domain",
        "cxml-identity",
        "cxml-invoice-buyer-domain",
        "cxml-invoice-buyer-identity",
        "cxml-invoice-secret",
        "cxml-invoice-supplier-domain",
        "cxml-invoice-supplier-identity",
        "cxml-protocol",
        "cxml-secret",
        "cxml-supplier-domain",
        "cxml-supplier-identity",
        "cxml-url",
        "enterprise",
        "name",
        "online-store",
        "payment-method",
        "po-email",
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
    }
  }
}
```
