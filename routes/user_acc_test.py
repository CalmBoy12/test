from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo , MongoClient
from dotenv import load_dotenv
# import pandas as pd
import certifi

load_dotenv()
app = Flask(__name__)
blueprint = Blueprint('user_acc_test', __name__)

# app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/?retryWrites=true&w=majority'

mongo1 = PyMongo(app, uri='mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/simulation?retryWrites=true&w=majority'
                 ,retryWrites=False, connect=True)

mongo2 = PyMongo(app, uri='mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/rainydrop?retryWrites=true&w=majority'
                 ,retryWrites=False, connect=True)
mongo3 = MongoClient('mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/one_min_raw_data?retryWrites=true&w=majority',tlsCAFile=certifi.where())


@blueprint.route('/user')
def user_acc():
    strategy_name = request.args.get('strategy_name')
    timestamp_end = request.args.get('timestamp_end')
    timestamp_start = request.args.get('timestamp_start')
    client_name = request.args.get('client_name')
    ETF_ticker = request.args.get('ETF_ticker')
    all = {}

    # Overview
    # user choose strategy name
    for x in strategy_name:
        col = mongo1.db.x
        cursor = col.find({"timestamp": {"$lte": timestamp_end, "$gte": timestamp_start}},
                          {"_id": 0, "NetLiquidation": 1, "timestamp": 1}).sort("_id", 1)
        list_ = list(cursor)
        # print(list_)
        all[x] = list_

    col = mongo2.db.Strategies
    cursor = col.find({"strategy_name": strategy_name}, {"_id": 0, "Since Inception Return": 1, "1 Yr Sharpe": 1,
                                                         "5 Yr Sharpe": 1, "Since Inception Sharpe": 1,
                                                         "1 Yr Return": 1,
                                                         "5 Yr Return": 1, "YTD Return": 1,
                                                         "Since Inception Sortino": 1,
                                                         "Since Inception Max Drawdown": 1,
                                                         "Since Inception Volatility": 1, "Since Inception Win Rate": 1,
                                                         "Since Inception Average Win Per Day": 1,
                                                         "Since Inception Profit Loss Ratio": 1,
                                                         "last nlv": 1, "Margin Ratio": 1}).limit(1)
    all['info_row'] = list(cursor)

    # composite
    col = mongo2.db.Strategies
    cursor = col.find({"strategy_name": strategy_name}, {"_id": 0, "Composite": 1}).limit(1)
    df = pd.DataFrame()
    for x in cursor:
        percentage = list(x["Composite"].values())
        ETF = list(x["Composite"].keys())
    df["weight"] = percentage
    df["ETF_ticker, ETF_name"] = ETF

    all['strategie'] = list(cursor)
    all['composite'] = df.to_dict(orients='records')

    # Trade history
    col = mongo2.db.Clients
    cursor = col.find({"client_name": client_name}, {"_id": 0, "transactions": 1}).limit(1)
    transac_list = cursor[0]["transactions"]
    # print(transac_list)
    col = mongo2.db.Transactions
    cursor = col.find({"transaction_id": {"$in": transac_list}}, {"_id": 0, "date_time": 1, "ETF_ticker": 1,
                                                                  "action": 1, "price": 1, "quantity": 1,
                                                                  "total_amount": 1, "strategy_name": 1})
    all['transaction'] = list(cursor)

    # composite table
    col = mongo2.db.Strategies
    cursor = col.find({"strategy_name": strategy_name}, {"_id": 0, "Composite": 1, "strategy_name": 1}).limit(1)
    df = pd.DataFrame()
    for x in cursor:
        percentage = list(x["Composite"].values())
        ETF = list(x["Composite"].keys())
        strategy = x["strategy_name"]
    df["weight"] = percentage
    df["ETF_ticker, ETF_name"] = ETF
    df["strategy_name"] = strategy_name
    all['composite_table'] = df.to_dict(orients='records')


    col = mongo3[ETF_ticker]
    cursor1 = col.find({"ETF_ticker": ETF_ticker}, {"_id": 0, "ETF_ticker": 1, "ETF_name": 1, "price": 1,
                                                    "price_change": 1, "price_%change": 1, "volatility": 1,
                                                    "return": 1, "dividend_yield": 1, "price_earnings": 1,
                                                    "field": 1}).limit(1)

    col = mongo3[ETF_ticker]
    cursor2 = col.find({}, {"_id": 0, "timestamp": 1, "close": 1}).limit(10)  # limit 10 for testing
    list_cur1 = list(cursor1)
    list_cur2 = list(cursor2)
    all["details"] = list_cur1
    all["graph"] = list_cur2

    return jsonify(all)