"""
    Command to log out.
"""

from discord.ext import commands
import discord

from dotenv import dotenv_values
from peewee import MySQLDatabase
# idk how to fix this so as well
# pylint: disable=import-error
from models import Session

config = dotenv_values(".env")

database = MySQLDatabase(
    config["DB_NAME"],
    user=config["DB_USR"],
    password=config["DB_USR_PASSWD"],
    host=config["DB_HOST"],
    port=3306,
)

class Logout(commands.Cog):
    """
    Command class.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def logout(self, ctx):
        """
        Function to logout the user.
        """
        # Check if the message is sent in a DM
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.send("Logout can only be done in a DM.")
            return

        # Check if user is logged in
        if not Session.select().where(Session.discord_id == str(ctx.author.id)).exists():
            await ctx.send("You are not logged in.")
            return

        # Confirmation prompt
        await ctx.send("Are you sure you want to log off? (yes/no)")

        def check(message):
            return message.author == ctx.author and isinstance(message.channel, discord.DMChannel) \
                and message.content.lower() in ["yes", "no"]

        try:
            confirmation_msg = await self.bot.wait_for("message", timeout=60, check=check)
            confirmation = confirmation_msg.content.lower()

            if confirmation == "yes":
                # Delete the session record
                session = Session.get(Session.discord_id == str(ctx.author.id))
                session.delete_instance()
                await ctx.send("You have been logged out.")
            else:
                await ctx.send("Logout cancelled.")
        except TimeoutError:
            await ctx.send("Confirmation timed out. Logout cancelled.")

async def setup(bot):
    """
    Runs to add the command to the bot
    """
    await bot.add_cog(Logout(bot))
