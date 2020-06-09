import random
import requests
import discord

class SlotsSession:
    def __init__(self, client, config):
        self.client = client
        self.config = config

        self.rate = ['banana']*3 + ['cherries']*3 + ['pear']*3 + ['melon']*3 + ['grapes']*3 + ['tangerine']*3 + ['watermelon']*3 + ['large_blue_diamond', 'dollar', 'innocent', 'bell']


        self.combos = {
            "banana3":1,
            "cherries2":1,
            "pear2":3,
            "melon2":3,
            "grapes2":3,
            "tangerine2":3,
            "watermelon2":3,
            "cherries3":3,
            "pear3":10,
            "melon3":10,
            "grapes3":10,
            "tangerine3":10,
            "watermelon3":10,
            "diamond2":20,
            "dollar2":10,
            "innocent2":20,
            "bell3":75,
            "dollar3":30,
            "innocent3":75,
            "diamond3":500
        }
        
        seed = requests.get('https://www.random.org/cgi-bin/randbyte?nbytes=16&format=f').text
        random.seed(seed)

    async def respond(self, message):
        conversation = message.channel
        author = message.author

        args = message.content.strip().split()[2:]

        if len(args) < 1:
            response = 'Usage: slots <bet>'
            await self.client.send(response, conversation)

            return

        uid = 'd' + str(author.id)
        self.username = self.client.commands['user'].get_username(uid)
        username = self.username

        if not username:
            response = 'You do not have a username. Create one with the **set** method.'
            await self.client.send(response, conversation)
            return

        try:
            bet = int(args[0])
        except:
            response = 'Must be an integer amount.'
            await self.client.send(response, conversation)
            return

        credit = self.client.commands['credit'].get_credit(uid)

        err = ""

        if bet == 0:
            err = 'Please don\'t waste my time.'
        elif bet < 0:
            err = 'Sneaky, but not good enough.'
        elif bet > credit:
            err = 'You don\'t have enough to wager this.'
        elif bet > 500:
            err = 'Max bet size is 500, sorry.'

        if err != "":
            await self.client.send(err, conversation)
            return

        line = self.get_line()
        payout = self.get_payout(line)
        
        line1 = self.get_line()
        line2 = self.get_line()
        
        win = bet*payout

        self.client.commands['credit'].set_credit(uid, credit - bet + win)
        
        await self.client.send(self.get_string(line1)+"\n"+self.get_string(line)+"  <-\n"+self.get_string(line2)+self.get_msg(win), conversation)

    def get_msg(self, win):
        if win > 0:
            return '\n\nYou won {} PokeDollars!'.format(win)
        return '\n\nYou lost everything.'
        
    def get_line(self):
        return [random.choice(self.rate) for i in range(3)]

    def get_payout(self, line):
        payout = 0
        for icon in line:
            combo = icon + str(line.count(icon))
            if combo in self.combos.keys():
                payout = max(payout, self.combos[combo])
        return payout

    def get_string(self, line):
        return " : ".join([":%s:"%i for i  in line])

def load(client, config):
	return SlotsSession(client, config)
