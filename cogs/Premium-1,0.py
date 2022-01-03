import discord
from discord import embeds
from discord.ext import commands, tasks
import sqlite3
from discord.utils import get, valid_icon_size
from .utils import checks


conn = sqlite3.connect('main.db')
c = conn.cursor()



class Premium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def premium(self, ctx):
        c.execute(f"SELECT Premium FROM guilds WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        if r[0] == "true":
            await ctx.send("Premium Valid")
            
        else:
            await ctx.send("No Premium")
        conn.commit()

    @commands.command()
    async def setpremium(self, ctx, premiumstatus, id):
        if ctx.author.id == 344426002409193472 or ctx.author.id == 843509858824618005:
            sql = ("UPDATE guilds SET Premium = ? WHERE guild_id = ?")
            val = (str(premiumstatus.lower()), str(id))
            c.execute(sql, val)
            conn.commit()
            a = discord.Embed()
            a.add_field(name='Success', value=f"set Premium for guild id ``{id}`` to ``{premiumstatus}``")
            
            await ctx.send(embed=a)
        else:
            embed = discord.Embed(colour=0xff0000)
            embed.add_field(name="**Insufficient Permission**", value="**ONLY DEVELOPER CAN USE THIS COMMAND!**")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Premium(bot))