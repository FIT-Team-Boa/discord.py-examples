"""Utilizes error handing to deal with errors from commands."""

from discord.ext import commands
import discord

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    print("CONNECTED!")

@bot.command()
async def hey(ctx, member : discord.Member):
    """Says hi to a member in the server."""
    await ctx.send("Hello {}!".format(member.name))

@bot.command()
async def boo(ctx):
    """Sends the message boo."""
    await ctx.send("Boo!")
boo_command = bot.get_command("boo")
boo_command.update(enabled=False)

@hey.error
async def hey_error(ctx, error):
    """Is run when a error occurs in the hey command."""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("ERROR: Missing argument of {}!".format(error.param))
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("ERROR: The member '{}' was not found!".format(error.argument))

@bot.event
async def on_command_error(ctx, error):
    """Runs for all other errors in commands."""
    if isinstance(error, commands.DisabledCommand):
        await ctx.send("ERROR: This command has been disabled!")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("ERROR: The command entered was not found!")

token = ""
with open('../token.txt') as f:
    token = f.readline().strip()

bot.run(token)
