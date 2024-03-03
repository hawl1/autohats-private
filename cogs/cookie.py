"""
    Example cog example that sends cookie emoji.
"""

from discord.ext import commands


class Cookie(commands.Cog):
    """
    Command class.
    """

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def cookie(self, ctx):
        """
        Function to register the command.
        """
        await ctx.send(":cookie:")


async def setup(bot):
    """
    Runs to add the command to the bot
    """
    await bot.add_cog(Cookie(bot))
