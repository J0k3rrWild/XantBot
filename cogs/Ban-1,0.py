import discord
from discord.colour import Color
from discord.ext import commands


xant_id = 774070605674315806



class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.list = [344426002409193472, 289032917286649856]

    @commands.command()
    async def unban(self, ctx, *, member):
     if ctx.message.author.guild_permissions.ban_members or ctx.author.id in self.list:
      if ctx.bot.top_role > user.top_role:
        if ctx.author.bot:
            return
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
     else:
        embed = discord.Embed()
        embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
        await ctx.send(embed=embed)

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                embed2 = discord.Embed(Colour=discord.Color.green)
                embed2.add_field(name='Success!', value=f'{user.name}#{user.discriminator} has been unbanned')
                await ctx.send(embed=embed2)
                await ctx.guild.unban(user)
                
                

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason = None):
     if ctx.message.author.guild_permissions.ban_members or ctx.author.id in self.list:
        if ctx.author.bot:
            return
        try:
            embed = discord.Embed(title="You've been Banned!", colour=0xff0000)
            embed.add_field(name='Administrator:',value=f'{ctx.author.name}',inline=False)
            embed.add_field(name='Server:',value=f'{ctx.guild.name}', inline=False)
            embed.add_field(name='Reason:',value=f'{reason}', inline=False)
            pv = await member.create_dm()
            await pv.send(embed=embed)
        except:
           pass
        try:
            await member.ban(reason= reason)
        except Exception as e:
            print(e)
        embed2 = discord.Embed(Colour=discord.Color.red)
        embed2.add_field(name='Banned!', value=f'**{member.name}** was banned by **{ctx.author.name}**. **[{reason}]**')
        await ctx.send(embed=embed2)
     else:
        embed = discord.Embed()
        embed.add_field(name="**Error**", value="Wrr...ong!, You are not allowed to execute this command...")
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Ban(bot))