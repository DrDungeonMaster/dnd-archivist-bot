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
from commons.common_functions import slack_reply
from commons.common_functions import textcode

from dice_roller import parse_roll
from dice_roller import hide_fudging
#from dice_roll_tester import test_dice

gm_users=['U010PH3H5HQ']

def diceroll_command_handler(text:str):
    text = " "+ text.strip()
    sub_text,clusters,dice_total,dice_range,fudged_rolls=parse_roll(text)
    if dice_total % 1 == 0:
        dice_total = int(dice_total)
    rolls_list = []
    for c in clusters:
        for r in range(0,len(clusters[c]['rolls'])):
            if c.endswith('d20') and len(clusters[c]['rolls']) <= 2:
                if str(clusters[c]['rolls'][r]) == '20':
                    clusters[c]['rolls'][r] = ':nat-20:'
                elif str(clusters[c]['rolls'][r]) == '1':
                    clusters[c]['rolls'][r] = ':crit-fail:'
            if 'r' in clusters[c]['rolls'][r] and ':' not in clusters[c]['rolls'][r]:
                clusters[c]['rolls'][r] = '~' + clusters[c]['rolls'][r].replace('r','~ _') + '_'
            if 'd' in clusters[c]['rolls'][r]:
                clusters[c]['rolls'][r] = '~' + clusters[c]['rolls'][r].replace('d','~')
        cluster_string = f"{c.split(':')[1]}: {' '.join(clusters[c]['rolls'])}"
        rolls_list.append(cluster_string)
    rolls_text = '\t' + "\n\t".join(rolls_list) + '\n'
    if dice_range[0] == dice_range[1]:
        dice_range_text = ''
    else:
        dice_range_text = f'  [{dice_range[0]},{dice_range[1]}]'
    if is_numeric(sub_text):
        if len(rolls_list) == 0:
            rolls_text = ''
            label = 'Value'
        else:
            label = 'Total'
        out_text = f'{rolls_text}*{label}: {dice_total}*{dice_range_text}'
    else:
        out_text = f'*{sub_text}*\n{rolls_text}*Total: {dice_total}*{dice_range_text}'
    return out_text, fudged_rolls


def lambda_handler(event, context):
    short_message= "It appears you did not include any text with your command. Please give me something to work with."
    missing_message = "Something went wrong. You may have stumbled upon a planned feature that is not yet implemented."
    slack_message = parse_event(event)
    text = textcode(slack_message['text'].replace("+"," "))
    response_url = slack_message['response_url'].replace('%2F','/').replace('%3A',':')
    channel_id = slack_message['channel_id']
    user_id = slack_message['user_id']
    user_token = slack_message['token']
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
    if command == 'roll':
        try:
            message_out,is_fudged = diceroll_command_handler(text)
            if is_fudged:
                if user_id in gm_users:
                    message_out = f'/{command} {hide_fudging(text)}\n\n' + message_out
                else:
                    message_out = f'/{command} {text}\n\n' + message_out + '\n\n:exclamation: *THIS ROLL WAS FUDGED WITHOUT AUTHORIZATION* :exclamation:'
            else:
                message_out = f'/{command} {text}\n\n' + message_out
            if is_gm:
                to_return = {'statusCode':200,'body':message_out}
            elif is_direct:
                message_out = f"<@{user_id}|{user_name}>: {message_out}"
                cmd=slack_reply(message_out,channel_id,response_url)
                to_return = {'statusCode':200}
            elif len(message_out) == 0:
                to_return = {'statusCode':200,'body':short_message}
            else:
                message_out = f"<@{user_id}|{user_name}>: {message_out}"
                cmd=slack_send(message_out,channel_id)
                to_return = {'statusCode':200}
        except Exception as err:
            error_text = error_text + str(err)
            to_return = {'statusCode':200,'body':error_text}
    else:
        to_return = {'statusCode':200,'body':missing_message}
    return to_return
