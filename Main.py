import random,requests
from random import randint,randrange
import time
from time import strftime
import datetime 
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound,CheckFailure, MissingRequiredArgument
import platform
from flask import Flask
from threading import Thread
import asyncio
import datetime
import os
import traceback
import json
import logging
import args
from discord.utils import get
import bs4
from bs4 import BeautifulSoup
import urllib3
import re
import praw
import string
import corona
import aiohttp
from time import gmtime
import humanfriendly
from os import system
import youtube_dl
from discord import FFmpegPCMAudio
import ffmpeg
import PIL
from PIL import Image, ImageDraw, ImageFont
import io

TOKEN = "your bot token here"

u = (random.randint(100,200))

dice = (random.randint(1,6))

amounts = {}

l = float('inf')

bot= commands.Bot('skull ')

def cooldown(rate, per_sec=0, per_min=0, per_hour=0, per_day=0,type=commands.BucketType.default):
    return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour + 86400 * per_day, type)

@bot.event	  
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name=f"skull help | {str(len(bot.guilds))} servers",url="https://www.twitch.tv/philipmarkjames/"))
  global amounts
try:
 with open('amounts.json') as f:
  amounts = json.load(f)
except FileNotFoundError:
  print("Could not load amounts.json")
  amounts = {}

  
@bot.event
async def on_dbl_vote(data):
  print(data)
  id=str(data.author.id)
  if id in amounts:
    amounts[id] += 10000
    await data.author.send("Hey, thanks for voting!")
    


                      
@bot.command()
async def premium(ctx):
    homeGuild = bot.get_guild(1234567890)  # Home Guild/Support Server; where user has "Patreon" role.
    patreonRole = get(homeGuild.roles, id=int(1234567890))  # Patreon role id
    member = []

    for pledger in homeGuild.members:
        if pledger == ctx.author:
            member = pledger

    if patreonRole in member.roles:
        await ctx.send("You are a Patreon.")
    else:
        await ctx.send("You are not a Patreon.")
                              
  

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
      await ctx.message.delete()
      await ctx.send("❌Command not found",delete_after=1)
      return
#share improve this answer follow
    elif isinstance(error,CheckFailure):
      await ctx.send("❌You don't had enough permission to execute this command")
      return
    elif isinstance(error,commands.CommandOnCooldown):
      seconds = error.retry_after
      m, s = divmod(seconds, 60)
      h, m = divmod(m, 60)
      d, h = divmod(h, 24)
      await ctx.send(f"You're on cooldown. Please wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds")
      return
   
@bot.event
async def on_guild_join(guild):
 for member in guild.members:
  id = member.id
  ids = [member.id for member in guild.members]
  for id in ids:
    # Do stuff here
    if id not in amounts:
       amounts[id] = 0
       _save
    for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
       link = bot.create_invite(max_age=0)
       channele = bot.get_channel(1234567890)#your channel id
  
       channele.send(link)
    e=discord.Embed(color=0x3366FF)
    e.add_field(name="Nice server! :slight_smile:",value="Thanks for adding me to your server :wink:, type `skull help` to get started! Join our [support server](https://discord.gg/Cf5a28H) if you need any help.")
    channel.send(embed=e)
    break


class LeaderBoardPosition:

    def __init__(self, user, coins):
        self.user = user
        self.coins = coins

leaderboards = []

for key, value in amounts.items():
 leaderboards.append(LeaderBoardPosition(key, value))

top = sorted(leaderboards, key=lambda x: x.coins, reverse=True)

@bot.command()
async def leaderboard(message,user:discord.User=None):
 ido = str(message.author)
 lol = await bot.fetch_user(top[0].user)
 loli = lol.name
 lol1 = await bot.fetch_user(top[1].user)
 loli1 = lol1.name
 lol2 = await bot.fetch_user(top[2].user)
 loli2 = lol2.name
 print(lol)
 print(loli)
 await asyncio.sleep(1)
 e=discord.Embed(color=0x3366FF,title="**__Top 3 richest users(global)__**",description=f"**🥇** {lol} with {top[0].coins} Blue coins\n"                  
 f"**🥈** {lol1} with {top[1].coins} Blue coins\n"
         f"**🥉** {lol2} with {top[2].coins} Blue coins\n")
 await message.channel.send(embed=e)
