"""
    Cog that sends a random number between 1 and 1000.
"""

import random
from discord.ext import commands


class RandomNumber(commands.Cog):
    """
    Command class.
    """

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def randomnumber(self, ctx):
        """
        Function to register the command.
        """
        await ctx.send(random.randint(1, 1000))


async def setup(bot):
    """
    Runs to add the command to the bot
    """
    await bot.add_cog(RandomNumber(bot))
