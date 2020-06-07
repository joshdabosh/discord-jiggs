class DailySession:
    def __init__(self, client, config):
        self.client = client
        self.config = config

        self.bonus = 100

    async def respond(self, message):
        conversation = message.channel
        author = message.author
        
        uid = 'd' + str(author.id)
        username = self.client.commands['user'].get_username(uid)

        if not username:
            response = 'You do not have a username. Create one with the <b>set</b> method.'
            await self.client.send(response, conversation)
            return

        if self.client.commands['credit'].refresh(uid):
            response = 'That\'s enough for today!'
            await self.client.send(response, conversation)
            return

        credit = self.client.commands['credit'].get_credit(uid)
        credit += self.bonus
        
        self.client.commands['credit'].set_credit(uid, credit)
        
        response = '{} PokeDollars added to your account!'.format(self.bonus)
        await self.client.send(response, conversation)


def load(client, config):
    return DailySession(client, config)
