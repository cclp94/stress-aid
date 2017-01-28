from flask.ext.pymongo import PyMongo
from flask import Flask
app = Flask(__name__)


# mongo = PyMongo('main')

# result = []
#     mongo.db.users.insert({"account_id": 43233})
#     cursor = mongo.db.users.find({}, {"_id": 0})
#     for c in cursor:
#     	result.append(c)


class Database(object):
    @staticmethod
    def insert_new_user(account_id):
        mongo = PyMongo(app)
        return mongo.db.users.insert({"account_id": account_id})

    @staticmethod
    def update_temp_list(number, quantifier, account_id):
        """
        update the array that stores the temp list (< 6 hours)
        """
        mongo = PyMongo(app)
        temp_data_list = [td for td in mongo.db.users.find_one({"account_id"}, {"_id": 0, "temp": 1})]
        print(temp_data_list)
        return 0

        # in temp, there's a time stamp and an array of {num, quant}

