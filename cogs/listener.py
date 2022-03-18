import discord, sys

from discord.ext import commands

sys.path.append("../")

class MessageListener(commands.Cog):

    def __init__(self, bot: discord.Bot):
        pass

    @commands.Cog.listener()
    async def on_message(self):
        pass