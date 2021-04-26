import os
import discord
from discord.ext import commands
from src.scraper import Scraper
from src.boy import Boy
from datetime import date
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
server_name = os.getenv('SERVER_NAME')

intents = discord.Intents.default()
intents.members = True

#client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

scraper = Scraper()
botd = Boy()


#print(client.user)

@bot.event
async def on_ready():
    server = bot.guilds[0]
    if server.name == server_name:
        print(f'{bot.user} has connected to {server.name}, id: {server.id}')

    print([name.name for name in server.members])


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
    await member.dm_channel.send("Welcome to the danger zone {}".format(member))
    


@bot.command(name='counters')
async def counters(ctx, name):
    await ctx.send("The list of counters for {} is:\n{}".format(name, scraper.getCounters(name)))


@bot.command(name='runes')
async def runes(ctx, name):
    await ctx.send("The list of runes for {} is:\n{}".format(name, scraper.getRunes(name)))


@bot.command(name='build')
async def builds(ctx, name):
    await ctx.send("The build for {} is:\n{}".format(name, scraper.getBuild(name)))


@bot.command(name='populate')
@commands.is_owner()
async def populate(ctx):
    scraper.populate()
    await ctx.send("Success!")

@bot.command(name='botd')
async def boy_of_the_day(ctx):
    server = bot.guilds[0]
    members = [name.name for name in server.members]

    if botd.isSelected():
        boy = botd.getBoy()
        await ctx.send(f'The boy of the day has already been selected ({boy}), try again tomorrow for your chance at being the boy of the day!')
        with open('img/dog.png', 'rb') as fh:
            f = discord.File(fh, filename='img/dog.png')
        await ctx.send(file=f)

    else:
        boy = botd.botd(members)

        for name in server.members:
            if name.name == boy:
                pfp = name.avatar_url
                embed = discord.Embed(title="Boy Of The Day!", description='Congratulations {}, you are the  boy of the day!'.format(name.mention), color=0xecce8b)
                embed.set_image(url=(pfp))
                await ctx.send(embed=embed)





@bot.command(name='shutdown')
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Goodbye")
    exit(0)

bot.run(token)
#client.run(token)
