from commons.common_functions import choose
from random import randint,gammavariate

from import_names import names

names['gnome']['nicks'] = names['tabaxi']['nouns']*5 + names['tabaxi']['adjectives']*3 + names['goblin']['parts']

type_options = ['first_last']*5 + ['two_first_last']*3 + ['first_nick_last']*7 + ['two_first_nick_last']*2 + ['first_two_last']*3 + ['first_nick_two_last']*5 + ['two_first_nick_two_last']*1 + ['academic']*3

nick_options = ['beginning', 'ending', 'separate']

def get_first(race:str = 'gnome', sex:str = 'both',names:dict=names):
    if sex == 'both' or sex == 'any':
        given_name = choose((names[race]['male'] + names[race]['female'] + names[race]['both']),1)[0]
    else:
        given_name = choose((names[race][sex] + names[race]['both']),1)[0]
    return given_name.title()

def get_nick(real_name: str=None, nick_format:str=None):
    if real_name is None:
        nick_format = 'separate'
    else:
        real_name = list(real_name)
    if nick_format is None:
        nick_format = choose(nick_options,1)[0]
    if nick_format == 'beginning':
        letters = randint(1,min(5,len(real_name)-1))
        nickname = []
        for i in range(0,letters):
            nickname = nickname + [real_name[i]]
    elif nick_format == 'ending':
        letters = randint(2,min(6,len(real_name)-1))
        real_name.reverse()
        nickname = []
        for i in range(0,letters):
            nickname = nickname + [real_name[i]]
        nickname.reverse()
    else:
        nickname=choose(names['gnome']['nicks'],1)[0]
    return "".join(nickname).title()

def get_academic_titles():
    titles = choose(names["gnome"]["titles"],round(gammavariate(0.75,2.5)))
    for i in range(0,len(titles)):
        if '{craft}' in titles[i]:
            titles[i] = titles[i].format(craft=choose(['Al','Br','Cl','Cp','Cg','Co','Co','Gb','J','L','M','P','S','T','We','Wo','M','Th','N'],1)[0],)
    titles = list(set(titles))
    for i in range(0,len(titles)):
        if '{artifice}' in titles[i]:
            titles[i] = titles[i].format(artifice=choose(['Al','Ar','Bs'],1)[0])
    return titles

def get_gnome_names(count:int=1,sex:str='both'):
    names_list = []
    name_types = choose(type_options,count)
    for pick in name_types:
        if pick == 'first_last':
            name = f'{get_first("gnome", sex)} {choose(names["gnome"]["family"],1)[0]}'
        elif pick == 'two_first_last':
            name = f'{get_first("gnome", sex)} {get_first("gnome",choose([sex,"both"],1)[0])} {choose(names["gnome"]["family"],1)[0]}'
        elif pick == 'first_nick_last':
            first_name = get_first("gnome", sex)
            nickname = get_nick(first_name)
            name = f'{first_name} \'{nickname}\' {choose(names["gnome"]["family"],1)[0]}'
        elif pick == 'two_first_nick_last':
            firstnames = [get_first("gnome", sex),get_first("gnome",choose([sex,"both"],1)[0])]
            nickname = get_nick(choose(firstnames,1)[0])
            name = f'{firstnames[0]} {firstnames[1]} \'{nickname}\' {choose(names["gnome"]["family"],1)[0]}'
        elif pick == 'first_two_last':
            name = f'{get_first("gnome", sex)} {choose(names["gnome"]["family"],1)[0]}-{choose(names["gnome"]["family"],1)[0]}'
        elif pick == 'first_nick_two_last':
            first_name = get_first("gnome", sex)
            nickname = get_nick(first_name)
            name = f'{first_name} \'{nickname}\' {choose(names["gnome"]["family"],1)[0]}-{choose(names["gnome"]["family"],1)[0]}'
        elif pick == 'two_first_nick_two_last':
            firstnames = [get_first("gnome", sex),get_first("gnome",choose([sex,"both"],1)[0])]
            nickname = get_nick(choose(firstnames,1)[0])
            name = f'{firstnames[0]} {firstnames[1]} \'{nickname}\' {choose(names["gnome"]["family"],1)[0]}-{choose(names["gnome"]["family"],1)[0]}'
        elif pick == 'academic':
            titles = get_academic_titles()
            name = ", ".join([f'{get_first("gnome", sex)} ob {get_first("gnome","both")}'] + titles)
        else:
            pick = 'first_last'
            name = f'{get_first("gnome", sex)} {choose(names["gnome"]["family"],1)[0]}'
        if pick != 'academic':
            name = name.title()
        names_list.append(name)
        
    return names_list
    
    
#def get_general_names(race:str="human",sex:str="both",count:int=1,names:dict=names):
#    
#    names_list=[]
#
#    
#    surname_options = names[race]['family']
#    givens = choose(given_name_options,count)
#    surnames = choose(surname_options,count)
#    
#    for i in range(0,count):
#        names_list.append(f'{givens[i]} {surnames[i]}'.strip())
#    
#    return names_list