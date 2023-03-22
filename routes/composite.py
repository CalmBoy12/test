from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo
import json
# from Json_data import '


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'


mongo = PyMongo(app, retryWrites=False, connect=True)

blueprint = Blueprint('composite', __name__)


# ****************** AssetAllocationAndETFs **********

@blueprint.route('/asset-allocation-etfs')
def AssetAllocationAndETFs():
    AssetAllocationAndETFs = mongo.db.AssetAllocationAndETFs
    AssetAllocationAndETFs_data = AssetAllocationAndETFs.find({})
    data = []
    for x in AssetAllocationAndETFs_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/asset-allocation-etfs', methods=['POST'])
def AssetAllocationAndETFsPost():
    AssetAllocationAndETFs = mongo.db.AssetAllocationAndETFs
    data = request.json
    # print('abc', data)
    AssetAllocationAndETFs.insert_one({'ETF_percentage': data['ETF_percentage'],
                                       'ETF_label': data['ETF_label']})

    return jsonify({'success': True, 'message': 'data inserted', 'data': data})
