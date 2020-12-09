from math import pi
from commons.common_functions import choose
from random import randint
from math import floor

### We are going to calculate the size of some dongers

# This code not tested on large+ creatures. Values subject to drastic change.

build_modifiers={
    'length': {
        'tiny':0.6,
        'small':0.8,
        'medium':1,
        'large':1.1,
        'huge':1.25,
        'gargantuan':1.5,
        'biped':1,
        'quadruped':2,
        'powerful':1.35,
        'heavy':1.5,
        'light':1,
        'cone':1.15,
        'hemi':0.9
        },
    'girth':{
        'tiny':0.8,
        'small':1,
        'medium':1,
        'large':0.9,
        'huge':0.8,
        'gargantuan':0.7,
        'biped':1,
        'quadruped':0.65,
        'powerful':1.25,
        'heavy':0.65,
        'light':1.35,
        'cone':0.85,
        'hemi':0.75
        }
    }
    
shape_descriptions={
    'main':{
        'cylinder':'of simple cylindrical shape',
        'cone':'of a tapered conical shape',
        'cone_cyl':'of cylindrical shape tapering to a pointed tip',
        'human':'of a standard humanoid form'
        },
    'features':{
        'barbs':'keratinized barbs',
        'knot':'a bulbous base knot',
        'flare':'a broad, flared head',
        'hemi':'a set of two paired hemipenes'
        }
    }

### Citation for human metrics, which serve as the basis of all calculations:
# Veale, D., Miles, S., Bramley, S., Muir, G., and Hosoll, J. "Am I normal? 
# A systematic review and constructions of nomograms for flaccid and erect penis length 
# and circumference in up to 15,521 men." BJU International, 115(6), 978-986.

database={}

