import discord
from discord.ext import commands
import sqlite3
from discord.utils import get

conn = sqlite3.connect('main.db')
c = conn.cursor()

class Autorole(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        c.execute(f"SELECT autorole FROM guilds_modules WHERE guild_id = {member.guild.id}")
        r = c.fetchone()
        autorole_module = r[0]
        if autorole_module == "on":
                c.execute(f"SELECT auto_role FROM guilds WHERE guild_id = {member.guild.id}")
                r = c.fetchone()
                auto_role = r[0]
                rl = get(member.guild.roles, id=auto_role)
                if auto_role == 0:
                    pass
                else:

                    if rl in member.roles:
                            pass
                    else:
                        rl = get(member.guild.roles, id=auto_role)
                        await member.add_roles(rl)
        else:
           pass



        
    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['set-auto-role','set_auto_role'])
    async def setautorole(self, ctx, role: discord.Role):
        c.execute(f"SELECT autorole FROM guilds_modules WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        autorole_module = r[0]
        if autorole_module == "on":
            
            c.execute(f"SELECT auto_role FROM guilds WHERE guild_id = {ctx.guild.id}")
            r = c.fetchone()
            sql = ("UPDATE guilds SET auto_role = ? WHERE guild_id = ?")
            val = (role.id, ctx.guild.id)
            c.execute(sql, val)

            embed = discord.Embed()
            embed.add_field(name='Success!', value=f'Role was update to {role.mention}')
            await ctx.send(embed=embed)    
            conn.commit()
        else:
            embed = discord.Embed()
            embed.add_field(name='Error!', value=f'AutoRole module is off in guilds modules. Use ``x!modules autorole [on/off] `` to change this')
            await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(Autorole(bot))