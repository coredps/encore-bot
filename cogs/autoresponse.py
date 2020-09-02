import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import re
import time
load_dotenv(dotenv_path='../')


class autoresponse(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        channel = self.client.get_channel(message.channel.id)
        message.content = message.content.lower()

        x = re.match('\w.*—', message.content)
        z = re.match('\w.*_', message.content)
        y = re.match('\w.*-', message.content)
        w = 'enc0re⁢⁤⁣⁢⁡‍⁤⁡‍‌⁢⁡‍‌⁢⁡‍‌‌⁢‍⁢⁢⁡⁣⁢⁡‍⁢⁤‍⁢‌⁡⁣‌⁡‍⁤⁡‌⁢‍⁡‌⁣{'
        if w in message.content or z:
            await channel.purge(limit=1)
            embed=discord.Embed(title="Warning logged", description=f'<@!{message.author.id}> don\'t post flags for EnCore here!', color=0x00ff00)
            await channel.send(embed=embed)

        if 'fuck' in message.content:
            await channel.purge(limit=1)
            time.sleep(1)
            await channel.send(f'<@!{message.author.id}> https://somesh.co/apshabd')

        if message.content == '.bash':
            await channel.send('root@ctf:~')

        if message.content == '.bash ls':
            await channel.send('```./ ../ flag.txt```')

        if message.content == '.bash pwd':
            await channel.send('/root')

        if message.content == '.bash cat flag.txt':
            await message.author.send('https://eroc.ml/encore/flags')

        if message.content == '.bash sl':
            await channel.send('Train goes choo choo')

        if message.content == '.bash rm -rf /':
            await channel.send('system failure')
            await channel.purge(limit=3)


def setup(client):
    client.add_cog(autoresponse(client))
