"""Groups commands and event listeners in the bot together using cogs."""

from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

class Happy(commands.Cog, name="happy_mood"):
    """A cog that is called 'happy_mood'."""
    def __init__(self, bot):
        """Initializes the cog."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Prints a message when the bot is ready."""
        print("I am happy!")

    @commands.command()
    async def happy(self, ctx):
        """Responds to a user command."""
        await ctx.send("I am happy! How about you?")
        await self.on_ready()

class Smiley(commands.Cog):
    """A cog that is called 'Smiley'."""
    def __init__(self, bot):
        """Initializes the cog."""
        self.bot = bot

    @commands.command()
    async def smile(self, ctx):
        """Returns a message to user after command."""
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
