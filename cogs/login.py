"""
    Command to login
"""

from discord.ext import commands
import discord

from dotenv import dotenv_values
from peewee import MySQLDatabase
from argon2 import PasswordHasher, exceptions
# if you are watching files, you know why.
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

ph = PasswordHasher()

class Login(commands.Cog):
    """
    Command class.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def login(self, ctx):
        """
        Function to log in the user.
        """
        # Check if the message is sent in a DM
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.send("Login can only be done in a DM.")
            return

        await ctx.send("Please enter your username:")

        def check(message):
            return message.author == ctx.author and isinstance(message.channel, discord.DMChannel)

        try:
            username_msg = await self.bot.wait_for("message", timeout=60, check=check)
            username = username_msg.content

            # Check if username exists
            try:
                user = User.get(User.username == username)
            except User.DoesNotExist:
                await ctx.send("Invalid username.")
                return

            await ctx.send("Please enter your password:")
            password_msg = await self.bot.wait_for("message", timeout=60, check=check)
            password = password_msg.content

            # Verify the password
            try:
                if ph.verify(user.password, password):
                    # Create a session for the logged-in user
                    session = Session(discord_id=str(ctx.author.id), account_id=user.id)
                    session.save()
                    await ctx.send("You have been logged in.")
                else:
                    await ctx.send("Invalid password.")
            except exceptions.VerifyMismatchError:
                await ctx.send("Invalid password.")
        except TimeoutError:
            await ctx.send("Login timed out. Please try again.")

async def setup(bot):
    """
    Runs to add the command to the bot
    """
    await bot.add_cog(Login(bot))
