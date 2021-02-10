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
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(pass_context=True)
async def memberCount(ctx):
    await ctx.send(str(ctx.guild.member_count))

@bot.command(pass_content=True)
async def teams(ctx, *names):
    teamz = []
    for name in names:
        teamz.append(name)
    await ctx.send(f'team 1 {teamz[::2]} \nteam 2 {teamz[1::2]}')

bot.run(config.bot['token'])