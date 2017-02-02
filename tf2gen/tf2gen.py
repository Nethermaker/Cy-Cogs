import random
import json
from collections import OrderedDict
from discord.ext import commands

from __main__ import send_cmd_help

loadouts = []

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
        pilot = '\n'.join(gen_pilot())

        await self.bot.say(
            "Here is your random pilot loadout, " + author.mention + ":\n"+ str(pilot)
        )

    #@gen.group(pass_context=True)
    #async def titan(self, ctx):
    #    """Generates random titan loadout"""

    #    author = ctx.message.author
    #    titan = '\n'.join(titan_gen())

    #    await self.bot.say(author.mention, titan)


def gen_pilot():
    items = []
    pilot_items = loadouts["pilot"]
    for key in pilot_items:
      items.append(key + ": " + random.choice(pilot_items[key]))
    return items


def titan_gen():
    pass


with open(tf2, 'r') as f:
    loadouts = json.loads(f.read())


def setup(bot):
    """Adds the cog"""
    bot.add_cog(tf2gen(bot))
