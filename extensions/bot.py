"""Utilizes extensions to showcase switching between groups of commands."""

from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    print("CONNECTED!")

@bot.command()
async def angry(ctx):
    """Allows user to switch to the angry extension."""
    if "sad" in bot.extensions:
        bot.unload_extension("sad")

    if "angry" in bot.extensions:
        await ctx.send("Angry already loaded!")
    else:
        bot.load_extension("angry")

@bot.command()
async def sad(ctx):
    """Allows user to switch to the sad extension."""
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
