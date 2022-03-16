import asyncio, discord, datetime, sys

sys.path.append("../")

from discord.ext import commands

from statistic_util import log, console, config

class _start(commands.Cog):
    
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_connect(self):
        log.append_log(f"===================== Started Session ({datetime.datetime.now().strftime('%m/%d %H:%M:%S')}) =====================")

        log.info("Discordに接続中...")
    
    @commands.Cog.listener()
    async def on_ready(self):
        log.info("接続しました。")

        log.info("設定を読み込み中...")
        self.cfg = config.loadConfig()
        log.info("読み込みました。")

        log.info("コンソールを起動しています...")
        console_task = asyncio.create_task(console.start())

def setup(bot: discord.Bot):
    bot.add_cog(_start(bot))