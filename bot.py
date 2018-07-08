import logging
logging.basicConfig(level=logging.INFO)
import config
import asyncio
from discord.ext import commands
bot = commands.Bot(',')


@bot.event
async def on_ready():
    logging.info("logged in as {0.user} ({0.user.id})".format(bot))

bot.run(config.token)
