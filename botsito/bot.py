import discord
from discord.ext import commands

intents = discord.Intents.default()  
intents.messages = True  
intents.message_content = True  

bot = commands.Bot(command_prefix="#", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está listo y conectado!')

@bot.command()
async def web(ctx):
    await ctx.send("🌍 ¡Descubre cómo puedes hacer la diferencia por el planeta! Haz clic en el enlace para conocer más sobre la importancia de cuidar nuestro ambiente: https://allisonlazaro.github.io/ambientalll/#consecuencias 🌱")

bot.run("MTMyNTE4ODQ0MzY0MjI2OTc0Ng.GISzNZ.npobv11bLDJZ8zUf_4CpHOqo3taq5UJWCHSS9A")