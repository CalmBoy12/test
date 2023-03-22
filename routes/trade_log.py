from flask import Blueprint, jsonify, Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)
blueprint = Blueprint('trade_log', __name__)

mongo = PyMongo(app, retryWrites=False)


@blueprint.route('/<id>')
def tradeLog(id):
    tradeLog = mongo.db.tradeLog
    tradeLog_data = tradeLog.find({"userId": id})
    data = []
    for x in tradeLog_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/', methods=['POST'])
def tradeLogPost():
    tradeLog = mongo.db.tradeLog
    data = request.json
    print('abc', data)
    tradeLog.insert_one({
        'time': data['time'],
        'data': data['data'],
        'action': data['action'],
        'security': data['security'],
        'transaction': data['transaction'],
        'amount': data['amount'],
        'status': data['status'],
        'userId': data['userId']
    })
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})
