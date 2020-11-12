import discord
from discord.ext import commands

class Sad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mood(self, ctx):
        await ctx.send("I am Sad. :(")

def setup(bot):
    bot.add_cog(Sad(bot))
    print("Sad setup!")

def teardown(bot):
    bot.remove_cog("Sad")
    print("Sad teardown!")
