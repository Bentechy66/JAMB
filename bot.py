import logging
logging.basicConfig(level=logging.INFO)
import config
import asyncio
from discord.ext import commands
bot = commands.Bot(',')

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.scan_url']

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
            bot.load_extension(extension)

@bot.event
async def on_ready():
    logging.info("logged in as {0.user} ({0.user.id})".format(bot))

bot.run(config.token)