#share improve this answer follow


@bot.command()
@commands.has_permissions(manage_roles=True)
async def setautorole(ctx,arg:discord.Role=None):
    print(ctx.guild.id)
    with open("auto.json") as f:
       data = json.load(f)
       print(data)
       id = str(ctx.guild.id)
    if id not in data:
      data[id]=int(arg.id)
      print(data[id])
      with open("auto.json", 'w') as f:
        json.dump(data, f)
        await ctx.send(f"{arg.mention} will be assigned to new members!")

@bot.command()
async def autorole(ctx):
  with open("auto.json") as f:
   data=json.load(f)
   if data in str(ctx.guild.id):
   # data=json.load(f)
    role=data[str(ctx.guild.id)]
    await ctx.send(f"<&{int(role)}>")
   else:
    await ctx.send("There's no auto roles.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removeautorole(ctx,arg:discord.Role=None):
  with open("auto.json") as f:
    data = json.load(f)
    id = str(ctx.guild.id)
    del data[id]
    await ctx.send(f"{arg.mention} will no longer be assigned to new members!")
    with open("auto.json", 'w') as f:
        json.dump(data, f)
        

@bot.event
async def on_member_join(member):
  with open("auto.json") as f:
   roles = json.load(f)
   role = roles[str(member.guild.id)]
   print(role)
   rolel = int(role)
   print(rolel)
   rolee = discord.utils.get(member.guild.roles, id = rolel )
   print(rolee)
   await member.add_roles( rolee  ) 


@bot.command() 
@commands.has_permissions(manage_channels = True)
async def nuke(ctx):
  p = ctx.channel.position
  print(p)
  clhannel = await ctx.channel.clone()
  await ctx.channel.delete()
  await clhannel.send("✅ Nuked this channel.")
  await clhannel.edit(position=int(p))

@bot.command()
async def membercount(ctx):
  await ctx.send(f"{len(ctx.guild.members)} members") 

@bot.command()#Creates a NSFW channel
async def NewNSFW(ctx, *, name):
  await ctx.guild.create_text_channel(name,nsfw=True)

@bot.command()#Creates a new category 
async def NewCategory(ctx, *, name):
    await ctx.guild.create_category(name)

@bot.command()#Creates a new voice channel 
async def NewVoice(ctx, *, name):
    await ctx.guild.create_voice_channel(name)


 
@bot.command()#Deletes the channel
@commands.has_permissions(manage_channels=True)
async def DeleteChannel(ctx):
  await ctx.channel.delete()


@bot.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, amount):
  if amount:
   await ctx.channel.edit(reason='Bot Slowmode Command', slowmode_delay=int(amount))
   await ctx.send("Slowmode set to %s seconds!"%amount)
  else:
   await ctx.send("Slowmode was %s seconds!"%amount)

bot.remove_command("help")
@bot.command()
async def help(ctx):
 await ctx.channel.trigger_typing()
 e = discord.Embed(color=0x3366FF)
 e.add_field(name="ping", value="Shows bot latency")
 e.add_field(name="hello", value="Says hi back")
 e.add_field(name="donate", value="Donate to support us")
 e.add_field(name="invite", value="Useful links")
 e.add_field(name="say", value="Repeats a message")
 e.add_field(name="** **", value="** **")
 e.add_field(name="__More__", value="** **")
 e.add_field(name="Moderation commands", value="skull moderation" ) 
 e.add_field(name="Economy commands", value="skull economy")
 
 e.set_footer(text="If you had any problems, please contact to the developer(PhilipMarkJames#1521)")
 await ctx.author.send(embed=e)
 await ctx.send("DM sent!")
 
