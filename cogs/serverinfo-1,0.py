import discord
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['server_info','server-info'])
    async def guild(self, ctx):
        embed = discord.Embed(
            title = '{}'.format(ctx.guild.name),
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text=f"Użył komendy: {ctx.author}", icon_url=ctx.author.avatar_url)

        roles = [role for role in ctx.guild.roles]

        embed.add_field(name="**Owner: **", value=f"{ctx.guild.owner}", inline=False)
        embed.add_field(name="**Guild_id: **", value=f"{ctx.guild.id}", inline=False)
        embed.add_field(name="**Created_at: **", value=ctx.guild.created_at.strftime("%A, %d %B %Y, %H:%M:%S UTC"), inline=False)
        embed.add_field(name=f"**Roles: **", value=f"{len(roles)}", inline=False)
        embed.add_field(name="**Members: **", value=f"{len(ctx.guild.members)}", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Server(bot))