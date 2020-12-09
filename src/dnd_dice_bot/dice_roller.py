import re
from secrets import randbelow as random
from random import shuffle
from random import uniform
from math import ceil


def die_roll(die_size:int=6,fast:bool=False):
    if fast:
        roll = ceil(uniform(0,die_size))
    else:
        roll=random(die_size)+1    
    return roll

def dice_roll_dist(die_size:int=20,rolls:int=100,force_rolls=None):
    results=[]
    counts={}
    for die_face in range(1,die_size+1):
        counts[str(die_face)]=0
    for dice_rolls in range(0,rolls):
        if force_rolls == 'min':
            roll = 1
        elif force_rolls == 'max':
            roll = die_size
        else:
            roll=die_roll(die_size)
        results.append(roll)
        counts[str(roll)]+=1
    total = sum(results)
    mean = total/len(results)
    return mean,counts,results

def dice_roll_multi(die_size:int=20,rolls:int=1,force_rolls=None):
    results=[]
    counts={}
    for dice_rolls in range(0,rolls):
        if force_rolls == 'min':
            roll = 1
        elif force_rolls == 'max':
            roll = die_size
        else:
            roll=die_roll(die_size)
        if str(roll) not in counts:
            counts[str(roll)] = 0
        results.append(roll)
        counts[str(roll)]+=1
    total = sum(results)
    mean = total/len(results)
    return mean,counts,results

def eval_dice_cluster(dice_cluster:str,force_rolls=None):
    
    if dice_cluster.startswith('A'):
        dice_cluster = f"{dice_cluster.replace('A','2')}k1"
    elif dice_cluster.startswith('D'):
        dice_cluster = f"{dice_cluster.replace('D','2')}k-1"
    elif dice_cluster.startswith('d'):
        dice_cluster = '1' + dice_cluster
    else:
        pass
    
    if 'k' in dice_cluster:
        keep_parts = dice_cluster.split('k')
        keep_num = int(keep_parts[-1].split('f')[0])
        dice_cluster = keep_parts[0]
    else:
        keep_num = None
        keep_parts = []
    
    reroll = None
    if 'r' in dice_cluster:
        [dice_cluster,reroll]=dice_cluster.split('r')
    else:
        for p in keep_parts:
            if 'r' in p:
                reroll = p.split('r')[1]
    
    num_dice,die_size = dice_cluster.split('d')

    mean,counts,results = dice_roll_multi(int(die_size),int(num_dice),force_rolls)
    
    ordered_rolls = [str(int) for int in results]
    
    dice_rerolled = []
    if reroll is not None:
        for r in range(0,len(results)):
            if results[r] <= int(reroll) and force_rolls is None:
                new_roll = die_roll(int(die_size))
                dice_rerolled.append(f'{results[r]}')
                ordered_rolls[r] = f'{results[r]}r{new_roll}'
                results[r] = new_roll
    
    if keep_num is not None and abs(keep_num) < int(num_dice):
        rolls_sorted = sorted(results,reverse=True)
        if keep_num < 0:
            keep_num = int(num_dice) - abs(keep_num)
            dice_kept = rolls_sorted[keep_num:]
            dice_discarded = rolls_sorted[:keep_num]
        else:
            dice_kept = rolls_sorted[:keep_num]
            dice_discarded = rolls_sorted[keep_num:]
    else:
        dice_kept = results
        dice_discarded = []
    dice_discarded.extend(dice_rerolled)
    
    for d in dice_discarded:
        for o in range(0,len(ordered_rolls)):
            if str(ordered_rolls[o]) == str(d):
                ordered_rolls[o] = f'{ordered_rolls[o]}d'
                break
    
    return ordered_rolls,dice_kept,dice_discarded


def identify_mathematical(command:str):
    regex='-?[\(\d]+[\s\+\-\\./\*\^\(\)\d]+[\d\)]+'
    formulae = re.findall(regex,command)
    return formulae

def eval_roll_command(command:str,force_rolls=None):
    cluster = 0
    store_rolls = {}
    total_value = 0
    
    regex = '[\dADd]+?[d]\d+[r\d+]?k?\-?[\d]*f?[\d]*'
    dice_clusters = re.findall(regex,command)

    fudged_rolls = False
    
    if len(dice_clusters) > 0:
        for d in dice_clusters:
            cluster += 1
            d_orig = str(d)
            if 'f' in d:
                fudged_rolls = True
                [d,fudge_to] = d.split('f')
                if force_rolls is None:
                    force_to = int(fudge_to)
                else:
                    force_to = force_rolls
            else:
                force_to = force_rolls
            
            if type(force_to) is int:
                total_kept=0
                while total_kept != force_to:
                    temp_ordered_rolls,temp_dice_kept,temp_dice_discarded=eval_dice_cluster(d,force_to)
                    total_kept = sum(temp_dice_kept)
                [ordered_rolls,dice_kept,dice_discarded]=[temp_ordered_rolls,temp_dice_kept,temp_dice_discarded]
            else:
                ordered_rolls,dice_kept,dice_discarded=eval_dice_cluster(d,force_to)
            store_rolls[f'{cluster}:{d}']={'rolls':ordered_rolls,'kept':dice_kept,'discarded':dice_discarded}
            total_roll = sum(dice_kept)
            #total_value += total_roll
            command = command.replace(d_orig,str(total_roll) + '+0',1)
        
    
    formulae = identify_mathematical(command)
    if len(formulae) > 0:
        for f in formulae:
            calc_result = eval(f.replace('^','**'))
            total_value += calc_result
            command = command.replace(f,str(calc_result),1)
    return command, total_value, store_rolls, fudged_rolls

def parse_roll(command:str):
    command = command.replace('+',' +').replace('-',' -')
    
    command_subst,total_value,store_rolls,fudged_rolls = eval_roll_command(command)
    
    command_min,min_value,min_rolls,min_fudge = eval_roll_command(command,'min')
    command_max,max_value,max_rolls,max_fudge = eval_roll_command(command,'max')
    value_range = [min_value,max_value]
    return command_subst,store_rolls,total_value,value_range,fudged_rolls

def hide_fudging(text:str):
    regex = 'f[\d]+'
    fudge_factors = re.findall(regex,text)
    for i in fudge_factors:
        text = text.replace(i,'',1)
    return text