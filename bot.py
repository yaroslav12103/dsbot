import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def hehbn(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def sum(ctx, a ,b):
    await ctx.send(f"Сумма равна: {int(a) + int(b)}")
    
@bot.command()
async def mult(ctx, a ,b):
    await ctx.send(f"Произведение равно: {int(a) * int(b)}")
    
@bot.command()
async def div(ctx, a ,b):
    await ctx.send(f"Частно равно: {int(a) : int(b)}")
    
@bot.command()
async def diff(ctx, a ,b):
    await ctx.send(f"Разность равна: {int(a) - int(b)}")
    
@bot.command()
async def stepen(ctx, a ,b):
    await ctx.send(f"Степень равна: {int(a) ** int(b)}")
bot.run("токен")
