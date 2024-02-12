"""
    Example cog example that sends cookie emoji.
"""

from discord.ext import commands
import httpx


class Cookie(commands.Cog):
    """
    Command class.
    """

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def register(self, ctx):
        """
        Function to register the command.
        """

        response = httpx.get("https://random-word-api.herokuapp.com/word").json()[0]
        await ctx.send(response)


async def setup(bot):
    """
    Runs to add the command to the bot
    """
    await bot.add_cog(Cookie(bot))
