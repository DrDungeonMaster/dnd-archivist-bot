import os

from random import randint
from base64 import b64decode

from commons.slack_params import token

symbol_conversions={
    "%20":" ",
    "%21":"!",
    "%22":'"',
    "%23":"#",
    "%24":"$",
    "%25":"%",
    "%26":"&",
    "%27":"'",
    "%28":"(",
    "%29":")",
    "%30":"*",
    "%2B":"+",
    "%2C":",",
    "%2D":"-",
    "%2E":".",
    "%2F":"/",
    "%3A":":",
    "%3B":";",
    "%3C":"<",
    "%3D":"=",
    "%3E":">",
    "%3F":"?",
    "%40":"@",
    "%5B":"[",
    "%5C":"\\",
    "%5D":"]",
    "%5E":"^",
    "%5F":"_",
    "%60":"`"
}

def choose(choices_list:list, num:int = 1):
    if type(choices_list) is set:
        choices_list = list(choices_list)
    elif type(choices_list) is dict:
        try:
            new_choices = []
            for i in choices_list:
                new_choices.extend([i]*choices_list[i])
            choices_list = new_choices
        except ValueError:
            choices_list = list(choices_list)
    out_choices = []
    n_options = len(choices_list)-1
    for i in range(1,num+1):
        out_choices.append(choices_list[randint(0,n_options)])
    return out_choices

def choose_separate(list_A:list,list_B:list):
    choice_A = ""
    choice_B = ""
    while choice_A == choice_B:
        choice_A = choose(list_A)[0]
        choice_B = choose(list_B)[0]
    return [choice_A,choice_B]

def parse_event(event):
    event_body = b64decode(event['body']).decode("utf-8")
    slack_data_dictionary={}
    data_fields=event_body.strip().split("&")
    for i in data_fields:
        [key,value] = i.split("=")
        slack_data_dictionary[key] = value
    return slack_data_dictionary

def is_numeric(string:str):
    try:
        value=float(string)
        numeric=True
    except ValueError:
        numeric=False
    return numeric

def textcode(text:str):
    for i in symbol_conversions:
        text = text.replace(i,symbol_conversions[i])
    return text

def arrange(text_list: list, per_row: int=1, lead_string: str=''):
    out_string = f'{lead_string}'
    for i in range(0,len(text_list)):
        if i % per_row == 0:
            if i == 0:
                pass
            else:
                out_string = out_string + f"\n{lead_string}"
        else:
            out_string = out_string + f"\t{lead_string}"
        out_string = out_string + text_list[i]
    return out_string


def slack_send(message: str, channel: str, token: str=token):
    cmd = f"curl -d token={token} -d channel={channel} -d as_user=true -d response_type=\"in_channel\" --data-urlencode text=\"{message}\" https://slack.com/api/chat.postMessage"
    os.system(cmd)
    return cmd

def slack_reply(message:str, channel:str, response_url:str, token:str=token):
    json_msg = '\'{' + f'"text":"{message}","token":"{token}","response_type":"in_channel"' + '}\''
    cmd = f'curl -X POST -H \'Content-type: application/json\' --data {json_msg} {response_url}'
    os.system(cmd)
    return cmd