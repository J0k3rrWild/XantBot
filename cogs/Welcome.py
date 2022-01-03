import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3  
conn = sqlite3.connect('main.db')
c = conn.cursor()

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['set_welcome_text', 'set-welcome-text', 'set-welcome-message', 'set_welcome_message'])
    @commands.has_permissions(administrator=True)
    async def setwelcometext(self, ctx, *, text):
        c.execute(f"SELECT welcome FROM guilds_modules WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        welcome_module = r[0]

        if welcome_module == "on":

            c.execute(f"SELECT welcome_text FROM guilds WHERE guild_id = {ctx.guild.id}")
            r = c.fetchone()
            sql = ("UPDATE guilds SET welcome_text = ? WHERE guild_id = ?")
            val = (text, ctx.guild.id)
            c.execute(sql, val)

            embed = discord.Embed()
            embed.add_field(name='Success!', value=f'Welcome text has been updated to ``{text}``')
            await ctx.send(embed=embed)    
            conn.commit()
        else:
            embed = discord.Embed()
            embed.add_field(name='Error!', value=f'Log module is off in guilds modules. Use ``x!modules log [on/off] `` to change this')
            await ctx.send(embed=embed)

    @commands.command(aliases=['set_leave_text', 'set-leave-text', 'set_leave_message', "set-leave-message"])
    @commands.has_permissions(administrator=True)
    async def setleavetext(self, ctx, *, text):
        c.execute(f"SELECT welcome FROM guilds_modules WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        welcome_module = r[0]

        if welcome_module == "on":

            c.execute(f"SELECT leave_text FROM guilds WHERE guild_id = {ctx.guild.id}")
            r = c.fetchone()
            sql = ("UPDATE guilds SET leave_text = ? WHERE guild_id = ?")
            val = (text, ctx.guild.id)
            c.execute(sql, val)

            embed = discord.Embed()
            embed.add_field(name='Success!', value=f'Leave text has been updated to ``{text}``')
            await ctx.send(embed=embed)
            conn.commit()
        else:
            embed = discord.Embed()
            embed.add_field(name='Error!',
                            value=f'Log module is off in guilds modules. Use ``x!modules log [on/off] `` to change this')
            await ctx.send(embed=embed)


    @commands.command(aliases=['set-log-channel', 'set_log_channel'])
    @commands.has_permissions(administrator=True)
    async def setwelcomechannel(self, ctx, channel:discord.TextChannel):
        c.execute(f"SELECT welcome FROM guilds_modules WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        welcome_module = r[0]

        if welcome_module == "on":

            c.execute(f"SELECT welcome_channel FROM guilds WHERE guild_id = {ctx.guild.id}")
            r = c.fetchone()
            sql = ("UPDATE guilds SET welcome_channel = ? WHERE guild_id = ?")
            val = (channel.id, ctx.guild.id)
            c.execute(sql, val)

            embed = discord.Embed()
            embed.add_field(name='Success!', value=f'Log Channel has been updated to {channel.mention}')
            await ctx.send(embed=embed)    
            conn.commit()
        else:
            embed = discord.Embed()
            embed.add_field(name='Error!', value=f'Log module is off in guilds modules. Use ``x!modules log [on/off] `` to change this')
            await ctx.send(embed=embed)  


    @commands.Cog.listener()
    async def on_member_join(self, member):

        c.execute(f"SELECT welcome FROM guilds_modules WHERE guild_id = {member.guild.id}")
        r = c.fetchone()
        welcome_module = r[0]

        if welcome_module == "on":
            if member.bot:
                pass
            else:
                c.execute(f"SELECT welcome_channel FROM guilds WHERE guild_id = {member.guild.id}")
                r = c.fetchone()
                welcome_channel = r[0]
                c.execute(f"SELECT welcome_text FROM guilds WHERE guild_id = {member.guild.id}")
                r1 = c.fetchone()
                welcome_text = r1[0]
                members = len(list(member.guild.members))
                mention = member.mention
                user = member.name
                guild = member.guild
                embed = discord.Embed(title="User joined the server!", colour=0x43780, description=str(welcome_text).format(members=members, mention=mention, user=user, guild=guild))
                embed.add_field(name="Account created at: ", value=member.created_at.strftime("%A, %d %B %Y, %H:%M:%S UTC"), inline=False)
                embed.set_thumbnail(url=f"{member.avatar_url}")
                embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                channel = self.bot.get_channel(int(welcome_channel))
                await channel.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        c.execute(f"SELECT welcome FROM guilds_modules WHERE guild_id = {member.guild.id}")
        r = c.fetchone()
        welcome_module = r[0]

        if welcome_module == "on":
            if member.bot:
                pass
            else:
                c.execute(f"SELECT welcome_channel FROM guilds WHERE guild_id = {member.guild.id}")
                r = c.fetchone()
                welcome_channel = r[0]
                c.execute(f"SELECT leave_text FROM guilds WHERE guild_id = {member.guild.id}")
                r1 = c.fetchone()
                welcome_text = r1[0]
                members = len(list(member.guild.members))
                mention = member.mention
                user = member.name
                guild = member.guild
                embed = discord.Embed(title="User has left from the server!", colour=0x43780,
                                      description=str(welcome_text).format(members=members, mention=mention, user=user,
                                                                           guild=guild,))
                embed.set_thumbnail(url=f"{member.avatar_url}")
                embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                channel = self.bot.get_channel(int(welcome_channel))
                await channel.send(embed=embed)
        else:
            pass

def setup(bot):
    bot.add_cog(Welcome(bot))
