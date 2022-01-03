import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect('main.db')
c = conn.cursor()

class Bug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blackbug(self, ctx, status, id):
        if ctx.author.id == 344426002409193472 or ctx.author.id == 289032917286649856:
            c.execute(f"SELECT id from blacklist where id = {id}")
            r = c.fetchone()
            if r is None:
                sql = (f"INSERT INTO blacklist(Status, id) VALUES(?,?)")
                val = (str(status.lower()), str(id))
                c.execute(sql, val)
                conn.commit()
                a = discord.Embed()
                a.add_field(name='Success', value=f"ID ``{id}``  ``{status}``")
                await ctx.send(embed=a)
            else:
                sql = ("UPDATE blacklist SET Status = ? WHERE id = ?")
                val = (str(status.lower()), str(id))
                c.execute(sql, val)
                conn.commit()
                a = discord.Embed()
                a.add_field(name='Success', value=f"ID ``{id}``  ``{status}``")
                await ctx.send(embed=a)
        else:
            embed = discord.Embed(colour=0xff0000)
            embed.add_field(name="**Insufficient Permission**", value="**ONLY DEVELOPER CAN USE THIS COMMAND!**")
            await ctx.send(embed=embed)

    @commands.cooldown(1, 10800, commands.BucketType.user)
    @commands.command()
    async def bug(self, ctx, *, bugstr):
     c.execute(f"SELECT Status FROM blacklist WHERE id = {ctx.author.id}")
     r = c.fetchone()
     if r is None:
      sql = (f"INSERT INTO blacklist(id, Status) VALUES(?,?)")
      val = (ctx.author.id, "unblocked")
      c.execute(sql, val)
      conn.commit()
      embed = discord.Embed(color=0x43780)
      embed.add_field(name="Bug", value=f'{bugstr}')
      embed.set_thumbnail(url=ctx.message.author.avatar_url)
      embed.add_field(name="User", value=f"{ctx.message.author.name}", inline=False)
      embed.add_field(name="User ID", value=f"{ctx.message.author.id}", inline=False)
      embed.add_field(name="Guild", value=f"{ctx.author.guild.name}", inline=False)
      embed.add_field(name="Guild ID", value=f"{ctx.author.guild.id}", inline=False)
      embed.add_field(name="Guild Owner", value=f"{ctx.guild.owner}", inline=False)
      embed.add_field(name="Data", value=ctx.message.created_at.strftime("%A, %d %B %Y, %H:%M:%S UTC"), inline=False)
      channel = self.bot.get_channel(int(690531273395142686))
      await channel.send(embed=embed)
      embed = discord.Embed(title=f'Bug Report', color=0x43780)
      embed.add_field(name="XantBot DevTeam", value=f"Your application has been given to the XantBot developers! Remember that next time you can use the command for 3 hours.", inline=False)
      embed.add_field(name="XantBot Official Discord", value=f"You need support or informations? Join to our discord https://discord.gg/HCH7zaFV24 and follow our changelog.", inline=False)
      await ctx.send(embed=embed)
     if r[0] == "blocked":
      embed2 = discord.Embed(title=f'Bug Report', color=0xff0000)
      embed2.add_field(name="ID BLACKLISTED", value=f"Your application cannot be sent because it has been flagged by developers as suspicious or spam, if it is a mistake and you want to appeal, please contact the support https://discord.gg/HCH7zaFV24",inline=False)
      await ctx.send(embed=embed2)
     else:
        if ctx.author.bot:
            return
        else:
            embed = discord.Embed(color=0x43780)
            embed.add_field(name="Bug", value=f'{bugstr}')
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.add_field(name="User", value=f"{ctx.message.author.name}", inline = False)
            embed.add_field(name="User ID", value=f"{ctx.message.author.id}", inline = False)
            embed.add_field(name="Guild", value=f"{ctx.author.guild.name}", inline = False)
            embed.add_field(name="Guild ID", value=f"{ctx.author.guild.id}", inline = False)
            embed.add_field(name="Guild Owner", value=f"{ctx.guild.owner}", inline = False)
            embed.add_field(name="Data", value=ctx.message.created_at.strftime("%A, %d %B %Y, %H:%M:%S UTC"), inline = False)
            channel = self.bot.get_channel(int(690531273395142686))
            await channel.send(embed=embed)
            embed = discord.Embed(title=f'Bug Report', color=0x43780)
            embed.add_field(name="XantBot DevTeam", value=f"Your application has been given to the XantBot developers! Remember that next time you can use the command for 3 hours.", inline=False)
            embed.add_field(name="XantBot Official Discord", value=f"You need support or informations? Join to our discord https://discord.gg/HCH7zaFV24 and follow our changelog.", inline=False)
            await ctx.send(embed=embed)

        
def guilds(self):
    return self.bot.guilds
def setup(bot):
    bot.add_cog(Bug(bot))