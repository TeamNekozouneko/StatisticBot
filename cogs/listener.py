import discord, sys

from discord.ext import commands

sys.path.append("../")

from statistic_util import dblib, config

class msgListener(commands.Cog):

    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self._last_member = None

        self.db = dblib.manager()
        self.cfg = config.loadConfig()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if (not self.cfg["msg"]["bot"]):
            if (message.author.bot):
                return
        
        tableName = f"{self.cfg['database']['prefix']}message"

        self.db.create_table(tableName, "author_id int, message_id int, guild_id int")

        self.db.insert(tableName, (message.author.id, message.id, message.guild.id))
    
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if (not self.cfg["msg"]["bot"]):
            if (message.author.bot):
                return
        
        tableName = f"{self.cfg['database']['prefix']}message"
        self.db.execute(f"DELETE FROM {tableName} WHERE message_id == {message.id}")

def setup(bot: discord.Bot):
    bot.add_cog(msgListener(bot))