import discord, asyncio, random, json
from discord.ext import commands
from discord.ext.commands import clean_content
per1 = ["Friendzone ;(",'"Only Friends"','"Fiends"',"Better, but its no love"]
per2 = ["Still Friendzone", "There is not much love here ... ;("]
per3 = ["But one person has little sense of romance!","But there's a small bit of love somewhere","I sense a small bit of love!", "But someone has a bit of love for someone..."]
per4 = ["There's a bit of love there!", "There is a bit of love there...",  "A small bit of love is in the air..."]
per5 = ["But it's very one-sided OwO", "It appears one sided!","There's some potential!","I sense a bit of potential!","There's a bit of romance going on here!", "I feel like there's some romance progressing!","The love is getting there..."]  
per6 = ["I feel the romance progressing!", "There's some love in the air!", "I'm starting to feel some love!"]
per7 = ["There is definitely love somewhere!","I can see the love is there! Somewhere...", "I definitely can see that love is in the air"]
per8 = ["Love is flying around you!", "You obviously have feelings for each other"]
per9 = ["You fit together!", "Together to Heaven!", "You fit together definitively!", "True love!", "Definitely more than love!"]
hearts = [":sparkling_heart:", ":heart_decoration:",  ":heart_exclamation:", ":heartbeat:", ":heartpulse:", ":hearts:",  ":blue_heart:", ":green_heart:", ":purple_heart:", ":revolving_hearts:", ":yellow_heart:", ":two_hearts:"]

class Ship(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                
        @commands.command()
        async def ship(self, ctx, name1 : clean_content, name2 : clean_content):
            shipnumber = random.randint(0,100)
            if 0 <= shipnumber <= 10:
               shipstate = "Very bad! {}".format(random.choice(per1))
            elif 10 < shipnumber <= 20:
                shipstate = "Bad! {}".format(random.choice(per2))
            elif 20 < shipnumber <= 30:
                shipstate = "Nothing special! {}".format(random.choice(per3))
            elif 30 < shipnumber <= 40:
                shipstate = "Uuuu! {}".format(random.choice(per4))
            elif 40 < shipnumber <= 60:
                shipstate = "That's it! {}".format(random.choice(per5))
            elif 60 < shipnumber <= 70:
                shipstate = "Good! {}".format(random.choice(per6))
            elif 70 < shipnumber <= 80:
                shipstate = "Very good! {}".format(random.choice(per7))
            elif 80 < shipnumber <= 90:
                shipstate = "Over average! {}".format(random.choice(per8))
            elif 90 < shipnumber <= 100:
                shipstate = "OMG true love! {}".format(random.choice(per9))

            if shipnumber <= 33:
                shipColor = 0xE80303
            elif 33 < shipnumber < 66:
                shipColor = 0xff6600
            else:
                shipColor = 0x3be801

            emb = (discord.Embed(color=shipColor,  title="Ship for:", description="**{0}** and **{1}** {2}".format(name1, name2, random.choice(hearts))))
            emb.add_field(name="Result:", value=f"{shipnumber}%", inline=True)
            emb.add_field(name="Status:", value=f"{shipstate}", inline=False)
            emb.set_author(name="Shipping", icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/microsoft/209/heart-with-arrow_1f498.png")
            await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(Ship(bot))