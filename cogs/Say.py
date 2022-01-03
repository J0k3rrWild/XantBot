import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472,314376447747948546]

    @commands.command()
    async def say(self, ctx, *, tekst):
        if ctx.message.author.guild_permissions.administrator or ctx.author.id in self.list:
            try:
                await ctx.message.delete()
                await ctx.send(f"{tekst}")
            except Exception as e:
                print(e)
        else:
            embed = discord.Embed()
            embed.add_field(name="**Error**",value="Wrr...ong!, You are not allowed to execute this command...")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Say(bot))