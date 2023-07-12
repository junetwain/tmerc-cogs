from redbot.core.bot import Red

from .welcomejun import Welcomejun


async def setup(bot: Red):
    await bot.add_cog(Welcomejun())
