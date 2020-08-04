import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='staff')
async def staff(ctx):
    response = 'Our staff team consists of @eth#3101, @helix#8781, @revv#8367, @zan#2327, along with @Cleft#5166. ' \
            'Feel free ' \
            'to tag' \
            ' @OG Sellouts or @Admin if you have any questions!'

    await ctx.send(response)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    chirag = [
        'STOP! Good God man! You almost got the cheese touch...'
    ]

    if 'chirag' in message.content.lower():
        response = random.choice(chirag)
        await message.channel.send(response)

    await bot.process_commands(message)

bot.run(TOKEN)

