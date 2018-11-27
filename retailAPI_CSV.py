import requests, json, numpy as np, io
import pandas as pd

url = "https://api.mist.com/api/v1/sites/44a479b8-c32f-4326-b2ad-39c79e4e7ac7/wlans"
#url = "https://api.mist.com/api/v1/self"
token = "Token iEFlXJzvJljYOnqcAe2UgyLfIgaKDkffEvxkrSm05D9Z8wsc31R6it34p918r6imuUFpEMGhMhsQk15ixMEPzMuCU4Gg51L1"
response = requests.get(url, headers={'Authorization': token}).content
#print(type(response))

rawdata = pd.read_csv(io.StringIO(response.decode('utf-8')))


#print(type(rawdata))
print(rawdata)
print(type(rawdata))
df = pd.DataFrame(rawdata, columns=["first_name", "last_name"])
df.to_csv("retail.csv")

#print(response)
#print(response[0])

#print(response.json())
#json_parsed = json.dumps(response)
#print(type(json_parsed))
#print(type(response_json))

#df = pd.read_json(response_json.json)

#print(df)



#outputfile = open('retail.csv', 'w', newline='')
#outputwriter = csv.writer(outputfile)

#with open('retail.json') as f:
#    data = json.load(f)
#df = json_normalize(data)
#f.to_csv('retail.csv')
