import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class User:

    def __init__(self, client, config):
        self.client = client
        self.config = config

        self.users_ref = None

    def build(self):
        self.users_ref = self.client.firebaseRef.child("users")

    def get_uid(self, username):
        if not self.users_ref:
            self.build()

        users = self.get_users()
        for uid in users:
            if users[uid]['username'] == username:
                return uid

        return None

    def get_username(self, uid):
        if not self.users_ref:
            self.build()

        return self.users_ref.child(uid + '/username').get()

    def set_username(self, uid, username):
        if not self.users_ref:
            self.build()

        self.users_ref.child(uid).update({
            'username': username
        })

    def get_users(self):
        if not self.users_ref:
            self.build()

        users = self.users_ref.get()
        if not users:
            return {}
        return users

    def get_username_list(self):
        if not self.users_ref:
            self.build()

        users = self.get_users()
        username_list = []
        for uid in users:
            if 'username' in users[uid]:
                username_list.append(users[uid]['username'])

        return username_list


def load(client, config):
    return User(client, config)
