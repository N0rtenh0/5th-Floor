import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file
TOKEN = os.getenv('DISCORD_TOKEN')  # Get token from environment variable

# Create intents instance and enable default intents
intents = discord.Intents.all()
# Enable message content intent (needed for message commands)
intents.message_content = True

# Pass intents to Bot constructor
bot = commands.Bot(command_prefix=".", intents=intents)

# Set up a background task that sends a message every 30 seconds
@tasks.loop(seconds=30)
async def send_alive_message():
    channel = bot.get_channel(1332650910538530908)  # Replace 'your_channel_id' with the actual channel ID
    if channel:
        await channel.send("I am alive!")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    send_alive_message.start()  # Start the task when the bot is ready

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello there, {ctx.author.mention}")

@bot.command(name="ts")
async def hello(ctx):
    await ctx.send(f"Teste bem sucedido, {ctx.author.mention}")


bot.run(TOKEN)
