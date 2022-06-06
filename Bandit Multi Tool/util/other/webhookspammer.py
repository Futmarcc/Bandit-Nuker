import time
import requests
import colorama
import os
from colorama import Fore, init, Back, Style

os.system("title     Webhook Spammer     $     Marcc#6666")

msg = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Spam Message: ")
webhook = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Webhook: ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} Message got sent : [{msg}]")
        except:
            time.sleep(8)
            exit()
bandit = 1
while bandit == 1:
    spam(msg, webhook)
    