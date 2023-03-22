from cgi import print_exception
from bson import ObjectId
from flask_cors import CORS
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from routes import portfolio, algorithm_mart,  algorithm_info, composite, main_page_test, user_acc_test, strategy_info_test, users
from datetime import datetime

import random


app = Flask(__name__)
new_app = Flask(__name__)

CORS(app, allow_headers=['Content-Type', 'Authorization',
     'Access-Control-Allow-Credentials'], supports_credentials=True)

# app.register_blueprint(users.blueprint, url_prefix='/users')
app.register_blueprint(composite.blueprint, url_prefix='/composite')
app.register_blueprint(algorithm_info.blueprint, url_prefix='/algo-info')
app.register_blueprint(portfolio.blueprint, url_prefix='/portfolio')
app.register_blueprint(main_page_test.blueprint, url_prefix='/main_page')
app.register_blueprint(user_acc_test.blueprint, url_prefix='/user_acc_test')
app.register_blueprint(strategy_info_test.blueprint,
                       url_prefix='/strategy_info_test')
app.register_blueprint(users.blueprint, url_prefix='/users')
app.register_blueprint(algorithm_mart.blueprint, url_prefix='/algo-mart')
# app.register_blueprint(fund_management.blueprint,
#                        url_prefix='/fund_management')
# app.register_blueprint(home.blueprint, url_prefix='/home')
# app.register_blueprint(stock_info.blueprint, url_prefix='/stock_info')
# app.register_blueprint(algorithm_principle.blueprint,
#                        url_prefix='/algo-principle')
# app.register_blueprint(trade_log.blueprint, url_prefix='/trade_log')
# app.register_blueprint(watchlist.blueprint, url_prefix='/watchlist')

app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'
new_app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/rainydrop?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)
new_mongo = PyMongo(new_app, retryWrites=False, connect=True)

tradingCards = mongo.db.tradingCards
trading_data = list(tradingCards.find({}))

Strategies = new_mongo.db.Strategies
Strategies_data = list(Strategies.find({}).limit(len(trading_data)))

arr = []
print('start')

@app.route('/')
def index():
    # users = mongo.db.users.insert_one({'name': 'ali'})
    return jsonify({'message': 'Wellcome To RESTFUL APIs.....'})


if __name__ == '__main__':
    app.run(debug=True)
