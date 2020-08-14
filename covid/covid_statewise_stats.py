#Lesson on : Exception handling and Logging
import json

from json.decoder import JSONDecodeError
import logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

statewise_data = {}

try:
    covid_statewise_filename = "covid_statewise_sample.json"
    file_descriptor = open(covid_statewise_filename)
    statewise_data = json.load(file_descriptor)
    state_name = "Karnataka"

except FileNotFoundError:
    logging.critical('File not found, debug why!?')

except JSONDecodeError:
    logging.error('Json structure is not right, check!')

def get_total_cases():
    count = 0
    for state, dist_data in statewise_data.items():
        for dist, dist_value in dist_data.items(): 
            for d_name, d_val in dist_value.items():
                for key, value in d_val.items():
                    if key == "active":
                        #print(key, value)
                        count = count + int(value)
    return count

count = get_total_cases()
print(count)


