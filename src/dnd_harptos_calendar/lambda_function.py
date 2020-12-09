import math
import boto3
import json
import logging
import os
import subprocess

from base64 import b64decode
from subprocess import call

def parse_event(event):
    event_body = b64decode(event['body']).decode("utf-8")
    slack_data_dictionary={}
    data_fields=event_body.strip().split("&")
    for i in data_fields:
        [key,value] = i.split("=")
        slack_data_dictionary[key] = value
        
    return slack_data_dictionary

### CONSTANT DATA ###

Months={
    "1":["Hammer","Deepwinter",31],
    "2":["Alturiak","The Claw of Cold",30],
    "3":["Ches","The Claw of Sunsets",30],
    "4":["Tarsakh","The Claw of Storms",31],
    "5":["Mirtul","The Melting",30],
    "6":["Kythorn","The Time of Flowers",30],
    "7":["Flamerule","Summertide",31],
    "8":["Eleasis","Highsun",30],
    "9":["Eleint","The Fading",30],
    "10":["Marpenoth","Leaffall",31],
    "11":["Uktar","The Rotting",31],
    "12":["Nightal","The Drawing Down",30]
    }

Holidays={
        "Midwinter":"Hammer 31",
        "Greengrass":"Tarsakh 31",
        "Midsummer":"Flamerule 31",
        "Shieldmeet":"Flamerule 32",
        "Highharvesttide":"Eleint 31",
        "the Festival of the Moon":"Uktar 31",
        "the Vernal Equinox":"Ches 19",
        "the Summer Solstice":"Kythorn 20",
        "the Autumnal Equinox":"Eleint 21",
        "the Winter Solstice":"Nighttal 20"
        }
        
Birthdays={ #These are placeholder dates, unless no one wants to actually pick a birthday.
        "Ageneai":["Hammer 1",1609],
        "Lukas":["Ches 22",1536],
        "MV":["Tarsakh 13",1603],
        "Velbar":["Marpenoth 11",1597],
        "Ondros":["Nightal 6",1574],
        "a random peasant":["Marpenoth 11",1596] # for testing shared birthdays
        }

Holidays_Reverse={v: k for k, v in Holidays.items()}

Lunar_Period=30 + 10.5/24 # Length of Selune's cycle in days

### FUNCTIONS ###

def numth (num):
    Number_Endings=["th","st","nd","rd","th","th","th","th","th","th"]
    Numth="%s%s" % (str(int(num)),Number_Endings[int(str(int(num))[-1])])
    return Numth
    
def wordnum (num):
    Number_Words=["First","Second","Third","Forth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"]
    if int(num) > 12:
        Wordnum=numth(num)
    else:
        Wordnum=Number_Words[int(num)-1]
    return Wordnum
    
### BASIC DATE ###

#print("\n\n[ ~* CALENDAR OF HARPTOS *~ ]\n")

def calendar(Date_Text:str,Year:int=1635):

    messages = []

    if Year % 4 == 0:
        Shieldmeet_Year = True
        Days = 366
        Months["7"][2]+=1
    else:
        Shieldmeet_Year = False
        Days = 365

    messages.append("The year is {Year} DR.\n".format(Year=str(Year),Days=str(Days)))

    [Month_Num,Day_of_Month]=Date_Text.split("-")

    Tenday=int((int(Day_of_Month))/10)+1
    Day_of_Tenday=((int(Day_of_Month)) % 10)
    Day_of_Year=0
    for num in range(1,int(Month_Num)):
        Day_of_Year+=Months[str(num)][2]
    Day_of_Year+=int(Day_of_Month)
    Date_Text="{Month} {Day}".format(Month=Months[Month_Num][0],Day=Day_of_Month)
    messages.append("This is the {Day} of the month of {Month}, also known as {Alt}.\n".format(Day=numth(Day_of_Month),Month=Months[Month_Num][0],Alt=Months[Month_Num][1]))

    if (int(Day_of_Month) < 31):
        messages.append("It is the {NDay} Day of the {NTen} Tenday and {Day_of_Year} day of the year.\n".format(NDay=wordnum(Day_of_Tenday),NTen=wordnum(Tenday),Day_of_Year=numth(Day_of_Year)))
    else:
        messages.append("It is the {Day_of_Year} day of the year.\n".format(Day_of_Year=numth(Day_of_Year)))

    messages.append(moon_phase(Day_of_Year))
    messages.extend(special_day(Date_Text,Year))
    return messages
    
