"""
## コンソール機能()
"""
import aioconsole, sys, discord, traceback

from . import dblib, config

from .Logging import log

class console:

    """コンソールの機能です(2)"""
    
    @classmethod
    async def start(self, bot: discord.Bot):
        """コンソールを起動します。"""
        db = dblib.manager()
        cfg = config.loadConfig()

        log.info("コンソールを起動しました。")
        cmd = await aioconsole.ainput("BOT> ")

        while True:
            log.info("コンソールコマンド\"{0}\"が使用されました。".format(cmd))

            try:
                if cmd == "help" or cmd == "?":
                    log.info("Console commands:")
                    log.info("help - Command help")
                    log.info("version - Bot version")
                    log.info("status - Bot status")
                elif cmd == "version" or cmd == "ver":
                    log.info("StatisticBot 1.0.3")
                elif cmd == "status" or cmd == "stats":
                    log.info("Display name: {0} ({1})".format(str(bot.user), bot.user.id))
                    log.info("2FA: {0}".format(bot.user.mfa_enabled))
                    log.info("")
                    log.info("Messages: {0} messages saved.".format(len(db.get_contents("StatisticBot_message"))))
                    log.info("Servers: {0} servers joined.".format(len(bot.guilds)))
                elif cmd == "stop" or cmd == "close" or cmd == "exit":
                    log.info("データベースのコミット中...")
                    db.force_commit()
                    log.info("データベースをクローズ中...")
                    db.close()
                    log.info("ボットを停止中...")
                    await bot.close()
                else:
                    log.info("そのようなコマンドを存在していません。")
            except Exception as e:
                log.err("コマンドの実行中に例外が発生しました。")
                log.err(traceback.format_exception_only(type(e), e)[0].rstrip("\n"))
            
            cmd = await aioconsole.ainput("BOT> ")