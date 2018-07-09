import discord
import config
import re
from virus_total_apis import PublicApi as VirusTotalPublicApi
from discord.ext import commands

vt = VirusTotalPublicApi(config.virustotal_api_key)

class ScanURLCog:
    # This cog will eventually scan any URLs it finds in messages to check if they are malicious. It will use it's own blacklist plus the VirusTotal API and delete any suspicious links.
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        # First, scan the message with the VirusTotal API
        #TODO: Select all URLs from a message
        url = re.search("(?P<url>https?://[^\s]+)", message.content).group("url") # Find a URL in the message, note that this currently only finds the first URL in the message
        if url != None:
            # If our url is not empty (a url was not found)
            response = vt.get_url_report(url)
            if int(response['results']['positives']) != 0:
                # No need to send the message if no maliciousness was found
                percent_malicious = (int(response['results']['positives']) / int(response['results']['total'])) * 100
                await message.channel.send('VirusTotal results: ' + str(response['results']['positives']) + ' / ' + str(response['results']['total']) + ' (' + str(percent_malicious) + '%) of scanners found that this link was malicious.')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case ScanURLCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(ScanURLCog(bot))
