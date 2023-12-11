# to confirm that firebase app starts before notifications API

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\Lenovo\Downloads\ecomitwaves-firebase-adminsdk-gojzc-8c41553d0c.json")
firebase_admin.initialize_app(cred, options={'projectId': 'ecomitwaves'})
