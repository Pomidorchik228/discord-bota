import discord
from discord.ext import commands
from key import *
from Lesson2 import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh + "h")

@bot.command()
async def add(ctx, left: int, right: int):
    """Сложите два числа вместе."""
    await ctx.send(left + right)

@bot.command()
async def keyword(ctx, arg=9):
    await ctx.send(f"||{passlovo(arg)}||")











bot.run(key())