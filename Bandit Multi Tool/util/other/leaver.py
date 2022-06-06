import discord
import colorama
from colorama import Fore, init, Back, Style

client = discord.Client()
token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ")



@client.event
async def on_ready():
    for guild in client.guilds:
        try:
            if guild.id:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} {e}")


client.run(token, bot=False)