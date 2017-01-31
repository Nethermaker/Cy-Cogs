import random
import discord
from discord.ext import commands

Tactical = ['Cloak', 'Pulse Blade', 'Grapple', 'Stim', 'A-wall', 'Phase Shift',
            'Holo Pilot']
Primary = ['R201', 'Hemlock', 'G2', 'Flatline', 'Car', 'Alternator', 'Volt',
           'R-97', 'Spitfire', 'Lstar', 'Devotion', 'Krabar', 'Double Take',
           'DMR', 'EVA-8', 'Mastiff', 'Cold War', 'Softball', 'SMR', 'EPG']
Secondary = ['Archer', 'MGL', 'Thunderbolt', 'Charge Laser', 'RE - 45',
             'P2016', 'Wingman Elite', 'Mozambique', 'Wingman']
Ordnance = ['Frag Grenade', 'Arc Grenade', 'Firestar', 'Gravity Star',
            'Electric Smoke Grenade', 'Satchel']
Kit1 = ['Power Cell', 'Fast Regen', 'Ordance Expert', 'Phase Embark']
Kit2 = ['Kill Report', 'Wallhang', 'Hover', 'Low Profile']
Titan = ['Ion', 'Tone', 'Legion', 'Ronin', 'Scorch', 'Northstar']


class loadouts:
    """Titanfall 2 loadout generator"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def loadout(self):
        """Generates random loadout"""

        list = '\n'.join(loadout())

        await self.bot.say(list)


def loadout():
    list = []
    list.append('Tactical: ' + str(random.choice(Tactical)))
    list.append('Primary: ' + str(random.choice(Primary)))
    list.append('Secondary: ' + str(random.choice(Secondary)))
    list.append('Ordanance: ' + str(random.choice(Ordnance)))
    list.append('Kit 1: ' + str(random.choice(Kit1)))
    list.append('Kit 2: ' + str(random.choice(Kit2)))
    list.append('Titan: ' + str(random.choice(Titan)))
    return list


def setup(bot):
    """Adds the cog"""
    bot.add_cog(loadouts(bot))
