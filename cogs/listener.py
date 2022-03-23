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
        black = self.cfg["msg"]["blackList"]
        # 条件分岐
        if (not self.cfg["msg"]["bot"]) and (message.author.bot):
            return

        if (message.author.id in black["id"]) or (message.author.name in black["in"]) or (message.author.name in black["name"]):
            return
        for blSt in black["startsWith"]:
            if message.author.name.startswith(blSt):
                return
        # データベースに登録

        tableName = f"{self.cfg['database']['prefix']}message"

        self.db.create_table(tableName, "author_id int, message_id int, guild_id int")

        self.db.insert(tableName, (message.author.id, message.id, message.guild.id))

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        black = self.cfg["msg"]["blackList"]
        # 条件分岐
        if (not self.cfg["msg"]["bot"]) and (message.author.bot):
            return

        if (message.author.id in black["id"]) or (message.author.name in black["in"]) or (message.author.name in black["name"]):
            return
        for blSt in black["startsWith"]:
            if message.author.name.startswith(blSt):
                return
        # データベースを編集

        tableName = f"{self.cfg['database']['prefix']}message"
        self.db.execute(f"DELETE FROM {tableName} WHERE message_id == {message.id}")

def setup(bot: discord.Bot):
    bot.add_cog(msgListener(bot))
