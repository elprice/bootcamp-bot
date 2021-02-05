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

@bot.command(pass_context=True)
async def memberCount(ctx):
    await ctx.send(str(ctx.guild.member_count))

bot.run(config.bot['token'])