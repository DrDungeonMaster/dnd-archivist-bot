from commons.common_functions import choose
from commons.common_functions import choose_separate
from random import randint
from random import shuffle

from import_names import names


tabaxi_names = names['tabaxi']
nouns = tabaxi_names['nouns']
adjectives = tabaxi_names['adjectives']
places = tabaxi_names['places']
gerunds = tabaxi_names['gerunds']
numbers = tabaxi_names['numbers']
colors = tabaxi_names['colors']
joiners = tabaxi_names['joiners']


type_options = ['adjective_noun']*65 + ['noun_adjective']*2 + ['adjective_place']*25 + ['noun_place']*10 + ['noun_of_place']*6 + ['number_places']*5 + ['noun_color']*17 + ['number_noun']*20 + ['number_gerund']*6 + ['noun_noun']*15 + ['noun_of_noun']*25 + ['verb_noun']*35


def correct_article(joiner:str,match:str):
    if '{article}' in joiner:
        if match.endswith('s'):
            joiner = joiner.format(article='').replace('  ',' ')
        elif match[0] in ['A','E','I','O','U']:
            joiner = joiner.format(article='an')
        else:
            joiner = joiner.format(article='a')
    return joiner

def correct_possessive(joiner:str,match:str):
    if '{possessive}' in joiner:
        if match.endswith('s'):
            joiner = joiner.format(possessive='\'')    
        else:
            joiner = joiner.format(possessive='\'s')
    return joiner

def is_correct_plural(number_word:str,noun:str):
    if number_word in numbers:
        if number_word.lower() == "one":
            if noun.endswith('s'):
                bool = False
            else:
                bool = True
        elif number_word.lower() == "zero":
            bool = True
        else:
            if noun.endswith('s'):
                bool = True
            else:
                bool = False
    else:
        if any(value in number_word.lower() for value in ['between','among','throughout']):
            if noun.endswith('s'):
                bool = True
            else:
                bool = False
        else:
            bool = True
    return bool

def get_valid(list:list,match:str):
    correct_plural = False
    while correct_plural is False:
        pick = correct_article(choose(list)[0],match)
        correct_plural = is_correct_plural(pick,match)
    return pick

def get_tabaxi_names(count:int=1):
    names_list = []
    for i in range(0,count):
        pick_index = randint(0,len(type_options)-1)
        pick = type_options[pick_index]
        if pick == 'adjective_noun':
            use_A = adjectives*5 + colors*3 + places + gerunds
            use_B = nouns*3 + places
            part_1,part_2 = choose_separate(use_A,use_B)
            names_list.append(f'{part_1} {part_2}')
        elif pick == 'noun_adjective':
            use_A = nouns*3 + places
            use_B = adjectives*3 + colors*3 + places + gerunds
            part_1,part_2 = choose_separate(use_A,use_B)
            names_list.append(f'{part_1}, {part_2}')
        elif pick == 'adjective_place':
            use_A = adjectives*3 + colors*3 + places + gerunds*2
            use_B = places
            part_1,part_2 = choose_separate(use_A,use_B)
            names_list.append(f'{part_1} {part_2}')
        elif pick == 'noun_place':
            use_A = nouns*5 + numbers + places
            use_B = places
            part_1,part_2 = choose_separate(use_A,use_B)
            names_list.append(f'{part_1} {part_2}')
        elif pick == 'noun_of_place':
            use_A = nouns*5 + colors + gerunds + places
            use_B = places
            part_1,part_2 = choose_separate(use_A,use_B)
            joiner = correct_article(choose(joiners['for_places'])[0],part_2)
            names_list.append(f'{part_1}{joiner}{part_2}')
        elif pick == 'noun_color':
            use_A = nouns*5 + places + numbers
            use_B = colors
            parts = choose_separate(use_A,use_B)
            shuffle(parts)
            part_1,part_2 = parts
            names_list.append(f'{part_1} {part_2}')
        elif pick == 'number_noun':
            use_A = numbers
            use_B = nouns + places*3
            part_1 = choose(use_A)[0]
            part_2 = choose(use_B)[0]
            names_list.append(f'{part_1} {part_2}')
        elif pick == 'number_gerund':
            use_A = numbers
            use_B = gerunds
            part_1 = choose(use_A)[0]
            part_2 = choose(use_B)[0]
            names_list.append(f'{part_1} {part_2}')
        elif pick == 'noun_of_noun':
            use_A = nouns*1 + colors*1 + places*1 + gerunds*1 + numbers*1
            use_B = nouns*3 + places
            part_1,part_2 = choose_separate(use_A,use_B)
            joiner = correct_possessive(correct_article(get_valid(joiners['for_nouns'],part_2),part_2),part_1)
            names_list.append(f'{part_1}{joiner}{part_2}')
        elif pick == 'verb_noun':
            use_A = gerunds
            use_B = nouns*3 + places
            part_1,part_2 = choose_separate(use_A,use_B)
            joiner = correct_possessive(correct_article(choose(joiners['for_verbs'])[0],part_2),part_1)
            names_list.append(f'{part_1}{joiner}{part_2}')
        else: 
            pick = 'noun_noun'
            use_A = nouns*10 + colors*3 + places*5 + gerunds*1 + numbers*4
            use_B = nouns*5 + places*1 + gerunds*3
            part_1,part_2 = choose_separate(use_A,use_B)
            names_list.append(f'{part_1} {part_2}')
    return names_list