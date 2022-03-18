import discord, os, sys, platform

from statistic_util import log, config

print("ボットを起動中")
print(f"Python: {sys.version} オペレーティングシステム: {platform.system()} {platform.version()}")

intent = discord.Intents.default()

intent.messages=True
intent.message_content=True
intent.guild_messages=True

bot = discord.Bot(intents=intent)

if not os.path.exists("config.json"):
    log.err("config.jsonが見つかりませんでした。生成しています...")
    config.saveDefaultConfig()
    log.warn("生成しました。config.jsonを確認してください。")

    sys.exit()

conf = config.loadConfig()

bot.load_extension("cogs._start")

bot.load_extension("cogs.listener")

bot.load_extension("cogs.dashboard")

try:
    bot.run(conf["token"])
except discord.errors.LoginFailure:
    log.err("トークンが無効です。config.jsonを確認してください。")