import discord

from discord.ext import commands

class MessageListener(commands.Cog):

    def __init__(self, bot: discord.Bot):
        pass

    @commands.Cog.listener()
    async def on_message(self):
        pass