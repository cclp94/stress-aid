from flask_pymongo import PyMongo
from flask import Flask
from datetime import datetime
app = Flask(__name__)
mongo = PyMongo(app)


class Database(object):
    @staticmethod
    def insert_new_user(account_id):
        return mongo.db.users.insert({"account_id": account_id, "compressed_data": []})

    @staticmethod
    def retreive_account():
        pass

    @staticmethod
    def mean(numbers):
        return float(sum(numbers)) / max(len(numbers), 1)


    @staticmethod
    def process_raw_temp_data(data_dump):
        """
        count number of negativity and how negative, percentage of negative / positive / neutral
        average rating for negative and for positive
        """
        if data_dump is None:
            return
        # mongo = PyMongo(app)
        list_data = data_dump["list"]
        result = {}
        pos = []
        neg = []
        neu = []
        
        for d in list_data:
            if d>0.3:
                pos.append(d)
            elif d< -0.3:
                neg.append(d)
            else:
                neu.append(d)
        result["posLen"] = len(pos)
        result["negLen"] = len(neg)
        result["neuLen"] = len(neu)
        result["totalDataLen"] = len(list_data)
        result["pos"] = Database.mean(pos)
        result["neg"] = Database.mean(neg)
        result["neu"] = Database.mean(neu)
        result["total"] = Database.mean(list_data)
        return result


    @staticmethod
    def update_temp_list(number, account_id):
        """
        update the array that stores the temp list (< 6 hours)
        """
        # mongo = PyMongo(app)
        temp_data = mongo.db.users.find_one({"account_id": account_id})

        if temp_data is None:
            return 0

        if "temp" in temp_data.keys():
            past = datetime.strptime(temp_data["temp"]["time"], "%Y-%m-%d %H:%M:%S.%f")
            now = datetime.now()

            #if it's 1 hour since the temp data dump started, then compress it and start new temp data dump
            if (now-past).total_seconds() > 60:
                #start new temp fuck me and compress data duck me
                data_dump = Database.process_raw_temp_data(temp_data["temp"])
                if data_dump is not None:
                    data_dump["time"] = temp_data["temp"]["time"]
                    temp_data["compressed_data"].append(data_dump)
                    #mongo.db.users.update({"account_id": account_id}, {"$push": {"compressed_data": data_dump}})
                
                temp_data["temp"]["time"] = str(now)
                temp_data["temp"]["list"] = []
                temp_data["temp"]["list"].append(number)

                mongo.db.users.remove({"account_id": account_id})
                mongo.db.users.insert(temp_data)
            


            else:
                mongo.db.users.update({"account_id": account_id}, {"$push":{"temp.list": number}})
            return "updated"
        
        else:
            data = {}
            data["time"] = str(datetime.now())
            data["list"] = []
            data["list"].append(number)


            mongo.db.users.update({"account_id": account_id}, {"$set": {"temp": data}})

            return "updated"


        return temp_data
    
    @staticmethod
    def am_i_depressed(account_id):
        """
        remove expired data (data > 1 hour old, for purposes of demo)
        return a score of average across 10 min (for demo purposes)
        """
        user_data = mongo.db.users.find_one({"account_id": account_id}, {"_id":0, "compressed_data": 1, "temp_data": 1})
        compressed_data = []
        neg_num = 0
        total_num = 0
        neg_value = []
        total_value = []

        for d in user_data["compressed_data"]:
            past = datetime.strptime(d["time"], "%Y-%m-%d %H:%M:%S.%f")
            now = datetime.now()
            if (now-past).total_seconds() < 7200:
                compressed_data.append(d)
                neg_value.append(d["neg"])
                total_value.append(d["total"])
                neg_num += d["negLen"]
                total_num += d["totalDataLen"]

        mongo.db.users.update({"account_id": account_id}, {"$set": {"compressed_data": compressed_data}})
        neg_value = Database.mean(neg_value)
        total_value = Database.mean(total_value)
        returnObj = {"neg_num": neg_num, "total_num": total_num, "neg_value": neg_value, "total_value": total_value}
        #print(returnObj)
        return returnObj















