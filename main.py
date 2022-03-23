import discord, os, sys, platform, traceback

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

for loadCogs in os.listdir("cogs/"):
    loadf = os.path.splitext(loadCogs)
    if loadf[1] == ".py":
        log.info("{0}を読み込み中".format(loadf[0]+loadf[1]))
        try:
            bot.load_extension("cogs."+loadf[0])
        except Exception as e:
            log.warn("{0}は無効なコグファイルです。".format(loadf[0]+loadf[1]))
            log.err(traceback.format_exception_only(type(e), e)[0].rstrip("\n"))
            continue

try:
    bot.run(conf["token"])    
except discord.errors.LoginFailure:
    log.err("トークンが無効です。config.jsonを確認してください。")