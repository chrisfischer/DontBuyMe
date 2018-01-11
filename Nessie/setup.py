from bson.json_util import dumps
from pymongo import MongoClient

client = MongoClient("mongodb://admin:password1@ds251287.mlab.com:51287/heroku_x5rvthjk")
db = client.get_default_database()


#ayments = db['payment-history']
#cursor = payments.find({}, { "_id": False})

#print (dumps(cursor))



'''

balance_history = [
    { 'date': '2017-02', 'balance': 814.07 },
    { 'date': '2017-03', 'balance': 874.66 },
    { 'date': '2017-04', 'balance': 890.66 },
    { 'date': '2017-05', 'balance': 1176.17 },
    { 'date': '2017-06', 'balance': 1000.68 },
    { 'date': '2017-07', 'balance': 714.33 },
    { 'date': '2017-08', 'balance': 468.01 },
    { 'date': '2017-09', 'balance': 464.34 },
    { 'date': '2017-10', 'balance': 590.35 },
    { 'date': '2017-11', 'balance': 611.16 },
    { 'date': '2017-12', 'balance': 923.63 }
]

balance = db['balance-history']
for h in balance_history:
  balance.insert(h)

payment_history = [
    { 'date': '2017-01', 'payment': 300.35},
    { 'date': '2017-02', 'payment': 800.00},
    { 'date': '2017-03', 'payment': 750.11},
    { 'date': '2017-04', 'payment':  50.00},
    { 'date': '2017-05', 'payment': 800.00},
    { 'date': '2017-06', 'payment': 800.00},
    { 'date': '2017-07', 'payment': 714.33},
    { 'date': '2017-08', 'payment': 468.00},
    { 'date': '2017-09', 'payment': 200.34},
    { 'date': '2017-10', 'payment': 400.35},
    { 'date': '2017-11', 'payment': 211.16}
]


payments = db['payment-history']

for h in payment_history:
  payments.insert(h)

cursor = payments.find()
for post in cursor:
    print(post)
'''

purchase_history = [
    {
      'date': '2017-12-04',
      'vendor': 'STARBUCKS',
      'price': '21.12'
    },
    {
      'date': '2017-12-04',
      'vendor': 'GREENBURG MULTIPLEX',
      'price': '13.23'
    },
    {
      'date': '2017-12-06',
      'vendor': 'UBER',
      'price': '54.40'
    },
    {
      'date': '2017-12-12',
      'vendor': 'AMAZON.COM',
      'price': '120.64'
    },
    {
      'date': '2017-12-14',
      'vendor': 'NETFLIX',
      'price': '9.99'
    },
    {
      'date': '2017-12-16',
      'vendor': 'KAPNOS TAVERNA',
      'price': '98.39'
    },
]

purchases = db['purchase-history']
purchases.insert(purchase_history)