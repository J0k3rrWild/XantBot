import discord
from discord.colour import Color
from discord.ext import commands
import sqlite3

conn = sqlite3.connect('main.db')
c = conn.cursor()


xant_id = 774070605674315806



class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472,314376447747948546]

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason=None):
       if ctx.message.author.guild_permissions.kick_members or ctx.author.id in self.list:
           if ctx.author.bot:
               return


           try:
             embed2 = discord.Embed()
             embed2.add_field(name="**Warn**",
             value=f"User **{member.name}** has been warned by **{ctx.author.name}**. Reason: **{reason}**")
             await ctx.send(embed=embed2)
             sql = (f"INSERT INTO warn(guild_id, user_warned, reason, author) VALUES(?,?,?,?)")
             val = (str(ctx.guild.id), str(member.id), str(reason), str(ctx.author.id))
             c.execute(sql, val)
             conn.commit()
             embed = discord.Embed(title="You've been Warned!", color=0x8f5d03)
             embed.add_field(name='Administrator:', value=f'{ctx.author.name}', inline=False)
             embed.add_field(name='Server:', value=f'{ctx.guild.name}', inline=False)
             embed.add_field(name='Reason:', value=f'{reason}', inline=False)
             pv = await member.create_dm()
             await pv.send(embed=embed)

           except:
               pass

    @commands.command()
    async def warns(self, ctx, member: discord.Member):
        if ctx.message.author.guild_permissions.kick_members or ctx.author.id in self.list:
            c.execute(f"SELECT user_warned, reason, author FROM warn where user_warned = {member.id} and guild_id = {ctx.guild.id}")
            r = c.fetchone()
            if r is None:
                a = discord.Embed()
                a.add_field(name='**Info**', value=f'User **{member.name}** dont have warns')
                await ctx.send(embed=a)
            else:
                c.execute(f"SELECT user_warned, reason, author FROM warn where user_warned = {member.id} and guild_id = {ctx.guild.id}")
                r = c.fetchall()
                a = discord.Embed()
                desc = ''
                v = 1
                for r in r:
                    members = await self.bot.fetch_user(r[2])
                    desc += f' **{v}**. Admin: **{members.name}** Reason: **{r[1]}**\n'
                    v += 1
                a.add_field(name=f'Warns {member}', value=desc)
                await ctx.send(embed=a)

    @commands.command(aliases=['remove-warns', 'remove_warns'])
    async def removewarns(self, ctx, member: discord.Member):
        if ctx.message.author.guild_permissions.manage_guild or ctx.author.id in self.list:
            c.execute(f"SELECT guild_id, user_warned FROM warn where user_warned = {member.id} and guild_id = {ctx.guild.id}")
            r = c.fetchone()
            if r is None:
                a = discord.Embed()
                a.add_field(name='**Info**', value=f'User **{member.name}** dont have warns')
                await ctx.send(embed=a)
            else:
                c.execute(f"DELETE FROM warn WHERE guild_id = {ctx.guild.id} and user_warned = {member.id}")
                conn.commit()
                a2 = discord.Embed()
                a2.add_field(name="**Warns**", value=f"User **{member.name}** warns removed")
                await ctx.send(embed=a2)






















def setup(bot):
    bot.add_cog(Warn(bot))