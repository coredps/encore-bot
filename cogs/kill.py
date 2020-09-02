import discord
from discord.ext import commands
import random
import time

class kills(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['kill', 'Kill'])
    async def _kill(self, ctx, *, killed):


            embed=discord.Embed(title="Person killed", description=f'<@!{ctx.author.id}> Has killed {killed}', color=0x000000)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(kills(client))
