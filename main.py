import asyncio
import discord
from discord import shard
from discord.ext import commands, tasks
import os
import time
import aiohttp
from itertools import cycle


TOKEN = open("TOKEN.txt", "r").read()

intents = discord.Intents.default()
intents.members = True
from threading import Thread

## COLORS ###############
wi = "\033[1;37m"  # >>White#
rd = "\033[1;31m"  # >Red   #
gr = "\033[1;32m"  # >Green #
yl = "\033[1;33m"  # >Yellow#
#########################

bot = commands.AutoShardedBot(commands.when_mentioned_or("x!", "X!"), case_insensitive=True, intents=intents)
bot.remove_command('help')
serwery = len(bot.guilds)
status = cycle([f"www.xantbot.pl", " x!help || @XantBot"])

xant_id = 653616901246681099

os.system("clear")

@bot.event
async def on_ready():
    print(rd + f"""
                         ╔═╗╔═╗          ╔╗      ╔══╗      ╔╗ 
                         ╚╗╚╝╔╝         ╔╝╚╗     ║╔╗║     ╔╝╚╗
                          ╚╗╔╝ ╔══╗ ╔═╗ ╚╗╔╝     ║╚╝╚╗╔══╗╚╗╔╝
                          ╔╝╚╗ ╚ ╗║ ║╔╗╗ ║║ ╔═══╗║╔═╗║║╔╗║ ║║ 
                         ╔╝╔╗╚╗║╚╝╚╗║║║║ ║╚╗╚═══╝║╚═╝║║╚╝║ ║╚╗ 
                         ╚═╝╚═╝╚═══╝╚╝╚╝ ╚═╝     ╚═══╝╚══╝ ╚═╝

                                   DevAdmin Console

            XantBot was Connect with {len(bot.users)} users and {len(bot.guilds)} servers in {bot.shard_count} shards.""")
    await asyncio.sleep(2)
    change_status.start()


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content == f"<@!{xant_id}>":

        j = discord.Embed(
            title="Ping",
            description=f"My prefix is <@!{xant_id}> or `x!`\n Use x!help to get help.",
        )
        await message.channel.send(embed=j)

    await bot.process_commands(message)


@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.online,
                                activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN, bot=True, reconnect=True)


