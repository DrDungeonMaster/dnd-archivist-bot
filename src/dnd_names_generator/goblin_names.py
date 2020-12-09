from commons.common_functions import choose
from random import randint

from import_names import names


goblin_names = names['goblin']

type_options = ['normal']*10 + ['short']*10 + ['first_last']*3 + ['two_part']*15 + ['three_part']*2 + ['long']*3

def get_goblin_names(count:int=1):
    names_list = []
    for i in range(0,count):
        pick_index = randint(0,len(type_options)-1)
        pick = type_options[pick_index]
        if pick == 'short':
            parts = choose(goblin_names['parts'],1)
            name = parts[0]
        elif pick == 'first_last':
            parts = choose(goblin_names['parts'],3)
            joiners = choose(goblin_names['joiners'],1)
            name = f'{parts[0]}{joiners[0]}{parts[1]}{parts[2].lower()}'
        elif pick == 'two_part':
            parts = choose(goblin_names['parts'],2)
            joiners = choose(goblin_names['joiners'],1)
            name = f'{parts[0]}{joiners[0]}{parts[1]}'
        elif pick == 'three_part':
            parts = choose(goblin_names['parts'],3)
            joiners = choose(goblin_names['joiners'],2)
            name = f'{parts[0]}{joiners[0]}{parts[1]}{joiners[1]}{parts[2]}'
        elif pick == 'long':
            parts = choose(goblin_names['parts'],3)
            name = f'{parts[0]}{parts[1].lower()}{parts[2].lower()}'
        else:
            pick = 'normal'
            parts = choose(goblin_names['parts'],2)
            name = f'{parts[0]}{parts[1].lower()}'
        end = choose(goblin_names['ends'],1)[0]
        names_list.append(name + end)
        
    return names_list