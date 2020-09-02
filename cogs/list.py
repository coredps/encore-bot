import discord
from discord.ext import commands

class List(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'listCommands', aliases = ['List', 'list', 'help'])
    async def listCommands(self, ctx):
        await ctx.send("Do you really think we will giveaway the flags")

def setup(client):
    client.add_cog(List(client))
    
