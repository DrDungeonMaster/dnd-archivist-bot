from itertools import cycle
from random import random
from random import betavariate as rand_beta
from random import uniform as rand_unif
from random import shuffle as shuffle
from copy import deepcopy as copy
from common_functions import choose

from loot_database import curses_data, coin_value, gems_data, gem_types, items_replace, items_data


### loot-holder dictionaries ###

master_coins_dict = {}
for coin in coin_value.keys():
    master_coins_dict[coin]=0
    
master_gems_dict = {}
for gem in gems_data.keys():
    master_gems_dict[gem]=[]

master_items_dict = {}
for item in items_data.keys():
    master_items_dict[item]=[]

### functions ###

def choose_curses(amount:float):
    if amount < 500:
        curse_level = 'non_cursed'
    elif amount < 2500:
        curse_level = 'curses_0'
    elif amount < 15000:
        curse_level = 'curses_1'
    elif amount < 50000:
        curse_level = 'curses_2'
    elif amount < 150000:
        curse_level = 'curses_3'
    else:
        curse_level = 'curses_4'
    return curse_level

def is_cursed(item_name:str, item_value:float, curses_dict:dict=curses_data['curses_4'], prob_cursed:float=0.01, bonus_value:int=0):
    if random() <= prob_cursed:
        cursed_item = True
    else:
        cursed_item = False
    if cursed_item is True:
        curse=choose(list(curses_dict.keys()))[0]
        curse_value_modifier=curses_dict[curse]
        item_value = item_value * curse_value_modifier + bonus_value
        item_name = item_name + f' *Curse of {curse}'
    return item_name, item_value

def choose_jewels_composition(amount:float):
    if amount < 25:
        composition = ''
    elif amount < 500:
        composition = 'FBA'
    elif amount < 5000:
        composition = 'GKCFB'
    elif amount < 50000:
        composition = 'MQHDPLG'
    elif amount < 500000:
        composition = 'NRIEMQHP'
    elif amount < 5000000:
        composition = 'TSJRIEM'
    else:
        composition = 'STOJNRIE'
    return composition

#master_coins_dict = {'Gold':0,'Platinum':0,'Silver':0,'Copper':0,'Electrum':0}
#master_gems_dict = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': []}
#master_items_dict = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': []}


def generate_coinage(amount:int,coin_type:str='Gold',coin_value:dict=coin_value,error_margin:float=0.10):
    value_coins = amount * (1 - rand_beta(2,4.5)) * (1+error_margin*1.5)
    count_coins = int(value_coins/coin_value[coin_type])
    return count_coins

def choose_coins_composition(amount:float):
    if amount < 2:
        composition = 'SC'
    elif amount < 10:
        composition = 'GSSC'
    elif amount < 100:
        composition = 'GPSJSC'
    elif amount < 1000:
        composition = 'GPJGS'
    elif amount < 10000:
        composition = 'PJGGS'
    else:
        composition = 'JPG'
    return composition

def assorted_coinage(amount:float,composition:str=None,error_margin:float=0.10,original_amount:int=None,coins_dict:dict=master_coins_dict):
    coins_dict = copy(coins_dict)
    if original_amount is None:
        original_amount = amount
    if composition is None:
        composition = choose_coins_composition(original_amount)
    for i in list(composition):
        if i.upper() == 'G' and amount > (error_margin*original_amount):
            count_coins = generate_coinage(amount,'Gold',error_margin=error_margin)
            coins_dict['Gold'] += count_coins
            amount += (-1 * count_coins * coin_value['Gold'])
        elif i.upper() == 'P' and amount > (error_margin*original_amount/coin_value['Platinum']):
            count_coins = generate_coinage(amount,'Platinum',error_margin=error_margin)
            coins_dict['Platinum'] += count_coins
            amount += (-1 * count_coins * coin_value['Platinum'])
        elif i.upper() == 'E' and amount > (error_margin*original_amount*coin_value['Electrum']):
            count_coins = generate_coinage(amount,'Electrum',error_margin=error_margin)
            coins_dict['Electrum'] += count_coins
            amount += (-1 * count_coins * coin_value['Electrum'])
        elif i.upper() == 'S' and amount > (error_margin*original_amount*coin_value['Silver']):
            count_coins = generate_coinage(amount,'Silver',error_margin=error_margin)
            coins_dict['Silver'] += count_coins
            amount += (-1 * count_coins * coin_value['Silver'])
        elif i.upper() == 'C' and amount > (error_margin*original_amount*coin_value['Copper']):
            count_coins = generate_coinage(amount,'Copper',error_margin=error_margin)
            coins_dict['Copper'] += count_coins
            amount += (-1 * count_coins * coin_value['Copper'])
        else:
            pass
    if amount > (error_margin*original_amount):
        coins_dict = assorted_coinage(amount*(1+error_margin/2),composition,error_margin,original_amount,coins_dict)
    return coins_dict

