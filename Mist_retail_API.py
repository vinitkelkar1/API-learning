import requests, json, csv
url1 = "https://api.mist.com/api/v1/orgs/a8c903ae-e6d0-42a7-b815-fe395dea8017/sites"
url = "https://api.mist.com/api/v1/self"
token = "Token iEFlXJzvJljYOnqcAe2UgyLfIgaKDkffEvxkrSm05D9Z8wsc31R6it34p918r6imuUFpEMGhMhsQk15ixMEPzMuCU4Gg51L1"
response = requests.get(url, headers={'Authorization': token})
#print(response.json())
response_json = response.json()
response_csv = response_json
print(type(response_json))
print(response_json)
print("#######################")
print(response_json["last_name"])
#print(response_json[0]["name"])

