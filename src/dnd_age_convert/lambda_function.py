import math
#import boto3
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

try:
    from age_convert import race_life_data
    from age_convert import race_age_info
    from age_convert import age_category
    from age_convert import convert_race_ages
    from age_convert import a_an
    error_text = ''
except Exception as err:
    error_text = str(err)


def age_command_handler(text:str):
    error = False
    out_text = None
    split_text = text.lower().split(' ')
    print(split_text)
    if len(split_text) == 0 or len(split_text) > 3:
        to_return = {'statusCode':200, 'body':error_message}
    elif len(split_text) == 1:
        if split_text[0] in race_life_data:
            to_race = split_text[0]
            from_race = None
            age = None
            mode = "info"
        else:
            error=True
    elif len(split_text) == 2:
        if split_text[0] in race_life_data and is_numeric(split_text[1]):
            mode = "convert"
            from_race = split_text[0]
            to_race = "human"
            age = split_text[1]
            age_numeric = float(age)
        elif is_numeric(split_text[0]) and split_text[1] in race_life_data:
            mode = "convert"
            from_race = "human"
            to_race = split_text[1]
            age = split_text[0]
            age_numeric = float(age)
        else:
            error=True
    elif len(split_text) == 3:
        if split_text[0] in race_life_data and is_numeric(split_text[1]) and split_text[2] in race_life_data:
            mode = "convert"
            from_race = split_text[0]
            to_race = split_text[2]
            age = split_text[1]
            age_numeric = float(age)
        else:
            error = True
    else:
        error = True
    if error:
        pass
    else:
        if mode == "convert":
            if age_numeric <= 0:
                out_text = "I'm terribly sorry, but I'm not sure how I would calculate the age of someone who has not yet been born..."
            else:
                result_age = convert_race_ages(age_numeric,from_race,to_race)
                if is_numeric(result_age):
                    result_age = int(round(result_age))
                    category = age_category(result_age, to_race)
                    if from_race != to_race:
                        out_text = f'{a_an(from_race).title()} {from_race} aged {age} years is an {category}, equivalent to {a_an(to_race).lower()} {to_race} of {result_age} years.'
                    else:
                        out_text = f'{a_an(from_race).title()} {from_race} aged {age} years is considered to be an {category}.'
                else:
                    if result_age == 'deceased':
                        out_text = f'At the age of {age} years, {a_an(from_race).lower()} {from_race} is most likely to be deceased.'
                    else:
                        out_text = f'At the age of {age} years, {a_an(from_race).lower()} {from_race} is considered to be an {result_age}.'
        else:
            out_text = race_age_info(to_race)
    return out_text


def lambda_handler(event, context):
    age_error_message = "Something went wrong. Either your age-conversion request is improperly formatted, or life-history data for that race is not available yet."
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
    if command == 'age' or command == 'gm-age':
        if text.lower().startswith('info') or len(text.strip()) < 1:
            races_available = []
            for i in race_life_data:
                races_available.append(i.strip().title())
            races_available.sort()
            message_out = "The races for which life-history information is available are:\n\t‣ " + "\n\t‣ ".join(races_available)
            to_return = {'statusCode':200,'body':message_out}
        else:
            try:
                message_out = age_command_handler(text)
                if is_gm or is_direct:
                    to_return = {'statusCode':200,'body':message_out}
                elif len(message_out) == 0:
                    to_return = {'statusCode':200,'body':age_error_message}
                else:
                    message_out = f"<@{user_id}|{user_name}>: {message_out}"
                    cmd=slack_send(message_out,channel_id)
                    to_return = {'statusCode':200}
            except Exception as err:
                error_text = error_text + str(err)
                to_return = {'statusCode':200,'body':age_error_message + error_text}
    else:
        to_return = {'statusCode':200,'body':missing_message}
    return to_return
