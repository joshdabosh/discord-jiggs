import discord
import json
import logging
import importlib
import os
import sys

import utils

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if len(sys.argv) > 1:
    if sys.argv[1].strip() == '-v' or sys.argv[1].strip() == '--verbose':
        logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


else:
    logging.basicConfig(format='[%(levelname)s] %(message)s')

log = logging.getLogger(__name__)


class Jiggs:
    def __init__(self):
        self.client = discord.Client()

        self.build_conf()
        self.build_commands()

        path = os.path.join("serviceAccount.json")
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': open("dburl.txt").read()
        })

        self.firebaseRef = db.reference('/')

    def build_conf(self):
        self.conf = json.loads(open("conf.json").read())

    def build_commands(self):
        self.commands = dict()

        files = self.conf["plugins"]
        for name in files:
            path = os.path.join(os.getcwd(), files[name]["path"])

            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            self.commands[name] = module.load(self, files[name])

            log.info("Added plugin '%s' to modules list", name)

    def start(self):
        @self.client.event
        async def on_ready():
            log.info("Logged in successfully!")

        @self.client.event
        async def on_message(message):

            log.info("Message received from %s: %s", message.author, message.content.strip())

            if message.author == self.client.user:
                return

            c = message.content.strip().split()

            if len(c) >= 2:
                if c[0] == self.conf["PREFIX"].strip():
                    if c[1] in self.commands.keys():
                        if callable(getattr(self.commands[c[1]], "respond", None)):
                            await self.commands[c[1]].respond(message)
                            log.info("Fired command '%s'", str(self.commands[c[1]]))
                        else:
                            log.info("Command '%s' is not callable", c[1])
                    else:
                        log.info("No such command '%s'", c[1])

                else:
                    return

            else:
                return

        try:
            self.client.run(os.environ["JIGGS_TOKEN"])
        except KeyError:
            log.critical("No env token found, so not starting")

    async def send(self, message, channel):
        await channel.send(message)

    async def embed(self, embed, channel):
        await channel.send(embed=embed)


def main():
    jiggs = Jiggs()
    jiggs.start()


if __name__ == "__main__":
    main()
