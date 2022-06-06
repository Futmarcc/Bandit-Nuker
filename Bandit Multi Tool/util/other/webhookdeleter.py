import time
import os
from colorama import Fore, init
import requests
init()

os.system("title     Webhook Deleter     $     Marcc#6666")

webhook = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Webhook: ")

def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print(f"\n{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} Webhook deleted!")
        os.system("pause >nul")  # Pause command in Batch (press any key to exit the code)
    elif check.status_code == 200:
        print(F"\n{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} webhhok delete failed!")
        os.system("pause >nul")

test = requests.get(webhook)
if test.status_code == 404:
    print(f"\n{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Invalid Webhook!")
    os.system("pause >nul")
elif test.status_code == 200:
    print(f"\n{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} Webhook Is valid")
    delete()