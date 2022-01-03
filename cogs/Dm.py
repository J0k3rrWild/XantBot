import discord
from discord.ext import commands, tasks
from discord.utils import get, valid_icon_size
import sqlite3
from discord import embeds
valid_icon_size
from .utils import checks


class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472,314376447747948546]


    @commands.command()
    async def dm (self, ctx, user: discord.Member = None, *, message=None):
         if ctx.message.author.guild_permissions.administrator or ctx.author.id in self.list:
            if user is None:
                await ctx.send("Well, who you sending this too?!")
            if user is not None:
                if message is None:
                    await ctx.send("What is the message you are sending?")
                if message is not None:
                    await ctx.send(f"``User {user} received your message.`` ")
                    embed = discord.Embed(colour = 0x22a6f2)
                    embed.add_field(name=f'Message from administrator:', value=f"{message}")
                    embed.set_footer(text=f"Message has been sended by administrator: {ctx.author} from: {ctx.guild}")
                    await user.send(embed=embed)
         else:
             embedd = discord.Embed(colour = 0x22a6f2)
             embedd.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
             await ctx.send(embed=embedd)





def setup(bot):
    bot.add_cog(Dm(bot))
