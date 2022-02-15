import discord
import os
import patchScrape
htmlS = patchScrape.htmlScraper() 

client = discord.Client()
my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send("Hello!")

  if message.content.startswith('lpn.' or 'LPN.' or 'Lpn.'):
    activeURL = htmlS.search()
    print(activeURL)
    await message.channel.send(activeURL)




client.run(my_secret)

