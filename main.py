"""
    main.py

    Loads cogs and commands
"""

import os
import datetime

import discord
from discord.ext import commands
from dotenv import dotenv_values

config = dotenv_values(".env")

intents = discord.Intents.default()
intents.message_content = True

from models import Session, User, get_database
from peewee import DateTimeField, SQL

bot = commands.Bot(command_prefix="!", intents=intents)

database = get_database()
User._meta.database = database

@bot.event
async def on_command(ctx):
    """
    on_command(ctx)

    Called whenever a command is used.

    Parameters:
        ctx (commands.Context): The context of the command.

    """

    if (
            not Session.select()
            .where(Session.discord_id == str(ctx.author.id))
            .exists()
        ):
        return
    
    user_id = ctx.author.id
    session = Session.get(str(user_id) == Session.discord_id)

    user = User.get(session.account_id)
    user.last_online = datetime.datetime.now()
    user.save()


@bot.event
async def on_ready():
    """
    on_ready()

    Loads commands and cogs to bot.
    """

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("------")


bot.run(config["DISCORD_TOKEN"])
