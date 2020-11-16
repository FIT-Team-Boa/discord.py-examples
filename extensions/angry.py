"""Is an extension representing the angry mood."""

from discord.ext import commands

class Angry(commands.Cog):
    """Is a cog for the given extension."""
    def __init__(self, bot):
        """Initializes the cog."""
        self.bot = bot

    @commands.command()
    async def mood(self, ctx):
        """Returns the current mood to the user."""
        await ctx.send("I am angry!")

def setup(bot):
    """Sets up the extension."""
    bot.add_cog(Angry(bot))
    print("Angry setup!")

def teardown(bot):
    """Removes the extension from use."""
    bot.remove_cog("Angry")
    print("Angry teardown!")
