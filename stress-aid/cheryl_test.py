from mongo_connection import Database
#import pymongo
import pprint
from pymongo import MongoClient

#Database.insert_user("145")


client = MongoClient()
pprint.pprint(client["stress_aid"].user.insert({"account_id": "123"}))
