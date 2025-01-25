import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

TOKEN = os.getenv('DISCORD_TOKEN')  # Get token from environment variable

# Create intents instance and enable default intents
intents = discord.Intents.default()
# Enable message content intent (needed for message commands)
intents.message_content = True

# Pass intents to Bot constructor
bot = commands.Bot(command_prefix="!teste", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(TOKEN)
