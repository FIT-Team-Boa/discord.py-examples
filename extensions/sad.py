"""Is an extension representing the sad mood."""

from discord.ext import commands

class Sad(commands.Cog):
    """Is a cog for the given extension."""
    def __init__(self, bot):
        """Initializes the cog."""
        self.bot = bot

    @commands.command()
    async def mood(self, ctx):
        """Returns the current mood to the user."""
        await ctx.send("I am Sad. :(")

def setup(bot):
    """Sets up the extension."""
    bot.add_cog(Sad(bot))
    print("Sad setup!")

def teardown(bot):
    """Removes the extension from use."""
    bot.remove_cog("Sad")
    print("Sad teardown!")
