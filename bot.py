import discord
from discord.ext import commands, tasks
import os, socket
from dotenv import load_dotenv
import threading, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
load_dotenv()


client = commands.Bot(command_prefix='.')

client.remove_command('help')

@client.event
async def on_ready():
#    firstBlood.start()
    await client.change_presence(status = discord.Status.online, activity=discord.Game("https://discord.io/coreisus"))
    print('Bot is ready')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command(aliases=['Flag'])
async def flag(ctx):
    if ctx.channel.type is discord.ChannelType.private:
        await ctx.send(os.getenv('FLAG'))
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send('Sssssshhh, not here. DM me maybe ;)')


client.run(os.getenv('TOKEN'))