@bot.command()
async def vote(ctx):
	e = discord.Embed(color=0x3366FF)
	e.add_field(
	 name="**__Vote Blue Guy to support us!__**",
	 value=
	 "** **"
	)
	e.add_field(
	 name="Bot's Base",
	 value="[vote here](https://botsbase.net/bot/702375332317233234)")
	await ctx.send(embed=e)
   
@bot.command()
async def economy(ctx):
 e=discord.Embed(color=0x3366FF)
 e.add_field(name="**__Economy commands__**",value="** **")
 e.add_field(name="register", value="Create an account")
 e.add_field(name="rob", value="Robs a user")
 e.add_field(name="balance", value="Shows your balance")
 e.add_field(name="beg", value="Earn coins by begging")
 e.add_field(name="leaderboard", value="Top richest users")
 e.set_footer(text="If you had any problems, please contact to the developer.(PhilipMarkJames#1521)")
 await ctx.author.send(embed=e)
 await ctx.send("DM sent!")

@bot.command()
@cooldown(1, per_day=1,type=commands.BucketType.user)
async def daily(ctx):
  id = str(ctx.author.id)
  amounts[id] += 1000
  await ctx.send(f"**1000 Blue Coins** were added to your wallet, {ctx.author.name}")

@bot.command()
async def moderation(ctx):
 e=discord.Embed(color=0x3366FF)
 e.add_field(name="addrole",value="Adds a role to the mentioned member")
 e.add_field(name="removerole",value="Removes a role to the mentioned member")
 e.add_field(name="clear",value="Deletes messages")
 e.add_field(name="kick", value="Kicks a member")
 e.add_field(name="ban", value="Bans a member")
 e.add_field(name="tempmute", value="Temporary mutes a member")
 e.add_field(name="slowmode",value="Sets the slowmode of a channel.")
 e.add_field(name="nuke", value="Nukes a channel")
 e.add_field(name="setautorole", value="Automatically gives the role to members who joined the server")
 e.add_field(name="removeautorole", value="Removes the auto role.")
 e.set_footer(text="If you had any problems, please contact to the developer.(PhilipMarkJames#1521)") 
 #e.setURL("heyyou6013@gmail.com")
 await ctx.author.send(embed=e)
 await ctx.send("DM sent!")

@bot.command()
async def google(ctx,*,arg):
  await ctx.send(f"https://www.google.com/search?q={arg.replace(' ', '+')}")
  



  

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
  author = ctx.author
  await user.add_roles(role)
  await ctx.send(f"Added **{role.name}** to **{user}**")



@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
  author = ctx.author
  await user.remove_roles(role)
  await ctx.send(f"Removed **{role.name}** from **{user}**")



@bot.command()
async def leave(ctx):
  await ctx.author.voice.channel.disconnect()

@bot.command()#Creates a new channel
async def NewChannel(ctx, *, name):
  await ctx.guild.create_text_channel(name=f"{arg}")

@bot.command()#Creates a new role
@commands.has_permissions(manage_roles = True)
async def NewRole(ctx,*,arg):
  await ctx.guild.create_role(name=f"{arg}")


@bot.command()
async def spoiler(ctx,*,arg):
  ## Add the space between every letter of the string

  string4=f"{arg}"
  string_revised="||||".join(arg)
  await ctx.send(f'||{string_revised}||')


  

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def work(ctx):
    primary_id = str(ctx.message.author.id)
    e=discord.Embed(color=0x3366FF)
    e.add_field(name=f"{ctx.author}", value=f"You performed a play and gained **{u} Blue Coins!**")
    await ctx.send(embed=e)
    amounts[primary_id] += u 
    _save()

   
