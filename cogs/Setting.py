import discord
from discord.ext import commands
import sqlite3
from .utils import checks
conn = sqlite3.connect('main.db')
c = conn.cursor()

class Command(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True,aliases=['modules'])
    @checks.is_admin()
    async def moduly(self, ctx):
        embed = discord.Embed(title="Modules")
        embed.add_field(name ="Log", value="``x!modules log [on/off]`` - Enable/Disable log module (join,leave)",  inline = False)
        embed.add_field(name ="Leveling", value="``x!modules leveling [on/off]``- Enable/Disable leveling module",  inline = False)
        embed.add_field(name ="Suggest", value="``x!modules suggest [on/off]`` - Enable/Disable suggest module",  inline = False)
        embed.add_field(name ="Autorole", value= "``x!modules autorole [on/off]`` - Enable/Disable suggest module",  inline = False)
        await ctx.send(embed=embed)


    @moduly.command()
    @checks.is_admin()
    async def log(self, ctx, status):
        status = status.lower()
        if status == "on" or status == "off":
            sql = ("UPDATE guilds_modules SET welcome = ? WHERE guild_id = ?")
            val = (status ,ctx.guild.id)
            c.execute(sql, val)
            conn.commit()
            a = discord.Embed()
            a.add_field(name ="**Success**", value=f"Module log has been set to ``{status}``")
            await ctx.send(embed=a)    
        else:
            a = discord.Embed()
            a.add_field(name ="**Usage**", value="x!modules leveling [on/off]")
            await ctx.send(embed=a)
    @moduly.command()
    @commands.has_permissions(manage_channels=True)
    async def leveling(self, ctx, status):
        status = status.lower()
        if status == "on" or status == "off":
            sql = ("UPDATE guilds_modules SET leveling = ? WHERE guild_id = ?")
            val = (status ,str(ctx.guild.id))
            c.execute(sql, val)
            conn.commit()
            a = discord.Embed()
                
            a.add_field(name ="**Success**", value=f"Module Leveling has been set to ``{status}``")
            await ctx.send(embed=a)
                
        else:
            a = discord.Embed()
            a.add_field(name ="**Usage**", value="x!modules leveling [on/off]")
            await ctx.send(embed=a)

    @moduly.command()
    @checks.is_admin()
    async def suggest(self, ctx,status):
            status = status.lower()
            if status == "on" or status == "off":

                sql = ("UPDATE guilds_modules SET suggests = ? WHERE guild_id = ?")
                val = (status ,str(ctx.guild.id))
                
                a = discord.Embed()
                a.add_field(name ="**Success**", value=f"Module Suggest has been set to ``{status}``")
                await ctx.send(embed=a)
                c.execute(sql, val)
                conn.commit()
            else:
                a = discord.Embed()
                a.add_field(name ="**Usage**", value="x!modules suggest [on/off]")
                await ctx.send(embed=a)

    @moduly.command()
    @checks.is_admin()
    async def autorole(self,ctx, status):
        status = status.lower()
        if status == "on" or status == "off":
            sql = ("UPDATE guilds_modules SET autorole = ? WHERE guild_id = ?")
            val = (status ,str(ctx.guild.id))
            c.execute(sql, val)
            a = discord.Embed()
            a.add_field(name ="**Success**", value=f"Module Autorole has been set to ``{status}``")

            await ctx.send(embed=a)            
            conn.commit()

        else:
            a = discord.Embed()
            a.add_field(name ="**Usage**", value="x!modules autorole [on/off]")
            await ctx.send(embed=a)
def setup(bot):
    bot.add_cog(Command(bot))