from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/?retryWrites=true&w=majority'

mongo1 = PyMongo(app, uri='mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/simulation?retryWrites=true&w=majority'
                 ,retryWrites=False, connect=True)

mongo2 = PyMongo(app, uri='mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/rainydrop?retryWrites=true&w=majority'
                 ,retryWrites=False, connect=True)

blueprint = Blueprint('mainpage', __name__)

# mongo = PyMongo(app, retryWrites=False)

@blueprint.route('/<strategy_name>')
def main_page(strategy_name):
    timestamp_end = request.args.get('timestamp_end')
    timestamp_start = request.args.get('timestamp_start')
    tags = request.args.get('tags')
    all = {}
    # for graph
    for x in strategy_name:
        col = mongo1.db.x
        cursor = col.find({"timestamp": {"$lte": timestamp_end, "$gte": timestamp_start}},
                          {"_id": 0, "NetLiquidation": 1, "timestamp": 1}).sort("_id", 1)
        list_ = list(cursor)
        all[x] = list_

    #for top gainer and bottom loser
    col = mongo2.db.Strategies
    cursor1 = col.find({}, {"_id": 0, "strategy_name": 1, "YTD Sharpe": 1, "5 Yr Sharpe": 1,
                            "YTD Return": 1, "5 Yr Return": 1, "Margin Ratio": 1,
                            "last nlv": 1}).limit(2).sort("YTD Return", -1)
    cursor2 = col.find({}, {"_id": 0, "strategy_name": 1, "YTD Sharpe": 1, "5 Yr Sharpe": 1,
                            "YTD Return": 1, "5 Yr Return": 1, "Margin Ratio": 1,
                            "last nlv": 1}).limit(2).sort("YTD Return", 1)
    list_cur1 = list(cursor1)
    list_cur2 = list(cursor2)
    # final = {}
    all["top"] = list_cur1
    all["bottom"] = list_cur2

    # for Trading cards
    col = mongo2.db.Strategies
    # tag = (user click in the frontend)
    if tags == "popular":
        cursor = col.find({"tags": {"$in": ["popular"]}}, {"_id": 0, "strategy_name": 1, "strategy_initial": 1,
                                                           "last daily change": 1, "last monthly change": 1})
    elif tags == "geo_focus":
        cursor = col.find({"tags": {"$in": ["geo_focus"]}}, {"_id": 0, "strategy_name": 1, "strategy_initial": 1,
                                                             "last daily change": 1, "last monthly change": 1})
    elif tags == "votility_rider":
        cursor = col.find({"tags": {"$in": ["votility_rider"]}}, {"_id": 0, "strategy_name": 1, "strategy_initial": 1,
                                                                  "last daily change": 1, "last monthly change": 1})
    elif tags == "long_term_value":
        cursor = col.find({"tags": {"$in": ["long_term_value"]}}, {"_id": 0, "strategy_name": 1, "strategy_initial": 1,
                                                                   "last daily change": 1, "last monthly change": 1})
    elif tags == "drawdown_protection":
        cursor = col.find({"tags": {"$in": ["drawdown_protection"]}},
                          {"_id": 0, "strategy_name": 1, "strategy_initial": 1,
                           "last daily change": 1, "last monthly change": 1})
    else:
        cursor = col.find({}, {"_id": 0, "strategy_name": 1, "strategy_initial": 1, "last daily change": 1,
                               "last monthly change": 1})

    all['portfolio'] = list(cursor)

    return jsonify(all)

