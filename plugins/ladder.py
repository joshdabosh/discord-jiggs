class LadderSession:
    def __init__(self, client, config):
        self.client = client
        self.config = config

    async def respond(self, message):
        conversation = message.channel
        author = message.author

        credit_list = self.client.commands['credit'].get_credit_list()
        credit_list = sorted(credit_list, reverse=True)[:10]
        response = 'PokeDollars Ladder:'
        
        for i in range(len(credit_list)):
            response += '\n{}. **{}**: {}'.format(i+1, credit_list[i][1], credit_list[i][0])
            
        await self.client.send(response, conversation)


def load(client, config):
    return LadderSession(client, config)
