"""
    Register command to register users.
"""

from discord.ext import commands
import discord

from dotenv import dotenv_values
from peewee import MySQLDatabase
from argon2 import PasswordHasher
# idk how to fix this so
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


class Register(commands.Cog):
    """
    Command class.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def register(self, ctx):
        """
        Function to initiate the registration process.
        """
        # Check if the message is sent in a DM
        if not isinstance(ctx.channel, discord.DMChannel):
            await ctx.send("Registration can only be done in a DM.")
            return

        # Check if user is already logged in
        if Session.select().where(Session.discord_id == str(ctx.author.id)).exists():
            await ctx.send(
                "You are already logged in. You cannot create another account."
            )
            return

        await ctx.send("Please enter your username:")

        def check(message):
            return message.author == ctx.author and isinstance(
                message.channel, discord.DMChannel
            )

        try:
            username_msg = await self.bot.wait_for("message", timeout=60, check=check)
            username = username_msg.content

            # Check if username is already taken
            if User.select().where(User.username == username).exists():
                await ctx.send(
                    "Sorry, that username is already taken. Please choose another one."
                )
                return

            await ctx.send("Please enter your password:")
            password_msg = await self.bot.wait_for("message", timeout=60, check=check)
            password = password_msg.content

            hashed_password = ph.hash(password)

            await ctx.send("Please enter your email (if you want to skip, type skip.):")
            email_msg = await self.bot.wait_for("message", timeout=60, check=check)
            email = email_msg.content if email_msg.content == "skip" else None

            # Check if email is already taken
            if email and User.select().where(User.email == email).exists():
                await ctx.send(
                    "Sorry, that email is already registered. Please use a different one or skip."
                )
                return

            # Create a new user record and save it to the database
            user = User(username=username, password=hashed_password, email=email)
            user.save()

            # Create a session for the registered user
            session = Session(discord_id=str(ctx.author.id), account_id=user.id)
            session.save()

            await ctx.send(f"Thank you, {username}, for registering.")
        except TimeoutError:
            await ctx.send("Registration timed out. Please try again.")


async def setup(bot):
    """
    Runs to add the command to the bot
    """
    await bot.add_cog(Register(bot))
