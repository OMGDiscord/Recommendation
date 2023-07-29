import discord
from discord.ext import commands

# Create a new bot instance
bot = commands.Bot(command_prefix='!')

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Simple command example
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your friendly Discord bot!')

# Run the bot
bot.run('MTExMDQ4MDY4NDcwMDY2ODAyNA.GhsyGl.yiLinw67vee0PkaVXJMcr2ctuM5XZKuwrGZVmo')
