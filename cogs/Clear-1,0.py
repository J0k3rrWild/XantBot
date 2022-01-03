import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472, 289032917286649856, 847873418720182334]

    @commands.command(aliases=['clear', 'wyczysc'])
    async def czysc(self, ctx, amount: int):
     if ctx.message.author.guild_permissions.manage_messages or ctx.author.id in self.list:
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed()
        embed.add_field(name='Success!', value=f'Cleared {amount} messages')
        await ctx.send(embed=embed)
     else:
         embed = discord.Embed()
         embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
         await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Clear(bot))