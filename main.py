import discord
from discord.ext import commands

from shared import *
from common import *

bot = commands.Bot(command_prefix=['!','^'], help_command=None, case_insensitive=True)

with open("private.txt", "r") as f:
    token=f.read()[8:]

@bot.command()
async def mmr(ctx):
    description=""
    args=[text.strip() for text in ctx.message.content[5:].split(",")]
    json_data=api_request(ctx, args)
    if not json_data:
        return
    for player in json_data["results"]:
        description+=f" []"

    embedVar = discord.Embed(title="",description=,colour=discord.Color.blue())
    embedVar.set_author(
        name='Current MMR',
        icon_url='https://www.mkwlounge.gg/images/logo.png'
    )
        

@bot.command()
async def test(ctx):
    print(ctx.author.nick)

bot.run(token)