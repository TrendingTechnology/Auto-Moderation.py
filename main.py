import os
import discord
from discord.ext import commands
import json
from discord.ext.commands import has_permissions, MissingPermissions
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from discord.utils import get
from datetime import datetime
intents = discord.Intents.all()
client = commands.Bot(command_prefix="+",help_command=None,intents=intents)


@client.event
async def on_ready():
  print("---------------------------------------------------------|")
  print(f"{client.user}({client.user.id}) is Ready to use!|")
  print("|---------------------------------------------------------|")
  DiscordComponents(client)
  try:
    with open("antiads.json","r") as f:
        antilink = json.load(f)
        checklink = antilink[str("YOUR-GUILD-ID")]
  except:
    checklink = "off"
    pass
  try:
    with open("antiping.json","r") as f:
        antiping = json.load(f)
        checkping = antiping[str("YOUR-GUILD-ID")]
  except:
    checkping = "off"
    pass
  try:
    with open("antiswear.json","r") as f:
        antiping = json.load(f)
        checkswear = antiping[str("YOUR-GUILD-ID")]
  except:
    checkswear = "off"
    pass
  try:
    with open("antispam.json","r") as f:
        antiping = json.load(f)
        checkspam = antiping[str("YOUR-GUILD-ID")]
  except:
    checkspam = "off"
    pass
  print("|---------------------------------------------------------|")
  if checklink == "on":
    print("|  ✅ Anti ads                                    |")
  if checklink == "off":
    print("|  ❌ Anti ads                                    |")
  if checkping == "on":
    print("|  ✅ Anti ping                                    |")
  if checkping == "off":
    print("|  ❌ Anti ping                                    |")
  if checkswear == "on":
    print("|  ✅ Anti swear                                   |")
  if checkswear == "off":
    print("|  ❌ Anti swear                                   |")
  if checkspam == "on":
    print("|  ✅ Anti spam                                    |")
  if checkspam == "off":
    print("|  ❌ Anti spam                                         |")
  print("|---------------------------------------------------------|")
  print("| Coded by G∙MAX#2255 and RoyalDj9730322#0001             |")
  print("|---------------------------------------------------------|")

@client.command()
async def help(ctx):
  help = discord.Embed(title="My Commands",description="**[[Github](https://github.com/GMAX2/Auto-Moderation.py)]** **[[Disbots.xyz](https://disbots.xyz)]**",color=discord.Color.blue())
  help.add_field(name="**Moderation Commands**",value="`+kick <@user> <reason>` - Kicks the user mentioned\n`+ban <@user> <reason>` - Bans the user mentioned\n`+settings` - Shows auto moderation settings",inline=False)
  help.add_field(name="**Auto Moderation Commands**",value="`+antilink` - Sends you the option to select to turn on or off Anti Link System\n`+antiswear` - Sends you the option to select to turn on or off Anti Swear System\n`+antispam` - Sends you the option to select to turn on or off Anti Spam System\n`+antiping` - Sends you the option to select to turn on or off Anti Ping System",inline=False)
  help.set_thumbnail(url=client.user.avatar_url)
  await ctx.send(embed=help)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member:discord.Member,*,reason):
  check = discord.Embed(title=f"Are you sure to kick {member.name}?",color=discord.Color.blue())
  await ctx.send(embed=check,
    components=[[
      Button(style=ButtonStyle.green,label = "Yes"),
      Button(style=ButtonStyle.red,label = "No"),
    ]])
  res = await client.wait_for("button_click")
  if ctx.author == res.author:
    if res.component.label == "Yes":
      await member.kick(reason=reason)
      await ctx.send(f"{ctx.author.name} kicked {member.name}\n**Reason:** {reason}")
      await res.respond(content = f"I have kicked {member.name}")
    if res.component.label == "No":
      await res.respond(content = "I have canceled kick command")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member:discord.Member,*,reason):
  check = discord.Embed(title=f"Are you sure to kick {member.name}?",color=discord.Color.blue())
  await ctx.send(embed=check,
    components=[[
      Button(style=ButtonStyle.green,label = "Yes"),
      Button(style=ButtonStyle.red,label = "No"),
    ]])
  res = await client.wait_for("button_click")
  if ctx.author == res.author:
    if res.component.label == "Yes":
      await member.ban(reason=reason)
      await ctx.send(f"{ctx.author.id} banned {member.name}\n**Reason:** {reason}")
      await res.respond(content = f"I have banned {member.name}")
    if res.component.label == "No":
      await res.respond(content = "I have canceled ban command")

