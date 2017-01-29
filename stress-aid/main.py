from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo
#from SemantriaApp import analyse
from mongo_connection import Database
from crossDomainAuth import crossdomain

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
@crossdomain(origin='*')
def updatetemp():
    """
    get the request's post data, run 
    """
    requestJson = request.get_json(force=True)
    user_account = requestJson["account_id"]
    message = requestJson["message"]
    print(requestJson)
    #do things with semantria API and put into db
    #analyseScore = str(analyse(message))
    semantria_score = [-0.7, 'negative']
    print(semantria_score)


    #store in database
    db_doc = Database.update_temp_list(semantria_score[0], user_account)
    #
    return jsonify(db_doc)







if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')