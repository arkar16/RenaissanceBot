import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@bot.command(name='staff')
async def staff(ctx):
    response = 'Our staff team consists of @eth#3101, @helix#8781, @revv#8367, @zan#2327, along with @Cleft#5166. ' \
            'Feel free ' \
            'to tag' \
            ' @OG Sellouts or @Admin if you have any questions!'

    await ctx.send(response)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    chirag = [
        'STOP! Good God man! You almost got the cheese touch...'
    ]

    if 'chirag' in message.content.lower():
        response = random.choice(chirag)
        await message.channel.send(response)


bot.run(TOKEN)
