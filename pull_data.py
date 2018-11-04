"""This script pulls the stock data from MongoDB"""

import requests
import heapq
from pymongo import MongoClient


def get_portfolio(lower_bound, upper_bound, scope, size):
    client = MongoClient(
        "mongodb+srv://jvering:berkeley2018@cluster0-1znwk.gcp.mongodb.net/test?retryWrites=true")
    db = client["stock-db"]
    collection = db["stocks"]
    result = collection.find()
    portfolio = []
    prel_portfolio = {}
    for obj in collection.find():
        try:
            risk = obj["latestPerf"][scope+"YearRisk"]
            stock = obj["ticker"]
            if risk > lower_bound and risk < upper_bound:
                prel_portfolio[stock] = obj["latestPerf"][scope+"YearSharpeRatio"]
        except KeyError:
            try:
                risk = obj["latestPerf"]["oneYearRisk"]
                stock = obj["ticker"]
                if risk > lower_bound and risk < upper_bound:
                    prel_portfolio[stock] = obj["latestPerf"]["oneYearSharpeRatio"]
            except:
                pass
    portfolio = heapq.nlargest(size, prel_portfolio, key=prel_portfolio.get)
    print(portfolio)
    return portfolio
