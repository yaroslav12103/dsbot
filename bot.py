from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import os, random, requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

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
    await ctx.send(f"Частно равно: {int(a) / int(b)}")
    
@bot.command()
async def diff(ctx, a ,b):
    await ctx.send(f"Разность равна: {int(a) - int(b)}")
    
@bot.command()
async def stepen(ctx, a ,b):
    await ctx.send(f"Степень равна: {int(a) ** int(b)}")

@bot.command()
async def mem(ctx):
    mem2 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRE6WRPerRERBeiTIEDD9T6E6VThytvJIDseg&s'
    await ctx.send(mem2)
        
        
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def weather(ctx, city,):
    try:
        city = city.replace(" ", "+")
        city = city.replace(".", "+")
        await ctx.send('Секунду...')
        print("(", city, ")")
        res = requests.get(f'https://www.google.ru/search?q={city}+погода', headers=headers)
        print("Searching in google......\n")
        soup = BeautifulSoup(res.text, 'html.parser')   
    
    # Изменим селекторы, чтобы соответствовать измененной структуре страницы
        location = soup.select('.BNeawe.iBp4i.AP7Wnd')[0].getText().strip()  
        time = soup.select('.BNeawe.tAd8D.AP7Wnd')[0].getText().strip()       
        info = soup.select('.BNeawe.tAd8D.AP7Wnd')[1].getText().strip() 
        weather = soup.select('.BNeawe.iBp4i.AP7Wnd')[1].getText().strip()
        
        await ctx.send(location)
        await ctx.send(time)
        await ctx.send(info)
        
    except Exception:
        await ctx.send('Город не найден, попробуй написать область')
        print("Ошибочка вышла")

    
bot.run("")
