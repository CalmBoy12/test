from flask import Blueprint, jsonify, Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)
blueprint = Blueprint('fund_management', __name__)

mongo = PyMongo(app, retryWrites=False)