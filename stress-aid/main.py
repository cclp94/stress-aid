from flask import Flask, jsonify, request
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
    semantria_score = [-0.7, 'negative']

    #store in database
    db_doc = Database.update_temp_list(semantria_score[0], user_account)
    #
    return jsonify(db_doc)







if __name__ == "__main__":
    app.run(debug=True)