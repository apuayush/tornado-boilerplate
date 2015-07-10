"""
SkyNet User database handler
"""
from skynet.db.db import mongodb

user_db = mongodb.user_db

def find_user_id(hashed, callback):
    user_db.find_one({'hashed': hashed}, callback = callback)