import discord
import os
import colorama
from colorama import Fore, init, Back, Style

os.system("title     Nickname Changer     $     Marcc#6666")

client = discord.Client()

token = input(f'{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ')
username = input (f'{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} New Nickname: ')

@client.event
async def on_ready():
    await client.edit_profile(password=None, username=username)
    
client.run(token, bot=False)