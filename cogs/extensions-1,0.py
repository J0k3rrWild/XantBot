import discord
from discord.ext import commands
import os
from .utils import checks
import random
import traceback

import asyncio

class Rozszerzenia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, cog=None):

        if not cog:
            async with ctx.typing():
                embed = discord.Embed(
                    title="Commands Reloaded!",
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    
                    if ext.endswith(".py") and not ext.startswith("_"):
                        
                        try:
                            self.bot.unload_extension(f"cogs.{ext[:-3]}")
                            self.bot.load_extension(f"cogs.{ext[:-3]}")
                            
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: `{ext}`",
                                value=e,
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                embed.add_field(name="**Success**",value=f'cogs was reloaded')
                await ctx.send(embed=embed)
        else:
            # reload the specific cog
            async with ctx.typing():
                embed = discord.Embed(
                    title="Command Reloaded!",
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog}.py"
                if not os.path.exists(f"./cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Reload error: `{ext}`",
                        value="the command does not exist.",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cogs.{ext[:-3]}")
                        self.bot.load_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(name="**Success**",value=f'cog was reloaded')
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"Reload Error: ``{ext}``",
                            value=desired_trace,
                            inline=False
                        )
                await ctx.send(embed=embed)
def listToString(s):
    str1 = " "  
    return (str1.join(s))

def setup(bot):
    bot.add_cog(Rozszerzenia(bot))