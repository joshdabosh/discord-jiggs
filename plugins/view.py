class ViewSession:
    def __init__(self, client, config):
        self.client = client
        self.config = config

    async def respond(self, message):
        conversation = message.channel
        author = message.author

        args = message.content.split()[2:]
        
        if len(args) < 1:
            response = 'Usage: view <username>'
            await self.client.send(response, conversation)
            return

        username = args[0]
        uid = self.client.commands['user'].get_uid(username)

        if not uid:
            response = '**{}** doesn\'t seem to be a real username.'.format(username)
            await self.client.send(response, conversation)
            return
            
        credit = self.client.commands['credit'].get_credit(uid)
        response = 'Username: **{}**'.format(username)
        response += '\nPokeDollars: {}'.format(credit)

        await self.client.send(response, conversation)

def load(client, config):
    return ViewSession(client, config)