database = {
    'centaur':{
        'str':12,
        'cha':14,
        'con':14,
        'height':78,
        'height_min':68,
        'height_max':88,
        'weight':900,
        'weight_min':600,
        'weight_max':1200,
        'build':['medium','quadruped','powerful'],
        'shape':['cylinder','flare']
        },
    'dragon':{ # This will be based on an 'adult' dragon, but dragons have a massive range of sizes
        'str':25,
        'con':23,
        'cha':18,
        'height':264,
        'height_min':180,
        'height_max':420,
        'weight':12000,
        'weight_min':4000,
        'weight_max':32000,
        'build':['huge','quadruped'],
        'shape':['cone','knot','flare','?barbs'],
        },
    'dragonborn':{
        'str':12,
        'cha':11,
        'height':75,
        'height_min':68,
        'height_max':82,
        'weight':238,
        'weight_min':179,
        'weight_max':367,
        'build':['medium','biped'],
        'shape':['cone','?barbs', '?knot'],
        'plural':'dragonborn',
        
        },
    'dwarf':{
        'str':11,
        'con':12,
        'height':51,
        'height_min':46,
        'height_max':56,
        'weight':155,
        'weight_min':119,
        'weight_max':226,
        'build':['medium','biped'],
        'shape':['human'],
        'plural':'dwarves'
        },
    'elf':{
        'height':65,
        'height_min':55,
        'height_max':78,
        'weight':133,
        'weight_min':77,
        'weight_max':186,
        'build':['medium','biped'],
        'shape':['human'],
        'plural':'elves'
        },
    'firbolg':{
        'height':76,
        'height_min':87,
        'height_max':98,
        'weight':266,
        'weight_min':179,
        'weight_max':463,
        'build':['medium','biped','powerful'],
        'shape':['human'],
        'plural':'firbolg'
        },
    'gnome':{
        'height':40,
        'height_min':37,
        'height_max':43,
        'weight':42,
        'weight_min':37,
        'weight_max':45,
        'build':['small','biped'],
        'shape':['human'],
        },
    'goblin':{
        'str':8,
        'con':11,
        'height':46,
        'height_min':43,
        'height_max':49,
        'weight':49,
        'weight_min':43,
        'weight_max':55,
        'build':['small','biped'],
        'shape':['human','?barbs'],
        },
    'goliath':{
        'str':12,
        'con':11,
        'height':89,
        'height_min':78,
        'height_max':100,
        'weight':300,
        'weight_min':250,
        'weight_max':350,
        'build':['medium','biped','powerful'],
        'shape':['human'],
        'extra':None
        },
    'half-elf':{
        'cha':12,
        'height':66,
        'height_min':59,
        'height_max':73,
        'weight':155,
        'weight_min':114,
        'weight_max':238,
        'build':['medium','biped'],
        'shape':['human'],
        'plural':'half-elves'
        },
    'half-ogre':{
        'str':17,
        'con':14,
        'cha':10,
        'height':83,
        'height_min':74,
        'height_max':92,
        'weight':365,
        'weight_min':300,
        'weight_max':425,
        'shape':['human','?flare'],
        'build':['large','biped']
        },
    'half-orc':{
        'str':12,
        'con':11,
        'height':69,
        'height_min':60,
        'height_max':78,
        'weight':217,
        'weight_min':114,
        'weight_max':380,
        'build':['medium','biped'],
        'shape':['human']
        },
    'halfling':{
        'height':36,
        'height_min':33,
        'height_max':39,
        'weight':40,
        'weight_min':37,
        'weight_max':43,
        'build':['small','biped'],
        'shape':['human'],
        },
    'human':{
        'str':11,
        'con':11,
        'cha':11,
        'height':67,
        'height_min':56,
        'height_max':82,
        'weight':165,
        'weight_min':82,
        'weight_max':272,
        'length':5.25,
        'length_min':3,
        'length_max':13,
        'girth':4.6,
        'girth_min':2.5,
        'girth_max':6.7,
        'build':['medium','biped'],
        'shape':['human'],
        },
    'kitsune':{
        'cha':12,
        'height':56,
        'height_min':64,
        'height_max':48,
        'weight':100,
        'weight_min':80,
        'weight_max':120,
        'build':['medium','biped'],
        'shape':['cone_cyl','knot'],
        'plural':'kitsune'
        },
    'lizardfolk':{
        'con':12,
        'height':68,
        'height_min':59,
        'height_max':77,
        'weight':197,
        'weight_min':118,
        'weight_max':360,
        'build':['medium','biped'],
        'shape':['cone','hemi'],
        'plural':'lizardfolk'
        },
    'loxodon':{
        'str':12,
        'con':11,
        'height':84,
        'height_min':78,
        'height_max':102,
        'weight':400,
        'weight_min':300,
        'weight_max':500,
        'build':['medium','biped','powerful'],
        'shape':['cylinder'],
        },
    'minotaur':{
        'str':12,
        'con':11,
        'height':102,
        'height_min':84,
        'height_max':114,
        'weight':485,
        'weight_min':350,
        'weight_max':600,
        'build':['medium','biped','powerful','heavy'],
        'shape':['cone_cyl']
        },
    'ogre':{
        'str':19,
        'con':16,
        'cha':7,
        'height':120,
        'height_min':105,
        'height_max':132,
        'weight':725,
        'weight_min':600,
        'weight_max':850,
        'build':['large','biped','powerful'],
        'shape':['human','flare'],
        },
    'orc':{
        'str':14,
        'con':12,
        'cha':10,
        'height':82,
        'height_min':72,
        'height_max':96,
        'weight':345,
        'weight_min':230,
        'weight_max':420,
        'build':['medium','biped','powerful'],
        'shape':['human'],
        },
    'sprite':{
        'str':3,
        'cha':11,
        'height':17,
        'height_min':12,
        'height_max':25,
        'weight':9,
        'weight_min':5,
        'weight_max':13,
        'build':['tiny','biped','light'],
        'shape':['cone_cyl','flare'],
        },
    'tabaxi':{
        'cha':11,
        'height':78,
        'height_min':66,
        'height_max':90,
        'weight':220,
        'weight_min':160,
        'weight_max':280,
        'build':['medium','biped'],
        'shape':['cone_cyl','barbs'],
        'plural':'tabaxi'
        },
    'tiefling':
        {
        'cha':12,
        'height':66,
        'height_min':52,
        'height_max':73,
        'weight':155,
        'weight_min':90,
        'weight_max':230,
        'build':['medium','biped'],
        'shape':['human','?barbs','?flare','?knot','?hemi']
        },
    'tortle':{
        'str':12,
        'height':70,
        'height_min':60,
        'height_max':80,
        'weight':400,
        'weight_min':300,
        'weight_max':500,
        'build':['medium','biped','heavy'],
        'shape':['cylinder','flare'],
        'plural':'tortles'
        }
    }
    
for i in database:
    database[i]['build'] = database[i]['build'] + database[i]['shape']

