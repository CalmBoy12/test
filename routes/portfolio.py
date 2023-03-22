from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo
from datetime import datetime
from data.data import newStrategyData
from data.data2 import capitalGrowth
from data.data3 import drawDown
from data.data4 import drawDownTable
from data.data5 import rollingReturnData

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'

mongo = PyMongo(app, retryWrites=False, connect=True)

blueprint = Blueprint('portfolio', __name__)


@blueprint.route('/overview-bottom-loser/<id>')
def overviewBottomLoser(id):
    try:
        overviewBottomLoser = mongo.db.overviewBottomLoser
        overviewBottomLoser_data = overviewBottomLoser.find({"userId": id})
        data = []
        for x in overviewBottomLoser_data:
            x['_id'] = str(x['_id'])
            data.append(x)
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/overview-top-gainer/<id>')
def overviewTopGainerGet(id):
    overviewTopGainer = mongo.db.overviewTopGainer
    overviewTopGainer_data = overviewTopGainer.find({"userId": id})
    data = []
    for x in overviewTopGainer_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/overview-bottom-loser', methods=['POST'])
def overviewBottomLoserPost():
    try:
        overviewBottomLoser = mongo.db.overviewBottomLoser
        data = request.json
        print('abc', data)
        overviewBottomLoser.insert_one({'ticker': data['ticker'],
                                        'name': data['name'],
                                        'price': data['price'],
                                        'change': data['change'],
                                        '%change': data['%change'],
                                        'relVol': data['relVol'],
                                        'algo': data['algo'],
                                        'userId': data['userId']})
        return jsonify({'success': True, 'message': 'data inserted', 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/overview-top-gainer', methods=['POST'])
def overviewTopGainerPost():
    try:
        overviewTopGainer = mongo.db.overviewTopGainer
        data = request.json
        print('abc', data)
        overviewTopGainer.insert_one({'ticker': data['ticker'],
                                      'name': data['name'],
                                      'price': data['price'],
                                      'change': data['change'],
                                      '%change': data['%change'],
                                      'relVol': data['relVol'],
                                      'algo': data['algo'],
                                      'userId': data['userId']})
        return jsonify({'success': True, 'message': 'data inserted', 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/all-trading-cards')
def tradingCardsGet():
    try:
        print('before')
        tradingCards = mongo.db.tradingCards
        print('after', tradingCards)
        allData = tradingCards.find({})
        print('allData', allData)

        data = []

        for x in allData:
            x['_id'] = str(x['_id'])
            data.append(x)

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/trading-cards', methods=['POST'])
def tradingCardsPost():
    try:
        tradingCards = mongo.db.tradingCards
        data = request.json
        tradingCards.insert_one({'strategyName': data['strategyName'],
                                'nlvDailyChange': data['nlvDailyChange'],
                                 'nlvMonthlyChange': data['nlvMonthlyChange'],
                                 'strategyInitial': data['strategyInitial']})

        return jsonify({'success': True, 'message': 'data inserted', 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/get-strategy-equity')
def strategyEquityGet():
    try:
        strategyEquityNLV1 = mongo.db.strategyEquityNLV1
        strategyEquityNLV2 = mongo.db.strategyEquityNLV2

        nlv1_data = strategyEquityNLV1.find({})
        nlv2_data = strategyEquityNLV2.find({})

        nlv1 = []
        nlv2 = []

        for i in nlv1_data:
            i['_id'] = str(i['_id'])
            nlv1.append(i)

        for i in nlv2_data:
            i['_id'] = str(i['_id'])
            nlv2.append(i)

        data = [
            {
                'name': '',
                'data': nlv1
            },
            {
                'name': '',
                'data': nlv2
            }
        ]

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/add-strategy-equity', methods=['POST'])
def strategyEquityPost():
    try:
        strategyEquityNLV1 = mongo.db.strategyEquityNLV1
        strategyEquityNLV2 = mongo.db.strategyEquityNLV2
        data = request.json

        nlv1 = []
        nlv2 = []

        for i in data['data']:
            print('i', i)
            nlv1.append({
                'x': datetime.utcfromtimestamp(i['timestamp']),
                'y': i['nlv1'],
                'timestamp': i['timestamp'],
                'created_at': datetime.utcnow()
            })
            nlv2.append({
                'x': datetime.utcfromtimestamp(i['timestamp']),
                'y': i['nlv2'],
                'timestamp': i['timestamp'],
                'created_at': datetime.utcnow()
            })

        # for i in newStrategyData:
        #     nlv1.append({
        #         'x': datetime.utcfromtimestamp(i[0]),
        #         'y': i[1],
        #         'timestamp': i[0],
        #         'created_at': datetime.utcnow()
        #     })
        #     nlv2.append({
        #         'x': datetime.utcfromtimestamp(i[0]),
        #         'y': i[2],
        #         'timestamp': i[0],
        #         'created_at': datetime.utcnow()
        #     })

        strategyEquityNLV1.insert_many(nlv1)
        strategyEquityNLV2.insert_many(nlv2)
        return jsonify({'success': True, 'message': 'data inserted'})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/high-yield-bonds-income-portfolio')
def highyeildBondsIncomePortfolio():
    highyeildBondsIncomePortfolio = mongo.db.HighYeildBondsIncomePortfolio
    highyeildBondsIncomePortfolio_data = highyeildBondsIncomePortfolio.find({})
    data = []
    for x in highyeildBondsIncomePortfolio_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})
