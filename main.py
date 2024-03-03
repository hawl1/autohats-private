"""
    main.py

    Loads cogs and commands
"""

import os

import discord
from discord.ext import commands
from dotenv import dotenv_values

config = dotenv_values(".env")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


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