def calculate_length(roll:int=10,height:float=database['human']['height'],constitution:int=10,charisma:int=10,build_mods:list=["medium","biped"]):
    con_mod = (constitution - 10)/2
    cha_mod = (charisma - 10)
    modified_roll = (roll + con_mod + cha_mod - 10)
    roll_term = modified_roll / 25
    height_mult = (height / database['human']['height']) ** 0.65
    min_adj = database['human']['height']/database['human']['height_min']
    max_adj = database['human']['height']/database['human']['height_max'] * 0.9
    build_mult = 1
    for i in build_mods:
        if i in build_modifiers['length']:
            build_mult = build_mult * build_modifiers['length'][i]
    length_base = max(database['human']['length_min'], 
        database['human']['length'] + 
        (max_adj * (database['human']['length_max']-database['human']['length']) * roll_term))
    if length_base == database['human']['length_min']:
        length_base = length_base * min_adj 
    length = length_base * height_mult * build_mult
    return length

def calculate_girth(roll:int=10,weight:float=database['human']['weight'],strength:int=10,constitution:int=10,build_mods:list=["medium","biped"]):
    str_mod = (strength - 10)
    con_mod = (constitution - 10)/2
    modified_roll = (roll + str_mod + con_mod - 10)
    roll_term = modified_roll / 25
    weight_mult = (weight / database['human']['weight']) ** 0.45
    min_adj = database['human']['weight']/database['human']['weight_min']
    max_adj = database['human']['weight']/database['human']['weight_max'] * 0.80
    build_mult = 1
    for i in build_mods:
        if i in build_modifiers['girth']:
            build_mult = build_mult * build_modifiers['girth'][i]
    girth_base = max(database['human']['girth_min'], 
        database['human']['girth'] + 
        (max_adj * (database['human']['girth_max']-database['human']['girth']) * roll_term))
    if girth_base == database['human']['girth_min']:
        girth_base = girth_base * min_adj 
    girth = girth_base * weight_mult * build_mult
    return girth

def dong_calculator(roll:int=10,height:float=database['human']['height'],weight:float=database['human']['weight'],strength:int=10,constitution:int=10,charisma:int=10,build_mods:list=["medium"],shape_mods:list=['human']):
    dicktionary = {}
    
    length = calculate_length(roll,height,constitution,charisma,build_mods)
    girth = calculate_girth(roll,weight,strength,constitution,build_mods)
    
    width = girth / pi
    
    if 'human' in shape_mods:
        head_len = min((length/4),width)
        lost_cyl_vol = (pi * (head_len) * ((width/2) ** 2))
        head_vol = (2/3) * pi * ((width*1.1/2) ** 3) - lost_cyl_vol
        volume = (pi * (length) * ((width/2) ** 2)) + head_vol
        dicktionary['shape']='human'
    elif 'cone' in shape_mods:
        volume = pi * length/3 * (width ** 2)
        dicktionary['shape']='cone'
    elif 'cone_cyl' in shape_mods:
        head_len = min((length/3),width*1.5)
        lost_cyl_vol = (pi * (head_len) * ((width/2) ** 2))
        head_vol = pi * head_len/3 * ((width/2) ** 2) - lost_cyl_vol
        volume = pi * length * ((width/2) ** 2) + head_vol
        dicktionary['shape']='cone_cyl'
    else:
        volume = pi * length * ((width/2) ** 2)
        dicktionary['shape']='cylinder'

    if 'barbs' in shape_mods:
        volume = volume * 1.02
        
    dicktionary['length']=round(length,2)
    dicktionary['girth']=round(girth,2)
    dicktionary['width']=round(width,2)
    
    if 'heavy' in build_mods:
        heavy_flare_mod = 1.5
    else:
        heavy_flare_mod = 1
    
    if 'flare' in shape_mods:
        if 'human' in shape_mods:
            flare_width = width * (1.45+roll/20) * heavy_flare_mod
            flare_vol = max(0,(1/3) * pi * head_len * (width/2 + flare_width/2 + (width/2 * flare_width/2)) - head_vol)
            flare_ratio = flare_width/(width*1.1)
        elif 'cone_cyl' in shape_mods:
            flare_width = width * (1.35+roll/20) * heavy_flare_mod
            flare_vol = max(0,(pi * head_len/3 * (flare_width ** 2)) - head_vol)
            flare_ratio = flare_width/width
        elif 'cone' in shape_mods:
            head_len = min(length/4,width*2.5)
            head_width = (width*2)*(head_len/(length*2))
            head_vol = pi * head_len/3 * (head_width ** 2)
            flare_width = head_width * (1.5+roll/20) * heavy_flare_mod
            flare_vol = max(0,(pi * head_len/3 * (flare_width ** 2)) - head_vol)
            flare_ratio = flare_width/head_width
        else:
            head_len = min((length/5),width)
            flare_width = width * (1.75+roll/20) * heavy_flare_mod
            lost_cyl_vol = (pi * (head_len) * ((width/2) ** 2))
            flare_vol = max(0,(1/3) * pi * head_len * (width/2 + flare_width/2 + (width/2 * flare_width/2)) - lost_cyl_vol)
            flare_ratio = flare_width/width
        dicktionary['flare_width']=round(flare_width,2)
        if 'cone' not in shape_mods:
            dicktionary['flare_width']=round(max(width,dicktionary['flare_width']),2)
        dicktionary['flare_vol']=round(flare_vol,1)
        dicktionary['flare_ratio']=round(flare_ratio,2)
        volume = volume + flare_vol
    
    if 'knot' in shape_mods:
        if 'cone' in shape_mods:
            knot_width = (width*1.5) * (1+(roll)/20)
            lost_cone_vol = (1/3) * pi * width*1.65/2 * ((width*1.65/2*(1-(width/length))) + (width*1.65/2) + (width*1.65/2 * width*2/2))
            knot_vol = max(0,((4/3) * pi * width/2 * (width*1.65/2) * knot_width/2)-lost_cone_vol)
            if knot_vol == 0:
                knot_width = width*1.65
            dicktionary['knot_width']=round(knot_width,2)
            dicktionary['knot_vol']=round(knot_vol,1)
            dicktionary['knot_ratio']=round(knot_width/width,2)
            volume = volume + knot_vol
        else:
            knot_width = width * (2+(roll)/20)
            lost_cyl_vol = pi * width * ((width/2) ** 2)
            knot_vol = max(0,((4/3) * pi * width/2 * width/2 * knot_width/2) - lost_cyl_vol)
            volume = volume + knot_vol
            if knot_vol == 0:
                knot_width = width
            dicktionary['knot_width']=round(knot_width,2)
            dicktionary['knot_vol']=round(knot_vol,1)
            dicktionary['knot_ratio']=round(knot_width/width,2)
            volume = volume + knot_vol
            
    dicktionary['volume']=round(volume,1)
            
    return dicktionary

