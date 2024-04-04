"""
    Command to get currency
"""

from dotenv import dotenv_values
from peewee import MySQLDatabase
from discord.ext import commands

# pylint: disable=import-error
from models import User, Session


config = dotenv_values(".env")

database = MySQLDatabase(
    config["DB_NAME"],
    user=config["DB_USR"],
    password=config["DB_USR_PASSWD"],
    host=config["DB_HOST"],
    port=3306,
)


class Currency(commands.Cog):
    """
    Command class.
    """

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def currency(self, ctx):
        """
        Function to register the command.
        """
        # Get the user's ID from the Discord context
        user_id = ctx.author.id

        if (
            not Session.select()
            .where(Session.discord_id == str(ctx.author.id))
            .exists()
        ):
            await ctx.send("You are not logged in.")
            return
        

        session = Session.get(str(user_id) == Session.discord_id)
        user = User.get(session.account_id)
        currency = user.coins

        await ctx.send(f"You have {currency} coins.")


async def setup(bot):
    """
    Runs to add the command to the bot
    """
    await bot.add_cog(Currency(bot))
