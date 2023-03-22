from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)
blueprint = Blueprint('algo-principle', __name__)

mongo = PyMongo(app, retryWrites=False)


@blueprint.route("/top/<id>")
def algoPrincipleTop(id):
    algoPrincipleTop = mongo.db.algoPrincipleTop
    algoPrincipleTop_data = algoPrincipleTop.find({"userId": id})
    data = []
    for x in algoPrincipleTop_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, "data": data})


@blueprint.route("/top", methods=["POST"])
def algoPrincipleTopPost():
    algoPrincipleTop = mongo.db.algoPrincipleTop
    data = request.json
    print("abc", data)
    algoPrincipleTop.insert_one({"name": data["name"],
                                 "Datetime": data["Datetime"],
                                 "avgReturn": data["avgReturn"],
                                 "volatility": data["volatility"],
                                 "winRate": data["winRate"],
                                 "annualReturn": data["annualReturn"],
                                 "sharpRatio": data["sharpRatio"],
                                 'userId': data['userId']})
    return jsonify({"success": True, 'message': "data inserted", "data": data})