def donger_race_metrics(race:str='human'):
    if 'str' in database[race]:
        strength = database[race]['str']
    else:
        strength = 10
    if 'con' in database[race]:
        constitution = database[race]['con']
    else:
        constitution = 10
    if 'cha' in database[race]:
        charisma = database[race]['cha']
    else:
        charisma = 10
    average_dong = dong_calculator(10,database[race]['height'],database[race]['weight'],strength-1,constitution-1,charisma-1,database[race]['build'],database[race]['shape'])
    min_dong = dong_calculator(1,database[race]['height_min'],database[race]['weight_min'],strength-5,constitution-5,charisma-5,database[race]['build'],database[race]['shape'])
    max_dong = dong_calculator(20,database[race]['height_max'],database[race]['weight_max'],strength+9,constitution+9,charisma+9,database[race]['build'],database[race]['shape'])
    dicktionary={'race':race,'average_dong':average_dong,'min_dong':min_dong,'max_dong':max_dong}
    return dicktionary

def generate_dickstribution(race:str='human'):

    length_dist = []
    girth_dist = []
    volume_dist = []
    
    other_dists={
        'knot_width':[],
        'knot_vol':[],
        'knot_ratio':[],
        'flare_width':[],
        'flare_vol':[],
        'flare_ratio':[]
        }
    
    build_mods = database[race]['build']
    shape_mods = database[race]['shape']

    print(shape_mods)

    min_height = database[race]['height_min']
    avg_height = database[race]['height']
    max_height = database[race]['height_max']
    min_weight = database[race]['weight_min']
    avg_weight = database[race]['weight']
    max_weight = database[race]['weight_max']
    
    n_steps = 50
    add_count=max(int(n_steps/2.5),1)
    
    height_step_high = (max_height - avg_height)/n_steps
    height_step_low = (avg_height - min_height)/n_steps
    weight_step_high = (max_weight - avg_weight)/n_steps
    weight_step_low = (avg_weight - min_weight)/n_steps
    
    height_range = []
    weight_range = []
    
    for i in range(0,n_steps):
        height_range = height_range + [avg_height - height_step_low*i]*add_count + [avg_height + height_step_high*i]*add_count
        weight_range = weight_range + [avg_weight - weight_step_low*i]*add_count + [avg_weight + weight_step_high*i]*add_count
        add_count = max(1,add_count-1)

    if 'str' in database[race]:
        str_score = database[race]['str']-1
    else:
        str_score = 10
    if 'con' in database[race]:
        con_score = database[race]['con']-1
    else:
        con_score = 10
    if 'cha' in database[race]:
        cha_score = database[race]['cha']-1
    else:
        cha_score = 10
    
    str_range = [str_score-5]*4 + [str_score - 4]*28 + [str_score - 3]*36 + [str_score - 2]*48 + [str_score-1]*72 + [str_score]*96 + [str_score+1]*64 + [str_score+2]*32 + [str_score+3]*16 + [str_score+4]*12 + [str_score+5]*8 + [str_score+6]*6 + [str_score+7]*4 + [str_score+8]*3 + [str_score+8]*2 + [str_score+9] + [str_score+10]
    con_range = [con_score-5]*4 + [con_score - 4]*28 + [con_score - 3]*36 + [con_score - 2]*48 + [con_score-1]*72 + [con_score]*96 + [con_score+1]*64 + [con_score+2]*32 + [con_score+3]*16 + [con_score+4]*12 + [con_score+5]*8 + [con_score+6]*6 + [con_score+7]*4 + [con_score+8]*3 + [con_score+8]*2 + [con_score+9] + [con_score+10]
    cha_range = [con_score-5]*4 + [cha_score - 4]*28 + [cha_score - 3]*36 + [cha_score - 2]*48 + [cha_score-1]*72 + [cha_score]*96 + [cha_score+1]*64 + [cha_score+2]*32 + [cha_score+3]*16 + [cha_score+4]*12 + [cha_score+5]*8 + [cha_score+6]*6 + [cha_score+7]*4 + [cha_score+8]*3 + [cha_score+8]*2 + [cha_score+9] + [cha_score+10] 
    
    dice_rolls = [i for i in range(1,21)] + [10]
    
    for i in range(0,5000):
        random_dong_draw = dong_calculator(
            roll=choose(dice_rolls)[0],
            height=choose(height_range)[0],
            weight=choose(weight_range)[0],
            strength=choose(str_range)[0],
            constitution=choose(con_range)[0],
            charisma=choose(cha_range)[0],
            build_mods=build_mods,
            shape_mods=shape_mods
            )
        #print(random_dong_draw)
        length_dist.append(random_dong_draw['length']-0.06)
        girth_dist.append(random_dong_draw['girth']+0.015)
        volume_dist.append(random_dong_draw['volume'])
        
        for o in other_dists:
            if o in random_dong_draw:
                other_dists[o].append(random_dong_draw[o])
        
    length_dist.sort()
    girth_dist.sort()
    volume_dist.sort()
    
    for o in other_dists:
        if len(other_dists[o]) > 1:
            other_dists[o].sort()
    
    return length_dist, girth_dist, volume_dist, other_dists

