'''
API - offers a way to pull data from the database:
    fields: fields from models.Listing to be queried

    plot: Lets you create aliases for variables. Need the same number of aliases as fields. Also filters null values.

    groupBy: currently only groups by location, will average the given field(s) by a 0.001 square degree regions and return either: (1) a tuple of the average value and coordinates if only one field was passed in, or (2) a tuple of coordinates and a dictionary of field name -> average value. Also filters null values.

    Other options:
        length(field): will create an alias length_field with the length of that character field

'''

import operator
from collections import OrderedDict

from .values import *

from bson.json_util import dumps
from pymongo import MongoClient, DESCENDING

def parse_get(o):
    key = o['key'][0]
    if key != apiKey:
        return null

    account = o['account'][0]
    if account != creditId:
        return null

    value = o['value'][0].split(' ')
    if len(value) != 1:
        return null
    field = value[0]

    client = MongoClient("mongodb://admin:password1@ds251287.mlab.com:51287/heroku_x5rvthjk")
    db = client.get_default_database()

    # return list of numerical fields
    if (field == 'currentBalance'):
        balances = db['balance-history']
        cursor = balances.find({}, {'balance': True, '_id': False}).sort([('date', DESCENDING)]).limit(1)
        return list(cursor)[0]['balance']

    if (field == 'balanceHistory'):
        balances = db['balance-history']
        cursor = balances.find({}, { "_id": False})
        toReturn = {}
        for d in cursor:
            toReturn[d['date']] = d['balance']
        l = sorted(toReturn.items(), key=operator.itemgetter(0))
        d = OrderedDict()
        for t in l:
            d[t[0]] = t[1]
        return d

    if (field == 'paymentHistory'):
        payments = db['payment-history']
        cursor = payments.find({}, { "_id": False})
        toReturn = {}
        for d in cursor:
            toReturn[d['date']] = d['payment']
        l = sorted(toReturn.items(), key=operator.itemgetter(0))
        d = OrderedDict()
        for t in l:
            d[t[0]] = t[1]
        return d

    if (field == 'purchaseHistory'):
        payments = db['purchase-history']
        cursor = payments.find()
        toReturn = []
        for d in cursor:
            toReturn.append({
                'date': d['date'],
                'vendor': d['vendor'], 
                'price': d['price'],
                'id': str(d['_id'])
            })
        toReturn.sort(key=lambda d: d['date'], reverse=True)
        return toReturn

    if (field == 'skippedHistory'):
        payments = db['skipped-history']
        cursor = payments.find()
        toReturn = []
        for d in cursor:
            toReturn.append({
                'date': d['date'],
                'vendor': d['vendor'], 
                'price': d['price'],
                'id': str(d['_id'])
            })
        toReturn.sort(key=lambda d: d['date'], reverse=True)
        return toReturn
        

def parse_post(o):
    key = o['key'][0]
    if key != apiKey:
        return null

    account = o['account'][0]
    if account != creditId:
        return null
    try:
        new_purchase = {
            'date': o['date'][0],
            'price': o['price'][0],
            'vendor': o['vendor'][0],
        }

        client = MongoClient("mongodb://admin:password1@ds251287.mlab.com:51287/heroku_x5rvthjk")
        db = client.get_default_database()
        payments = db['skipped-history']
        payments.insert(new_purchase)

        return 200
    except:
        return 400

