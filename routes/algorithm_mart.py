from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)
blueprint = Blueprint('algo-mart', __name__)


mongo = PyMongo(app, retryWrites=False)


@blueprint.route('/<id>')
def algoMart(id):
    algoMart = mongo.db.algoMart
    algoMart_data = algoMart.find({"userId": id})
    data = []
    for x in algoMart_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/', methods=['POST'])
def algoMartPost():
    algoMart = mongo.db.algoMart
    data = request.json
    print('abc', data)
    algoMart.insert_one({'img': data['img'],
                         'title': data['title'],
                         'author': data['author'],
                         'subscribe': data['subscribe'],
                         'return': data['return'],
                         'desc': data['desc'],
                         'userId': data['userId']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})


@blueprint.route('/algo-mart-graph/<key>')
def historicalGraph(key):
    historicalGraph = mongo.db.historicalGraphNew
    # print('historicalGraph',historicalGraph)
    historicalGraph_data = historicalGraph.find({'key': key})
    data = []
    for x in historicalGraph_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})