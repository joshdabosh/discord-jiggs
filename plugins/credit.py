import os
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class Credit:

    def __init__(self, client, config):
        self.client = client
        self.config = config

        self.users_ref = None

    def build(self):
        self.users_ref = self.client.firebaseRef.child('users')

    def init_credit(self, uid):
        self.users_ref.child(uid).update({
            'credit': 0
        })

    def get_credit(self, uid):
        if not self.users_ref:
            self.build()

        credit = self.users_ref.child(uid + '/credit').get()
        if not credit:
            self.init_credit(uid)
            return 0

        return credit

    def set_credit(self, uid, credit):
        if not self.users_ref:
            self.build()

        self.users_ref.child(uid).update({
            'credit': credit
        })

    def get_credit_list(self):
        if not self.users_ref:
            self.build()

        users = self.client.commands['user'].get_users()
        credit_list = []
        for uid in users:
            if 'username' in users[uid] and 'credit' in users[uid]:
                credit_list.append((users[uid]['credit'], users[uid]['username']))
        return credit_list

    def refresh(self, uid):
        if not self.users_ref:
            self.build()

        current = int(time.time() / 86400)
        daily = self.users_ref.child(uid + '/daily').get()
        if daily != current:
            self.users_ref.child(uid).update({
                'daily': current
            })

            return False
        return True


def load(client, config):
    return Credit(client, config)
