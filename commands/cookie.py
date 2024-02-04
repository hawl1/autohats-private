from discord.ext import commands

@commands.group()
async def cookie(ctx):
    await ctx.send(':cookie:')
    
async def setup(bot):
    bot.add_command(cookie)