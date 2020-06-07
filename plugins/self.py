class SelfSession:
    def __init__(self, client, config):
        self.client = client
        self.config = config

    async def respond(self, message):
        conversation = message.channel
        author = message.author
        
        uid = 'd' + str(author.id)
        username = self.client.commands['user'].get_username(uid)
        
        if not username:
            response = 'You do not have a username. Create one with the <b>set</b> method.'
            await self.client.send(response)
            return

        
        credit = self.client.commands['credit'].get_credit(uid)
        response = 'Username: **{}**'.format(username)
        response += '\nPokedollars: {}'.format(credit)

        await self.client.send(response, conversation)


def load(client, config):
    return SelfSession(client, config)