### MOON PHASE ###
def moon_phase(Day_of_Year:str,Year:int=1635):

    Days_Since_Zero=int((Year*365.25)+Day_of_Year)-1
    Cycle_Percent=(round((Days_Since_Zero % Lunar_Period)/Lunar_Period*100) % 100)/100
    #print("It has been %s days since the start of Year 0." % Days_Since_Zero)
    #print("We are now %s through a lunar cycle." % Cycle_Percent)

    Moon_Percent=abs(math.cos(Cycle_Percent*math.pi))

    if Moon_Percent > 0.999:
        Moon_Phase = "Full Moon"
    elif Moon_Percent < 0.035:
        Moon_Phase = "New Moon"
    else:
        if Cycle_Percent < 0.5: # First Half, Waning
            State = "Waning"
        else: # Second Half, Waxing
            State = "Waxing"
        if Moon_Percent < 0.45:
            Moon_Phase = "%s Crescent" % State
        elif Moon_Percent > 0.55:
            Moon_Phase = "%s Gibbous" % State
        else:
            Moon_Phase = "%s Half-Moon" % State
            
    moonphase = ("The phase of the moon is %s.\n" % Moon_Phase)

    return moonphase

### SPECIAL DAYS ###

def special_day(Date_Text:str,Year:int=1635):

    messages = []

    if Date_Text in Holidays_Reverse:
        messages.append("Today is {Holiday}!\n".format(Holiday=Holidays_Reverse[Date_Text]))
        
    Birthdays_Today=[]
    for Name in Birthdays:
        if Birthdays[Name][0] == Date_Text:
            Age=Year-Birthdays[Name][1]
            Text="{Name}'s {Age}".format(Name=Name,Age=numth(Age))
            Birthdays_Today.append(Text)
    if len(Birthdays_Today) > 0:
        messages.append("Today is %s's birthday!\n" % " and ".join(Birthdays_Today))

    return messages

def lambda_handler(event, context):
    error_message = "To access the Calendar of Harptos, you need to give either a date (1-1) or a year and date (1635 1-1)."
    slack_message = parse_event(event)
    text = slack_message['text'].replace("+"," ")
    response_url = slack_message['response_url'].replace('%2F','/').replace('%3A',':')
    channel_id = slack_message['channel_id']
    if slack_message['channel_name'] == "directmessage":
        is_direct = True
    else:
        is_direct = False
    if slack_message['command'].replace('%2F','/').startswith("/gm-"):
        is_gm = True
    else:
        is_gm = False
    split_text = text.split(' ')
    if len(split_text) > 1:
        try:
            year = int(split_text[0])
            date = split_text[1]
            messages = calendar(date,year)
            message_out = "".join(messages) #.replace("\n",' ')
            if is_direct or is_gm:
                to_return = {'statusCode':200,'body':message_out}
            else:
                os.system(f'curl -F token=xoxb-1024876019475-1071760249010-0fCbhu8NzXN2luAD6QGzGC44 -F channel={channel_id} -F text="{message_out}" https://slack.com/api/chat.postMessage')
                to_return = {'statusCode':200}
        except:
            to_return = {'statusCode':200, 'body':error_message}
    elif len(split_text) == 1:
        try:
            date = split_text[0]
            messages = calendar(date)
            message_out = "".join(messages) #.replace("\n",' ')
            if is_direct or is_gm:
                to_return = {'statusCode':200,'body':message_out}
            else:
                os.system(f'curl -F token=xoxb-1024876019475-1071760249010-0fCbhu8NzXN2luAD6QGzGC44 -F channel={channel_id} -F text="{message_out}" https://slack.com/api/chat.postMessage')
                to_return = {'statusCode':200}
        except:
            to_return = {'statusCode':200, 'body':error_message}
    else:
        to_return = {'statusCode':200, 'body':error_message}

    return to_return
