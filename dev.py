import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(e)

@bot.tree.command(name="ping", description="Commande simple pour obtenir le badge Active Developer")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong ! 🙂")

TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(TOKEN)
