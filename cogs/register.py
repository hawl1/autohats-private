from discord.ext import commands

class register(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def register(self, ctx):
        await ctx.send('This is an example command.')

async def setup(bot):
    await bot.add_cog(register(bot))
