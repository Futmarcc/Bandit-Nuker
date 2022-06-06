import os
from dhooks import Webhook
from dhooks import Webhook
from colorama import Fore, init

os.system("title     Webhook Infos     $     Marcc#6666")

init()

hook = Webhook(input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Webhook: "))
hook.get_info()
print(f"\n {Fore.GREEN}[{Fore.GREEN}@{Fore.GREEN}]{Fore.RESET} GUILD ID: {hook.guild_id}")
print(f" {Fore.GREEN}[{Fore.GREEN}@{Fore.GREEN}]{Fore.RESET} CHANNEL ID: {hook.channel_id}")
print(f" {Fore.GREEN}[{Fore.GREEN}@{Fore.GREEN}]{Fore.RESET} USERNAME: {hook.default_name}")
print(f" {Fore.GREEN}[{Fore.GREEN}@{Fore.GREEN}]{Fore.RESET} IMAGE: {hook.default_avatar_url}")
os.system("pause >nul")
exit()