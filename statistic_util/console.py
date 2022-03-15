"""
## コンソール機能()
"""

import aioconsole, sys

from . import *

pattern = [
    {
        "aliases": ["?"],
        "cmd": log.info,
        "name": "help"
    },
    {
        "aliases": ["exit", "alt+f4"],
        "cmd": sys.exit,
        "name": "stop"
    }
]

async def start():
    log.info("コンソールを起動しました。")
    cs = await aioconsole.ainput("~ $ ")

    while True:
        for pt in pattern:
            if (pt["name"] == cs) or (cs in pt["aliases"]):
                r = pt["cmd"]("help - ヘルプを表示")
        cs = await aioconsole.ainput("~ $ ")