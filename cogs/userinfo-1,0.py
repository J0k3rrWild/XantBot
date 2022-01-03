import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['user_info', 'user-info'])
    async def userinfo(self, ctx, member:discord.Member):
        embed = discord.Embed(
            title = f":wrench: | Userinfo",
            colour = discord.Colour.green(),
            timestamp=ctx.message.created_at
        )
        roles = [role for role in member.roles]

        embed = discord.Embed(timestamp=ctx.message.created_at)

        embed.set_author(name=f"{member} Info")
        embed.set_thumbnail(url=member.avatar_url)
    

        embed.add_field(name="**ID: **", value=member.id, inline=False)
        embed.add_field(name="**Name: **", value=member.display_name, inline=False)

        embed.add_field(name="**Account created at: **", value=member.created_at.strftime("%A, %d %B %Y, %H:%M:%S UTC"), inline=False)
        embed.add_field(name="**Server join at: **", value=member.joined_at.strftime("%A, %d %B %Y, %H:%M:%S UTC"), inline=False)

        embed.add_field(name=f"**All Roles** ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="**The highest role: **", value=member.top_role.mention, inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UserInfo(bot))
