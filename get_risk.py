import requests
import heapq
from pymongo import MongoClient


def get_risk(portfolio):
    client = MongoClient(
        "mongodb+srv://jvering:berkeley2018@cluster0-1znwk.gcp.mongodb.net/test?retryWrites=true")
    db = client["stock-db"]
    collection = db["stocks"]
    result = collection.find()
    portfolio_risk = {}
    for obj in collection.find():
        ticker = obj["ticker"]
        if ticker in portfolio:
            portfolio_risk[ticker] = obj["latestPerf"]["oneYearRisk"]
    return portfolio_risk
