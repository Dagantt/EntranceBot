import os

import discord
from discord import Member, VoiceChannel
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        members = '\n - '.join([member.name for member in guild.members])
        print(
            f'{client.user.name} is connected to the following guild:\n'
            f'- {guild.name}(id: {guild.id})'
        )

bot = commands.Bot(command_prefix='µ')

@bot.command(name='ping', help='Responds with Pong')
async def ping(ctx):
    response = 'Pong'
    await ctx.send(response)

@bot.command(name='play', help='temp : play yt video passed in argument', pass_context = True)
async def play(ctx, url):
    author = ctx.message.author
    voice_channel = author.voice.channel
    vc = await VoiceChannel.connect(voice_channel)

    response = 'Playing ' + url + " in " + voice_channel.name;
    await ctx.send(response)

    player = await vc.play() #TODO
    player.start()

bot.run(TOKEN)


client.run(TOKEN)