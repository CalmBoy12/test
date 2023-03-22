from flask import Blueprint, jsonify, Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)
blueprint = Blueprint('watchlist', __name__)

mongo = PyMongo(app, retryWrites=False)


@blueprint.route('/stock/<id>')
def watchlistStock(id):
    watchlistStock = mongo.db.watchlistStock
    watchlistStock_data = watchlistStock.find({"userId": id})
    data = []
    for x in watchlistStock_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/suggestions/<id>')
def watchlistSuggestions(id):
    watchlistSuggestions = mongo.db.watchlistSuggestions
    watchlistSuggestions_data = watchlistSuggestions.find({"userId": id})
    data = []
    for x in watchlistSuggestions_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/stock', methods=['POST'])
def watchlistStockPost():
    watchlistStock = mongo.db.watchlistStock
    data = request.json
    print('abc', data)
    watchlistStock.insert_one({'name': data['name'],
                              'price': data['price'],
                               'change': data['change'],
                               'volatility': data['volatility'],
                               'ret': data['ret'],
                               'divyield': data['divyield'],
                               'ticker': data['ticker'],
                               'pe': data['pe'],
                               'field': data['field'],
                               'userId': data['userId']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})


@blueprint.route('/suggestions', methods=['POST'])
def watchlistSuggestionsPost():
    watchlistSuggestions = mongo.db.watchlistSuggestions
    data = request.json
    print('abc', data)
    watchlistSuggestions.insert_one({'name': data['name'],
                                     'price': data['price'],
                                     'change': data['change'],
                                     'volatility': data['volatility'],
                                     'ret': data['ret'],
                                     'divyield': data['divyield'],
                                     'ticker': data['ticker'],
                                     'pe': data['pe'],
                                     'field': data['field'],
                                     'userId': data['userId']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})
