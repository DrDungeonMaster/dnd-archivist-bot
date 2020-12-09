import math
import boto3
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

from dnd_loot_generator import generate_loot_text

def loot_command_handler(text:str):
    error=False
    split_text = text.split(' ')
    if split_text[0] == '':
        amount = randint(100,35000)
    elif len(split_text) == 1:
        amount = int(split_text[0])
    else:
        pass
    generated_loot = generate_loot_text(amount)
    explanation = f'Generated {amount} Gold worth of loot:'
        
    return generated_loot,explanation

def lambda_handler(event, context):
    loot_error_message = "Something went wrong -- no loot was generated. Your request may have been improperly formatted."
    loot_insufficient_message = "Something went wrong -- no loot was generated. Your specified loot amount may have been too low ..."
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
    if command == 'loot' or command == 'gm-loot':
        if text.lower().startswith('info'):
            message_out = "Currently, loot generation can take one parameter: an integer amount of Gold. If no amount is specified, an amount between 100 and 35,000 Gold will be chosen randomly."
            to_return = {'statusCode':200,'body':message_out}
        else:
            try:
                generated_loot,explanation = loot_command_handler(text)
                if len(generated_loot) == 0:
                    to_return = {'statusCode':200,'body':loot_insufficient_message}
                else:
                    message_out = f'{explanation}\n{generated_loot}'
                    if is_gm or is_direct:
                        to_return = {'statusCode':200,'body':message_out}
                    elif len(generated_loot) < 1:
                        to_return = {'statusCode':200,'body':loot_error_message}
                    else:
                        message_out = f"<@{user_id}|{user_name}>: {message_out}"
                        cmd=slack_send(message_out,channel_id)
                        to_return = {'statusCode':200}
            except:
                to_return = {'statusCode':200,'body':loot_error_message}
    else:
        to_return = {'statusCode':200,'body':missing_message}
    return to_return
