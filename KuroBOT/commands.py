# KuroBOT Command List
from discord.ext import commands

class KuroCommands(commands.Cog, name="Commands"):
    def __init__(self, curry: commands.Bot):
        self.bot = curry

    @commands.command(name="spaceops", brief='Link Space Ops Arcade Download')
    async def spaceops(self, message):
        await message.channel.send("Space Ops Arcade is an Android Free to Play Game available on google play! Get it here: https://play.google.com/store/apps/details?id=com.aboveconstraints.spaceops")

    @commands.command(name="constraints", brief='Explain Constraints')
    async def constraints(self, message):
        await message.channel.send("Constraints is a multiplayer game in development by xcibe95x featuring Paragon Characters!, it's a big thing, it require time, but it's coming :3")
    
def setup(curry: commands.Bot):
    curry.add_cog(KuroCommands(curry))