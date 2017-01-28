from flask import Flask, jsonify, request
#from flask.ext.pymongo import PyMongo
from flask_pymongo import PyMongo
from mongo_connection import Database

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def hello():
    result = []
    cursor = mongo.db.users.find({}, {"_id": 0})
    for c in cursor:
    	result.append(c)
    return jsonify(result)

@app.route("/insertnewuser")
def mongotest():
    Database.insert_new_user(456)
    result = []
    cursor = mongo.db.users.find({}, {"_id": 0})
    for c in cursor:
    	result.append(c)
    return jsonify(result)

@app.route("/updatetemp", methods = ['POST'])
def updatetemp():
    """
    get the request's post data, run 
    """
    user_account = request.form["account_id"]
    message = request.form["message"]
    #do things with semantria API and put into db
    #
    semantria_score = [-0.8, 'negative']

    #store in database
    Database.update_temp_list(semantria_score[0], semantria_score[1], user_account)
    #
    return user_account







if __name__ == "__main__":
    app.run(debug=True)