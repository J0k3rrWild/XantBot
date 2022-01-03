import discord
import asyncio
from discord.colour import Color
from discord.ext import commands
import sqlite3
conn = sqlite3.connect("main.db")
c = conn.cursor()

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472,314376447747948546]


    @commands.command(pass_context = True)
    async def mute(self,ctx, member: discord.Member, *, reason = None):
      if ctx.message.author.guild_permissions.manage_roles or ctx.author.id in self.list:
            c.execute(f"SELECT mute_role FROM guilds WHERE guild_id = {ctx.guild.id}")
            r = c.fetchone()
            mute_role = r[0]
            c.execute(f"SELECT mute_role FROM guilds WHERE guild_id = {ctx.guild.id}")
            r = c.fetchone()
            mute_rolee = r[0]
            role_id = ctx.guild.get_role(mute_rolee)
            role = discord.utils.get(ctx.guild.roles, name=f"{role_id}")
            if mute_role == 0:
                e = discord.Embed()
                e.add_field(name="**Error**", value="You cannot give mute because the role has not been set, use ``x!set-mute-role <@role>``")
                await ctx.send(embed=e)
                c.execute(f"SELECT mute_role FROM guilds WHERE guild_id = {ctx.guild.id}")
            if role in member.roles:
                embed = discord.Embed()
                embed.add_field(name="**Error**", value="Error! User is already muted!")
                await ctx.send(embed=embed)
            if role not in member.roles:
                await member.add_roles(role)
                embed = discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**! Reason: {2}".format(member, ctx.message.author, reason), color=0x4fffc1)
                await ctx.send(embed=embed)
                embed = discord.Embed(title="You've been Muted!", colour=0xff0000)
                embed.add_field(name='Administrator:', value=f'{ctx.author.name}', inline=False)
                embed.add_field(name='Server:', value=f'{ctx.guild.name}', inline=False)
                embed.add_field(name='Reason:', value=f'{reason}', inline=False)
                pv = await member.create_dm()
                await pv.send(embed=embed)

      else:
          embed = discord.Embed()
          embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
          await ctx.send(embed=embed)





    @commands.command(pass_context = True)
    async def unmute(self,ctx, member: discord.Member):
     if ctx.message.author.guild_permissions.manage_roles or ctx.author.id in self.list:
        c.execute(f"SELECT mute_role FROM guilds WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        mute_rolee = r[0]
        role_id = ctx.guild.get_role(mute_rolee)
        role = discord.utils.get(ctx.guild.roles, name=f"{role_id}")
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0x4fffc1)
            await ctx.send(embed=embed)
            embed = discord.Embed(title="You've been Unmuted!", colour=0x12ee1c)
            embed.add_field(name='Administrator:', value=f'{ctx.author.name}', inline=False)
            embed.add_field(name='Server:', value=f'{ctx.guild.name}', inline=False)
            pv = await member.create_dm()
            await pv.send(embed=embed)
        else:
            embed = discord.Embed()
            embed.add_field(name="**Error**", value="Error! User is not muted!")
            await ctx.send(embed=embed)

     else:
         embed = discord.Embed()
         embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
         await ctx.send(embed=embed)

    @commands.command(aliases=['set-mute-role','set_mute_role'])
    async def setmuterole(self, ctx, role: discord.Role):
     if ctx.message.author.guild_permissions.administrator or ctx.author.id in self.list:
            sql = ("UPDATE guilds SET mute_role = ? WHERE guild_id = ?")
            val = (role.id, ctx.guild.id)
            c.execute(sql, val)
            embed = discord.Embed()
            embed.add_field(name='Success!', value=f'Mute Role was update to {role.mention}')
            await ctx.send(embed=embed)    
            conn.commit()
     else:
         embed = discord.Embed()
         embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
         await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Mute(bot))