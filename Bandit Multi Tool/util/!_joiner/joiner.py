import requests
import colorama
import os
from colorama import Fore, init, Back, Style

os.system("title     Server Joiner     $     Marcc#6666")

link = input(f'{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Server Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print (f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} Tokens joined!")