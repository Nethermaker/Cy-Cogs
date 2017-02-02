import random
import json
from discord.ext import commands

from __main__ import send_cmd_help

loadouts = []

keys = []

tf2 = "data/tf2gen/tf2gen.json"


class tf2gen:
    """Titanfall 2 loadout generator"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, no_pm=True)
    async def gen(self, ctx):
        """Generator commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @gen.group(pass_context=True)
    async def pilot(self, ctx):
        """Generates random pilot loadout"""

        author = ctx.message.author
        pilot = '\n'.join(pilot_gen())

        await self.bot.say(author.mention + "\n"+ str(pilot))

    #@gen.group(pass_context=True)
    #async def titan(self, ctx):
    #    """Generates random titan loadout"""

    #    author = ctx.message.author
    #    titan = '\n'.join(titan_gen())

    #    await self.bot.say(author.mention, titan)


def pilot_gen():
    p = []
    pilot_items = loadouts["pilot"]
    for key in pilot_items:
      p.append(key + ": " + random.choice(pilot_items[key]):
    return p


def titan_gen():
    pass


with open(tf2, 'r') as f:
        loadouts = json.loads(f.read())
        for c in loadouts:
            if loadouts[c]:
                keys.append(c)
                for n in loadouts[c]:
                    if loadouts[c][n]:
                        keys.append(n)


def setup(bot):
    """Adds the cog"""
    bot.add_cog(tf2gen(bot))
