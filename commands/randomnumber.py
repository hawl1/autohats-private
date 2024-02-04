from discord.ext import commands
import random

@commands.group()
async def randomnumber(ctx):
    number = random.randint(1,1000)

    await ctx.send(number)
    
async def setup(bot):
    bot.add_command(randomnumber)