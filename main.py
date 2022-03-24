import argparse, discord, os, platform, statistic_util, sys, traceback

from statistic_util import log, config

parser = argparse.ArgumentParser(description='StatisticBotのコマンドパラメーターです。')

parser.add_argument('-t', '--token', help='設定のトークンを無視して強制的にこのトークンを指定します。', type=str, default=None)
parser.add_argument('--generate-config', help='設定ファイルを生成します。', action='store_true')
parser.add_argument('--no-load-cogs', help='コグを読み込まないで実行します。', action='store_true')

args = parser.parse_args()

print("ボットを起動中...")
print(f"Python: {sys.version} オペレーティングシステム: {platform.system()} {platform.version()}")

intent = discord.Intents.default()

intent.messages=True
intent.message_content=True
intent.guild_messages=True

bot = discord.Bot()

if not os.path.exists("config.json") or args.generate_config:
    if not args.generate_config:
        log.err("config.jsonが見つかりませんでした。生成しています...")
    else:
        log.info("config.jsonを生成中...")
    config.saveDefaultConfig()
    log.warn("生成しました。config.jsonを確認してください。")

    sys.exit()

conf = config.loadConfig()

if not args.no_load_cogs:
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
    if args.token is None:
        bot.run(conf["token"])    
    else:
        bot.run(args.token)
except discord.errors.LoginFailure:
    log.err("トークンが無効です。config.jsonを確認してください。")