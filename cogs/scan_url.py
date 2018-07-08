import discord
from discord.ext import commands


class ScanURLCog:
    # This cog will eventually scan any URLs it finds in messages to check if they are malicious. It will use it's own blacklist plus the VirusTotal API and delete any suspicious links.
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        print(message)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case ScanURLCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(ScanURLCog(bot))
