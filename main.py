from fastapi import FastAPI
from typing import List
from utils import clean_data, process_to_output, standard_process_to_output
import json, os

# schema
from schema.data import Data

# Define the Project root
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

# define the files needed for processing
abc_input  = os.path.join(PROJECT_ROOT, "input/abcInput.json")
test_input  = os.path.join(PROJECT_ROOT, "input/test.json")
new_data = os.path.join(PROJECT_ROOT, "input/newData.json")

app = FastAPI()

response_model=List[Data]

@app.get("/clean/data",
         summary="use this endpoint to process the different data into clean data",
         )
def get_data():
    # clean the json files
    data = clean_data(abc_input)
    data2 = clean_data(test_input)
    data3 = clean_data(new_data)
    # combine the clean data into one list
    ls = data + data2+data3

    # process the data into a common schema
    # the function process_to_output will write a json file into the cleandata.json
    res = standard_process_to_output(ls)

    return res

