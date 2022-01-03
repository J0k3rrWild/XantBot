import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx):
                    
        latency = round(self.bot.latency * 1000)

        if latency <= 199:
            latencyColor = 0x3be801
        elif 199 < latency < 499:
            latencyColor = 0xff6600
        else:
            latencyColor = 0xE80303

        embed = discord.Embed(color=latencyColor)
        embed.add_field(name='Pong!', value=f"Bot latency: {latency} ms ", inline=False)
                
        await ctx.send(embed=embed)
   

def setup(bot):
    bot.add_cog(Ping(bot))
    