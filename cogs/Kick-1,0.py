import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472,314376447747948546]


    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = "None"):
       if ctx.message.author.guild_permissions.kick_members or ctx.author.id in self.list:
        if ctx.author.bot:
            return


        try:
            embed = discord.Embed(title="You've been Kicked!", colour=0xff0000)
            embed.add_field(name='Administrator:',value=f'{ctx.author.name}',inline=False)
            embed.add_field(name='Server:',value=f'{ctx.guild.name}', inline=False)
            embed.add_field(name='Reason:',value=f'{reason}', inline=False)
            pv = await member.create_dm()
            await pv.send(embed=embed)
        except:
           pass
        try:
            await member.kick(reason=reason)
        except Exception as e:
            print(e)
        embed2 = discord.Embed()
        embed2.add_field(name='Kicked!', value=f'``{member.name}`` was kicked by ``{ctx.author}``. [{reason}]')
        await ctx.send(embed=embed2)
       else:
           embed = discord.Embed()
           embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
           await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Kick(bot))
