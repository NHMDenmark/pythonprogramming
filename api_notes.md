## HTTP
https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
https://developer.mozilla.org/en-US/docs/Glossary/Request_header

## Using the GBIF API by hand:

Send a request:
kimstp@hodor ~ % nc api.gbif.org 80

GET /v1/species/5231190/vernacularNames HTTP/1.1
host: api.gbif.org
accept: application/json,text/html

This should give a response with a HTTP header and JSON payload.



Basic programming notes:
How to install python - follow this guide https://wiki.python.org/moin/BeginnersGuide/Download


