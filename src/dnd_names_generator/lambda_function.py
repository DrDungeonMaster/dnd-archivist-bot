import math
import json
import logging
import os
import subprocess

from random import randint
from base64 import b64decode
from subprocess import call

from commons.common_functions import choose
from commons.common_functions import parse_event
from commons.common_functions import is_numeric
from commons.common_functions import arrange
from commons.common_functions import slack_send

from import_names import names
from hybrid_names import hybrid_options

from general_names import get_general_names
from hybrid_names import get_hybrid_names
from goblin_names import get_goblin_names
from tabaxi_names import get_tabaxi_names
from gnome_names import get_gnome_names

from shop_names import get_shop_names
from shop_names import categories_dict as shop_categories

for i in hybrid_options:
    names[i]=hybrid_options[i]
    

def get_names(race:str='human',sex:str='both',count:int=1):
    names_list = []
    if race == 'goblin':
        sex = None
        names_list = get_goblin_names(count)
    elif race == 'tabaxi':
        sex = None
        names_list = get_tabaxi_names(count)
    elif race in hybrid_options:
        [race_1,race_2] = hybrid_options[race]['parent_races']
        [r1_given_rate,r1_surname_rate] = hybrid_options[race]['mix']
        names_list = get_hybrid_names(count=count,race_1=race_1,race_2=race_2,r1_given_rate=r1_given_rate,r1_surname_rate=r1_surname_rate)
    elif race == 'gnome':
        names_list = get_gnome_names(count,sex)
    elif race in names:
        names_list = get_general_names(race,sex,count)
    else:
        names_list = []
    if race == 'orc':
        for i in range(0,len(names_list)):
            names_list[i] = names_list[i].upper()
    return names_list

def names_command_handler(text:str):
    split_text = text.split(' ')
    if len(split_text) == 0 or len(split_text) > 3:
        to_return = {'statusCode':200, 'body':error_message}
    elif len(split_text) == 1:
        if split_text[0] in names:
            race = split_text[0]
            count = 10
            sex = 'both'
        elif is_numeric(split_text[0]):
            race = 'human'
            count = int(split_text[0])
            sex = 'both'
        elif split_text[0] in names['human']:
            race = 'human'
            count = 10
            sex = split_text[0]
        else:
            error=True
    elif len(split_text) == 2:
        if split_text[0] in names:
            race = split_text[0]
            if is_numeric(split_text[1]):
                count = int(split_text[1])
                sex = 'both'
            else:
                count = 10
                sex = split_text[1]
        else:
            race = 'human'
            sex = split_text[0]
            count = int(split_text[1])
    else:
        race = split_text[0]
        sex = split_text[1]
        count = int(split_text[2])
        
    generated_names = get_names(race,sex,count)
    if count > 1:
        s = 's'
    else:
        s = ''
    if sex != 'both':
        race_gender = f'{sex} {race}'
    else:
        race_gender = f'{race}'
    explanation = f'Generated {count} {race_gender} name{s}:'
    
    return generated_names,explanation

def shop_names_handler(text:str):
    number = 10
    keywords = text.replace(","," ").split(" ")
    keywords_valid = []
    for i in keywords:
        if is_numeric(i):
            number = int(i)
        elif type(i) is str and i in shop_categories:
            keywords_valid.append(i)
        else:
            pass
    generated_names = get_shop_names(" ".join(keywords_valid),number)
    explanation = f'Generated {number} shop names with the keywords {str(keywords_valid)}:'
    
    return generated_names,explanation

def lambda_handler(event, context):
    names_error_message = "Something went wrong. Either your names request was improperly formatted, or that race is not available yet."
    shops_error_message = "Something went wrong. It is likely that your shops names request was improperly formatted, or contained no usable keywords."
    missing_message = "Something went wrong. You may have stumbled upon a planned feature that is not yet implemented."
    slack_message = parse_event(event)
    text = slack_message['text'].replace("+"," ")
    response_url = slack_message['response_url'].replace('%2F','/').replace('%3A',':')
    channel_id = slack_message['channel_id']
    user_id = slack_message['user_id']
    user_name = slack_message['user_name']
    command = slack_message['command'].replace('%2F','')
    if slack_message['channel_name'] == "directmessage":
        is_direct = True
    else:
        is_direct = False
    if slack_message['command'].replace('%2F','/').startswith("/gm-"):
        is_gm = True
    else:
        is_gm = False
    if command == 'names' or command == 'gm-names':
        if text.lower().startswith('info') or len(text.strip()) < 1:
            races_available = []
            for i in names:
                races_available.append(i.strip().title())
            message_out = "The races for which generated names are currently available are:\n\t‣ " + "\n\t‣ ".join(races_available)
            to_return = {'statusCode':200,'body':message_out}
        else:
            try:
                names_list,explanation = names_command_handler(text)
                names_list = [f'\t{i}' for i in names_list]
                message_out = f'{explanation}\n{arrange(names_list,1)}'
                if len(names_list) > 20 or is_gm or is_direct:
                    to_return = {'statusCode':200,'body':message_out}
                elif len(names_list) == 0:
                    to_return = {'statusCode':200,'body':names_error_message}
                else:
                    message_out = f"<@{user_id}|{user_name}>: {message_out}"
                    cmd=slack_send(message_out,channel_id)
                    to_return = {'statusCode':200}
            except:
                to_return = {'statusCode':200,'body':names_error_message}
    elif command == 'shops' or command == 'gm-shops':
        if text.lower().startswith('info') or len(text.strip()) < 1:
            categories_available = []
            for i in shop_categories.keys():
                categories_available.append(i.strip().title())
            categories_available = sorted(categories_available)
            message_out = "The shop keywords currently available are:\n\t‣ " + "\n\t‣ ".join(categories_available)
            to_return = {'statusCode':200,'body':message_out}
        else:
            try:
                names_list,explanation = shop_names_handler(text)
                names_list = [f'\t{i}' for i in names_list]
                message_out = f'{explanation}\n{arrange(names_list,1)}'
                if len(names_list) > 20 or is_gm or is_direct:
                    to_return = {'statusCode':200,'body':message_out}
                elif len(names_list) == 0:
                    to_return = {'statusCode':200,'body':error_message}
                else:
                    message_out = f"<@{user_id}|{user_name}>: {message_out}"
                    cmd=slack_send(message_out,channel_id)
                    to_return = {'statusCode':200}
            except:
                to_return = {'statusCode':200,'body':shops_error_message}
    else:
        to_return = {'statusCode':200,'body':missing_message}
    return to_return