def calculate_percentile(score:float,distribution:list):
    distribution.sort()
    if score < distribution[0]:
        percentile = 0
    elif score > distribution[-1]:
        percentile = 100
    else:
        for i in range(0,len(distribution)):
            if score <= distribution[i]:
                break
        percentile = (i-1)/len(distribution)
    return percentile
    
def percentile_format(score:float):
    if score == 0:
        score_txt = "<0.01 %ile"
    elif score == 100:
        score_txt = ">99.99 %ile"
    else:
        score_txt = f"{round(score * 100,2)} %ile"
    return score_txt

def score_size(length:float, girth:float, volume:float, flare_width:float=None, flare_ratio:float=None, knot_width:float=None, knot_ratio:float=None, race:str='human'):
    length_dist, girth_dist, volume_dist, other_dists = generate_dickstribution(race=race)
    length_per = calculate_percentile(length,length_dist)
    girth_per = calculate_percentile(girth,girth_dist)
    volume_per = calculate_percentile(volume,volume_dist)
    other_scores={}
    if flare_width is not None and len(other_dists['flare_width']) > 0:
        flare_width_per = calculate_percentile(flare_width,other_dists['flare_width'])
        other_scores['flare_width_per']=flare_width_per
    if flare_ratio is not None and len(other_dists['flare_width']) > 0:
        flare_ratio_per = calculate_percentile(flare_ratio,other_dists['flare_ratio'])
        other_scores['flare_ratio_per']=flare_ratio_per
    if knot_width is not None and len(other_dists['knot_width']) > 0:
        knot_width_per = calculate_percentile(knot_width,other_dists['knot_width'])
        other_scores['knot_width_per']=knot_width_per
    if knot_ratio is not None and len(other_dists['knot_width']) > 0:
        knot_ratio_per = calculate_percentile(knot_ratio,other_dists['knot_ratio'])
        other_scores['knot_ratio_per']=knot_ratio_per
    
    return length_per, girth_per, volume_per, other_scores

