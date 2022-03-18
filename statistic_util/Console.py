"""
## コンソール機能()
"""
import aioconsole, sys

from . import dblib, config

from .Logging import log

class console:

    """コンソールの機能です(2)"""
    
    @classmethod
    async def start(self):
        """コンソールを起動します。"""
        db = dblib.manager()
        cfg = config.loadConfig()

        log.info("コンソールを起動しました。")
        cs = await aioconsole.ainput("~ $ ")

        while True:
            pattern = [
                {
                    "aliases": ["?"],
                    "output": [
                        "help - コマンドのヘルプを表示",
                        "stop - ボットを停止します。"
                        ],
                    "cmd": None,
                    "name": "help"
                },
                {
                    "aliases": ["exit", "alt+f4"],
                    "cmd": sys.exit,
                    "output": None,
                    "name": "stop"
                },
                {
                    "aliases": ["stats"],
                    "cmd": None,
                    "output": [
                        f"ALL MESSAGES: "+ str(len(db.get_contents(f'{cfg["database"]["prefix"]}message')))
                    ],
                    "name": "status"
                }
            ]
            runned = False
            log.info(f"コンソールコマンド \"{cs}\" を実行しました。")
            for pt in pattern:
                if (pt["name"] == cs) or (cs in pt["aliases"]):
                    runned = True
                    if (not pt["output"] is None):
                        for out in pt["output"]:
                            log.info(out)
                    if (not pt["cmd"] is None):
                        pt["cmd"]()
            if (not runned):
                log.info(f"\"{cs}\" というコマンドは存在していません。ヘルプを参照してください。")

            cs = await aioconsole.ainput("~ $ ")        