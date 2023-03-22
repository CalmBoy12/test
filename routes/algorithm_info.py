from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://nft:nft123@mathtrade.yvcna.mongodb.net/nft-flask?retryWrites=true&w=majority'


mongo = PyMongo(app, retryWrites=False, connect=True)

blueprint = Blueprint('algo-info', __name__)


@blueprint.route('/<id>')
def algoInfo(id):
    algoInfo = mongo.db.algoInfo
    algoInfo_data = algoInfo.find({"userId": id})
    data = []
    for x in algoInfo_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/to-trade/<id>')
def algoInfoToTrade(id):
    algoInfoTrade = mongo.db.algoInfoTrade
    algoInfoTrade_data = algoInfoTrade.find({"userId": id})
    data = []
    for x in algoInfoTrade_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route("/top/<id>")
def algoInfoTop(id):
    algoInfoTop = mongo.db.algoInfoTop
    algoInfoTop_data = algoInfoTop.find({"userId": id})
    data = []
    for x in algoInfoTop_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, "data": data})


@blueprint.route('/related-constituent-stock/<id>')
def algoRelatedConstituentStock(id):
    algoRelatedConstituentStock = mongo.db.algoRelatedConstituentStock_new
    algoRelatedConstituentStock_data = algoRelatedConstituentStock.find({'trading_card_id': id})
    data = []
    for x in algoRelatedConstituentStock_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})

@blueprint.route('/information-top/<id>')
def informationTop(id):
    informationTop = mongo.db.information_top
    informationTop_data = informationTop.find({'trading_card_id': id})
    data = []
    for x in informationTop_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/to-trade', methods=['POST'])
def algoInfoToTradePost():
    algoInfoTrade = mongo.db.algoInfoTrade
    data = request.json
    print('abc', data)
    algoInfoTrade.insert_one({'name': data['name'],
                              'date': data['date'],
                              'time': data['time'],
                              'price': data['price'],
                              'userId': data['userId']
                              })
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})


@blueprint.route('/', methods=['POST'])
def algoInfoPost():
    algoInfo = mongo.db.algoInfo
    data = request.json
    print('abc', data)
    algoInfo.insert_one({'ticker': data['ticker'],
                         'name': data['name'],
                         'price': data['price'],
                         'change': data['change'],
                         'userId': data['userId']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})

    # userId


@blueprint.route("/top", methods=["POST"])
def algoInfoTopPost():
    algoInfoTop = mongo.db.algoInfoTop
    data = request.json
    print("abc", data)
    algoInfoTop.insert_one({"name": data["name"],
                            "Datetime": data["Datetime"],
                            "avgReturn": data["avgReturn"],
                            "volatility": data["volatility"],
                            "winRate": data["winRate"],
                            "annualRatio": data["annualRatio"],
                            "sharpRatio": data["sharpRatio"],
                            'userId': data['userId']})
    return jsonify({"success": True, 'message': "data inserted", "data": data})


@blueprint.route('/related-constituent-stock', methods=['POST'])
def algoRelatedConstituentStockPost():
    algoRelatedConstituentStock = mongo.db.algoRelatedConstituentStock
    data = request.json
    print('abc', data)
    algoRelatedConstituentStock.insert_one({'ticker': data['ticker'],
                                            'name': data['name'],
                                            'price': data['price'],
                                            'change': data['change'],
                                            'userId': data['userId']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})

# ****************** Overview **********


@blueprint.route('/overview/<id>')
def algoInfoOverview(id):
    algoInfoOverview = mongo.db.algoInfoOverview_new
    # algoInfoOverview_data = algoInfoOverview.find({"userId": id})
    algoInfoOverview_data = algoInfoOverview.find({'trading_card_id': id})
    # algoInfoOverview_data = algoInfoOverview.find({})
    data = []
    for x in algoInfoOverview_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})
    # f = './Json_data/Overview.json'
    # with open(f) as overview:
    #     Overview_data = json.load(overview)
    # for i in Overview_data['overview']:
    #     overview = i
    # return jsonify({'success': True, 'data': [overview]})


