import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    staff = 'Our staff team consists of @eth#3101, @helix#8781, @revv#8367, @zan#2327, along with @Cleft#5166. ' \
            'Feel free ' \
            'to tag' \
            ' @OG Sellouts or @Admin if you have any questions!'
    pog = [
        'pog',
        'poggers',
        'pogCHAMP',
        'pogies',
        'pog champ'
    ]

    chirag = [
        'STOP! Good God man! You almost got the cheese touch...'
    ]

    if message.content == 'staff':
        response = staff
        await message.channel.send(response)

    if 'pog' in message.content.lower():
        response = random.choice(pog)
        await message.channel.send(response)

    #if 'chirag' in message.content.lower():
        #response = random.choice(chirag)
        #await message.channel.send(response)


client.run(TOKEN)
