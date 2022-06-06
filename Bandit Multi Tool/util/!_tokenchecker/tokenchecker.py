from requests import get, post
from random import randint
import colorama
import os
from colorama import Fore, init, Back, Style

os.system("title     Token Checker     $     Marcc#6666")

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET}You need to verify for this tool!" in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Verify account for this action!" in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open("tokens.txt","r") as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                    print(f'{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} {token} {Fore.GREEN}valid')
                    checked.append(token)
                else:
                    print(f'{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} {token} {Fore.RED}invalid')
        if len(checked) > 0:
            save = input(f'{len(checked)} \n{banner}{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Save vaild tokens? (y/n)').lower()
            if save == 'y':
                name = randint(100000000, 9999999999)
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(f'Tokens Save To {name}.txt File!')
        input('Exit BANDIT Nuker')
    except:
        input(f'{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Tokens.txt not found!')