@blueprint.route('/overview', methods=['POST'])
def algoInfoOverviewPost():
    algoInfoOverview = mongo.db.algoInfoOverview
    data = request.json
    print('abc', data)
    algoInfoOverview.insert_one({'total_return_percentage': data['total_return_percentage'],
                                 'net_profit': data['net_profit'],
                                 'net_liquidation': data['net_liquidation'],
                                 'sharpe_ratio': data['sharpe_ratio'],
                                 'compounding_re': data['compounding_re'],
                                 'margin_ratio': data['margin_ratio'],
                                 'sortino_ratio': data['sortino_ratio'],
                                 'max_drawdown': data['max_drawdown'],
                                 'alpha': data['alpha'],
                                 'volatility': data['volatility'],
                                 'win_rate': data['win_rate'],
                                 'average_win': data['average_win'],
                                 'profit_loss_ratio': data['profit_loss_ratio']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})


# ****************** HISTORICAL-RETURNS **********


@blueprint.route('/historical-returns/<id>')
def HistoricalReturns(id):
    HistoricalReturns = mongo.db.HistoricalReturns_new
    HistoricalReturns_data = HistoricalReturns.find({'trading_card_id': id})
    data = []
    for x in HistoricalReturns_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/historical-returns', methods=['POST'])
def HistoricalReturnsPost():
    HistoricalReturns = mongo.db.HistoricalReturns
    data = request.json
    print('abc', data)
    HistoricalReturns.insert_one({'period': data['period'],
                                  'return': data['return'],
                                  'adj_return': data['adj_return'],
                                  'standard_deviation': data['standard_deviation'],
                                  'max_drawdown': data['max_drawdown'],
                                  'pos_neg_months': data['pos_neg_months']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})

# ****************** portfolio-dividend-yield **********


@blueprint.route('/portfolio-dividend-yield')
def PortfolioDividendYield():
    PortfolioDividendYield = mongo.db.PortfolioDividendYield
    PortfolioDividendYield_data = PortfolioDividendYield.find()
    data = []
    for x in PortfolioDividendYield_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/portfolio-dividend-yield', methods=['POST'])
def PortfolioDividendYieldPost():
    PortfolioDividendYield = mongo.db.PortfolioDividendYield
    data = request.json
    print('abc', data)
    PortfolioDividendYield.insert_one({'weight': data['weight'],
                                       'ETF_name': data['ETF_name'],
                                       'div_yield_current_year': data['div_yield_current_year'],
                                       'div_yield_last_year': data['div_yield_last_year']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})

# ****************** portfolio-efficiency **********


@blueprint.route('/portfolio-efficiency/<id>')
def PortfolioEfficiency(id):
    PortfolioEfficiency = mongo.db.PortfolioEfficiency_new
    PortfolioEfficiency_data = PortfolioEfficiency.find({'trading_card_id': id})
    data = []
    for x in PortfolioEfficiency_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


@blueprint.route('/portfolio-efficiency', methods=['POST'])
def PortfolioEfficiencyPost():
    PortfolioEfficiency = mongo.db.PortfolioEfficiency
    data = request.json
    print('abc', data)
    PortfolioEfficiency.insert_one({'parameter': data['parameter'],
                                    'value': data['value'],
                                    'compare_same_risk': data['compare_same_risk'],
                                    'comapre_all_portfolios': data['comapre_all_portfolios']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})

# ****************** TradeLog **********


@blueprint.route('/trade-log/<id>')
def TradeLog(id):
    TradeLog = mongo.db.TradeLog_new
    TradeLog_data = TradeLog.find({'trading_card_id': id})
    data = []
    for x in TradeLog_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})\

@blueprint.route('/trade-log', methods=['POST'])
def TradeLogPost():
    TradeLog = mongo.db.TradeLog
    data = request.json
    # print('abc', data)
    TradeLog.insert_one({'ETF_name': data['ETF_name'],
                         'date_time': data['date_time'],
                         'price': data['price'],
                         'quantity': data['quantity'],
                         'proceeds': data['proceeds']})
    return jsonify({'success': True, 'message': 'data inserted', 'data': data})


