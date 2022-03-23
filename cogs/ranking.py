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
            if r[0] == ctx.author.id:
                break
            author_rank = author_rank+1
        else:
            author_rank="N/A"
        
        ran = 1
        ranksL = []
        for ranked in counts:
            if (ran == 11):
                break
            ranksL = ranksL + [f"{ran}. <@!{ranked[0]}> ({ranked[1]})"]
            ran = ran+1
        
        rf = '\n'.join(ranksL)

        embed = discord.Embed(title="サーバーランキング", description=rf)

        await ctx.interaction.response.send_message(embed=embed, ephemeral=True)
    
def setup(bot: discord.Bot):
    bot.add_cog(Ranking(bot))