@bot.command(aliases=["bal"])
async def balance(ctx,user: discord.User = None):
  id = str(ctx.author.id)
  if user == None:
   e=discord.Embed(color=0x3366FF)
   e.add_field(name=f"{ctx.author.name}'s balance", value=f"Wallet: {amounts[id]} Blue Coins") 
   await ctx.send(embed=e)
  if user != None:
      e=discord.Embed(color=0x3366FF)
      e.add_field(name=f"{user.name}'s balance", value=f"Wallet:{amounts[str(user.id)]} Blue Coins")
      await ctx.send(embed=e)
  if id not in amounts:
      amounts[id] = 0
      



@bot.command()  
@commands.has_permissions(administrator= True)
async def lock(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
  await ctx.send(f"Locked {ctx.channel.mention}!")
  
@bot.command() 
@commands.has_permissions(administrator= True)
async def unlock(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
  await ctx.send(f"Unlocked {ctx.channel.mention}!")
  
@bot.command()
@commands.has_permissions(administrator= True)
async def public(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True)
  await ctx.send("This channel is now public!")
  
@bot.command()
@commands.has_permissions(administrator= True)
async def private(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False)
  await ctx.send("This channel is now private!")
    
@bot.command(pass_context=True)
async def register(ctx):
    id = str(ctx.message.author.id)
    if id not in amounts.keys():
        amounts[id] = 100
        await ctx.send("You are now registered")
        _save()
    else:
        await ctx.send("You already have an account")

      

@bot.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
async def rob(ctx,other:discord.User=None):
  primary_id = str(ctx.message.author.id)
  other_id = str(other.id)
  print(amounts[other_id])
  rb = randint(0,1000)
  per = randint(0,10)
  if primary_id not in amounts:
    await ctx.send("You do not have an account")
  elif other_id not in amounts:
    await ctx.send("The other party does not have an account")
  elif amounts[primary_id] < 1000:
    await ctx.send("You need at least `1000` Blue Coins to rob someone")
  elif amounts[other_id] < 1000:
    await ctx.send("The other party doesn't have `1000` Blue Coins")
  elif per == 10:
    await ctx.send("You were caught by the person you stole from. You lost **100 Blue Coins**.")
    amounts[primary_id] -= 100
    amounts[other_id] += 100
    _save
    await other.send(f"**{ctx.author}** tried to steal from you in **{ctx.guild.name}**, but failed.")
  else:
    amounts[primary_id] += rb
    amounts[other_id] -= rb
    _save
    await ctx.send(f"{ctx.author.mention} :white_check_mark: You robbed **{rb} Blue Coins** from **{other}**!")
    await other.send(f"**{ctx.author}** has stolen **{rb} Blue Coins** from you in **{ctx.guild.name}**!")
    



@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def transfer(ctx, amount: int, other: discord.User=None):
    primary_id = str(ctx.message.author.id)
    other_id = str(other.id)
    if primary_id not in amounts:
        await ctx.send("You do not have an account")
    elif other_id not in amounts:
        await ctx.send("The other party does not have an account")
    elif amounts[primary_id] < amount:
        await ctx.send("You cannot afford this transaction")
    else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        await ctx.send("Transaction complete")
    _save()

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def beg(ctx):
  beg=randint(0, 1000)
  per = randint(0,10)
  id=str(ctx.message.author.id)
  if id in amounts:
    amounts[id] += beg
    await ctx.send(f"**Your friend** had donated {beg} to {ctx.author.mention}!")
    _save()
  elif per == 10:
    await ctx.send(f"**Your friend:** I'm poor.")

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)





@bot.command(pass_context=True)
async def ping(ctx):
	before = time.monotonic()
	message = await ctx.send("Pong!")
	ping = (time.monotonic() - before) * 1000
	await message.edit(content=f"Pong! `{int(ping)}ms`")
	print(f'Ping {int(ping)}ms')

    

@bot.command()
async def invite(ctx):
	e = discord.Embed(color=0x3366FF)
	e.add_field(
	 name="Add Blue Guy",
	 value=
	 "[Here](https://top.gg/bot/702375332317233234)"
	)
	e.add_field(
	 name="Official Support Server",
	 value="[Here](https://discord.gg/Cf5a28H)")
	await ctx.send(embed=e)


@bot.command()
async def donate(ctx):
	e = discord.Embed(color=0x3366FF)
	e.add_field(
	 name="Blue Guy Premium",
	 value="Help fund Blue Guy to keep it alive and perform well!")
	e.add_field(
	 name="Monthly Support",
	 value="[patreon](https://www.patreon.com/BlueGuyDiscordBot)")
	e.add_field(
	 name="Other Methods", value="[paypal](https://paypal.me/lowjunnhoi)")
	await ctx.send(embed=e)



bot.command()
async def say(ctx,*, arg):
  try:
   await ctx.send(f"{arg}\n"
   f"** **"
   f"- {ctx.author.mention}")
  except:
    await ctx.send("What do you want me to say huh?")
	
@bot.command()
async def random(ctx):
    e=discord.Embed(color=0x3366FF)
    e.add_field(name=f"{ctx.author}", value=f"🎲You rolled **{dice}**!")
    await ctx.send(embed=e)




@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(message, user: discord.Member = None):
	mention = message.author.mention
	if (user):
		await message.channel.send(f"Kicked {user.mention}!")
		await message.guild.kick(user)


@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send('You dont have permission to execute this command')

@bot.command()
async def youtube(ctx,*,search): 
  await ctx.send(f"https://www.youtube.com/results?search_query={search.replace(' ', '+')}")
  
@bot.command()
@commands.has_permissions(ban_members=True )
async def ban(ctx,user:discord.User=None,*,arg):
  await ctx.guild.ban(user,reason=arg)
  await ctx.send(f"Banned {user.mention}!")
  await user.send(f"You have been banned from {ctx.guild.name}. Reason: {arg}")
  print(arg)
		
@bot.command()
async def clear(ctx, limit: int):
  await ctx.message.delete()
  await ctx.channel.purge(limit=limit)
  await ctx.send("Deleted %s messages!"%limit, delete_after=1)

@bot.command(pass_context=True)
async def hello(message):
	mention = message.author.mention
	await message.channel.send(f"hi {mention}!")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User = None):
	if user == None:
		await ctx.send("You forgot to add the user id")
	if user != None:
		await ctx.guild.unban(user)
		await ctx.send(f"Unbanned {user.mention}!")




