import discord
from discord.ext import commands

from tokends import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def server (ctx):
    await ctx.send(dir(ctx))

bot.run(TOKEN)

