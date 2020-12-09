### Use this to update a database with more names, etc. ###
# Not used by Lambda Function


import os,yaml,json,shutil

def load_database(json_path: str):
    with open(json_path,'rb') as database_input:
        data_dict = yaml.safe_load(database_input)
    return data_dict


def recursive_dict_clean(input):
    if type(input) is list:
        try:
            to_return = sorted(list(set(input)))
        except TypeError:
            to_return = input
    elif type(input) is dict:
        to_return = {}
        for i in input:
            to_return[i] = recursive_dict_clean(input[i])
    else:
        to_return = input
    return to_return


def write_database(json_path: str, new_database: dict, overwrite:bool=False, pretty:bool=True):
    if os.path.isfile(json_path) is True:
        if overwrite is False:
            raise
        else:
            shutil.move(json_path,json_path + '.old')
    with open(json_path,'w') as data_out:
        if pretty:
            data_out.write(json.dumps(new_database,sort_keys=True,indent=4, separators=(',',': ')))
        else:
            data_out.write(json.dumps(new_database))
    return None


def add_to_database(database_path: str, database_key: str, list_to_add: list, unique: bool=False):
    database = load_database(database_path)
    database_key = database_key.replace(':','"]["')
    existing_data = eval(f'database["{database_key}"]')
    if type(existing_data) is list:
        eval(f'database["{database_key}"].extend(list_to_add)')
    else:
        raise
    if unique is True:
        database = recursive_dict_clean(database)
    write_database(database_path, database, overwrite=True)
    return None