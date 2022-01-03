import discord
from discord.ext import commands

class Stats(commands.Cog):
        
        def __init__(self, bot):
                self.bot = bot

        @commands.command(aliases=['stats','staty', 'status'])
        async def statystyki(self, ctx):    
                embed = discord.Embed(title='Statistics', colour=0x43780)

                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                embed.add_field(name="Servers", value=len(self.bot.guilds))
                embed.add_field(name='All users', value=len(self.bot.users))
                embed.add_field(name='Channels', value=f"{sum(1 for g in self.bot.guilds for _ in g.channels)}")
                embed.add_field(name="Library", value=f"Discord.py")
                embed.add_field(name="Bot Latency", value=f"{round(self.bot.latency * 1000)} ms")
                await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Stats(bot))