@blueprint.route('/get-capital-growth')
def capitalGrowthGet():
    try:
        capitalGrowthNLV = mongo.db.capitalGrowthNLV
        capitalGrowthAdjustedNLV = mongo.db.capitalGrowthAdjustedNLV

        nlv_data = capitalGrowthNLV.find({})
        adjusted_nlv_data = capitalGrowthAdjustedNLV.find({})

        nlv = []
        adjusted_nlv = []

        for i in nlv_data:
            i['_id'] = str(i['_id'])
            nlv.append(i)

        for i in adjusted_nlv_data:
            i['_id'] = str(i['_id'])
            adjusted_nlv.append(i)

        data = [
            {
                'name': 'Capital Growth',
                'data': nlv
            },
            {
                'name': 'US Inflation Adjusted',
                'data': adjusted_nlv
            }
        ]

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/add-capital-growth', methods=['POST'])
def capitalGrowthPost():
    try:
        capitalGrowthNLV = mongo.db.capitalGrowthNLV
        capitalGrowthAdjustedNLV = mongo.db.capitalGrowthAdjustedNLV
        data = request.json
        capitalGrowthNLV.insert_one({'x': datetime.utcfromtimestamp(data['timestamp']),
                                    'y': data['nlv'],
                                     'timestamp': data['timestamp'],
                                     'created_at': datetime.utcnow()})
        capitalGrowthAdjustedNLV.insert_one({'x': datetime.utcfromtimestamp(data['timestamp']),
                                            'y': data['adjusted_nlv'],
                                             'timestamp': data['timestamp'],
                                             'created_at': datetime.utcnow()})

        # nlv = []
        # adjusted_nlv = []

        # for i in capitalGrowth:
        #     nlv.append({
        #         'x': datetime.utcfromtimestamp(i[0]),
        #         'y': i[1],
        #         'timestamp': i[0],
        #         'created_at': datetime.utcnow()
        #     })
        #     adjusted_nlv.append({
        #         'x': datetime.utcfromtimestamp(i[0]),
        #         'y': i[2],
        #         'timestamp': i[0],
        #         'created_at': datetime.utcnow()
        #     })

        # capitalGrowthNLV.insert_many(nlv)
        # capitalGrowthAdjustedNLV.insert_many(adjusted_nlv)
        return jsonify({'success': True, 'message': 'data inserted'})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/get-drawdown/<id>')
