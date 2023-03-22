from flask import Blueprint, jsonify, Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)
blueprint = Blueprint('stock_info', __name__)

mongo = PyMongo(app, retryWrites=False)


@blueprint.route('/overview/<id>')
def overviewStock(id):
    overviewStock = mongo.db.overviewStock
    overviewStock_data = overviewStock.find({"userId": id})
    data = []
    for x in overviewStock_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/principle-table/<id>')
def stockinfoPrincipleTable(id):
    stockinfoPrincipleTable = mongo.db.stockinfoPrincipleTable
    stockinfoPrincipleTable_data = stockinfoPrincipleTable.find({"userId": id})
    data = []
    for x in stockinfoPrincipleTable_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route("/related-constituent-stock/<id>")
def stockRelatedConstituent(id):
    stockRelatedConstituent = mongo.db.stockRelatedConstituent
    stockRelatedConstituent_data = stockRelatedConstituent.find({"userId": id})
    data = []
    for x in stockRelatedConstituent_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, "data": data})


@blueprint.route('/related-constituent-stock', methods=['POST'])
def stockRelatedConstituentPost():
    stockRelatedConstituent = mongo.db.stockRelatedConstituent
    data = request.json
    print('abc', data)
    stockRelatedConstituent.insert_one({'ticker': data['ticker'],
                                        'name': data['name'],
                                        'price': data['price'],
                                        'change': data['change'],
                                        'changeB': data['changeB'],
                                        'userId': data['userId']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})


@blueprint.route('/overview', methods=['POST'])
def overviewStockPost():
    overviewStock = mongo.db.overviewStock
    data = request.json
    print('abc', data)
    overviewStock.insert_one({'ticker': data['ticker'],
                              'name': data['name'],
                              'price': data['price'],
                              'exposure': data['exposure'],
                              'dailyChange': data['dailyChange'],
                              'marketValue': data['marketValue'],
                              'pL': data['pL'],
                              'userId': data['userId']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})


@blueprint.route('/principle-table', methods=['POST'])
def stockinfoPrincipleTablePost():
    stockinfoPrincipleTable = mongo.db.stockinfoPrincipleTable
    data = request.json
    print('abc', data)
    stockinfoPrincipleTable.insert_one({
        'ticker': data['ticker'],
        'name': data['name'],
        'market': data['market'],
        'price': data['price'],
        'time': data['time'],
        'volatility': data['volatility'],
        'monthReturn': data['monthReturn'],
        'high': data['high'],
        'low': data['low'],
        'prevClose': data['prevClose'],
        'volume': data['volume'],
        'turnOver': data['turnOver'],
        'wkHigh': data['wkHigh'],
        'wkLow': data['wkLow'],
        'divYield': data['divYield'],
        'userId': data['userId']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})
