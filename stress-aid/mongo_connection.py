from flask_pymongo import PyMongo
from flask import Flask
app = Flask(__name__)


class Database(object):
    @staticmethod
    def insert_new_user(account_id):
        mongo = PyMongo(app)
        return mongo.db.users.insert({"account_id": account_id})

    @staticmethod
    def retreive_account():
        pass

    @staticmethod
    def update_temp_list(number, quantifier, account_id):
        """
        update the array that stores the temp list (< 6 hours)
        """
        mongo = PyMongo(app)
        temp_data_list = mongo.db.users.find_one({"account_id": account_id}, {"_id": 0, "temp": 1})
        if temp_data_list["temp"]:
        	return temp_data_list["temp"]["time"]
        # else:
        # 	mongo.db.users.update_one({"account_id": account_id}, {$set: {temp: {time: [[number, quantifier]]}}})
    	
        return temp_data_list

        # in temp, there's a time stamp and an array of {num, quant}
