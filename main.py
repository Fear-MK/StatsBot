import discord
from discord.ext import commands

from shared import *
from common import *

bot = commands.Bot(command_prefix=['!','^'], help_command=None, case_insensitive=True)

with open("private.txt", "r") as f:
    token=f.read()[8:]

@bot.command()
async def mmr(ctx, *args):
    json_data, ladder_type=api_request(ctx, split_args(list(args)))
    if json_data == "Failed":
        return
  
    embed = discord.Embed(colour=discord.Color.purple())
    embed.set_author(
        name=f"Lounge {ladder_type.upper()} MMR",
        icon_url="https://cdn.discordapp.com/icons/387347467332485122/5035e39312f7aadd75a29011e37a96f1.png"
    )

    json_data.sort(key=lambda x: x["current_mmr"], reverse=True)

    for player in json_data:
        embed.add_field(name=player["player_name"],value=f"[{str(player['current_mmr'])}]({str(player['url'])})",inline=True)
    
    await ctx.send(embed=embed)

@bot.command()
async def lr(ctx, *args):
    json_data, ladder_type=api_request(ctx, split_args(list(args)))
    if json_data == "Failed":
        return
  
    embed = discord.Embed(colour=discord.Color.purple())
    embed.set_author(
        name=f"Lounge {ladder_type.upper()} LR",
        icon_url="https://cdn.discordapp.com/icons/387347467332485122/5035e39312f7aadd75a29011e37a96f1.png"
    )

    json_data.sort(key=lambda x: x["current_lr"], reverse=True)

    for player in json_data:
        embed.add_field(name=player["player_name"],value=f"[{str(player['current_lr'])}]({str(player['url'])})",inline=True)
    
    await ctx.send(embed=embed)

@bot.command(aliases=["lrmmr"])
async def mmrlr(ctx, *args):
    json_data, ladder_type=api_request(ctx, split_args(list(args)))
    if json_data == "Failed":
        return
  
    embed = discord.Embed(colour=discord.Color.purple())
    embed.set_author(
        name=f"Lounge {ladder_type.upper()} LR/MMR",
        icon_url="https://cdn.discordapp.com/icons/387347467332485122/5035e39312f7aadd75a29011e37a96f1.png"
    )

    json_data.sort(key=lambda x: x["current_lr"], reverse=True)

    for player in json_data:
        embed.add_field(name=player["player_name"],value=f"[{str(player['current_lr'])} LR/{str(player['current_mmr'])} MMR]({str(player['url'])})",inline=True)
    
    await ctx.send(embed=embed)

print("Bot Started")

bot.run(token)