@client.command()
async def settings(ctx):
  config = discord.Embed(title="**Config!**",description=f"\nWhen i join server all setting will be default [Invite Me](https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot)",color=discord.Color.blue())
  try:
    with open("antiads.json","r") as f:
        antilink = json.load(f)
        checklink = antilink[str(ctx.guild.id)]
  except:
    checklink = "off"
    pass
  try:
    with open("antiping.json","r") as f:
        antiping = json.load(f)
        checkping = antiping[str(ctx.guild.id)]
  except:
    checkping = "off"
    pass
  try:
    with open("antiswear.json","r") as f:
        antiping = json.load(f)
        checkswear = antiping[str(ctx.guild.id)]
  except:
    checkswear = "off"
    pass
  try:
    with open("antispam.json","r") as f:
        antiping = json.load(f)
        checkspam = antiping[str(ctx.guild.id)]
  except:
    checkspam = "off"
    pass
  if checklink == 'on':
    config.add_field(name="Anti Link",value="<a:dis_on:855688790391521290>",inline=False)
  if checklink == 'off':
    config.add_field(name="Anti Link",value="<a:dis_off:855688791434985472>",inline=False)
  if checkspam == 'on':
    config.add_field(name="Anti Spam",value="<a:dis_on:855688790391521290>",inline=False)
  if checkspam == 'off':
    config.add_field(name="Anti Spam",value="<a:dis_off:855688791434985472>",inline=False)
  if checkping == 'on':
    config.add_field(name="Anti Ping",value="<a:dis_on:855688790391521290>",inline=False)
  if checkping == 'off':
    config.add_field(name="Anti Ping",value="<a:dis_off:855688791434985472>",inline=False)
  if checkswear == 'on':
    config.add_field(name="Anti Swear",value="<a:dis_on:855688790391521290>",inline=False)
  if checkswear == 'off':
    config.add_field(name="Anti Swear",value="<a:dis_off:855688791434985472>",inline=False)
  await ctx.send(embed=config)
  
@client.command()
@commands.has_permissions(manage_messages = True)
async def antilink(ctx):
  with open("antiads.json","r") as f:
    antilink = json.load(f)
  antilinkembed = discord.Embed(title="Please select the option given below!",color=discord.Color.red())
  await ctx.send(embed=antilinkembed,
    components=[[
      Button(style=ButtonStyle.green,label = "On"),
      Button(style=ButtonStyle.red,label = "Off"),
    ]])
  res = await client.wait_for("button_click")
  if ctx.author == res.author:
    if res.component.label == "On":
      antilink[ctx.guild.id] = 'on'
      with open("antiads.json","w") as fp:
        json.dump(antilink,fp)
      await res.respond(content = "Anti Link System is turned on!")
    if res.component.label == "Off":
      antilink[ctx.guild.id] = 'off'
      with open("antiads.json","w") as fp:
        json.dump(antilink,fp)
      await res.respond(content = "Anti Link System is turned off!")

@client.command()
@commands.has_permissions(manage_messages = True)
async def antiping(ctx):
  with open("antiping.json","r") as f:
    antiping = json.load(f)
  antipingembed = discord.Embed(title="Please select the option given below!",color=discord.Color.red())
  await ctx.send(embed=antipingembed,
    components=[[
      Button(style=ButtonStyle.green,label = "On"),
      Button(style=ButtonStyle.red,label = "Off"),
    ]])
  res = await client.wait_for("button_click")
  if ctx.author == res.author:
    if res.component.label == "On":
      antiping[ctx.guild.id] = 'on'
      with open("antiping.json","w") as fp:
        json.dump(antiping,fp)
      await res.respond(content = "Anti Ping System is turned on!")
    if res.component.label == "Off":
      antiping[ctx.guild.id] = 'off'
      with open("antiping.json","w") as fp:
        json.dump(antiping,fp)
      await res.respond(content = "Anti Ping System is turned off!")

@client.command()
@commands.has_permissions(manage_messages = True)
async def antiswear(ctx):
  with open("antiswear.json","r") as f:
    antiswear = json.load(f)
  antiswearembed = discord.Embed(title="Please select the option given below!",color=discord.Color.blue())
  await ctx.send(embed=antiswearembed,
    components=[[
      Button(style=ButtonStyle.green,label = "On"),
      Button(style=ButtonStyle.red,label = "Off"),
    ]])
  res = await client.wait_for("button_click")
  if ctx.author == res.author:
    if res.component.label == "On":
      antiswear[ctx.guild.id] = 'on'
      with open("antiping.json","w") as fp:
        json.dump(antiswear,fp)
      await res.respond(content = "Anti Swear System is turned on!")
    if res.component.label == "Off":
      antiswear[ctx.guild.id] = 'off'
      with open("antiping.json","w") as fp:
        json.dump(antiswear,fp)
      await res.respond(content = "Anti Swear System is turned off!")

