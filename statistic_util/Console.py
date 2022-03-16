"""
## コンソール機能()
"""
import aioconsole, sys

from .Logging import log

class console:
    """コンソールの機能です(2)"""
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
        }
    ]
    
    @classmethod
    async def start(self):
        """コンソールを起動します。"""
        log.info("コンソールを起動しました。")
        cs = await aioconsole.ainput("~ $ ")

        while True:
            for pt in self.pattern:
                if (pt["name"] == cs) or (cs in pt["aliases"]):
                    if (not pt["output"] is None):
                        for out in pt["output"]:
                            log.info(out)
                    if (not pt["cmd"] is None):
                        pt["cmd"]()
            cs = await aioconsole.ainput("~ $ ")        