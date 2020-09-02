import discord
from discord.ext import commands

class About(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name= 'about', aliases=['About', 'AboutCore', 'Aboutcore', 'aboutcore', 'aboutCORE'])
    async def about(self, ctx):
        await ctx.send('Instituted in 2008 by the students of Delhi Public School Dwarka, COЯE was established with the aim of promoting competence and excellence in the field of computer and information technology at school, as well as various inter-school symposia. COЯE hosted its first Inter School Symposium in 2008. Since then, we have not looked back.')
    

def setup(client):
    client.add_cog(About(client))