def donger_text(race:str='human',roll:int=10,height:float=database['human']['height'],weight:float=database['human']['weight'],strength:int=10,constitution:int=10,charisma:int=10):
    result_dickt=dong_calculator(roll=roll,height=height,weight=weight,strength=strength,constitution=constitution,charisma=charisma,build_mods=database[race]['build'],shape_mods=database[race]['shape'])
    length = result_dickt['length']
    width = result_dickt['width']
    girth = result_dickt['girth']
    volume = result_dickt['volume']
    print(result_dickt)
    
    if 'flare_width' in result_dickt:
        flare_width = result_dickt['flare_width'] 
    else:
        flare_width = None
    if 'flare_ratio' in result_dickt:
        flare_ratio = result_dickt['flare_ratio'] 
    else:
        flare_ratio = None
        
    if 'knot_width' in result_dickt:
        knot_width = result_dickt['knot_width'] 
    else:
        knot_width = None
    if 'knot_ratio' in result_dickt:
        knot_ratio = result_dickt['knot_ratio'] 
    else:
        knot_ratio = None
    
    length_per, girth_per, volume_per, other_scores = score_size(length=length,girth=girth,volume=volume,flare_width=flare_width,flare_ratio=flare_ratio,knot_width=knot_width,knot_ratio=knot_ratio,race=race)
    
    if race.lower().startswith(tuple(['a','e','i','o','u'])):
        a_an = 'an'
    else:
        a_an = 'a'
        
    if 'plural' in database[race]:
        race_plural = database[race]['plural']
    else:
        race_plural = race + 's'
    
    height_feet=floor(height/12)
    height_inches=int(round(height % 12,0))
    height_text = f"{height_feet}'{height_inches}\""
    
    text_out = [f'The subject is {a_an} {race} with the following parameters:',
        f'\tHeight: {height_text}',
        f'\tWeight: {round(weight,1)} lbs.',
        f'\tStrength: {strength}',
        f'\tConstitution: {constitution}',
        f'\tCharisma: {charisma}',
        f'\tLuck: {roll}/20\n']
    
    text_out=text_out + [f"{a_an.title()} {race} with these parameters should have endowment of approximately the following:",
        f"\tLength: {length} in.",
        f"\tWidth: {width} in.",
        f"\tGirth: {girth} in."]
        
    print(result_dickt)
        
    if 'flare_width' in result_dickt:
        text_out.append(f"\tFlare Width: {result_dickt['flare_width']} in.")
    if 'flare_ratio' in result_dickt:
        text_out.append(f"\tFlare Ratio: {result_dickt['flare_ratio']}:1")
    if 'knot_width' in result_dickt:
        text_out.append(f"\tKnot Width: {result_dickt['knot_width']} in.")
    if 'knot_ratio' in result_dickt:
        text_out.append(f"\tKnot Ratio: {result_dickt['knot_ratio']}:1")
        
    text_out.append(f"\tVolume: {volume} in.³")
        
    text_out=text_out + [
        f"\nCompared to other {race_plural}:",
        f"\tLength: {percentile_format(length_per)}",
        f"\tWidth/Girth: {percentile_format(girth_per)}"
        ]
        
    if 'flare_width_per' in other_scores:
        text_out.append(f"\tFlare Width: {percentile_format(other_scores['flare_width_per'])}")
    if 'flare_ratio_per' in other_scores:
        text_out.append(f"\tFlare Ratio: {percentile_format(other_scores['flare_ratio_per'])}")
    if 'knot_width_per' in other_scores:
        text_out.append(f"\tKnot Width: {percentile_format(other_scores['knot_width_per'])}")
    if 'knot_ratio_per' in other_scores:
        text_out.append(f"\tKnot Ratio: {percentile_format(other_scores['knot_ratio_per'])}")
        
    text_out.append(f"\tVolume: {percentile_format(volume_per)}")

    print("\n".join(text_out))
    return "\n".join(text_out)

