from discord.ext import commands
import httpx

@commands.group()
async def randomword(ctx):
    response = httpx.get("https://random-word-api.herokuapp.com/word").json()[0]

    await ctx.send(response)
    
async def setup(bot):
    bot.add_command(randomword)