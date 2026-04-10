---
title: "R24_Contracts_API.json"
url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/R24/R24_Contracts_API.json"
final_url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/R24/R24_Contracts_API.json"
content_type: "application/json"
classification: "json_asset"
fetched_at: "2026-04-10T01:55:51+00:00"
---

# R24_Contracts_API.json

```json
{
  "swagger": "2.0",
  "info": {
    "version": "",
    "title": "Coupa API",
    "description": "RESTful API that provides robust access to read, edit, or integrate your data with the Coupa platform. The [JSON](/api_docs/5.json) and [YAML](/api_docs/5.yaml) are also available."
  },
  "host": "dashmaster24-4.coupadev.com",
  "basePath": "/api",
  "tags": [
    {
      "name": "LegalDocument",
      "description": "Legal Documents API"
    },
    {
      "name": "Contract",
      "description": "Contracts API"
    },
    {
      "name": "ContractTemplate",
      "description": "Contract Templates API"
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
    "/contracts/{contract_id}/legal_documents/{id}/attach": {
      "post": {
        "tags": [
          "LegalDocument"
        ],
        "summary": "Attaches a file to a legal document",
        "description": "Attaches a file to a legal document",
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
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/LegalDocument"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/contracts/{contract_id}/legal_documents/{id}/complete": {
      "put": {
        "tags": [
          "LegalDocument"
        ],
        "summary": "Moves this legal document to the completed state",
        "description": "Moves this legal document to the completed state",
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
            "name": "LegalDocument",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/LegalDocument"
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
            "description": "LegalDocument object",
            "schema": {
              "items": {
                "$ref": "#/definitions/LegalDocument"
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
    "/contracts/{contract_id}/legal_documents/{id}/submit_for_approval": {
      "put": {
        "tags": [
          "LegalDocument"
        ],
        "summary": "Submits the legal document for approval",
        "description": "Submits the legal document for approval",
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
            "name": "LegalDocument",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/LegalDocument"
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
            "description": "LegalDocument object",
            "schema": {
              "items": {
                "$ref": "#/definitions/LegalDocument"
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
    "/contracts/{contract_id}/legal_documents/{id}/add_approver": {
      "put": {
        "tags": [
          "LegalDocument"
        ],
        "summary": "Adds an approver for this legal document",
        "description": "Adds an approver for this legal document",
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
            "name": "LegalDocument",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/LegalDocument"
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
            "description": "LegalDocument object",
            "schema": {
              "items": {
                "$ref": "#/definitions/LegalDocument"
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
    "/contracts/{contract_id}/legal_documents/{id}/remove_approval": {
      "put": {
        "tags": [
          "LegalDocument"
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
            "name": "LegalDocument",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/LegalDocument"
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
            "description": "LegalDocument object",
            "schema": {
              "items": {
                "$ref": "#/definitions/LegalDocument"
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
    "/contracts/{contract_id}/legal_documents": {
      "get": {
        "tags": [
          "LegalDocument"
        ],
        "summary": "Query legal documents",
        "description": "Query legal documents",
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
            "description": "LegalDocument objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/LegalDocument"
              },
              "xml": {
                "name": "legal-documents",
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
          "LegalDocument"
        ],
        "summary": "Create a new legal document for a contract",
        "description": "Create a new legal document for a contract",
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
            "name": "LegalDocument",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/LegalDocument"
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
              "$ref": "#/definitions/LegalDocument"
            }
          },
          "400": {
            "description": "Bad Request"
          }
        }
      }
    },
    "/contracts/{contract_id}/legal_documents/{id}": {
      "get": {
        "tags": [
          "LegalDocument"
        ],
        "summary": "Show legal document",
        "description": "Show legal document",
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
            "description": "LegalDocument object",
            "schema": {
              "$ref": "#/definitions/LegalDocument"
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
          "LegalDocument"
        ],
        "summary": "Update legal document",
        "description": "Update legal document",
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
            "name": "LegalDocument",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/LegalDocument"
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
            "description": "LegalDocument object",
            "schema": {
              "items": {
                "$ref": "#/definitions/LegalDocument"
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
          "LegalDocument"
        ],
        "summary": "Update legal document",
        "description": "Update legal document",
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
            "name": "LegalDocument",
            "in": "body",
            "required": false,
            "schema": {
              "$ref": "#/definitions/LegalDocument"
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
            "description": "LegalDocument object",
            "schema": {
              "items": {
                "$ref": "#/definitions/LegalDocument"
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
    "/contracts/{id}/update_published": {
      "put": {
        "tags": [
          "Contract"
        ],
        "summary": "Updates a contract when it's published.",
        "description": "Updates a contract when it's published.",
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
    "/contracts/templates": {
      "get": {
        "tags": [
          "ContractTemplate"
        ],
        "summary": "Query contract templates",
        "description": "Query contract templates",
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
            "description": "ContractTemplate objects",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/ContractTemplate"
              },
              "xml": {
                "name": "contract-templates",
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
    "/contracts/templates/{id}": {
      "get": {
        "tags": [
          "ContractTemplate"
        ],
        "summary": "Show contract template",
        "description": "Show contract template",
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
            "description": "ContractTemplate object",
            "schema": {
              "$ref": "#/definitions/ContractTemplate"
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
          "$ref": "#/definitions/BusinessGroup"
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
          "$ref": "#/definitions/Purpose"
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
          "type": "integer",
          "description": "The delegate ID that made the approval (if applicable)",
          "format": "integer",
          "readOnly": true
        },
        "delegates": {
          "$ref": "#/definitions/DelegateApproval"
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
          "$ref": "#/definitions/ApprovalReason"
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
          "$ref": "#/definitions/UserSimple"
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
          "$ref": "#/definitions/Purpose"
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
        "consent": {
          "type": "string",
          "description": "Notice to Consent",
          "format": "string(255)",
          "enum": [
            "notice",
            "consent",
            "not_required",
            "not_assignable"
          ]
        },
        "content-groups": {
          "$ref": "#/definitions/BusinessGroup"
        },
        "contract-owner": {
          "$ref": "#/definitions/UserSimple"
        },
        "contract-terms": {
          "$ref": "#/definitions/ContractTerm"
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
          "type": "string",
          "description": "No of Renewals",
          "format": "string(255)"
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
            "US/Pacific-New",
            "US/Samoa",
            "UTC",
            "Universal",
            "W-SU",
            "WET",
            "Zulu",
            "International Date Line West",
            "Midway Island",
            "American Samoa",
            "Hawaii",
            "Alaska",
            "Pacific Time (US & Canada)",
            "Tijuana",
            "Mountain Time (US & Canada)",
            "Arizona",
            "Chihuahua",
            "Mazatlan",
            "Central Time (US & Canada)",
            "Saskatchewan",
            "Guadalajara",
            "Mexico City",
            "Monterrey",
            "Central America",
            "Eastern Time (US & Canada)",
            "Indiana (East)",
            "Bogota",
            "Lima",
            "Quito",
            "Atlantic Time (Canada)",
            "Caracas",
            "La Paz",
            "Santiago",
            "Newfoundland",
            "Brasilia",
            "Buenos Aires",
            "Montevideo",
            "Georgetown",
            "Greenland",
            "Mid-Atlantic",
            "Azores",
            "Cape Verde Is.",
            "Dublin",
            "Edinburgh",
            "Lisbon",
            "London",
            "Casablanca",
            "Monrovia",
            "Belgrade",
            "Bratislava",
            "Budapest",
            "Ljubljana",
            "Prague",
            "Sarajevo",
            "Skopje",
            "Warsaw",
            "Zagreb",
            "Brussels",
            "Copenhagen",
            "Madrid",
            "Paris",
            "Amsterdam",
            "Berlin",
            "Bern",
            "Rome",
            "Stockholm",
            "Vienna",
            "West Central Africa",
            "Bucharest",
            "Cairo",
            "Helsinki",
            "Kyiv",
            "Riga",
            "Sofia",
            "Tallinn",
            "Vilnius",
            "Athens",
            "Istanbul",
            "Minsk",
            "Jerusalem",
            "Harare",
            "Pretoria",
            "Kaliningrad",
            "Moscow",
            "St. Petersburg",
            "Volgograd",
            "Samara",
            "Kuwait",
            "Riyadh",
            "Nairobi",
            "Baghdad",
            "Tehran",
            "Abu Dhabi",
            "Muscat",
            "Baku",
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
            "Kathmandu",
            "Astana",
            "Dhaka",
            "Sri Jayawardenepura",
            "Almaty",
            "Novosibirsk",
            "Rangoon",
            "Bangkok",
            "Hanoi",
            "Jakarta",
            "Krasnoyarsk",
            "Beijing",
            "Chongqing",
            "Hong Kong",
            "Urumqi",
            "Kuala Lumpur",
            "Taipei",
            "Perth",
            "Irkutsk",
            "Ulaanbaatar",
            "Seoul",
            "Osaka",
            "Sapporo",
            "Tokyo",
            "Yakutsk",
            "Darwin",
            "Adelaide",
            "Canberra",
            "Melbourne",
            "Sydney",
            "Brisbane",
            "Hobart",
            "Vladivostok",
            "Guam",
            "Port Moresby",
            "Magadan",
            "Srednekolymsk",
            "Solomon Is.",
            "New Caledonia",
            "Fiji",
            "Kamchatka",
            "Marshall Is.",
            "Auckland",
            "Wellington",
            "Nuku'alofa",
            "Tokelau Is.",
            "Chatham Is.",
            "Samoa"
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
          "$ref": "#/definitions/ReasonInsightEvent"
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
          "type": "string",
          "description": "Value of Renewal Length",
          "format": "string(255)"
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
          "format": "draft"
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
          "$ref": "#/definitions/Tagging"
        },
        "tags": {
          "$ref": "#/definitions/Tag"
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
          "format": "string(255)",
          "readOnly": true,
          "enum": [
            "MasterContract",
            "AmendmentContract"
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
        "contract-type",
        "end-date",
        "name",
        "number",
        "reason-insight-events",
        "start-date",
        "status",
        "supplier"
      ]
    },
    "ContractTemplate": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean",
          "description": "Is Template Active",
          "format": "boolean",
          "readOnly": true
        },
        "authoring-method": {
          "type": "string",
          "description": "Authoring Method",
          "format": "string(255)",
          "readOnly": true,
          "enum": [
            "msword",
            "msword_and_online"
          ]
        },
        "content-groups": {
          "$ref": "#/definitions/BusinessGroup"
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
        "hierarchy-type": {
          "type": "string",
          "description": "Hierarchy Type",
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
          "type": "integer",
          "description": "The delegate ID that made the approval (if applicable)",
          "format": "integer",
          "readOnly": true
        },
        "delegates": {
          "$ref": "#/definitions/DelegateApproval"
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
          "$ref": "#/definitions/ApprovalReason"
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
          "$ref": "#/definitions/Warehouse"
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
    "LegalDocument": {
      "type": "object",
      "properties": {
        "clm-id": {
          "type": "string",
          "description": "CLM ID",
          "format": "string(255)"
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
        },
        "url": {
          "type": "string",
          "description": "External link to legal document",
          "format": "string(255)"
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
          "$ref": "#/definitions/BusinessGroup"
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
          "$ref": "#/definitions/BusinessGroup"
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
          "$ref": "#/definitions/Contact"
        },
        "content-groups": {
          "$ref": "#/definitions/BusinessGroup"
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
        "invoice-emails": {
          "$ref": "#/definitions/InvoiceEmail"
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
          "$ref": "#/definitions/RemitToAddress"
        },
        "restricted-account-types": {
          "$ref": "#/definitions/AccountType"
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
          "$ref": "#/definitions/SupplierAddress"
        },
        "supplier-sites": {
          "$ref": "#/definitions/SupplierSite"
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
          "$ref": "#/definitions/BusinessGroup"
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
          "$ref": "#/definitions/Purpose"
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
          "$ref": "#/definitions/BusinessGroup"
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
          "$ref": "#/definitions/RemitToAddress"
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
    "User": {
      "type": "object",
      "properties": {
        "account-groups": {
          "$ref": "#/definitions/AccountGroup"
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
          "$ref": "#/definitions/UserGroup"
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
        "content-groups": {
          "$ref": "#/definitions/BusinessGroup"
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
          "$ref": "#/definitions/InventoryOrganization"
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
          "$ref": "#/definitions/Role"
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
          "$ref": "#/definitions/UserGroup"
        },
        "work-confirmation-approval-limit": {
          "$ref": "#/definitions/ApprovalLimit"
        },
        "working-warehouses": {
          "$ref": "#/definitions/Warehouse"
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
          "$ref": "#/definitions/BusinessGroup"
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
          "$ref": "#/definitions/UserSimple"
        }
      },
      "required": [
        "name"
      ]
    },
    "UserSimple": {
      "type": "object",
      "properties": {
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
          "$ref": "#/definitions/WarehouseLocation"
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
