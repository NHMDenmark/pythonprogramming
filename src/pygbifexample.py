from pygbif import species


querystring = "Carludovica drudei"
res = species.name_lookup(q=querystring, rank="species", type="checklist", limit=1)

if res['count'] == 0:
    print("No match")
else:
    print("Closes matching scientific name: " + res['results'][0]['scientificName'])


print(res)
