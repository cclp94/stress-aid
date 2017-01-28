#rom pymongo import MongoClient
import pprint

from flask import Flask
from flask.ext.pymongo import PyMongo

mongo = PyMongo('stress_aid')

