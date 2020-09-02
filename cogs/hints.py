import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import re
import time
load_dotenv(dotenv_path='../')


class hints(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        channel = self.client.get_channel(747014382587871273)
        message.content = message.content.lower()

        if 'hint for rsa_madness bhai dalde' == message.content:
            embed=discord.Embed(title="Hint for rsa_madness", description=f'e = 65537', color=0x00ff00)
            await channel.send(embed=embed)

        if 'hint for weatherr bhai dalde' == message.content:
            embed=discord.Embed(title="Hint for Weather", description=f'trailing new line character is used', color=0x00ff00)
            await channel.send(embed=embed)

        if 'hint for exxt bhai dalde' == message.content:
            embed=discord.Embed(title="Hint for Ext", description=f'Bruteforce allowed extention', color=0x00ff00)
            await channel.send(embed=embed)


        if 'hint for exxt lastlevelbrozpt. 1' == message.content:
            embed=discord.Embed(title="Hint for lastlevelbrozpt. 1", description=f'the one with the lesser likes', color=0x00ff00)
            await channel.send(embed=embed)



def setup(client):
    client.add_cog(hints(client))
