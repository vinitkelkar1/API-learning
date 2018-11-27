## This script is for Vinit_test org
import requests, json, csv
url = "https://api.mist.com/api/v1/orgs/faf021c2-a174-42f2-851a-dfd54141806/sites"
token = "Token GGreVZwizB6ZKrBafsXQbAF3nVPc8OgAtlOzBgihwuqhb7A4lQMYPc1brycMI3foalCslOtQGMzjcY8Z5SgcgXd6wdI7nnbh"
response = requests.get(url, headers={'Authorization': token})
#print(response.json())
response_json = response.json()
print(type(response_json))
print(response_json)
print("#######################")
print(response_json[0])
#print(response_json[0]["name"])
