class ListSession:
    def __init__(self, client, config):
        self.client = client
        self.config = config

    async def respond(self, message):
        conversation = message.channel

        credit_list = self.client.commands['credit'].get_credit_list()
        credit_list = sorted(credit_list, reverse=True)
        names = []
        for i in credit_list:
            names.append(credit_list[i][1])
        names = sorted(names)

        response = 'List: '

        for i in range(len(credit_list)):
            response += '\n{}'.format(names)

        await self.client.send(response, conversation)


def load(client, config):
    return ListSession(client, config)