import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

os.system("title     Mass Report     $     Marcc#6666")

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system

print(f"""                                                                                          
{Fore.RED} x {Fore.RED}[{Fore.GREEN}-->{Fore.RED}] {Fore.RESET}Options
{Fore.RED} {1} {Fore.RED}[{Fore.GREEN}-->{Fore.RED}] {Fore.RESET}Illegal Conent
{Fore.RED} {2} {Fore.RED}[{Fore.GREEN}-->{Fore.RED}] {Fore.RESET}Harrassment
{Fore.RED} {3} {Fore.RED}[{Fore.GREEN}-->{Fore.RED}] {Fore.RESET}Spam or Phishing Links
{Fore.RED} {4} {Fore.RED}[{Fore.GREEN}-->{Fore.RED}] {Fore.RESET}Self harm
{Fore.RED} {5} {Fore.RED}[{Fore.GREEN}-->{Fore.RED}] {Fore.RESET}NSFW Content
""")

token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Invalid Token")
        input()
guild_id1 = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Server ID: ")
channel_id1 = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Channel ID: ")
message_id1 = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Message ID: ")
reason1 = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Option: ")


def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{Fore.GREEN} {Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Sent Report {b+Fore.BLUE}::{Fore.GREEN} ID {message_id1}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"MassReport By Marcc#6666 | Sent: %s" % sent)
      sent += 1
      
    elif r.status_code == 401:
      print(f"{Fore.RED} {Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.RED} {Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Error")


print()
for i in range(500, 1000):
    Thread(target=Main).start()