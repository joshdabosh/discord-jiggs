import discord


class HelpSession:

    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.build_usage()

    def build_usage(self):

        sorted_dict = {}
        for i in sorted(self.config['commands']):
            sorted_dict[i] = self.config['commands'][i]

        self.usage = discord.Embed(title="Commands that Jiggs understands:", color=int(self.client.conf["COLOR"], 16))

        for command in sorted_dict:
            self.usage.add_field(name=command, value=sorted_dict[command], inline=False)

    async def respond(self, message):
        await self.client.embed(self.usage, message.channel)


def load(pearl, config):
    return HelpSession(pearl, config)
