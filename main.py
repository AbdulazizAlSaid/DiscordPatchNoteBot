import discord
import os
import patchScrape
from keep_alive import keep_alive
htmlS = patchScrape.dexertoPatchScraper() 

client = discord.Client()
my_secret = os.environ['TOKEN']


  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  message.content = message.content.lower()
  
  if message.author == client.user:
    return


  if message.content=='$hello':
    await message.channel.send("Hello! I am the Patch Note Bot! Type $commands to learn what I can do for you!")
    
  if message.content == '$commands':
    await message.channel.send('Commands: \npn. : patch notes, follow those with different games for different patch notes. \nGames: \nlol : League of Legends \ntft : Teamfight Tactics \nvalo : Valorant \napex : Apex Legends')
  
  if message.content.startswith('pn.'):
    if message.content.endswith('lol'):
      patchCommand = 'lol'
    elif message.content.endswith('tft'):      
      patchCommand = 'tft'
    elif message.content.endswith('valo'):
      patchCommand = 'valo'
    elif message.content.endswith('apex'):
      patchCommand = 'apex'
    else:
      await message.channel.send('Incorrect command, please type $commands to learn what I can do for you!')
      
    activeURL = htmlS.search(patchCommand)
    print(activeURL)
    await message.channel.send(activeURL)
keep_alive()
client.run(my_secret)