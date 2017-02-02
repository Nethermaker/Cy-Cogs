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
            "Here is your random Pilot loadout, " + author.mention + ":\n\n"+ str(pilot)
        )

    @gen.group(pass_context=True)
    async def titan(self, ctx):
        """Generates random titan loadout"""

        author = ctx.message.author
        titan = '\n'.join(gen_titan())

        await self.bot.say(
            "Here is your random Titan loadout, " + author.mention + ":\n\n"+ str(titan)
        )
        
    @gen.group(pass_context=True)
    async def all(self, ctx):
        """Generates random loadout"""

        author = ctx.message.author
        all = '\n'.join(gen_all())

        await self.bot.say(
            "Here is your random loadout, " + author.mention + ":\n\n"+ str(all)
        )


def gen_pilot():
    items = []
    pilot_items = loadouts["pilot_items"]
    for key in pilot_items:
      items.append(key + ": " + random.choice(pilot_items[key]))
    return items


def gen_titan():
    items = []
    titan_items = loadouts["titan_items"]
    titan = ""
    for key in titan_items:
        if isinstance(titan_items[key], list):
            if key == "Titan":
                titan = random.choice(titan_items[key])
                items.append(key + ": " + titan)
            else:
                items.append(key + ": " + random.choice(titan_items[key]))
        else:
            items.append(key + ": " + random.choice(dict(titan_items[key].items())[titan]))
            
    return items

def gen_all():
    items = []
    items.extend(gen_pilot())
    items.extend(gen_titan())
    return items

with open(tf2, 'r') as f:
    loadouts = json.loads(f.read(), object_pairs_hook=OrderedDict)


def setup(bot):
    """Adds the cog"""
    bot.add_cog(tf2gen(bot))
