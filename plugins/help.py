import discord


class HelpSession:

    def __init__(self, client, config):
        self.usage = discord.Embed(title=("Commands that Jiggs understands:".format(self.client.conf['PREFIX'])),
                                   color=int(self.client.conf["COLOR"], 16))
        self.client = client
        self.config = config
        self.build_usage()

    def build_usage(self):
        for command in self.config['commands']:
            self.usage.add_field(name=command, value=self.config['commands'][command], inline=False)

    async def respond(self, message):
        await self.client.embed(self.usage, message.channel)


def load(pearl, config):
    return HelpSession(pearl, config)