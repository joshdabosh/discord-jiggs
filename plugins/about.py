class AboutSession:

    about = "Jiggs is an open-source bot, and you can find the source code at <https://github.com/joshdabosh/discord-jiggs>\n\n\
If you'd like to invite Jiggs to your own server, you can do so by clicking <https://discord.com/oauth2/authorize?client_id=576794788393648138&scope=bot>"

    def __init__(self, client, config):
        self.client = client
        self.config = config
	
    
    async def respond(self, message):
        await self.client.send(self.about, message.channel)

def load(client, config):
    return AboutSession(client, config)
