import discord
from discord.ext import commands
import random
import time

class EightBall(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', '8Ball'])
    async def _8ball(self, ctx, *, question):
        responses =['It is certain.','It is decidedly so.','Without a doubt.',
                    'Yes – definitely.','You may rely on it.','As I see it, yes.',
                    'Most likely.','Outlook good.','Yes.',
                    'Signs point to yes.',' Reply hazy, try again.','Ask again later.',
                    ' Better not tell you now.',' Cannot predict now.','Concentrate and ask again.',
                    'Don\'t count on it.',' My reply is no.',' My sources say no.',
                    'Outlook not so good.','Very doubtful.','pls ask rbv','anonimbus might know','bruh','TS pros']
        
        if '.flag' in question:
            await ctx.channel.purge(limit=1)
            return

        if 'where' and 'flag' in question:
            await ctx.send('shhhh all flags are secretly stored at <https://eroc.ml/encore/flags>')
            time.sleep(1)
            await ctx.channel.purge(limit=2)
            return

        if 'is' and 'earth' in question:
            await ctx.send(f'Question: {question}\nAnswer: Always has been')
            return

        if 'gay' in question:
            await ctx.send('gei is u')
            return


        if '8thie' in question:
            await ctx.send('eSpice 8thies more like jokers')
            return


        if 'enc0re{' in question:
            await ctx.channel.purge(limit=1)
            await ctx.send('Oh no no! Don\'t post flags here.')
        else:
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(client):
    client.add_cog(EightBall(client))
