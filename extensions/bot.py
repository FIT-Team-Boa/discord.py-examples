import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    print("CONNECTED!")

@bot.command()
async def angry(ctx):
    if "sad" in bot.extensions:
        bot.unload_extension("sad")

    if "angry" in bot.extensions:
        await ctx.send("Angry already loaded!")
    else:
        bot.load_extension("angry")

@bot.command()
async def sad(ctx):
    if "angry" in bot.extensions:
        bot.unload_extension("angry")

    if "sad" in bot.extensions:
        await ctx.send("Sad already loaded!")
    else:
        bot.load_extension("sad")

token = ""
with open('../../token.txt') as f:
    token = f.readline().strip()

bot.run(token)