def race_donger_text(race:str='human'):
    info_dickt=donger_race_metrics(race)
    
    if 'plural' in database[race]:
        race_plural = database[race]['plural']
    else:
        race_plural = race + 's'
    
    if 'hemi' in database[race]['shape']:
        hemi=True
    else:
        hemi=False
    
    shape=''
    
    main_shape=None
    features=[]
    sometimes_features=[]
    
    for i in database[race]['shape']:
        if i in shape_descriptions['main']:
            if hemi:
                main_shape=f"{race_plural.title()} each possess {shape_descriptions['features']['hemi']} {shape_descriptions['main'][i]}"
            else:
                main_shape=f"{race_plural.title()} have phalli {shape_descriptions['main'][i]}"
        elif i in shape_descriptions['features'] and i != 'hemi':
            features.append(shape_descriptions['features'][i])
        elif i.startswith('?'):
            if i.replace('?','') in shape_descriptions['features']:
                sometimes_features.append(shape_descriptions['features'][i.replace('?','')])
        else:
            print(f'Unsupported feature: {i}')
            
    if len(features) > 0:
        if len(features) <= 2:
            shape = main_shape + f", with {' and '.join(features)}."
        else:
            features[-1] = f'and {features[-1]}' 
            shape = main_shape + ", with {', '.join(features)}."
    else:
        shape = main_shape + "."
        
    if len(sometimes_features) > 0:
        if len(sometimes_features) <= 2:
            shape = shape + f' Some individuals possess {" and/or ".join(sometimes_features)}.'
        else:
            sometimes_features[-1] = f'and/or {sometimes_features[-1]}' 
            shape = shape + f" Some individuals possess {', '.join(sometimes_features)}."
    
    text_out = [
        f"{shape}\n",
        f"For {race_plural}, an average individual would measure in at approximately:",
        f"\tLength: {info_dickt['average_dong']['length']} in.",
        f"\tWidth: {info_dickt['average_dong']['width']} in.",
        f"\tGirth: {info_dickt['average_dong']['girth']} in."]
    if 'flare_width' in info_dickt['average_dong']:
        text_out.append(f"\tFlare Width: {info_dickt['average_dong']['flare_width']} in.")
    if 'flare_ratio' in info_dickt['average_dong']:
        text_out.append(f"\tFlare Ratio: {info_dickt['average_dong']['flare_ratio']}:1")
    if 'knot_width' in info_dickt['average_dong']:
        text_out.append(f"\tKnot Width: {info_dickt['average_dong']['knot_width']} in.")
    if 'knot_ratio' in info_dickt['average_dong']:
        text_out.append(f"\tKnot Ratio: {info_dickt['average_dong']['knot_ratio']}:1")
    text_out.append(f"\tVolume: {info_dickt['average_dong']['volume']} in.³")
        
    text_out = text_out + [
        f"\nThe minimum healthy measurements are considered to be:",
        f"\tLength: {info_dickt['min_dong']['length']} in.",
        f"\tWidth: {info_dickt['min_dong']['width']} in.",
        f"\tGirth: {info_dickt['min_dong']['girth']} in."]
    if 'flare_width' in info_dickt['min_dong']:
        text_out.append(f"\tFlare Width: {info_dickt['min_dong']['flare_width']} in.")
    if 'flare_ratio' in info_dickt['min_dong']:
        text_out.append(f"\tFlare Ratio: {info_dickt['min_dong']['flare_ratio']}:1")
    if 'knot_width' in info_dickt['min_dong']:
        text_out.append(f"\tKnot Width: {info_dickt['min_dong']['knot_width']} in.")
    if 'knot_ratio' in info_dickt['min_dong']:
        text_out.append(f"\tKnot Ratio: {info_dickt['min_dong']['knot_ratio']}:1")
    text_out.append(f"\tVolume: {info_dickt['min_dong']['volume']} in.³")
    
    text_out = text_out + [
        f"\nThe most impressive recorded individual measured:",
        f"\tLength: {info_dickt['max_dong']['length']} in.",
        f"\tWidth: {info_dickt['max_dong']['width']} in.",
        f"\tGirth: {info_dickt['max_dong']['girth']} in."]
    if 'flare_width' in info_dickt['max_dong']:
        text_out.append(f"\tFlare Width: {info_dickt['max_dong']['flare_width']} in.")
    if 'flare_ratio' in info_dickt['max_dong']:
        text_out.append(f"\tFlare Ratio: {info_dickt['max_dong']['flare_ratio']}:1")
    if 'knot_width' in info_dickt['max_dong']:
        text_out.append(f"\tKnot Width: {info_dickt['max_dong']['knot_width']} in.")
    if 'knot_ratio' in info_dickt['max_dong']:
        text_out.append(f"\tKnot Ratio: {info_dickt['max_dong']['knot_ratio']}:1")
    text_out.append(f"\tVolume: {info_dickt['max_dong']['volume']} in.³")
        
    print("\n".join(text_out))
    return "\n".join(text_out)
    
