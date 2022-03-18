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
        
        l = []
        for msg in self.db.get_contents(f"{self.cfg['database']['prefix']}message"):
            if (msg[0] == ctx.author.id):
                l = l + [msg]
        
        i = []
        for msg in self.db.get_contents(f"{self.cfg['database']['prefix']}message"):
            if (msg[0] == ctx.author.id and msg[3] == ctx.guild.id):
                i = i + [msg]
        
        embed = discord.Embed(title="ダッシュボード", color=discord.Color.green())
        embed.add_field(name="メッセージ件数", value=f"{'{:,}'.format(len(i))}/{'{:,}'.format(len(l))}件")

        await ctx.edit(embed=embed)

def setup(bot: discord.Bot):
    bot.add_cog(Dashboard(bot))