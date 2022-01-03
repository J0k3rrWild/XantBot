import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()
import random
from discord.ext.commands import Bot
import math
from .utils import checks

class Ranks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472, 289032917286649856]

    @commands.command(aliases=['add_level_rank', 'add-level-rank'])
    async def setlevelrank(self, ctx, role : discord.Role, lvl):
     if ctx.message.author.guild_permissions.administrator or ctx.author.id in self.list:
        c.execute(f"SELECT Premium FROM guilds WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        premium = r[0]
        if premium == "true":

            c.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{ctx.guild.id}' and role_id = '{role.id}'")
            r = c.fetchone()
            if r is None:
                sql = ("INSERT INTO ranks(guild_id, role_id, level) VALUES(?,?,?)")
                val = (str(ctx.guild.id), str(role.id), lvl)
                c.execute(sql, val)
                conn.commit()
                embed3 = discord.Embed()
                embed3.add_field(name='**Success**', value="Role was successfully added!")
                await ctx.send(embed=embed3)
            else:
                embed4 = discord.Embed()
                embed4.add_field(name='**Error**', value="This role exist in list")
                await ctx.send(embed=embed4)
        else:
            e = discord.Embed()
            e.add_field(name='**Premium required!**', value="This feature is available in the Premium package, if you want buy, join to our discord https://discord.gg/HCH7zaFV24 and ask support about it")
            await ctx.send(embed=e)

    @commands.command(aliases=['remove_level_rank', 'remove-level-rank'])
    async def removelevelrank(self, ctx, role : discord.Role):
       if ctx.message.author.guild_permissions.administrator or ctx.author.id in self.list:
        c.execute(f"SELECT Premium FROM guilds WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        premium = r[0]
        if premium == "true":

            c.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{ctx.guild.id}' and role_id = '{role.id}'")
            r = c.fetchone()
            if r is not None:
                c.execute("DELETE FROM ranks WHERE guild_id = '{}' and role_id = '{}'".format(ctx.guild.id, role.id))
                conn.commit()
                embed2 = discord.Embed()
                embed2.add_field(name='**Success**', value="Role was successfully removed!")
                await ctx.send(embed=embed2)
            else:
                embed3 = discord.Embed()
                embed3.add_field(name='**Error**', value="This role don't exist in list")
                await ctx.send(embed=embed3)
        else:
            e = discord.Embed()
            e.add_field(name='**Premium required!**', value="This feature is available in the Premium package")
            await ctx.send(embed=e)

    @commands.command(aliases=['level_ranks', 'level-ranks'])
    async def lista(self, ctx):
       if ctx.message.author.guild_permissions.administrator or ctx.author.id in self.list:
        c.execute(f"SELECT Premium FROM guilds WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        premium = r[0]
        if premium == "true":
            c.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{ctx.guild.id}'")
            r = c.fetchall()
            if r is None:
                embed3 = discord.Embed()
                embed3.add_field(name='**Error**', value="List is empty")
                await ctx.send(embed=embed3)
            else:
                ranks = ''
                for r in r:
                    role = ctx.guild.get_role(int(r[0]))
                    ranks += f'- {role.name} » {str(r[1])} Lvl.\n'
                embed = discord.Embed()
                embed.add_field(name='**Roles for Levels**', value=f"{ranks}")
                await ctx.send(embed=embed)
        else:
            e = discord.Embed()
            e.add_field(name='**Premium required!**', value="This feature is available in the Premium package")
            await ctx.send(embed=e)

class LvlCog(commands.Cog, name='Leveling'):

    def __init__(self, bot):
        self.bot = bot

    async def ranking(self, message):
        c.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{message.guild.id}'")
        r = c.fetchall()
        c.execute(f"SELECT user_id, user_exp, user_level FROM levels WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
        r1 = c.fetchone()
        lvl = int(r1[2])
        for r in r:
            role = message.guild.get_role(int(r[0]))
            try:
                if lvl >= int(r[1]):
                    await message.author.add_roles(role)
            except:
                return



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
                pass
        else:
            try:
                c.execute(f"SELECT leveling FROM guilds_modules WHERE guild_id = {message.guild.id}")
                r = c.fetchone()
                leveling_module = r[0]


                if leveling_module == "on":

                    c.execute(f"SELECT user_id FROM levels WHERE guild_id = '{message.guild.id}' and user_id='{message.author.id}'")
                    r = c.fetchone()

                    if r is None:
                        insert_user_level("levels",message.guild.id, message.author.id, 1, 0, 0 ,0)
                        sql = ("INSERT INTO tlevels(guild_id, user_id, xp_time) VALUES(?,?,?)")
                        val = (str(message.guild.id), str(message.author.id), datetime.datetime.utcnow())
                        c.execute(sql, val)
                        conn.commit()

                    else:
                        if message.content.startswith('x!'):
                            pass
                        else:
                            c.execute(f"SELECT xp_time FROM tlevels WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
                            result2 = c.fetchone()
                            datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
                            time_diff = datetime.datetime.strptime(str(datetime.datetime.utcnow()), datetimeFormat)\
                                - datetime.datetime.strptime(str(result2[0]), datetimeFormat)
                            if time_diff.seconds >= 5:
                                sql = ("UPDATE tlevels SET xp_time = ? WHERE guild_id = ? and user_id = ?")
                                val = (datetime.datetime.utcnow(), str(message.guild.id), str(message.author.id))
                                c.execute(sql, val)
                                conn.commit()
                                add_exp(message.author.id, message.guild.id)
                                c.execute(f"SELECT user_id, user_level, user_exp, user_total_exp, user_messages FROM levels WHERE guild_id = '{message.guild.id}' and user_id='{message.author.id}'")
                                r2 = c.fetchone()

                                totalexp = int(r2[3])
                                xp_start = int(r2[2])
                                lvl_start = int(r2[1])
                                xp_end = math.floor(2 * (lvl_start ^ 2) + 50 * lvl_start + 100)
                                if xp_end < xp_start:

                                    embed = discord.Embed()
                                    embed.add_field(name='Level Up!',value=f"{message.author.mention} was gain {lvl_start + 1} level.", inline=False)

                                    await message.channel.send(embed=embed)

                                    sql = ("UPDATE levels SET user_level = ? WHERE guild_id = ? and user_id = ?")
                                    val = (int(lvl_start + 1), str(message.guild.id), str(message.author.id))
                                    c.execute(sql, val)
                                    sql = ("UPDATE levels SET user_exp = ?, user_total_exp = ? WHERE guild_id = ? and user_id = ?")
                                    val = (0, totalexp, str(message.guild.id), str(message.author.id))
                                    c.execute(sql, val)

                                    await LvlCog(self).ranking(message)
                                    conn.commit()

                                else:
                                    await LvlCog(self).ranking(message)
                            else:
                                sql = ("UPDATE tlevels SET xp_time = ? WHERE guild_id = ? and user_id = ?")
                                val = (datetime.datetime.utcnow(), str(message.guild.id), str(message.author.id))
                                c.execute(sql, val)
                                conn.commit()
                else:
                    pass
            except Exception as e:
                pass
    @commands.command(aliases=['rank', 'level', 'lvl', 'lv'])
    async def poziom(self, ctx, user:discord.User=None):

        c.execute(f"SELECT leveling FROM guilds_modules WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        leveling_module = r[0]

        if leveling_module == "on":

            if user is not None:
                c.execute(f"SELECT user_id, user_level, user_exp, user_total_exp, user_messages FROM levels WHERE guild_id = '{ctx.guild.id}' and user_id = '{user.id}'")
                r = c.fetchone()
                if r is None:
                    embed = discord.Embed()
                    embed.add_field(name=':no_entry: | Error!',value=f"The user is not in the database, after writing several messages he will be added to it")
                    await ctx.send(embed=embed)
                else:

                    await ctx.send(embed=rank_embed(user.name, user.id, ctx.guild.id, user.avatar_url))
            elif user is None:
                c.execute(f"SELECT user_id, user_level, user_exp , user_total_exp, user_messages FROM levels WHERE guild_id = '{ctx.message.guild.id}' and user_id = '{ctx.message.author.id}'")
                r = c.fetchone()
                if r is None:

                    embed = discord.Embed()
                    embed.add_field(name='Error',value=f"You are not in Database, Write some messages, to added you in server table")
                    await ctx.send(embed=embed)
                else:

                    await ctx.send(embed=rank_embed(ctx.author.name, ctx.author.id, ctx.guild.id, ctx.author.avatar_url))
        else:
            embed = discord.Embed()
            embed.add_field(name='Error!', value=f'Leveling module is off in guilds modules. Use ``x!modules leveling [on/off] `` to change this')
            await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    async def top(self, ctx):
        c.execute(f"SELECT user_id, user_exp, user_level FROM levels WHERE guild_id = '{ctx.guild.id}' ORDER BY user_level DESC, user_exp DESC")
        r = c.fetchall()
        if r is None:
            embed = discord.Embed()
            embed.add_field(name='*Error*',value="Leaderboard is empty")
            await ctx.send(embed=embed)
        else:
            c.execute(f"SELECT user_id, user_exp, user_level FROM levels WHERE guild_id = '{ctx.guild.id}' ORDER BY user_level DESC, user_exp DESC")
            r = c.fetchall()
            desc = ''
            v = 1

            for r in r:
                if v > 10:
                    break

                if r[0] == None:
                    continue

                user = self.bot.get_user(int(r[0]))
                lvl = r[2]
                desc += f' {v}. **{str(user)}** *(level {lvl})*\n'
                v += 1

            embed = discord.Embed()
            embed.add_field(name=':trophy:   **Top 10**    :trophy:', value=desc)
            embed.set_footer(text=f'{ctx.guild}')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

def rank_embed(user_name, user_id, guild, user_av):

    c.execute(f"SELECT user_id, user_level, user_exp , user_total_exp, user_messages FROM levels WHERE guild_id = '{guild}' and user_id = '{user_id}'")
    r = c.fetchone()
    xp_end = math.floor(2 * (int(r[1]) ^ 2) + 50 *int(r[1]) + 100)
    embed = discord.Embed(title=f":wrench: | Level {user_name}")
    embed.add_field(name='lvl:',value=f"{str(r[1])}")
    embed.add_field(name='Exp:',value=f"{str(r[2])}/{xp_end}")
    pasek = int(r[2])/int(xp_end)*100
    embed.add_field(name='Progress:',value=f"{int(pasek)}%")
    embed.add_field(name='Total Exp:',value=f"{str(r[3])}",)
    embed.add_field(name='Messages:',value=f"{str(r[4])}")
    embed.set_thumbnail(url=user_av)
    return embed



def leveling_module(guildid):
    c.execute(f"SELECT leveling FROM guilds_modules WHERE guild_id = {guildid}")
    r = c.fetchone()
    leveling_module = r[0]

    return leveling_module


def add_exp(user, guild):
    c.execute(f"SELECT user_id, user_level, user_exp , user_total_exp, user_messages FROM levels WHERE guild_id = '{guild}' and user_id='{user}'")
    r1 = c.fetchone()
    randmexp = random.randint(1,3)
    addexp = int(r1[2]) + randmexp
    totalexp = int(r1[3]) + randmexp
    mess = int(r1[4])
    sql = ("UPDATE levels SET user_exp = ?, user_total_exp = ?, user_messages = ? WHERE guild_id = ? and user_id = ?")
    val = (addexp , totalexp , mess + 1,  str(guild), str(user))
    c.execute(sql, val)
    conn.commit()

def insert_user_level(table, guild_id, autor_id, level,exp,total_exp, messages):

    sql = (f"INSERT INTO {table}(guild_id, user_id, user_level,user_exp, user_total_exp, user_messages) VALUES(?,?,?,?,?,?) ")
    val = (guild_id,autor_id,level,exp,total_exp,messages)
    c.execute(sql,val)
    conn.commit()


def setup(bot):
    bot.add_cog(LvlCog(bot))
    bot.add_cog(Ranks(bot))


