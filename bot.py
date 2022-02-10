from multiprocessing import context
from PIL import Image
from pytesseract import *
from io import BytesIO
import requests
import discord
from discord.ext import commands, tasks
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  print('{0.user} is on'.format(client))

@client.event
async def on_message(message):
  link = message.attachments[0]
  response = requests.get(link)
  img  = Image.open(BytesIO(response.content))
  output = pytesseract.image_to_string(img)
  await message.channel.send(output)

client.run (tokenhere)
