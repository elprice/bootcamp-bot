import config
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=config.bot['prefix'])

@bot.event
async def on_ready():
    print(f'{bot.user} has connected!')
    await bot.change_presence(activity=discord.Game(name=" a fun game."))
    
@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send('pong')

bot.run(config.bot['token'])