from commons.common_functions import choose
from random import randint

from import_names import names


def get_general_names(race:str="human",sex:str="both",count:int=1,names:dict=names):
    
    names_list=[]
    
    if sex == 'both' or sex == 'any':
        given_name_options = names[race]['male'] + names[race]['female'] + names[race]['both']
    else:
        given_name_options = names[race][sex] + names[race]['both']
    
    surname_options = names[race]['family']
    givens = choose(given_name_options,count)
    surnames = choose(surname_options,count)
    
    for i in range(0,count):
        names_list.append(f'{givens[i]} {surnames[i]}'.strip())
    
    return names_list