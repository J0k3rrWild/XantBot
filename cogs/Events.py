import discord
from discord.ext import commands
import sqlite3
from discord.ext.commands import CommandNotFound
import re


conn = sqlite3.connect("main.db")
c = conn.cursor()




#with open('badwords.txt','r') as f:
    #bad_words = '|'.join(s for l in f for s in l.split(', '))
    #bad_word_checker = re.compile(bad_words).search

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_command(self, ctx):
    #     c.execute(f"SELECT Status FROM blacklist WHERE id = {ctx.author.id}")
    #     r = c.fetchone()
    #     if r[0] == "blocked":
    #         embed2 = discord.Embed(title=f'You are been banned', color=0xff0000)
    #         embed2.add_field(name="ID BLACKLISTED", value=f"Your cannot use our bot because you are be flagged by developers as suspicious or spam, if it is a mistake and you want to appeal, please contact the support https://discord.gg/HCH7zaFV24", inline=False)
    #         await ctx.send(embed=embed2)





    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.message.add_reaction(emoji='❌')
            return
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed()
            embed.add_field(name="**Error**",value="Wrr...ong!, In your command i detected Missing Argument")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed()
            embed.add_field(name="**Error**",value="Wrr...ong!,Invalid argument...")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed()
            embed.add_field(name="**Error**",value="Wrr...ong!, You are not allowed to execute this command...")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed()
            embed.add_field(name="**Error**",value="Wrr...ong!, I am not authorized to execute this command...")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.DisabledCommand):
            embed = discord.Embed()
            embed.add_field(name="**Error**",value="Wrr...ong!, This command has been disabled by the Developers...")
            await ctx.send(embed=embed)
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 and int(m) == 0:
                z = discord.Embed()
                z.add_field(name="**Error**",value=f"You must wait {int(s)} seconds to use this command!")
                await ctx.send(embed=z)
            elif int(h) == 0 and int(m) != 0:
                z = discord.Embed()
                z.add_field(name="**Error**",value=f"You must wait {int(m)} minutes and {int(s)} seconds to use this command!!")
                await ctx.send(embed=z)
            else:
                z = discord.Embed()
                z.add_field(name="**Error**",value=f"You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!")
                await ctx.send(embed=z)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        try:
            c.execute(f"DELETE FROM levels WHERE user_id ={member.id} and guild_id = {member.guild.id}")
            conn.commit()
        except Exception as e:
            pass

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        c.execute(f"SELECT guild_id FROM guilds WHERE guild_id = {guild.id}")
        r = c.fetchone()
        if r is None:
            sql = ("INSERT INTO guilds(guild_id, Premium, welcome_channel, welcome_text,leave_text,suggests_channel, mute_role, auto_role) VALUES(?,?,?,?,?,?,?,?)")
            val = (guild.id, "false", 0, str(None), str(None), 0,0,0)
            c.execute(sql, val)
            conn.commit()
        c.execute(f"SELECT guild_id FROM guilds_modules WHERE guild_id = {guild.id}")
        r1 = c.fetchone()
        if r1 is None:
            sql = ("INSERT INTO guilds_modules(guild_id, leveling, economy, welcome, autorole, suggests) VALUES(?,?,?,?,?,?)")
            val = (guild.id, "off", "off", "off", "off","off")
            c.execute(sql, val)
            conn.commit()


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        c.execute(f"SELECT guild_id FROM guilds WHERE guild_id = {guild.id}")
        r = c.fetchone()
        if r is not None:
            
            c.execute(f"DELETE FROM guilds WHERE guild_id = {guild.id}")
            conn.commit()
        c.execute(f"SELECT guild_id FROM guilds_modules WHERE guild_id = {guild.id}")
        r1 = c.fetchone()
        if r1 is not None:
            c.execute(f"DELETE FROM guilds_modules WHERE guild_id = {guild.id}")
            conn.commit()


    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            c.execute(f"SELECT guild_id FROM guilds WHERE guild_id={message.guild.id}")
            r = c.fetchone()
            if r is None:
                sql = ("INSERT INTO guilds(guild_id, Premium, welcome_channel, welcome_text,leave_text,suggests_channel, mute_role, auto_role) VALUES(?,?,?,?,?,?,?,?)")
                val = (message.guild.id, "false", 0, str(None), str(None), 0,0,0)
                c.execute(sql, val)
                conn.commit()
        except Exception as e:
            pass
       
        try:
            c.execute(f"SELECT guild_id FROM guilds_modules WHERE guild_id={message.guild.id}")
            r1=c.fetchone()
            if r1 is None:  
                sql = ("INSERT INTO guilds_modules(guild_id, leveling, economy, welcome, autorole, suggests) VALUES(?,?,?,?,?,?)")
                val = (message.guild.id, "off", "off", "off", "off","off")
                c.execute(sql, val)
                conn.commit()
        except Exception as e:
            pass


def setup(bot):
    bot.add_cog(Events(bot))

