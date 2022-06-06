import requests
import random
import string
import time
import os
import colorama
from colorama import Fore, init, Back, Style

os.system("title     Nitro Generator     $     Marcc#6666")

num = int(input(f'{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Amount to gen & check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print(f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Please wait!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"{Fore.GREEN}[{Fore.GREEN}-->{Fore.GREEN}]{Fore.RESET} Generated {num} Codes!")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"{Fore.GREEN} Valid {Fore.RESET} | {nitro} ")
            break
        else:
            print(f"{Fore.RED} Invalid {Fore.RESET} | {nitro} ")

input(f"\n{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} Codes generated and saved to Nitro Codes.txt {Fore.RESET}")
