import requests


baseURL = 'https://api.gbif.org'

#  Fetch all vernacular names for a given species
# https://techdocs.gbif.org/en/openapi/v1/species#/Species/getNameUsageVernacularNames
r = requests.get(baseURL + '/v1/species/5231190/vernacularNames')
print(r)
print("Headers:")
print(r.headers)
print("JSON:")
print(r.json())
print("Limit =  " + str(r.json()["limit"]))
print(r.json()["results"][0]["vernacularName"])



# Do a fuzzy match between querystring and GBIF taxon backbone
# https://techdocs.gbif.org/en/openapi/v1/species#/Searching%20names/matchNames
# r = requests.get(baseURL + '/v1/species/match?name=Helianthus annuus')
# print(r)
# print("Headers:")
# print(r.headers)
# print("JSON:")
# print(r.json())
