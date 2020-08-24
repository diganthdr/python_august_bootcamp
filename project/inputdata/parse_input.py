import json
import requests

def get_input_data():
    print("Getting input from API...")
    data = requests.get("https://api.covid19india.org/state_district_wise.json")
    statewise_data = data.json()
    return statewise_data
