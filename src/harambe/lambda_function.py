import math
import boto3
import json
import logging
import os
import subprocess

from base64 import b64decode
from subprocess import call

from commons.common_functions import choose
from commons.common_functions import parse_event
from commons.common_functions import slack_send
from commons.common_functions import textcode

from harambe import database as race_health_data
from harambe import race_donger_text
from harambe import donger_text
from harambe import describe_random_dong

info_message = "\n".join([':gorilla: _*DICKS OUT FOR HARAMBE*_ :gorilla:',
    '\nYou have discovered a secret command. It calculates penis sizes, because we are all very mature here.',
    '\n_*Command format options:*_',
    "\nRaces List: 'races' — Lists races with available info.",
    '\nRace Info: <race> — Gives you the statistical distribution for the race specified.',
    "\nRandomly Generate: 'random', 'random' <race>, or <race> 'random' — Generates a random individual and scores their assets.",
    '\nCalculate: This calculates metrics for a specific character.\n\tSpecify some/all of the following parameters as text followed by a colon:',
    '\t - race:<character race>',
    '\t - height:<height in inches or as ft.\'in.">',
    '\t - weight:<weight in lbs>',
    '\t - str:<strength score>',
    '\t - con:<constitution score>',
    '\t - cha:<charisma score>',
    '\t - roll:<1d20 die roll result>'])
    
error_message = 'Something went wrong. Maybe you tried to select a race that is not included yet, or maybe you just fucked up. Try again.'

def dong_command_handler(text:str):
    error = False
    out_text = None
    split_text = text.lower().split(' ')
    try:
        if len(text) == 0:
            out_text = info_message
        elif len(split_text) == 1:
            if split_text[0].lower() in race_health_data:
                out_text = race_donger_text(split_text[0])
            elif split_text[0].lower() == 'races':
                out_text = "The currently-supported races are as follows:\n\t" + "\n\t".join(list(race_health_data.keys())).title()
            elif split_text[0].lower() == 'random':
                race = choose(list(race_health_data.keys()))[0]
                out_text = describe_random_dong(race)
            elif split_text[0].lower().startswith('info'):
                out_text = info_message
            else:
                error=True
        elif len(split_text) == 2 and ((split_text[0].lower() in race_health_data and split_text[1].lower() == 'random') or (split_text[0].lower() == 'random' and split_text[1].lower() in race_health_data)):
            if split_text[0].lower() in race_health_data:
                race=split_text[0]
            else:
                race=split_text[1]
            out_text = describe_random_dong(race)
        else:
            roll=None
            height=None
            weight=None
            strength=None
            constitution=None
            charisma=None
        
            for i in split_text:
                if i.lower().startswith('race:'):
                    race = i.split(":").lower()
                elif ":" not in i and i in race_health_data:
                    race = i.lower()
                elif i.lower().startswith('roll:'):
                    roll=int(i.split(":")[1])
                elif i.lower().startswith('height:'):
                    height=i.split(":")[1]
                    if "'" in height:
                        feet = float(height.split("'")[0])
                        try:
                            inches = float(height.split("'")[1].replace('"',''))
                        except:
                            inches = 0.0
                        height = feet*12 + inches
                    else:
                        height = int(height)
                elif i.lower().startswith('weight:'):
                    weight=int(i.split(":")[1].split("l")[0])
                elif i.lower().startswith('str:'):
                    strength=int(i.split(":")[1])
                elif i.lower().startswith('con'):
                    constitution=int(i.split(":")[1])
                elif i.lower().startswith('cha'):
                    charisma=int(i.split(":")[1])
                else:
                    pass
        
            if race is None:
                race='human'
            if roll is None:
                roll=10
            if height is None:
                height = race_health_data[race]['height']
            if weight is None:
                weight = race_health_data[race]['weight']
            if strength is None:
                if 'str' in race_health_data[race]:
                    strength = race_health_data[race]['str']
                else:
                    strength = 10
            if constitution is None:
                if 'con' in race_health_data[race]:
                    constitution = race_health_data[race]['con']
                else:
                    constitution = 10
            if charisma is None:
                if 'cha' in race_health_data[race]:
                    charisma = race_health_data[race]['cha']
                else:
                    charisma = 10
            out_text = donger_text(race=race,roll=roll,height=height,weight=weight,strength=strength,constitution=constitution,charisma=charisma)
    except Exception as err:
            error=True
            err_txt=str(err)
    if error is True:
        out_text = ''
    return out_text


def lambda_handler(event, context):
    slack_message = parse_event(event)
    text = textcode(slack_message['text'].replace("+"," "))
    response_url = slack_message['response_url'].replace('%2F','/').replace('%3A',':')
    channel_id = slack_message['channel_id']
    user_id = slack_message['user_id']
    user_name = slack_message['user_name']
    command = slack_message['command'].replace('%2F','')
    try:
        if slack_message['channel_name'] == "directmessage":
            is_direct = True
        else:
            is_direct = False
        if command == 'harambe':
            try:
                message_out = dong_command_handler(text)
                if len(message_out) == 0:
                    to_return = {'statusCode':200,'body':error_message}
                else:
                    #message_out = f"<@{user_id}|{user_name}>: {message_out}"
                    to_return = {'statusCode':200,'body':message_out}
            except Exception as err:
                to_return = {'statusCode':200,'body':error_message}
    except Exception as err:
        to_return = {'statusCode':200,'body':error_message}
    return to_return
