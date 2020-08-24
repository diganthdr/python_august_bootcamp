import json
def get_subs_data():
    print("Getting subscriber data")

    #load subscription json, map count data to subscribers
    fd = open("subs\\subscription_data.json")
    subscription_data = json.load(fd) 
    return subscription_data