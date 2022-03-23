import discord, sys

from discord.ext import commands
from collections import Counter

sys.path.append("../")
from statistic_util import dblib, config, utils

class Ranking(commands.Cog):

    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self._last_member = None

        self.db = dblib.manager()
        self.config = config.loadConfig()
    
    @commands.slash_command(name="ranking", description="サーバーのランキングを取得します。")
    async def rankingCmd(self, ctx: discord.ApplicationContext):
        ranks = self.db.get_contents(f"{self.config['database']['prefix']}message", f"guild_id = {ctx.guild_id}")

        membId = []
        for guild in ranks:
            membId = membId + [guild[0]]
        
        c = Counter(membId)
        counts = c.most_common()

        author_rank = 1
        for r in counts:
            print(r[0])
            if r[0] == ctx.author.id:
                break
            author_rank = author_rank+1
        else:
            author_rank="N/A"

        embed = discord.Embed(title="サーバーランキング", description="あなたは{0}人中{1}位です。".format(ctx.author.guild.member_count, author_rank))

        await ctx.interaction.response.send_message(embed=embed, ephemeral=True)
        print(f"{c}\n\n{counts}\n\n{author_rank}")
    
def setup(bot: discord.Bot):
    bot.add_cog(Ranking(bot))