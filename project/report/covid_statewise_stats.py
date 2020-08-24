#Lesson on : Exception handling and Logging
import json

from json.decoder import JSONDecodeError
import logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

statewise_data = {}

import requests
import json


try:
    #covid_statewise_filename = "covid_statewise_sample.json"
    #file_descriptor = open(covid_statewise_filename)
    data = requests.get("https://api.covid19india.org/state_district_wise.json")
    statewise_data = data.json()
    #json.load(file_descriptor)
    state_name = "Karnataka"

except FileNotFoundError:
    logging.critical('File not found, debug why!?')

except JSONDecodeError:
    logging.error('Json structure is not right, check!')


def get_total_cases(state_name, statewise_data):
    #print("get_total_cases:", state_name, statewise_data)
    count = 0

    for state, dist_data in statewise_data.items():
        if state  not in state_name or not isinstance(dist_data, dict):
            continue
        
        for dist, dist_value in dist_data.items(): 
            if not isinstance(dist_value, dict):
                continue

            for d_name, d_val in dist_value.items():
                if not isinstance(dist_value, dict):
                    continue

                for key, value in d_val.items():
                    if key == "active":
                        count = count + int(value)
    
    print(count)
    return count




def _get_total_cases(state_name, statewise_data):
    count = 0
    import pdb
    pdb.set_trace()

    if not isinstance(statewise_data,dict):
        return

    #Solution: 1 -> pop the "State Unassigned" item from dict.
    #statewise_data.pop("State Unassigned")

    for state, dist_data in statewise_data.items():
        #if state == "Unassigned Val": ##STUPID! wrong string.
        if state == "Unassigned":
            continue

        for dist, dist_value in dist_data.items(): 
            if dist == "Unassigned":
                continue
            
            for d_name, d_val in dist_value.items():
                if d_name == "Unassigned":
                    continue

                print("dist:", d_name, "Val:", d_val, type(d_val))
                print(d_val.items())

                for key, value in d_val.items():
                    if key == "active":
                        #print(key, value)
                        count = count + int(value)
                        #print(count)
    return count


if __name__ == "__main__":
    get_total_cases("Karnataka", statewise_data)