import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from scraper import counters
from datetime import datetime


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
server_name = os.getenv('SERVER_NAME')

intents = discord.Intents.default()
intents.members = True

#client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)


#print(client.user)

@bot.event
async def on_ready():
    server = bot.guilds[0]
    if server.name == server_name:
        print(f'{bot.user} has connected to {server.name}, id: {server.id}')

    print(server.members)


"""
ON MESSAGE NOT NEEDED YET
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content != None:
        print(message.content)
"""


@bot.event
async def on_member_join(member):
    #channel = discord.utils.get(member.guild.text_channels, name="welcome")
    print(f'Hi {member}')
    await member.create_dm()
    await member.dm_channel.send("Welcome to the fuck zone {}".format(member))
    #await channel.send("Welcome to the fuck zone {}".format(member))

@bot.command(name='erniebot')
async def league(ctx, name):
    start_time = datetime.now()
    await ctx.send("The list of counters for {} is:\n{}".format(name, counters(name)))
    await ctx.send("This query took {}".format(datetime.now()-start_time))

@bot.command(name='shutdown')
@commands.is_owner()
async def shutdown(ctx):
    exit(0)

bot.run(token)
#client.run(token)
