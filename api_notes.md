This is notes for me to remember what to talk about in the workshop.
Not really useful for others.

## Web API's
A web server providing programmatic access to data and functions
on the server. Your program sends a request to the server and acts like
a web browser. The server sends a response back to your program.

Use this example: [GBIF API](https://techdocs.gbif.org/en/openapi/)

## Hypertext Transfer Protocol (HTTP) 
Discuss illustrations found here:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview

Request methods and headers:
https://developer.mozilla.org/en-US/docs/Glossary/Request_header

Response headers and status codes:
https://developer.mozilla.org/en-US/docs/Glossary/Response_header

### Using the GBIF API by hand:

Send a request:
```bash
nc api.gbif.org 80
```
Request:
```http
GET /v1/species/5231190/vernacularNames HTTP/1.1
host: api.gbif.org
accept: application/json,text/html
```

This should give a response with a HTTP header and JSON payload.


## What is JSON?
JavaScript Object Notation (JSON) is a lightweight data-interchange format.
It contains either dictionaries (key-value pairs) or lists of dictionaries.

Example:
```json
{
  "name": "John Doe",
  "age": 42,
  "children": [
    {
      "name": "Mille",
      "age": 10
    },
    {
      "name": "Mikkel",
      "age": 8
    }
  ]
}
```

Look at the response from the GBIF API. 

## The requests package
The [requests](https://pypi.org/project/requests/) package is a simple HTTP library for Python.
It allows you to send HTTP requests and get responses.
See [documentation](https://requests.readthedocs.io/en/latest/).


### Making a request to gbif.org
Explain the code

### Making a request to gbif.org using pygbif package
Explain the [code](src/pygbifexample.py)


### Using the Specify API
Explain the [code](src/specifyexample.py)

See also the [tables API](https://specify-snm.science.ku.dk/documentation/api/tables/) documentation
and the [operations API](https://specify-snm.science.ku.dk/documentation/api/operations/) documentation.

We need the [operations API](https://specify-snm.science.ku.dk/documentation/api/operations/) to login and logout.
The [tables API](https://specify-snm.science.ku.dk/documentation/api/tables/) allows us to interact with
the Specify database.

WARNING: You can make serious damage to the Specify database if you are not careful.