def describe_random_dong(race:str=choose(list(database.keys()))[0]):

    min_height = database[race]['height_min']
    avg_height = database[race]['height']
    max_height = database[race]['height_max']
    min_weight = database[race]['weight_min']
    avg_weight = database[race]['weight']
    max_weight = database[race]['weight_max']
    
    n_steps = 50
    add_count=max(int(n_steps/2.5),1)
    
    height_step_high = (max_height - avg_height)/n_steps
    height_step_low = (avg_height - min_height)/n_steps
    weight_step_high = (max_weight - avg_weight)/n_steps
    weight_step_low = (avg_weight - min_weight)/n_steps
    
    height_range = []
    weight_range = []
    
    for i in range(0,n_steps):
        height_range = height_range + [avg_height - height_step_low*i]*add_count + [avg_height + height_step_high*i]*add_count
        weight_range = weight_range + [avg_weight - weight_step_low*i]*add_count + [avg_weight + weight_step_high*i]*add_count
        add_count = max(1,add_count-1)

    if 'str' in database[race]:
        str_score = database[race]['str']-1
    else:
        str_score = 10
    if 'con' in database[race]:
        con_score = database[race]['con']-1
    else:
        con_score = 10
    if 'cha' in database[race]:
        cha_score = database[race]['cha']-1
    else:
        cha_score = 10
    
    str_range = [str_score-5]*4 + [str_score - 4]*28 + [str_score - 3]*36 + [str_score - 2]*48 + [str_score-1]*72 + [str_score]*96 + [str_score+1]*64 + [str_score+2]*32 + [str_score+3]*16 + [str_score+4]*12 + [str_score+5]*8 + [str_score+6]*6 + [str_score+7]*4 + [str_score+8]*3 + [str_score+8]*2 + [str_score+9] + [str_score+10]
    con_range = [con_score-5]*4 + [con_score - 4]*28 + [con_score - 3]*36 + [con_score - 2]*48 + [con_score-1]*72 + [con_score]*96 + [con_score+1]*64 + [con_score+2]*32 + [con_score+3]*16 + [con_score+4]*12 + [con_score+5]*8 + [con_score+6]*6 + [con_score+7]*4 + [con_score+8]*3 + [con_score+8]*2 + [con_score+9] + [con_score+10]
    cha_range = [con_score-5]*4 + [cha_score - 4]*28 + [cha_score - 3]*36 + [cha_score - 2]*48 + [cha_score-1]*72 + [cha_score]*96 + [cha_score+1]*64 + [cha_score+2]*32 + [cha_score+3]*16 + [cha_score+4]*12 + [cha_score+5]*8 + [cha_score+6]*6 + [cha_score+7]*4 + [cha_score+8]*3 + [cha_score+8]*2 + [cha_score+9] + [cha_score+10] 
    
    dice_rolls = [i for i in range(1,21)] + [10]
    
    
    r_roll=choose(dice_rolls)[0]
    r_height=choose(height_range)[0]
    r_weight=choose(weight_range)[0]
    r_strength=choose(str_range)[0]
    r_constitution=choose(con_range)[0]
    r_charisma=choose(cha_range)[0]

    height_feet=floor(r_height/12)
    height_inches=int(round(r_height % 12,0))
    height_text = f"{height_feet}'{height_inches}\""
    
    if race.lower().startswith(tuple(['a','e','i','o','u'])):
        a_an = 'an'
    else:
        a_an = 'a'
    
    output_text = donger_text(
        race=race,
        roll=r_roll,
        height=r_height,
        weight=r_weight,
        strength=r_strength,
        constitution=r_constitution,
        charisma=r_charisma)
        
    return output_text
