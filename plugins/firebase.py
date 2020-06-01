import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Firebase:

	def __init__(self, pearl):
		self.pearl = pearl
		
		path = os.path.join("serviceAccount.json")
		cred = credentials.Certificate(path)
		firebase_admin.initialize_app(cred, {
			'databaseURL': open("../dburl.txt")
		})

		self.ref = db.reference('/')

def initialize(pearl):
	return Firebase(pearl)
