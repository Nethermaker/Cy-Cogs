from discord.ext import commands
from cogs.utils import checks

from __main__ import send_cmd_help

banlist = 'data/gbans/banlist.txt'
serverlist = 'data/gbans/serverlist.txt'


class Gbans:
    """Talos protection module"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, no_pm=True)
    @checks.is_owner()
    async def g(self, ctx):
        """Gbans commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    #@g.group(pass_context=True)
    #async def ban(self, ctx, user: discord.Member):
    #    """Bans user globally and locally"""

    #    author = ctx.message.author
    #    if not check_server(self, ctx):
    #        return

    #    with open('data/gbans/banlist.txt', 'a+') as banlist:
    #        banlist.seek(0)
    #        bannedids = banlist.read().splitlines()

    #        if author == user:
    #            await self.bot.say("You can't ban yourself.")
    #        elif user.id in bannedids:
    #            await self.bot.say("User already banned.")
    #        else:
    #            banlist.write(user.id + '\n')
    #            try:
    #                await self.bot.kick(user)
    #            except:
    #                pass

    @g.group(pass_context=True)
    async def list(self, ctx):
        """Lists all globally banned users"""

        author = ctx.message.author
        if not check_server(self, ctx):
            return

        with open(banlist, 'r') as b:
            bannedids = '\n'.join(b.read().splitlines())

            await self.bot.send_message(author, bannedids)

    @g.group(pass_context=True)
    async def toggle(self, ctx):
        """Toggles Talos server protection"""

        server = ctx.message.server.id

        if check_server(self, ctx):
            with open(serverlist, 'r+') as s:
                serverids = s.readlines()
                s.seek(0)
                for i in serverids:
                    if i != server + "\n":
                        s.write(i)
                s.truncate()
            await self.bot.say("Protection disabled.")
        else:
            with open('data/gbans/servers.txt', 'a') as s:
                s.write(server + '\n')
                await self.bot.say("Protection enabled.")

    @g.group(pass_context=True)
    async def status(self, ctx):
        """Shows protection status"""

        if check_server(self, ctx):
            await self.bot.say("Protection `online`.")
        else:
            await self.bot.say("Protection `offline`.")

    async def on_member_join(self, member):
        """Checks member if they are banned"""

        server = member.server.id
        with open(serverlist, 'r') as s:
            serverids = s.read().splitlines()
            if server in serverids:
                with open(banlist, 'r') as b:
                    bannedids = b.read().splitlines()
                    if member.id in bannedids:
                        # await self.bot.send_message(member, str(member.server)
                        #                             + " is protected by Talos.")
                        try:
                            await self.bot.kick(member)
                        except:
                            pass


def check_server(self, ctx):
        with open(serverlist, 'r') as s:
            serverids = s.read().splitlines()
            server = ctx.message.server.id

            return server in serverids


def setup(bot):
    """Adds the cog"""
    bot.add_cog(Gbans(bot))
