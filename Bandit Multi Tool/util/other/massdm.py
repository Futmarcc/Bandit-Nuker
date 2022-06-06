import discord
import colorama
import os
from colorama import Fore, init, Back, Style

os.system("title     Mass DM     $     Marcc#6666")

token = input(f'{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ')
message = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Message: ")

client = discord.Client()

@client.event
async def on_connect():
    for friend in client.user.friends:
        try:
            await friend.send(message)
            print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} Messaged {friend.name}")
        except:
            pass

    for channel in client.private_channels:
        try:
            await channel.send(message)
            print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} Sent MSG to {friend.name}")
        except:
            pass
            
client.run(token, bot=False)