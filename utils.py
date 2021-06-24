import json, os
from collections import OrderedDict

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

output_folder = os.path.join(PROJECT_ROOT, "output/")

def clean_data(file_name:str) ->list:

    data_clean = []
    col_names = []

    # open a file to convert json into python type using json.loads
    with open(file_name) as d:
        data = json.load(d)

    # extract columns and rows
    columns = data['columns']
    rows = data['rows']

    keyys = list(columns[0].keys())


    # get column names only
    for i in columns:
        col_names.append(i['name'])

    # extract the values from the row
    for j in rows:
        val = j['values']
        n = zip(col_names, val)
        data_clean.append(dict(n))

    return data_clean


def process_to_output(ls):

    new_output = []

    for each in ls:
        values = list(each.values())
        new_dict = {"name": values[0], "accountNumber": values[1], "type": values[2]}
        new_output.append(new_dict)

    with open(output_folder+"cleandata.json", "w") as c:
        json.dump(new_output, c)

    return new_output


def standard_process_to_output(ls):
    new_output = []

    for each in ls:
        key_list = list(each.keys())
        if "companyAccount" in key_list:
            new_keys = ["account", "accountNumber", "accountType"]
            new = dict(zip(new_keys, each.values()))
            new_output.append(new)

        if "firmAccount" in key_list:
            new_keys = ["account", "accountNumber", "accountType"]
            new = dict(zip(new_keys, each.values()))
            new_output.append(new)

        if "newAccount" in key_list:
            new_keys = ["accountType","accountNumber","account"]
            new = dict(zip(new_keys, each.values()))
            new_output.append(new)

        with open(output_folder + "cleandata.json", "w") as c:
            json.dump(new_output, c)

    return new_output






