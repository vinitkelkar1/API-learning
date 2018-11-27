def device():
    routers = ["router1", "router2", "router3"]
    return routers

def security(device):
    #credentials = {"router1": "password1", "router2":"password2", "router3":"password3"}
    print ("the value inherited from function is", device)
    #return credentials
    for item in device:
        credentials = {item[:]:'password1'}
        print(credentials)

print(device())
print(security(device()))