def generate_gemstones(amount:int,composition:str=None,gems_data:dict=gems_data,error_margin:float=0.10,prob_cursed:float=0.01, curses_dict:dict=None):
    if composition is None:
        composition = choose_jewels_composition(amount)
    if curses_dict is None:
        curse_level = choose_curses(amount)
        curses_dict = curses_data[curse_level]
    gems_dict = copy(master_gems_dict)
    gems_total_value = 0
    if len(composition) == 0:
        pass
    else:
        for i in cycle(list(composition)):
            if gems_total_value > (amount * (1-error_margin)):
                break
            gem_info = gems_data[i]
            gem_size = gem_info[0]
            gem_type = gem_info[1]
            gem_description = choose(gem_types[gem_type],1)[0]
            gem_value = gem_info[2]
            if prob_cursed > 0 and len(curses_dict) >= 1:
                gem_description,gem_value=is_cursed(gem_description,gem_value,curses_dict,prob_cursed,250)
            probability_factor = (3*gem_value)/(amount-gems_total_value)
            if probability_factor <= 0:
                add_gem = True
            else:
                add_gem = round(rand_beta(2.5,probability_factor))
            if bool(add_gem) is True:
                gems_total_value += gem_value
                gems_dict[i].append(gem_description)
    return gems_dict

def total_coins_value(coins_dict:dict,coin_value:dict=coin_value):
    total_value = 0
    for i in coins_dict:
        total_value += coins_dict[i] * coin_value[i]
    return total_value

def parse_gems_dict(gems_dict:dict,gems_data:dict=gems_data):
    total_gems_value = 0
    total_gems_count = 0
    output_dict = {}
    for i in gems_dict:
        num_gems = len(gems_dict[i])
        gems_value = num_gems * gems_data[i][2]
        rarity_class = gems_data[i][1]
        size_class = gems_data[i][0]
        total_gems_value += gems_value
        total_gems_count += num_gems
        if num_gems > 0:
            if size_class not in output_dict:
                output_dict[size_class]={}
            if rarity_class not in output_dict[size_class]:
                output_dict[size_class][rarity_class]=[]
            output_dict[size_class][rarity_class].extend(gems_dict[i])
    text_report = []
    for i in output_dict:
        size_count = 0
        size_lines = []
        for j in output_dict[i]:
            rarity_count = len(output_dict[i][j])
            size_count += rarity_count
            size_lines.append(f'{rarity_count} {j} ({",".join(output_dict[i][j])})')
        size_lines.reverse()
        size_line = f'{size_count} {i}: ' + ", ".join(size_lines)
        text_report.append(size_line)
    start_text = f'You found {total_gems_count} gemstones:'
    value_text = f'Total value: {total_gems_value}'
    text_report = [start_text] + text_report + [value_text]
    return text_report

def test_gemstones(input_number:int):
    gemstones_found=generate_gemstones(input_number)
    text_report=parse_gems_dict(gemstones_found)
    print("\n".join(text_report))
    return None


def choose_items_composition(amount:float):
    if amount < 5:
        composition = ''
    elif amount < 25:
        composition = 'AFA'
    elif amount < 500:
        composition = 'LFW2BXA'
    elif amount < 2500:
        composition = 'R22MGYLFB'
    elif amount < 10000:
        composition = 'RYGM3XHS2CWB'
    elif amount < 25000:
        composition = 'RHSZN4YC3XC'
    elif amount < 75000:
        composition = 'RTZIO4HZ4DYSRC'
    elif amount < 250000:
        composition = 'RU1JP5E1DY4S'
    elif amount < 1000000:
        composition = 'RVKQ16EUJ5PD'
    elif amount < 5000000:
        composition = 'RQKKEV161ZZ'
    else:
        composition = 'VKQ61E'
    return composition