@bot.command()
async def servercount(ctx):
	await ctx.send("I'm in " + str(len(bot.guilds)) + " servers")

@bot.command()
async def avatar(ctx,member:discord.User=None):
  await ctx.send(f"{member.avatar_url}") 
	
@bot.command()
@commands.has_permissions(administrator=True)
async def nick(ctx,member:discord.User,*,name):
	await member.edit(nick=name)
	await ctx.send(f"Renamed {member.mention} to {name}")
	
@bot.command()
@commands.has_permissions(manage_roles=True)
async def tempmute(ctx, member:discord.Member , time: int):
 if discord.utils.get(member.guild.roles, name="Muted"):
  role = discord.utils.get(member.guild.roles, name="Muted")
  await discord.Member.add_roles(member, role)
  await ctx.send(f"{member.mention} has been muted for {time} minutes")
  await asyncio.sleep(time * 60)
  await discord.Member.remove_roles(member, role)
 else:
  perms = discord.Permissions(send_messages=False, read_messages=True)
  await ctx.guild.create_role(name="Muted", permissions=perms)
  


@bot.event
async def on_message(message):
  await bot.process_commands(message)
  purgeChannel = bot.get_channel(751658648320868381)
  if (message.content.startswith(f'{bot.user.mention}')):
        await message.channel.send("Hi, my prefix was `skull`" ) 
  if message.channel == purgeChannel: 
    #await bot.process_command(message)
    await purgeChannel.purge(limit=1)

bot.run(TOKEN)
