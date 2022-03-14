import discord, os, sys, platform

from stastic_util import *
import stastic_util

print("ボットを起動中")
print(f"Python: {sys.version} オペレーティングシステム: {platform.system()} {platform.version()}")

bot = discord.Bot()

if not os.path.exists("confing.json"):
    log.err("config.jsonが見つかりませんでした。生成しています...")
    config.saveDefaultConfig()
    log.warn("生成しました。config.jsonを確認してください。")

    sys.exit()

conf = config.loadConfig()

try:
    bot.run(conf["token"])
except discord.errors.LoginFailure:
    log.err("トークンが無効です。config.jsonを確認してください。")