def generate_items(amount:int,composition:str=None,items_data:dict=items_data,error_margin:float=0.10,prob_cursed:float=0.02, curses_dict:dict=None):
    if composition is None:
        composition = choose_items_composition(amount)
    if curses_dict is None:
        curse_level = choose_curses(amount)
        curses_dict = curses_data[curse_level]
    items_dict = copy(master_items_dict)
    items_total_value = 0
    unique_items = []
    if len(composition) == 0:
        pass
    else:
        for i in cycle(list(composition)):
            if items_total_value > (amount * (1-error_margin)):
                break
            item_info = items_data[i]
            item_type = item_info[0]
            item_rarity = item_info[1]
            possible_items = list(item_info[2].keys())
            item_name = choose(possible_items)[0]
            if '~' in item_name:
                unique = True
                if item_name in unique_items:
                    duplicate = True
                    print(f'Removed duplicate item: {item_name}')
                else:
                    duplicate = False
                    unique_items.append(item_name)
            else:
                duplicate = False
                unique = False
            if not duplicate:
                item_value = item_info[2][item_name]
                if prob_cursed > 0 and len(curses_dict) >= 1 and not unique:
                    item_name,item_value=is_cursed(item_name,item_value,curses_dict,prob_cursed,500)
                probability_factor = (3*item_value)/(amount-items_total_value)
                if probability_factor <= 0:
                    add_item = True
                else:
                    add_item = round(rand_beta(2.5,probability_factor))
                if bool(add_item) is True:
                    item_name = update_item_name(item_name)
                    items_total_value += item_value
                    items_dict[i].append(item_name.replace('~',''))
    return items_dict
    
def make_verbose_items(items_dict:dict,items_data:dict=items_data):
    verbose_items_dict={}
    for i in items_dict.keys():
        if len(items_dict[i]) > 0:
            verbose_items_dict[f'{items_data[i][0]}, {items_data[i][1]}'] = items_dict[i]
            
    return verbose_items_dict

def update_item_name(item_name:str,items_replace:dict=items_replace):
    if '{' in item_name and '}' in item_name:
        for i in items_replace:
            replacement = choose(items_replace[i])[0]
            item_name = item_name.replace('{' + i + '}',replacement)
    else:
        pass
    item_name = item_name.title().replace("'S ","'s ").replace('Of','of').replace(' The',' the')
    return item_name



def generate_loot(amount:int):
    loot_results={'coins':None,'gemstones':None,'items':None}
    loot_totals=copy(loot_results)
    loot_types=list(loot_results.keys())
    shuffle(loot_types)
    allocated_value = 0
    for loot in loot_types:
        remaining_value = amount - allocated_value
        if loot == loot_types[-1]:
            loot_type_value = remaining_value
        else:
            loot_type_value = round(rand_unif(0,remaining_value))
            if loot_type_value < amount/10:
                loot_type_value=0
            elif remaining_value - loot_type_value < amount/10:
                loot_type_value = remaining_value
        loot_totals[loot]=loot_type_value
        allocated_value = allocated_value + loot_type_value
        if loot == 'coins':
            loot_results[loot]=assorted_coinage(loot_type_value)
        elif loot == 'gemstones':
            loot_results[loot]=make_verbose_items(generate_gemstones(loot_type_value),gems_data)
        elif loot == 'items':
            loot_results[loot]=make_verbose_items(generate_items(loot_type_value),items_data)
        else:
            loot_results[loot]=loot_type_value
    print(loot_totals)
    return loot_results
        
def generate_loot_text(amount:int):
    loot_results = generate_loot(amount)
    output_text = []
    for loot in sorted(list(loot_results.keys())):
        if type(loot_results[loot]) is int or type(loot_results[loot]) is str:
            pass
        else:
            temp_text=[]
            temp_text.append(f"\n  {loot.title()}:")
            category_total=0
            for category in loot_results[loot]:
                if type(loot_results[loot][category]) is int:
                    if loot_results[loot][category] > 0:
                        category_total += 1
                        text_line = f'    {loot_results[loot][category]} {category} pieces'
                        temp_text.append(text_line)
                else:
                    itemcount = len(loot_results[loot][category])
                    if itemcount > 0:
                        category_total += 1
                        if loot == 'gemstones':
                            category_label = f'    {itemcount} {category}'
                            if itemcount > 1:
                                category_label = category_label.replace(',','s,')
                            temp_text.append(category_label)
                            for indiv_item in loot_results[loot][category]:
                                temp_text.append(f'        {indiv_item}')
                        else:
                            for indiv_item in loot_results[loot][category]:
                                temp_text.append(f'      {indiv_item}')
        if category_total > 0:
            output_text.extend(temp_text)
            temp_text=[]
    output_text_paragraph = "\n".join(output_text)
    
    return output_text_paragraph
    
    