def drawdownGet(id):
    try:
        drawdown = mongo.db.drawdown_graph_data

        result = drawdown.find({'trading_card_id': id})

        data = []

        for i in result:
            data.append([i['timestamp'], i['y']])

        return jsonify({'length': len(data),'success': True, 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/add-drawdown', methods=['POST'])
def drawdownPost():
    try:
        drawdown = mongo.db.drawdown_graph_data
        data = request.json
        drawdown.insert_one({'x': datetime.utcfromtimestamp(data['timestamp']),
                            'y': data['drawdown'],
                             'timestamp': data['timestamp'],
                             'created_at': datetime.utcnow()})

        # data = []

        # for i in drawDown:
        #     data.append({
        #         'x': datetime.utcfromtimestamp(i[0]),
        #         'y': i[1],
        #         'timestamp': i[0],
        #         'created_at': datetime.utcnow()
        #     })

        # drawdown.insert_many(data)
        return jsonify({'success': True, 'message': 'data inserted'})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/get-drawdown-table/<id>')
def drawdownTableGet(id):
    try:
        drawdownTable = mongo.db.drawdown_data

        result = drawdownTable.find({'trading_card_id': id})

        data = []

        for i in result:
            i['_id'] = str(i['_id'])
            data.append(i)

        return jsonify({'length': len(data), 'success': True, 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/add-drawdown-table', methods=['POST'])
def drawdownTablePost():
    try:
        drawdownTable = mongo.db.drawdownTable
        data = request.json
        drawdownTable.insert_one({'drawdown': data['drawdown'],
                                  'drawdown_start': data['drawdown_start'],
                                  'drawdown_bottom': data['drawdown_bottom'],
                                  'drawdown_months': data['drawdown_months'],
                                  'recovery_end': data['recovery_end'],
                                  'recovery_months': data['recovery_months'],
                                  'total_months': data['total_months'],
                                  'created_at': datetime.utcnow()})

        # data = []

        # for i in drawDownTable:
        #     i['created_at'] = datetime.utcnow()
        #     data.append(i)

        # drawdownTable.insert_many(data)
        return jsonify({'success': True, 'message': 'data inserted'})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/get-rolling-returns-graph/<id>')
def rollingReturnsGraph(id):
    try:
        rollingReturns_graph = mongo.db.rollingReturns_graph

        result = rollingReturns_graph.find({'trading_card_id': id})

        data = []

        for i in result:
            i['_id'] = str(i['_id'])
            data.append(i)

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})

@blueprint.route('/get-rolling-returns/<id>')
def rollingReturnsGet(id):
    try:
        rollingReturns = mongo.db.rollingReturns_new

        result = rollingReturns.find({'trading_card_id': id})

        data = []

        for i in result:
            i['_id'] = str(i['_id'])
            data.append(i)

        return jsonify({'success': True, 'data': data})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/add-rolling-returns', methods=['POST'])
def rollingReturnsPost():
    try:
        rollingReturns = mongo.db.rollingReturns
        data = request.json
        rollingReturns.insert_one({'period': data['period'],
                                   'average_return': data['average_return'],
                                   'best_return': data['best_return'],
                                   'worst_return': data['worst_return'],
                                   'negative_periods': data['negative_periods'],
                                   'created_at': datetime.utcnow()})

        # data = []

        # for i in rollingReturnData:
        #     i['created_at'] = datetime.utcnow()
        #     data.append(i)

        # rollingReturns.insert_many(data)
        return jsonify({'success': True, 'message': 'data inserted'})
    except Exception as e:
        print('e', e)
        return jsonify({'success': False})


@blueprint.route('/high-yield-bonds-income-portfolio-returns')
def highyeildBondsIncomePortfolioReturns():
    highyeildBondsIncomePortfolioReturns = mongo.db.highyeildBondsIncomePortfolioReturns
    # print('highyeildBondsIncomePortfolioReturns',highyeildBondsIncomePortfolioReturns)
    highyeildBondsIncomePortfolioReturns_data = highyeildBondsIncomePortfolioReturns.find({
    })
    data = []
    for x in highyeildBondsIncomePortfolioReturns_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True,  'data': data})


# @blueprint.route('/highyeild-bonds-income-portfolio-returns', methods=['POST'])
# def highyeildBondsIncomePortfolioReturns():
#     highyeildBondsIncomePortfolioReturns = mongo.db.highyeildBondsIncomePortfolioReturns
#     data = request.json
#     print('abc', data)
#     highyeildBondsIncomePortfolioReturns.insert_one({'ticker': data['ticker'],
#                                  'name': data['name'],
#                                  'price': data['price'],
#                                  'change': data['change'],
#                                  'userId': data['userId']})
#     return jsonify({'success': True, 'message': 'data inserted', 'data': data})

@blueprint.route('/historical-graph/<id>')
def historicalGraph(id):
    historicalGraph = mongo.db.historicalGraphNew
    # print('historicalGraph',historicalGraph)
    historicalGraph_data = historicalGraph.find({'trading_card_id': id})
    data = []
    for x in historicalGraph_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'success': True, 'data': data})


# @blueprint.route('/historical-graph', methods=['POST'])
# def historicalGraphPost():
#     historicalGraph = mongo.db.historicalGraph
#     data = request.json
#     print('abc', data)
#     historicalGraph.insert_one({'key': data['key'],
#                                 'data': data['data']})
#     return jsonify({'success': True, 'message': 'data inserted', 'data': data})
