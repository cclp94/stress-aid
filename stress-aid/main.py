from flask import Flask, jsonify
import pprint
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def hello():
    result = []
    mongo.db.users.insert({"account_id": 43233})
    cursor = mongo.db.users.find({}, {"_id": 0})
    for c in cursor:
    	result.append(c)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)