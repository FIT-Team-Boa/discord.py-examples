import discord
from discord.ext import commands

class Angry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mood(self, ctx):
        await ctx.send("I am angry!")

def setup(bot):
    bot.add_cog(Angry(bot))
    print("Angry setup!")

def teardown(bot):
    bot.remove_cog("Angry")
    print("Angry teardown!")
