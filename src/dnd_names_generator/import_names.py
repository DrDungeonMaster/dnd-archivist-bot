import os,json

def load_database(json_path: str):
    with open(json_path,'rb') as database_input:
        data_dict = json.load(database_input)
    return data_dict

names = load_database('names_database.json')

orc_surname_freq = 0.78
goblin_vulgarity_freq = 0.04


if orc_surname_freq <= 0:
    names['orc']['family'] = ['']
elif orc_surname_freq < 1:
    blank_names = ['']*int(len(names['orc']['family'])*(1-orc_surname_freq))
    names['orc']['family'].extend(blank_names)
else:
    pass
    

if goblin_vulgarity_freq >= 1:
    names['goblin']['parts'] = names['goblin']['vulgarity']
elif goblin_vulgarity_freq < 0:
    pass
else:
    vulgar_names = names['goblin']['vulgarity'] * int(len(names['goblin']['parts'])*goblin_vulgarity_freq/len(names['goblin']['vulgarity']))
    names['goblin']['parts'].extend(vulgar_names)
