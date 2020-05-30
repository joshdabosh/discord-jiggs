class SetSession:
    def __init__(self, client, config):
        self.client = client
        self.config = config
	
    
    async def respond(self, message):
        conversation = message.channel
        author = message.author

        args = message.content.strip().split()[2:]

        if len(args) == 0:
            await self.client.send("Usage: set <username>", conversation)
            return

        await self.client.send(author.id, conversation)
        
        uid = "d"+str(author.id)

def load(client, config):
    return SetSession(client, config)
