import numpy as np

from common_functions import is_numeric

e = 2.71828

race_life_data={
'human':[1,18,95,'Lin','Lin'],
'elf':[6,100,800,'Log','Lin'],
'dragonborn':[0.7,16,80,'Log','Exp'],
'half-elf':[0.9,21,185,'Lin','Exp'],
'gnome':[3,35,450,'Lin','Log'],
'loxodon':[2,60,450,'Log','Exp'],
'tortle': [0.3,50,400,'Log','Lin'],
'dog': [0.15,1,15,'Exp','Lin'],
'halfling': [1.5,20,160,'Lin','Exp'],
'dragon': [5,100,4500,'Lin','Log'],
'goblin': [0.25,8,60,'Lin','Lin'],
'kobold': [0.2,7,120,'Exp','Exp'],
'orc': [0.75,12,50,'Log','Exp'],
'half-orc': [0.75,14,70,'Lin','Exp'],
'dwarf': [2,50,400,'Log','Lin'],
'tabaxi': [1,18,95,'Lin','Lin'],
'tiefling': [1,18,115,'Lin','Lin'],
'kalashtar': [1,18,100,'Lin','Lin'],
'genasi': [1,18,120,'Lin','Exp'],
'aasimar': [1,18,160,'Lin','Exp']
}

aging_types = {
'Lin':'at a fairly constant rate',
'Log': 'mostly at the beginning',
'Exp': 'mostly at the end'}

reverse_aging_type = {
'Lin':'Lin',
'Log':'Exp',
'Exp':'Log'
    }

def a_an(text:str):
    vowels = ['a','e','i','o','u']
    an = False
    for i in vowels:
        if text.lower().startswith(i):
            an = True
    if an is True:
        out = 'an'
    else:
        out = 'a'
    return out

def run_model(input_value:float,model_type:str,training_X:list,training_Y:list):
    if model_type == 'Lin':
        model_result = lin_model(input_value,training_X,training_Y)
    elif model_type == "Log":
        model_result = log_model(input_value,training_X,training_Y)
    elif model_type == "Exp":
        model_result = exp_model(input_value,training_X,training_Y)
    else:
        print("Model type not supported.")
        model_result = None
    return model_result

def lin_model(input_value:float,training_X:list,training_Y:list):
    model_params = np.polyfit(training_Y, training_X, 1)
    print('Linear')
    print(model_params)
    model_result = model_params[0]*input_value + model_params[1]
    return model_result

def exp_model(input_value:float,training_X:list,training_Y:list):
    model_params = np.polyfit(training_Y, np.log(training_X), 1)
    print('Exponential')
    print(model_params)
    model_result = pow(e,model_params[0]*input_value)*pow(e,model_params[1])
    return model_result

def log_model(input_value:float,training_X:list,training_Y:list):
    model_params = np.polyfit(np.log(training_Y), training_X, 1)
    print('Logarithmic')
    print(model_params)
    model_result = model_params[0]*np.log(input_value) + model_params[1]
    return model_result

def race_to_human_age(age:int, race:str):
    human_data = race_life_data['human']
    race_data = race_life_data[race]
    infancy = race_data[0]
    adult =  race_data[1]
    death = race_data[2]
    maturation_type = race_data[3]
    aging_type = race_data[4]
    if age < 0:
        converted_age = 'unborn'
    elif age < infancy:
        converted_age = 'infant'
    elif age > death:
        converted_age = 'deceased'
    elif age < adult:
        X = [human_data[0],human_data[1]]
        Y = [infancy,adult]
        converted_age = run_model(age,maturation_type,X,Y)
    else:
        X = [human_data[1],human_data[2]]
        Y = [adult,death]
        converted_age = run_model(age,aging_type,X,Y)
    return converted_age

def human_to_race_age(age:float, race:str):
    human_data = race_life_data['human']
    human_infancy = human_data[0]
    human_adult = human_data[1]
    human_death = human_data[2]
    race_data = race_life_data[race]
    infancy = race_data[0]
    adult =  race_data[1]
    death = race_data[2]
    maturation_type = race_data[3]
    aging_type = race_data[4]
    if age < 0:
        converted_age = 'unborn'
    elif age < human_infancy:
        converted_age = 'infant'
    elif age > human_death:
        converted_age = 'deceased'
    elif age < human_adult:
        Y = [human_data[0],human_data[1]]
        X = [infancy,adult]
        converted_age = run_model(age,maturation_type,X,Y)
    else:
        Y = [human_data[1],human_data[2]]
        X = [adult,death]
        converted_age = run_model(age,aging_type,X,Y)
    return converted_age

def convert_race_ages(age:float, race_from:str, race_to:str):
    if is_numeric(age) is False:
        converted_age = age
    elif race_from == 'human':
        converted_age = human_to_race_age(age,race_to)
    elif race_to == 'human':
        converted_age = race_to_human_age(age,race_from)
    else:
        age_in_human = race_to_human_age(age,race_from)
        converted_age = human_to_race_age(age_in_human,race_to)
    return converted_age

def age_category(age:float, race:str):
    if is_numeric(age) is False:
        age_category = age
    else:
        infant = race_life_data[race][0]
        adult = race_life_data[race][1]
        death = race_life_data[race][2]
        if age < 0:
            age_category = 'unborn'
        elif age <= infant:
            age_category = 'infant'
        elif age <= adult:
            age_category = 'adolescent'
        elif age <= death:
            age_category = 'adult'
        else:
            age_category = 'deceased'
    return age_category

def race_age_info(race:str):
    infant = race_life_data[race][0]
    infant_months = round(infant*12)
    if infant % 1 != 0:
        if infant_months == 1:
            infant_text = f'{infant_months} month'
        else:
            infant_text = f'{infant_months} months'
    else:
        if infant == 1:
            infant_text = f'{infant} year'
        else:
            infant_text = f'{infant} years'
    adult = race_life_data[race][1]
    if adult == 1:
        adult_text = f'{adult} year'
    else:
        adult_text = f'{adult} years'
    death = race_life_data[race][2]
    death_text = f'{death} years'
    maturation_type = race_life_data[race][3]
    aging_type = race_life_data[race][4]
    if race == 'human':
        maturation_text = 'They'
        aging_text = ''
    elif aging_type == maturation_type:
        aging_explanation = aging_types[aging_type]
        if aging_type != 'Lin':
            maturation_text = f'They mature and experience aging {aging_explanation} of the these respective periods and'
        else:
            maturation_text = f'They mature and age {aging_explanation} and'
        aging_text = ''
    else:
        maturation_explanation = aging_types[maturation_type]
        maturation_text = f'They mature {maturation_explanation}'
        if maturation_type != 'Lin':
            maturation_text = maturation_text + ' of their adolescense'
        maturation_text = maturation_text + " and"
        aging_explanation = aging_types[aging_type]
        aging_text = f'{a_an(race).title()} {race} experiences the effects of further aging {aging_explanation}'
        if aging_type == 'Exp':
            aging_text = aging_text + ' of their life. '
        elif aging_type == 'Log':
            aging_text = aging_text + ' of their adulthood. '
        else:
            aging_text = aging_text + '. '
    out_text = f'Members of the {race.lower()} race are considered infants until the age of {infant_text}. {maturation_text} are considered mature at {adult_text} of age. {aging_text}A healthy {race.lower()} can live for around {death_text}.'
    return out_text