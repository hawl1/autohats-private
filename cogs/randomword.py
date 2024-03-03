"""
    Cog that sends a random word
"""

from discord.ext import commands
import httpx


class RandomWord(commands.Cog):
    """
    Command class.
    """

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def randomword(self, ctx):
        """
        Function to send a random word.
        """

        response = httpx.get("https://random-word-api.herokuapp.com/word").json()[0]
        await ctx.send(response)


async def setup(bot):
    """
    Runs to add the command to the bot
    """
    await bot.add_cog(RandomWord(bot))
