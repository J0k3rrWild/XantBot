import discord
from discord.ext import commands
import inspect
import os
class Eval(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.list = [344426002409193472,314376447747948546, 843509858824618005]


    @commands.command(pass_context=True, aliases=['eval'])
    async def evall(self,ctx, *, command):
     if ctx.author.id in self.list:
        res = eval(command)
        if inspect.isawaitable(res):
            print(res)
            await ctx.send(await res)
        else:
            print(res)
            await ctx.send(res)
     else:
        embed = discord.Embed(colour=0xff0000)
        embed.add_field(name="**Insufficient Permission**", value="**ONLY DEVELOPER CAN USE THIS COMMAND!**")
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Eval(bot))