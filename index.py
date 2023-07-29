import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1
    print(f"SampleDiscordBot is in {guild_count} guilds.")

@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("Hey dirtbag")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am your friendly Discord bot!")
# Run the bot
bot.run('Token')