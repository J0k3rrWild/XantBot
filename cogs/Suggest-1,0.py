import discord
from discord.ext import commands
import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()
class Suggest(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['set_suggest_channel', 'set-suggest-channel'])
    @commands.has_permissions(administrator=True)
    async def setsuggestchannel(self, ctx, channel:discord.TextChannel):
        c.execute(f"SELECT suggests FROM guilds_modules WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        suggest_module = r[0]

        if suggest_module == "on":

            c.execute(f"SELECT suggests_channel FROM guilds WHERE guild_id = {ctx.guild.id}")
            r = c.fetchone()
            sql = ("UPDATE guilds SET suggests_channel = ? WHERE guild_id = ?")
            val = (channel.id, ctx.guild.id)
            c.execute(sql, val)

            embed = discord.Embed()
            embed.add_field(name='Success!', value=f'Sugget channel has been updated to {channel.mention}')
            await ctx.send(embed=embed)    
            conn.commit()
        else:
            embed = discord.Embed()
            embed.add_field(name='Error!', value=f'Suggest module is off in guilds modules. Use ``x!modules suggest [on/off] `` to change this')
            await ctx.send(embed=embed)  



    @commands.command(aliases=['sugestia', 'suggest'])
    async def propozycja(self, ctx, *, arg):
        c.execute(f"SELECT suggests FROM guilds_modules WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        suggest_module = r[0]
        if suggest_module == "on":
            c.execute(f"SELECT suggests_channel FROM guilds WHERE guild_id = {ctx.guild.id}")
            r1 = c.fetchone()
            suggest_channel = r1[0]
            if suggest_channel == 0:
                embed = discord.Embed()
                embed.add_field(name='**Error**', value='the channel has not been set. Use ``x!set-suggest-channel [#channel] `` to set it')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title = "Suggestion",
                    description = f"**Content:**\n```{arg}```"
                )
                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                channel = self.bot.get_channel(id=int(suggest_channel))
                msg = await channel.send(embed=embed)
                await msg.add_reaction("✔️")
                await msg.add_reaction("❌")
        else:
            embed = discord.Embed()
            embed.add_field(name='Error!', value=f'Suggest module is off in guilds modules. Use ``x!modules suggest [on/off] `` to change this')
            await ctx.send(embed=embed) 
def setup(bot):
    bot.add_cog(Suggest(bot))