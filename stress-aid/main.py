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
    request_info = request.get_json(force=True)
    account_id = request_info["user_id"]
    Database.insert_new_user(account_id)
    # result = []
    # cursor = mongo.db.users.find({}, {"_id": 0})
    # for c in cursor:
    #     result.append(c)
    return "ok"

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
    semantria_score = -0.2
    print(semantria_score)


    #store in database
    db_doc = Database.update_temp_list(semantria_score, user_account)
    #
    return jsonify(db_doc)

@app.route("/amidepressed", methods=['POST'])
def amidepressed():
    """
    check if user is depressed or not, basically at this point just returns a JSON
    """
    requestJson = request.get_json(force=True)
    user_account = requestJson["account_id"]
    depression = Database.am_i_depressed(user_account)
    print(depression)
    return jsonify(depression)





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')