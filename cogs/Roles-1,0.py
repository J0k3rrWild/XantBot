import discord, json, asyncio
from discord.ext import commands
import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()


class RoleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472,843509858824618005]

    @commands.command(aliases=['add-role'])
    async def addrole(self, ctx, user : discord.Member, role : discord.Role):
     if ctx.message.author.guild_permissions.manage_roles or ctx.author.id in self.list:
      if ctx.author.top_role > user.top_role or ctx.author.id in self.list or ctx.author == ctx.guild.owner:
       await user.add_roles(role)
       embed = discord.Embed()
       embed.add_field(name='Success!', value=f" the role ** {role} ** has been successfully added to the user **{user.mention}**")
       await ctx.send(embed=embed)
      else:
          embed = discord.Embed()
          embed.add_field(name="**Error**", value="Your role is lower than target")
          await ctx.send(embed=embed)
     else:
         embed = discord.Embed()
         embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
         await ctx.send(embed=embed)


    @commands.command(aliases=['remove-role'])
    async def removerole(self, ctx, user : discord.Member, *, role : discord.Role):
       if ctx.message.author.guild_permissions.manage_roles or ctx.author.id in self.list:
        if ctx.author.top_role > user.top_role or ctx.author.id in self.list or ctx.author == ctx.guild.owner:
            await user.remove_roles(role)
            embed = discord.Embed()
            embed.add_field(name='Deleted!', value=f" the role ** {role} ** has been successfully removed from user **{user.mention}**")
            await ctx.send(embed=embed)
       else:
           embed = discord.Embed()
           embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
           await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(RoleCommands(bot))