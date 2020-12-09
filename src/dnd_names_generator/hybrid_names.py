from commons.common_functions import choose
from random import randint
from random import shuffle

from import_names import names
from general_names import get_general_names

hybrid_options = {}
hybrid_options['half-elf'] = {'parent_races':['elf','human'],'mix':[0.50,0.35]}
hybrid_options['half-orc'] = {'parent_races':['orc','human'],'mix':[0.65,0.15]}

def get_hybrid_names(race_1:str, count:int=1, race_2:str='human', sex:str='both', r1_given_rate:float=0.50, r1_surname_rate:float=0.50,names:dict=names):
    names_list = []
    
    if r1_given_rate > 1:
        r1_given_rate = 1
    if r1_surname_rate > 1:
        r1_surname_rate > 1
        
    r2_given_rate = 1 - r1_given_rate
    r2_surname_rate = 1 - r1_surname_rate
    
    choices_r1g = round(count * r1_given_rate) 
    choices_r1s = round(count * r1_surname_rate)
    
    choices_r2g = count - choices_r1g
    choices_r2s = count - choices_r1s
    
    if sex == 'both' or sex == 'any':
        givens_list_1 = choose(names[race_1]['male'] + names[race_1]['female'],choices_r1g)
        givens_list_2 = choose(names[race_2]['male'] + names[race_2]['female'],choices_r2g) 
    else:
        givens_list_1 = choose(names[race_1][sex],choices_r1g)
        givens_list_2 = choose(names[race_2][sex],choices_r2g)
        
    surnames_list_1 = choose(names[race_1]['family'],choices_r1s)
    surnames_list_2 = choose(names[race_2]['family'],choices_r2s)
    
    givens_list = givens_list_1 + givens_list_2
    surnames_list = surnames_list_1 + surnames_list_2
    
    shuffle(givens_list)
    shuffle(surnames_list)
    
    for i in range(0,count):
        names_list.append(f'{givens_list[i]} {surnames_list[i]}'.strip())
        
    return names_list