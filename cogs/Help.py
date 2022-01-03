import discord
from discord.ext import commands, tasks
from discord.utils import get, valid_icon_size
import sqlite3
from discord import embeds
valid_icon_size
from .utils import checks



conn = sqlite3.connect('main.db')
c = conn.cursor()

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        


    @commands.command()
    async def help(self, ctx, name=None):
        c.execute(f"SELECT Premium FROM guilds WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        status = r[0]
        
        if name is None:
            embed = discord.Embed(
                title = '📄 Commands list',
                description = f'Mouse over the name of a command or type ``help [command]`` to get information about it. \n\n ``Your premium status: {status}``',
                colour = 0x4fffc1
            )
            embed.add_field(name='General:', value='[`stats`](http://xantbot.pl/ "Checks bot informations.") [`ping`](http://xantbot.pl/ "Checks bot latency.") [`server-info`](http://xantbot.pl/ "Displays the current server information.") [`user-info`](http://xantbot.pl/ "Displays the current user information.") [`bug`](http://xantbot.pl/ "Report a bot bug to developer support.") [`suggest`](http://xantbot.pl/ "Write suggest to your server.")')
            embed.add_field(name='Games:', value='[`lotto`](http://xantbot.pl/ "Select your 3 numbers and wait a luck :D")')
            embed.add_field(name='Level:', value='[`rank`](http://xantbot.pl/ "Check your server rank") [`add-level-rank`](http://xantbot.pl/ "add the roles you get after reaching the appropriate level") [`remove-level-rank`](http://xantbot.pl/ "remove the roles you get after reaching the appropriate level") [`top`](http://xantbot.pl/ "Check your server leaderboard") [`level-ranks`](http://xantbot.pl/ "Shows all the ranks you get for the level")')
            embed.add_field(name='4Fun:', value='[`avatar`](http://xantbot.pl/ "Shows user avatar.") [`8ball`](http://xantbot.pl/ "Ask the Bot about something.") [`ship`](http://xantbot.pl/ "ship two people and check how they fit together.") ')
            embed.set_footer(text='Use ``help-adm`` to display a list of administration commands.')
            await ctx.send(embed=embed)


        elif name.lower() == 'ping':
            embed = discord.Embed(
                title = 'x!ping',
                description = '**Checks the stability of the bot.**',
                colour = 0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!ping`', inline=False)
            embed.add_field(name='*Example:*', value='`x!ping`')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)


        elif name.lower() == 'level-ranks':
            embed = discord.Embed(
                title = 'x!level-ranks',
                description = '**Shows all the ranks you get for the level.**',
                colour = 0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!level-ranks`', inline=False)
            embed.add_field(name='*Example:*', value='`x!level-ranks`')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)


        elif name.lower() == 'avatar':
            embed = discord.Embed(
                title='x!avatar',
                description='**Shows user avatar.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!avatar`', inline=False)
            embed.add_field(name='*Example:*', value='`x!avatar @J0ker` Shows @J0ker user avatar.')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)

        elif name.lower() == 'stats':
            embed = discord.Embed(
                title = 'x!stats',
                description = '**Shows full bot status and informations.**',
                colour = 0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!stats`', inline=False)
            embed.add_field(name='*Example:*', value='`x!stats`')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)

        elif name.lower() == 'server-info':
            embed = discord.Embed(
                title = 'x!server-info',
                description = '**Shows the server information.**',
                colour = 0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!server-info`', inline=False)
            embed.add_field(name='*Example:*', value='`x!server-info`')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)

        elif name.lower() == 'user-info':
            embed = discord.Embed(
                title='x!user-info',
                description='**Shows information about the selected user.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!user-info [<user>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!server-info @J0ker` Shows information about @J0ker')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)


        elif name.lower() == 'bug':
            embed = discord.Embed(
                title='x!bug',
                description='**Reports a bug to the development team.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!bug [<info>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!bug command x!ban @user shows error!` Reports a bug about x!ban command to the development team')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)


        elif name.lower() == 'lotto':
            embed = discord.Embed(
                title='x!lotto',
                description='**Creates a lotto ticket with 3 numbers, the drawing takes 15 seconds.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!lotto`', inline=False)
            embed.add_field(name='*Example:*', value='`x!lotto` ')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)


        elif name.lower() == 'suggest':
            embed = discord.Embed(
                title='x!suggest',
                description='**Sends suggestions on designated channel by admin.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!suggest [<text>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!suggest adding 4fun roles to the server` Submits proposal to add the 4fun roles on designated channel by admin, keep in mind that others may vote to express their support ')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)


        elif name.lower() == 'rank':
            embed = discord.Embed(
                title='x!rank',
                description='**Shows your (and others) community contribution and level.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!rank <user>`', inline=False)
            embed.add_field(name='*Example:*', value='`x!rank` Shows your community contribution and level')
            embed.add_field(name='*Example2:*', value='`x!rank @J0ker` Shows @J0ker community contribution and level')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)


        elif name.lower() == 'add-level-rank':
            embed = discord.Embed(
                title='x!add-level-rank',
                description='**Adds ranks per level.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!add-level-rank [<role>] [<level>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!add-level-rank @contributor 10` Adds a rank to the users upon reaching level 10.')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)


        elif name.lower() == 'remove-level-rank':
            embed = discord.Embed(
                title='x!remove-level-rank',
                description='**Removes ranks per level.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!remove-level-rank [<role>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!remove-level-rank @contributor` Removes a rank to the users upon reaching level 10.')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)


        elif name.lower() == 'top':
            embed = discord.Embed(
                title='x!top',
                description='**Shows the top 10 users of the server.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!top`', inline=False)
            embed.add_field(name='*Example:*', value='`x!top` ')
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)

        elif name.lower() == '8ball':
            embed = discord.Embed(
                title='x!8ball',
                description='**Asks bot about something.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!8ball [<question>]`', inline=False)
            embed.add_field(name='*Example:*', value="`x!8ball Someday I will find love?` Asks bot if you'll ever find love.")
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)


        elif name.lower() == 'ship':
            embed = discord.Embed(
                title='x!ship',
                description='**Checks if the people are in love.**',
                colour=0x4fffc1
            )
            embed.add_field(name='*Usage:*', value='`x!ship [<user1>] [<user2>]`', inline=False)
            embed.add_field(name='*Example:*', value="`x!ship @J0ker @Katiana` Checks if @J0ker and @Katiana love each other.")
            embed.set_footer(text='Required permissions: None')
            await ctx.send(embed=embed)





    @commands.command(aliases=['help-adm', 'helpadm'])
    async def help_adm(self, ctx, name=None):
        c.execute(f"SELECT Premium FROM guilds WHERE guild_id = {ctx.guild.id}")
        r = c.fetchone()
        status = r[0]

        if name is None:
            embed = discord.Embed(
                title = '⚙️ Admin commands',
                description = f'Mouse over the name of a command or type ``help-adm [command]`` to get information about it. \n\n ``Your premium status: {status}``',
                colour = 0x22a6f2
            )

            embed.add_field(name='Server:', value='[`dm`](http://xantbot.pl/ "DM to user as bot.") [`kick`](http://xantbot.pl/ "Kick user.") [`warn`](http://xantbot.pl/ "Warn user.") [`warns`](http://xantbot.pl/ "Show user warns.") [`remove-warns`](http://xantbot.pl/ "Remove all user warns.") [`ban`](http://xantbot.pl/ "Ban user.") [`clear`](http://xantbot.pl/ "Clear messages.") [`unban`](http://xantbot.pl/ "Unban user.") [`say`](http://xantbot.pl/ "Say something with bot!.") [`mute`](http://xantbot.pl/ "Mute selected user!.") [`unmute`](http://xantbot.pl/ "Unmute selected ussser!.")')
            embed.add_field(name='Roles:', value='[`add-role`](http://xantbot.pl/ "Add role to user.") [`remove-role`](http://xantbot.pl/ "Remove role from user.")')
            embed.add_field(name='Modules:', value='[`modules`](http://xantbot.pl/ " Modules configuration.") [`set-mute-role`](http://xantbot.pl/ " Set the Mute role.") [`set-log-channel`](http://xantbot.pl/ " Set the welcome channel.") [`set-suggest-channel`](http://xantbot.pl/ "Set the suggest channel.") [`set-auto-role`](http://xantbot.pl/ "Set Join Role.") [`set-welcome-text`](http://xantbot.pl/ "Set the welcome text.") [`set-leave-text`](http://xantbot.pl/ "Set the leave text.")')
            embed.set_footer(text='Use ``help`` to display a list of general commands.')
            await ctx.send(embed=embed)
        
        elif name.lower() == 'autorole':
            embed = discord.Embed(
                title = 'x!autorole',
                description = '**Sets the ranks given when the user enters server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!autorole [<role>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!autorole @test` adds the rank "test" to the list of ranks given upon entry')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)

        elif name.lower() == 'kick':
            embed = discord.Embed(
                title = 'x!kick',
                description = '**Kick user from the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!kick [<user>] <reason>`', inline=False)
            embed.add_field(name='*Example:*', value='`x!kick @badperson think about this!` remove user from the server with optional note "think about this!" remember, this person will receive a dm message.')
            embed.set_footer(text='Required permissions: Kick')
            await ctx.send(embed=embed)

        elif name.lower() == 'warn':
            embed = discord.Embed(
                title = 'x!warn',
                description = '**Warns user.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!warn [<user>] <reason>`', inline=False)
            embed.add_field(name='*Example:*', value='`x!warn @badperson stop do this!` warn user on the server with optional note "stop do this!" remember, this person will receive a dm message.')
            embed.set_footer(text='Required permissions: Kick')
            await ctx.send(embed=embed)

        elif name.lower() == 'warns':
            embed = discord.Embed(
                title = 'x!warns',
                description = '**Show user warns.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!warns [<user>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!warns @badperson` Show all user warns.')
            embed.set_footer(text='Required permissions: Kick')
            await ctx.send(embed=embed)

        elif name.lower() == 'remove-warns':
            embed = discord.Embed(
                title = 'x!remove-warns',
                description = '**Show user warns.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!remove-warns [<user>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!remove-warns @badperson` Remove all user warns.')
            embed.set_footer(text='Required permissions: Manage Guild')
            await ctx.send(embed=embed)



        elif name.lower() == 'ban':
            embed = discord.Embed(
                title = 'x!ban',
                description = '**Ban user from the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!ban [<user>] <reason>`', inline=False)
            embed.add_field(name='*Example:*', value='`x!ban @badperson bye bye!` ban user from the server with optional note "bye bye!" remember, this person will receive a dm message.')
            embed.set_footer(text='Required permissions: Ban')
            await ctx.send(embed=embed)


        elif name.lower() == 'dm':
            embed = discord.Embed(
                title = 'x!dm',
                description = '**Dm to user as bot.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!dm [<user>] [<text>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!dm @J0ker Check new #announcement!` Send dm as bot to user @J0ker with text "Check new #announcement!".')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)




        elif name.lower() == 'clean':
            embed = discord.Embed(
                title = 'x!clean',
                description = '**Clears selected chat from messages.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!clean [<number>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!clean 20` clears selected chat from 20 messages.')
            embed.set_footer(text='Required permissions: Manage messages')
            await ctx.send(embed=embed)

        elif name.lower() == 'unban':
            embed = discord.Embed(
                title = 'x!unban',
                description = '**Unbans the user from the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!unban [<nick with hashtag>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!unban @badperson#2137` unbans the user @badperson#2137 from the server.')
            embed.set_footer(text='Required permissions: Ban')
            await ctx.send(embed=embed)

        elif name.lower() == 'say':
            embed = discord.Embed(
                title = 'x!say',
                description = '**Write as bot on the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!say [<message>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!say hello world!` write as bot message "hello world!" on the server.')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)
            
        elif name.lower() == 'mute':
            embed = discord.Embed(
                title = 'x!mute',
                description = '**Mute user on the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!mute [<user>] <reason>`', inline=False)
            embed.add_field(name='*Example:*', value='`x!mute @badperson easy` mutes user @badperson on the server with optional note "easy" remember, this person will receive a dm message.')
            embed.set_footer(text='Required permissions: Manage roles')
            await ctx.send(embed=embed)

        elif name.lower() == 'unmute':
            embed = discord.Embed(
                title = 'x!unmute',
                description = '**Unmutes user on the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!unmute [<user>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!mute @badperson` unmutes user @badperson on the server .')
            embed.set_footer(text='Required permissions: Manage roles')
            await ctx.send(embed=embed)

        elif name.lower() == 'add-role':
            embed = discord.Embed(
                title = 'x!add-role',
                description = '**Adds a role to a specified user on the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!add-role [<user>] [<role>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!add-role @J0ker @moderator` adds role @moderator to user @J0ker.')
            embed.set_footer(text='Required permissions: Manage roles')
            await ctx.send(embed=embed)

        elif name.lower() == 'remove-role':
            embed = discord.Embed(
                title = 'x!remove-role',
                description = '**Removes a role from a specific user on the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!remove-role [<user>] [<role>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!remove-role @J0ker @moderator` removes role @moderator from user @J0ker.')
            embed.set_footer(text='Required permissions: Manage roles')
            await ctx.send(embed=embed)

        elif name.lower() == 'set-mute-role':
            embed = discord.Embed(
                title = 'x!set-mute-role',
                description = '**Set mute role on the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!set-mute-role [<role>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!set-mute-role @Muted` set role @Muted as mute role.')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)

        elif name.lower() == 'set-log-channel':
            embed = discord.Embed(
                title = 'x!set-log-channel',
                description = '**Sets the log channel (Join, Leave).**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!set-mute-role [<channel>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!set-log-channel #logs` Sets the channel #logs as log channel.')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)

        elif name.lower() == 'set-suggest-channel':
            embed = discord.Embed(
                title = 'x!set-suggest-channel',
                description = '**Sets the suggest.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!set-suggest-channel [<channel>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!set-suggest-channel #suggestion` Sets the channel #suggestion as log channel.')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)

        elif name.lower() == 'set-auto-role':
            embed = discord.Embed(
                title = 'x!set-auto-role',
                description = '**Sets the role that any user joining the server will get by default.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!set-auto-role [<role>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!set-auto-role @player` Sets the role @player as default role when joining.')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)

        elif name.lower() == 'set-welcome-text':
            embed = discord.Embed(
                title = 'x!set-welcome-text',
                description = '**Sets welcome text in your log module when new user joining to the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!set-welcome-text [<text>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!set-welcome-text Hello user in our server!` Sets welcome text as "Hello user in our server!".')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)

        elif name.lower() == 'set-leave-text':
            embed = discord.Embed(
                title = 'x!set-leave-text',
                description = '**Sets leave text in your log module when new user leave from the server.**',
                colour = 0x22a6f2
            )
            embed.add_field(name='*Usage:*', value='`x!set-leave-text [<text>]`', inline=False)
            embed.add_field(name='*Example:*', value='`x!set-welcome-text Bye Bye I hope you back!` Sets welcome text as "Bye Bye I hope you back!".')
            embed.set_footer(text='Required permissions: Administrator')
            await ctx.send(embed=embed)



        

def setup(bot):
    bot.add_cog(Help(bot))
    