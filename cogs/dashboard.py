from collections import Counter
import discord, sys
from discord.ext import commands

sys.path.append("../")
from statistic_util import dblib, log, LogLevel, config

class Dashboard(commands.Cog):
    
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self._last_member = None

        self.db = dblib.manager()
        self.cfg = config.loadConfig()
    
    @commands.slash_command(name="dashboard", description="ユーザーのダッシュボードを表示します。")
    async def cmd_dashboard(self, ctx: discord.ApplicationContext):
        await ctx.interaction.response.send_message(embed=discord.Embed(title="データベースにアクセス中...", color=discord.Color.green()), ephemeral=True)

        embed = discord.Embed(title="ダッシュボード", color=discord.Color.green())
        
        try:
            l = []
            for msg in self.db.get_contents(f"{self.cfg['database']['prefix']}message", f"author_id = {ctx.author.id}"):
                if (msg[0] == ctx.author.id):
                    l = l + [msg]
        
            i = []
            for msg in self.db.get_contents(f"{self.cfg['database']['prefix']}message", f"author_id = {ctx.author.id} AND guild_id = {ctx.author.guild.id}"):
                if (msg[0] == ctx.author.id and msg[2] == ctx.guild.id):
                    i = i + [msg]
        
            embed.add_field(name="メッセージ件数", value=f"{'{:,}'.format(len(i))}/{'{:,}'.format(len(l))}件")
        except TypeError as e:
            embed.add_field(name="メッセージ件数", value="取得できませんでした。")

        try:
            s = []
            for guild in self.db.get_contents(f"{self.cfg['database']['prefix']}message", f"author_id = {ctx.author.id}"):
                s = s + [guild[2]]

            guild_id = Counter(s).most_common()[0][0]
            guild_message_count = Counter(s).most_common()[0][1]

            g = self.bot.get_guild(guild_id)

            embed.add_field(name="一番メッセージを送信するサーバー", value=f"{g.name} ({'{:,}'.format(guild_message_count)})")
        except:
            embed.add_field(name="一番メッセージを送信するサーバー", value="取得できませんでした。")

        await ctx.edit(embed=embed)

def setup(bot: discord.Bot):
    bot.add_cog(Dashboard(bot))