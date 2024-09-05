import discord
from discord.ext import commands
import os
import subprocess
from config import TOKEN
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="nx-hackingbot!", intents=intents)

def install_depencies():
    subprocess.run(['apt-get', 'install', 'hydra'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subprocess.run(['apt-get', 'install', 'nikto'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subprocess.run(['apt-get', 'install', 'nmap'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

install_depencies()

def load_commands():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != "__init__.py":
            bot.load_extension(f'commands.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")


load_commands()

bot.run(TOKEN)