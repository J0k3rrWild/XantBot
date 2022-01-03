import discord
from discord.ext import commands
import random

class MagicBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['8ball','ball'])
    async def magicznakula(self, ctx, * , pyt):
        odpowiedz = '{}'.format(random.choice([
                            "Yes, definitely :8ball:",
                            "There is little chance of that :8ball:",                                
                            "I think so :8ball:",
                            "There's a possibility :8ball:",
                            "It looks good :8ball:",
                            "Yes! :8ball:",
                            "Of course :8ball:",
                            "You have to work hard :8ball:",
                            "Ask for it later :8ball:",
                            "May not :8ball:",
                            "You have no chance :8ball:",
                            "Don't ask about it anymore  :8ball:",
                            "My answer is .. No :8ball:",
                            "My code says no :8ball:",
                            "It doesn't look good :8ball:",
                            "Are you okay? :8ball:",
                            "There is something about it! :8ball:",
                            "You can only dream :8ball:",
                            "It must be a bug! :8ball:",
                            "Hahahahaha :8ball:",
                            "Yes, of course :8ball:",
                            "I think not :8ball:",
                            "Very :8ball:",
                            "Certainly not :8ball:"]))

        embed = discord.Embed()
        embed.add_field(name="Question", value=f"{pyt}", inline= False)
        embed.add_field(name="Answer", value=f'{odpowiedz}', inline= False)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(MagicBall(bot))