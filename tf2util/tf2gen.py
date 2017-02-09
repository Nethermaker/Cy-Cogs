import random
import json
from collections import OrderedDict
from discord.ext import commands

from __main__ import send_cmd_help

loadouts = []

loadoutData = "data/tf2util/loadout_items.json"


class tf2util:
    """Titanfall 2 utilities"""

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

    @gen.group(pass_context=True, hidden=True)
    async def cancer(self, ctx):
        """Generates cancerous loadout"""
        
        author = ctx.message.author
        authorRoles = author.roles
        serverRoles = Server.roles
        validRoleNames = ["Admins", "Mods"]
        validUsers = ["@Ginger#1304", "@Vorducas#6921", "@Nethermaker#9667"]
        validRoleObjects = []
        for (role in serverRoles) {
            if (role.name in validRoleNames) {
                validRoleObjects.append(role)
        
        if (set(validRoleObjects).isdisjoint(set(authorRoles)) or author.mention in validUsers):
            all = "\n".join(gen_cancer())
            
            await self.bot.say(
                "Here is your random loadout, " + author.mention + ":\n\n" + str(all)
            )   

def gen_pilot():
    items = []
    pilot_items = loadouts["pilot_items"]
    for key in pilot_items:
      items.append("**" + key + "**: " + random.choice(pilot_items[key]))
    return items


def gen_titan():
    items = []
    titan_items = loadouts["titan_items"]
    titan = ""
    for key in titan_items:
        if isinstance(titan_items[key], list):
            if key == "Titan":
                titan = random.choice(titan_items[key])
                items.append("**" + key + "**: " + titan)
            else:
                items.append("**" + key + "**: " + random.choice(titan_items[key]))
        else:
            items.append("**" + key + "**: " + random.choice(dict(titan_items[key].items())[titan]))
            
    return items

def gen_all():
    items = []
    items.extend(gen_pilot())
    items.extend(gen_titan())
    return items
    
def gen_cancer():
    items = []
    pilot_items = loadouts["pilot_items"]
    items.append("**Tactical**: A-Wall")
    items.append("**Primary**: " + str(random.choice(["Devotion", "Hemlok BF-R"])))
    items.append("**Secondary**: MGL Mag Launcher")
    items.append("**Ordnance**: Arc Grenade")
    items.append("**Kit 1**: Power Cell")
    items.append("**Kit 2**: Low Profile")
    items.append("**Execution**: " + str(random.choice(pilot_items["Execution"])))
    items.append("**Boost**: Pilot Sentry")
    items.append("**Titan**: Tone")
    items.append("**Kit 1**: Overcore")
    items.append("**Kit 2**: Pulse-Echo")
    items.append("**Titanfall Kit**: Dome Shield")
    return items


with open(loadout_data, 'r') as f:
    loadouts = json.loads(f.read(), object_pairs_hook=OrderedDict)


def setup(bot):
    """Adds the cog"""
    bot.add_cog(tf2util(bot))
