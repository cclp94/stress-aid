from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo
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
    get the request's post data and parse it
    """
    user_account = request.form["account_id"]
    message = request.form["message"]
    #do things with semantria API and put into db
    #
    #
    #
    return 200

    


if __name__ == "__main__":
    app.run(debug=True)