@client.command()
@commands.has_permissions(manage_messages = True)
async def antispam(ctx):
  with open("antispam.json","r") as f:
    antispam = json.load(f)
  antispamembed = discord.Embed(title="Please select the option given below!",color=discord.Color.blue())
  await ctx.send(embed=antispamembed,
    components=[[
      Button(style=ButtonStyle.green,label = "On"),
      Button(style=ButtonStyle.red,label = "Off"),
    ]])
  res = await client.wait_for("button_click")
  if ctx.author == res.author:
    if res.component.label == "On":
      antispam[ctx.guild.id] = 'on'
      with open("antispam.json","w") as fp:
        json.dump(antispam,fp)
      await res.respond(content = "Anti Spam System is turned on!")
    if res.component.label == "Off":
      antispam[ctx.guild.id] = 'off'
      with open("antispam.json","w") as fp:
        json.dump(antispam,fp)
      await res.respond(content = "Anti Spam System is turned off!")

@antiswear.error
async def antiswear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await client.send_message(ctx.message.channel, text)

@antispam.error
async def antispam_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await client.send_message(ctx.message.channel, text)

@antiping.error
async def antiping_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await client.send_message(ctx.message.channel, text)

@antilink.error
async def antilink_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await client.send_message(ctx.message.channel, text)

time_window_milliseconds = 5000
max_msg_per_window = 7
author_msg_times = {}

with open('badwords.txt') as file:
    file = file.read().split()

@client.event
async def on_message(message):
    with open("antiads.json","r") as f:
      antilink = json.load(f)
    checklink = antilink[str(message.guild.id)]
    with open("antiping.json","r") as f:
      antiping = json.load(f)
    checkping = antiping[str(message.guild.id)]
    with open("antiswear.json","r") as f:
      antiswear = json.load(f)
    checkswear = antiswear[str(message.guild.id)]
    with open("antispam.json","r") as f:
      antispam = json.load(f)
    checkspam = antispam[str(message.guild.id)]
    if checklink == 'on':
      if "https://disbots.xyz" in message.content:
        pass
      elif "https" in message.content:
        if message.author.guild_permissions.manage_messages:
          pass
        await message.delete()
        await message.channel.send(f"{message.author.mention} Please dont send links here")
      elif "http" in message.content:
        if message.author.guild_permissions.manage_messages:
          pass
        await message.delete()
        await message.channel.send(f"{message.author.mention} Please dont send links here")
      elif "www." in message.content:
        if message.author.guild_permissions.manage_messages:
          pass
        await message.delete()
        await message.channel.send(f"{message.author.mention} Please dont send links here")
    if checkping == 'on':
      if "<@" in message.content:
        if message.author.guild_permissions.manage_messages:
          pass
        await message.delete()
        await message.channel.send(f"{message.author.mention} Please dont ping anyone here")
    if checkswear == 'on':
      if message.author.guild_permissions.manage_messages:
          pass
      for badword in file:
        if badword in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention} Please dont use that word!")
    if checkspam == 'on':
      global author_msg_counts
      author_id = message.author.id
      curr_time = datetime.datetime.now().timestamp() * 1000
      if not author_msg_times.get(author_id, False):
          author_msg_times[author_id] = []
      author_msg_times[author_id].append(curr_time)
      expr_time = curr_time - time_window_milliseconds
      expired_msgs = [
          msg_time for msg_time in author_msg_times[author_id]
          if msg_time < expr_time
      ]
      for msg_time in expired_msgs:
          author_msg_times[author_id].remove(msg_time)
      if len(author_msg_times[author_id]) > max_msg_per_window:
          muted = discord.utils.get(message.guild.roles,name="Muted")
          await message.author.add_role(muted)
          await message.channel.send(f"Muted {message.author.mention}\n**Reason:** Spamming")
    await client.process_commands(message)
  
@client.event
async def on_guild_join(guild):
  with open("antiads.json","r") as f:
    antilink = json.load(f)
  antilink[str(guild.id)] = 'on'
  with open("antiads.json","w") as fp:
    json.dump(antilink,fp)
  with open("antiping.json","r") as f:
    antiping = json.load(f)
  antiping[str(guild.id)] = 'on'
  with open("antiping.json","w") as fp:
    json.dump(antilink,fp)
  with open("antiswear.json","r") as f:
    antiswear = json.load(f)
  antiswear[str(guild.id)] = 'off'
  with open("antiswear.json","w") as fp:
    json.dump(antiswear,fp)
  with open("antispam.json","r") as f:
    antispam = json.load(f)
  antispam[str(guild.id)] = 'off'
  with open("antispam.json","w") as fp:
    json.dump(antiswear,fp)


client.run("BOT-TOKEN")