import re

class SetSession:
    def __init__(self, client, config):
        self.client = client
        self.config = config

    async def respond(self, message):
        conversation = message.channel
        author = message.author

        try:
            new = message.content.strip().split()[2]

        except IndexError:
            await self.client.send("Usage: /jiggs set <username>", conversation)
            return

        uid = 'd' + str(author.id)
        old = self.client.commands['user'].get_username(uid)
        username_list = self.client.commands['user'].get_username_list()

        err = ""

        if len(new) < 3 or len(new) > 20:
            err = 'Username must be between 3 and 20 characters long.'

        elif not re.match('^[a-z0-9]*$', new):
            err = 'Username must only contain alphanumeric characters.'

        elif new == old:
            err = 'That\'s your current username, silly!'

        elif new in username_list:
            err = 'Sorry, **{}** is already taken.'.format(new)

        if err != "":
            await self.client.send(err, conversation)
            return

        self.client.commands['user'].set_username(uid, new)
        response = 'You are now set to **{}**!'.format(new)

        await self.client.send(response, conversation)
        
def load(client, config):
    return SetSession(client, config)
