import json

def clean_data(file_name:str) ->list:

    data_clean = []
    col_names = []

    # open a file to convert json into python type using json.loads
    with open(file_name) as d:
        data = json.load(d)

    # extract columns and rows
    columns = data['columns']
    rows = data['rows']

    # get column names only

    for i in columns:
        col_names.append(i['name'])

    # extract the values from the row
    for j in rows:
        val = j['values']
        n = zip(col_names, val)
        data_clean.append(dict(n))

    return data_clean






