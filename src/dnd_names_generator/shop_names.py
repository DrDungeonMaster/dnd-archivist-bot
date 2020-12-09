from commons.common_functions import choose
from commons.common_functions import choose_separate
from random import randint

#from import_names import names


choices = ['noun'] + ['adjective'] + ['adjective_noun'] + ['adjective_and_adjective'] + ['noun_and_noun'] + ['noun_noun_noun'] + ['adjective_adjective_noun'] + ['adjective_adjective_adjective'] + ['noun_adjective_noun']

categories_dict={
'magic':{'noun':['Arts','Rite','Ritual','Rituals','Arcanum','Secret'],'adjective':['Starry','Ensorcled','Sacred','Mystic','Ritual','Arcane','Secret','Enchanted','Lost']},
'human':{'noun':['People','Mankind'],'adjective':['Standard']},
'elf':{'noun':['Forest','Leaf','Zephyr'],'adjective':['Sylvan','Eternal','Gossamer']},
'dwarf':{'noun':['Hammer','Axe','Cave','Crag','Mountain','Forge','Stone'],'adjective':['Deep','Stone','Iron','Brass','Mountain','Stout','Short','Bearded','Golden','Forged','Dwarven','Drunken']},
'tabaxi':{'noun':['Cat'],'adjective':['Feline']},
'weapons':{'noun':['Sword','Saber','Bow','Arrow','Blade','Axe','Spear','Steel','Iron','Bullet','Hunter'],'adjective':['Slaying','Razor-Sharp','Metal','Steel']},
'equipment':{'noun':['Swords','Shields','Gear','Tools'],'adjective':['Handy','Essential']},
'general':{'noun':['Town','City'],'adjective':['General']},
'pets':{'noun':['Companion','Companions','Buddy','Stable','Mounts','Pal','Pets','Friend','Friends','Birds','Beasts','Fishes','Puppers'],'adjective':['Furry','Scaly','Slippery','Snuggly','Cuddly','Loyal','Well-Trained']},
'inn':{'noun':['Bed','Hearth'],'adjective':['Welcoming','Hungry','Cozy']},
'tavern':{'noun':['Ale','Spirits'],'adjective':['Jolly','Drunken','Loaded']},
'occult':{'noun':['Curse','Crossroads','Raven','Grave','Graveyard'],'adjective':['Accursed','Forbidden','Craven','Dark','Spooky','Twilight']},
'potions':{'noun':['Brew','Cauldron','Tonics','Elixers'],'adjective':['Bubbling']},
'gang':{'noun':['Crawlers'],'adjective':['Night','Fightin\'']},
'ship':{'noun':['Voyage','Maiden','Trader'],'adjective':['Flying','of the Waves','of the Wind','Mermaid\'s','Merman\'s','Ocean\'s']},
'store':{'noun':['Mart','Retailer','Bazaar','Boutique','Emporeum','Market'],'adjective':['For Less','For You','On-Sale','For All Occasions','One-Stop','Discount']},
'sea':{'noun':['Ocean','Sea','Tide','Waves','Spray','Salt','Mermaid','Merman','Sailor','Captain'],'adjective':['Salty','Nautical','Sailing']}
}

def populate_choices(key_string,categories_dict:dict=categories_dict):
    nouns=[]
    adjectives=[]
    
    terms = key_string.split(" ")
    
    for i in terms:
        if i in categories_dict:
            nouns.extend(categories_dict[i]['noun'])
            adjectives.extend(categories_dict[i]['adjective'])
    return nouns,adjectives

def generate_shop(choice:str,noun:list,adjective:list):
    if choice == 'noun':
        odds_the = 0.90
        [choice] = choose(noun,1)
        name = choice
        if randint(1,100)/100 <= odds_the:
            name = f'The {name}'
    elif choice == 'adjective':
        odds_the = 0.65
        [choice] = choose(adjective,1)
        name = choice
        if randint(1,100)/100 <= odds_the and ' the ' not in choice.lower():
            name = f'The {name}'
    elif choice == 'adjective_noun':
        odds_the = 0.50
        [choice_1,choice_2] = choose_separate(adjective,noun)
        name = f'{choice_1} {choice_2}'
        if randint(1,100)/100 <= odds_the:
            name = f'The {name}'
    elif choice == 'adjective_and_adjective':
        odds_the = 0.35
        odds_or = 0.35
        if randint(1,100)/100 <= odds_or:
            conjunction = 'or'
        else:
            conjunction = 'and'
        [choice_1,choice_2] = choose_separate(adjective,adjective)
        name = f'{choice_1} {conjunction} {choice_2}'
        if randint(1,100)/100 <= odds_the:
            name = f'The {name}'
    elif choice == 'noun_and_noun':
        odds_the = 0.50
        odds_or = 0.20
        if randint(1,100)/100 <= odds_or:
            conjunction = 'or'
        else:
            conjunction = 'and'
        [choice_1,choice_2] = choose_separate(noun,noun)
        name = f'{choice_1} {conjunction} {choice_2}'
        if randint(1,100)/100 <= odds_the:
            name = f'The {name}'
    elif choice == 'noun_noun_noun':
        odds_the = 0.20
        odds_or = 0.10
        if randint(1,100)/100 <= odds_or:
            conjunction = 'or'
        else:
            conjunction = 'and'
        [choice_1] = choose(noun,1)
        [choice_2,choice_3] = choose_separate(noun,noun)
        name = f'{choice_1}, {choice_2}, {conjunction} {choice_3}'
        if randint(1,100)/100 <= odds_the:
            name = f'The {name}'
    elif choice == 'adjective_adjective_noun':
        odds_the = 0.20
        odds_comma = 0.35
        if randint(1,100)/100 <= odds_comma:
            conjunction = ', '
        else:
            conjunction = ' '
        [choice_1,choice_2,choice_3] = choose(adjective,2) + choose(noun,1)
        name = conjunction.join([choice_1,choice_2,choice_3])
        if randint(1,100)/100 <= odds_the:
            name = f'The {name}'
    elif choice == 'adjective_adjective_adjective':
        odds_the = 0.10
        odds_comma = 0.85
        if randint(1,100)/100 <= odds_comma:
            conjunction = ', '
        else:
            conjunction = ' '
        [choice_1,choice_2,choice_3] = choose(adjective,1) + choose_separate(adjective,adjective)
        name = conjunction.join([choice_1,choice_2,choice_3])
        if randint(1,100)/100 <= odds_the:
            name = f'The {name}'
    else:
        choice = 'noun'
        name=generate_shop(choice,noun,adjective)
    
    return name.title()

def get_shop_names(key_string:str,number:int=10):
    shops_list=[]
    nouns,adjectives=populate_choices(key_string)
    for i in range(0,number):
        format = choose(choices)[0]
        shops_list.append(generate_shop(format,nouns,adjectives))
    return shops_list
