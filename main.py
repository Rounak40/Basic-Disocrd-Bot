

# Import modules

import discord
from discord.ext import commands
import requests
import json
import random

#Enter your discord bot token & Prefix here
TOKEN = 'TOKEN'
prefix = '!'

#define your bot
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)


#Its a event which will run when the bot is ready/online.
@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)
    print("I'm ready")

#Here you can add your cmds


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")

#play dice
@bot.command()
async def dice(ctx):
    
    #get a random number from ["1","2","3","4","5","6"]
    roll = random.choice(["1","2","3","4","5","6"])
    
    await ctx.send("**You rolled a: **" + roll)

#Clear messages of any channel
#Checks if message is in a guild, checks if user has permission to do so
@bot.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number_of_messages: int):
    #check if user has permission to manage channels
    try:
        await ctx.channel.purge(limit=messages_to_delete+1)
        await ctx.send(f"Successfully cleared {str(number)} messages from this channel")
    except Exception as e:
        # if bot doesn't have permission to delete messages.
        await ctx.send(f"Failed to delete messages because {e}")

#some calculating commands

@bot.command()
async def percent(ctx, a: int, b: int):
    divide3 = (a/b)
    ans = divide3*100
    embed = discord.Embed(title="Solved", description=str(ans), color=0x1500ff)
    await ctx.send(embed=embed)

@bot.command()
async def root(ctx, number):
    root_value = int(number)**(1/2.0)
    embed = discord.Embed(title="Solved", description=str(number) + " **root is** " + str(root_value), color=0x1500ff)
    await ctx.send(embed=embed)

@bot.command()
async def square(ctx, number):
    squared_value = int(number) * int(number)
    embed = discord.Embed(title="Solved", description=str(number) + " **squared is** " + str(squared_value), color=0x1500ff)
    await ctx.send(embed=embed)


#passing two values in cmd (a: int, b: int)
@bot.command()
async def add(ctx, a: int, b: int):
    embed = discord.Embed(title="Solved", description=a+b, color=0x1500ff)
    await ctx.send(embed=embed)

@bot.command()
async def multiply(ctx, a: int, b: int):
    embed = discord.Embed(title="Solved", description=a*b, color=0x1500ff)
    await ctx.send(embed=embed)

@bot.command()
async def divide(ctx, a: int, b: int):
    divide25 = (a/b)
    embed = discord.Embed(title="Solved", description=str(divide25), color=0x1500ff)
    await ctx.send(embed=embed)

@bot.command()
async def subtract(ctx, a: int, b: int):
    embed = discord.Embed(title="Solved", description=a-b, color=0x1500ff)
    await ctx.send(embed=embed)


#api based command
# 1. Requests to url
# 2. Grab data from response
# 3. Send it to the channel
@bot.command()
async def bitcoin(ctx):
    
    #define url
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    
    #make "GET" request
    response = requests.get(url)
    
    #grab data from response
    value = response.json()['bpi'] ['USD'] ['rate']

    #send data in channel
    await ctx.send("Current Bitcoin Price is: $" + value)
    
#example of embed messages

#get info of server
@bot.command()
async def serverinfo(ctx):
    
    embed = discord.Embed(name=f"{ctx.message.server.name}'s info".format, color=0x00ff00)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.set_footer(text="Basic example of embed message!")
    
    await ctx.send(embed=embed)

# get info of any user
@bot.command()
async def userinfo(ctx, user: discord.Member):
    
    embed = discord.Embed(title=f"{user.name}'s Info",color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined At", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="Basic example of embed message!")
    
    await ctx.send(embed=embed)


#get avatar of any user
@bot.command()
async def avatar(ctx, user: discord.Member):
    
    embed=discord.Embed(title=f"Avater of {user}", color=0x1500ff)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text="Basic example of embed message!")
                     
    await ctx.send(embed=embed)
    
# Run the bot with the token
bot.run(TOKEN)
