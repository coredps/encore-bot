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


'''
global ch
ch =  {23: {'name': 'TEST_1', 'solved': False}}
'''

global connectionData
connectionData = {}


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




'''
@tasks.loop(seconds=180)
async def firstBlood():

    allSolved = True
    keys = dict.keys(ch)
    for i in keys:
        if not(ch[i]['solved']):
            allSolved = False

    if(allSolved):
        return
    
    channel = client.get_channel(int(os.getenv('FIRST_BLOOD_CHANNEL')))

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-processu')


    usernameStr = os.getenv('USER')
    passwordStr = os.getenv('PASSWORD')

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options )

    print('loading')
    browser.get(('htssp://ctf.tarush.co/login'))
    print('loaded')

    username = browser.find_element_by_id('name')
    username.send_keys(usernameStr)
    password = browser.find_element_by_id('password')
    password.send_keys(passwordStr)

    submitBtn = browser.find_element_by_id('_submit')
    submitBtn.click()

    for i in keys:
        
        if(ch[i]['solved']):
            continue

        browser.get((f'https://ctf.tarush.co/api/v1/challenges/{i}/solves'))
        html = browser.page_source
        time.sleep(2)
        html = html[html.index('{'):html.rindex('}')+1]
        print(html)
        y = json.loads(html)
            
        try: y['data']
        except:
            print('key error')
            continue

        if(y['data']==[]):
            continue

        if(y['data']==[]):
            print(f'no data for {ch[i]}')
            continue

        ch[i]['solved'] = True
        # print(f'`First blood for challenge: {ch[i]["name"]} goes to {y["data"][0]["name"]}`')
        print("sending")
        await channel.send(f'```css\n🩸 First blood for .{ch[i]["name"]} goes to [{y["data"][0]["name"]}]```')
    browser.close()
    print('Completed!')
'''
@client.command(aliases=['Flag'])
async def flag(ctx):
    if ctx.channel.type is discord.ChannelType.private:
        await ctx.send(os.getenv('FLAG'))
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send('Sssssshhh, not here. DM me maybe ;)')


client.run(os.getenv('TOKEN'))
