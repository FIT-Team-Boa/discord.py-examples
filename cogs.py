import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

class Happy(commands.Cog, name="happy_mood"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("I am happy!")

    @commands.command()
    async def happy(self, ctx):
        await ctx.send("I am happy! How about you?")
        await self.on_ready()

class Smiley(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def smile(self, ctx):
        await ctx.send(":)")
        happy = self.bot.get_cog("happy_mood")
        if happy is not None:
            await happy.on_ready()

bot.add_cog(Happy(bot))
bot.add_cog(Smiley(bot))

token = ""
with open('../token.txt') as f:
    token = f.readline().strip()

bot.run(token)
