import discord
from discord.ext import commands
import random
import asyncio
class Lotto(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def lotto(self, ctx):
        nr = []
        nr2 = []
        for i in range(3):
            nr.append(random.randint(50,100))
        for i in range(3):
            nr2.append(random.randint(50,100))
        embedone = discord.Embed()
        embedone.add_field(name="Your Numbers", value=f'{nr[0]}, {nr[1]}, {nr[2]}', inline = False)
        embedone.add_field(name='Lotto Number', value=f'XXX, XXX, XXX', inline = False)
        embedone.set_footer(text='Wait 15 seconds to complete the draw')
        msg =await ctx.send(embed=embedone)
        await asyncio.sleep(15)
        if nr[0] in nr2 or nr[1] in nr2 or nr[2] in nr2:
            wincolor = 0x3be801
            embedtwo = discord.Embed(color=wincolor)   
            embedtwo.add_field(name="Your Numbers", value=f'{nr[0]}, {nr[1]}, {nr[2]}', inline = False)
            embedtwo.add_field(name='Lotto Numbers', value=f'{nr2[0]}, {nr2[1]}, {nr2[2]}', inline = False)
            embedtwo.add_field(name="Result", value="Win", inline= False)
            embedtwo.set_footer(text='draw was ended')
            await msg.edit(embed=embedtwo)
        else:
            losecolor = 0xE80303
            embedtwo = discord.Embed(color=losecolor)   
            embedtwo.add_field(name="Your Numbers", value=f'{nr[0]}, {nr[1]}, {nr[2]}', inline = False)
            embedtwo.add_field(name='Lotto Numbers', value=f'{nr2[0]}, {nr2[1]}, {nr2[2]}', inline = False)
            embedtwo.add_field(name="Result", value="Lose", inline= False)
            embedtwo.set_footer(text='draw was ended')
            await msg.edit(embed=embedtwo)
def setup(bot):
    bot.add_cog(Lotto(bot))

    