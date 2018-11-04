import requests
import os

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions
import json

from flask import Flask, request, Response
app = Flask(__name__)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    iam_apikey='NwvDOYXpN8uvuypEKCvobulZyUQT57uWbYp4JQoHUWOH',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)

from flask_cors import CORS, cross_origin
CORS(app)


from create_dict import create_desc_dict, create_name_dict

company_dict = create_name_dict()
desc_dict = create_desc_dict()

from flask import jsonify

@app.route("/get_sentiment", methods=['POST'])
@cross_origin()
def get_average_sentiment():
    print(request.get_json(force=True))
    company = request.get_json()['company']
    print(company_dict[company])
    url = ('https://newsapi.org/v2/everything?'
        'q="' + company_dict[company] + '"&'
        'from=2018-10-10&'
        'sortBy=relevancy&'
        'apiKey=accb9b5d018348ff86fd7f9565673758&'
        'language=en'
        '&pageSize=5')
    response = requests.get(url)

    response = response.json()
    #print(response)
    if 'articles' in response:
        articles = response['articles']
    else:
        articles = []
    avg = 0

    for article in articles:
        try:
            response = natural_language_understanding.analyze(
                url=article['url'],
                features=Features(sentiment=SentimentOptions())).get_result()

            avg += response['sentiment']['document']['score']
        except:
            print("Error")

    return jsonify({ "sentiment": avg / 5 })

@app.route("/get_stock_portfolio", methods=["POST"])
@cross_origin()
def get_stock_portfolio():
    jsoned = request.get_json()
    age = jsoned['age']
    checked = jsoned['checked']
    from risk import riskIndex, scope
    from pull_data import get_portfolio
    from get_risk import get_risk
    import math
    portfolio = get_portfolio(riskIndex(age, checked), riskIndex(age, checked)+0.3, scope(checked), 5)
    risks = get_risk(portfolio)
    print(portfolio)

    new_dict = {}
    for stock in portfolio:
        new_dict[stock] = desc_dict[stock]

    return jsonify({
        "portfolio": portfolio,
        "riskIndex": math.floor(riskIndex(age, checked) * 100),
        "descriptions": new_dict,
        "risks": risks
    })