customerId = '5a5794666514d52c7774a388'
checkingId = '5a5796f16514d52c7774a38a'
creditId = '5a5796596514d52c7774a389'

apiKey = '896c897b5f52485fd3e9b049b4af1cc5'

current_month = '2017-12'

balence_history = {
    '2017-01' : 726.24,
    '2017-02' : 814.07,
    '2017-03' : 874.66,
    '2017-04' : 890.66,
    '2017-05' : 1176.17,
    '2017-06' : 1000.68,
    '2017-07' : 714.33,
    '2017-08' : 468.01,
    '2017-09' : 464.34,
    '2017-10' : 590.35,
    '2017-11' : 611.16,
    '2017-12' : 923.63
}

payment_history = {
    '2017-01' : 300.35,
    '2017-02' : 800.00,
    '2017-03' : 750.11,
    '2017-04' :  50.00,
    '2017-05' : 800.00,
    '2017-06' : 800.00,
    '2017-07' : 714.33,
    '2017-08' : 468.00,
    '2017-09' : 200.34,
    '2017-10' : 400.35,
    '2017-11' : 211.16
}

purchase_history = {
    '2017-12-04': {
        'vendor': 'STARBUCKS',
        'price': '21.12'
    },
    '2017-12-04': {
        'vendor': 'GREENBURG MULTIPLEX',
        'price': '13.23'
    },
    '2017-12-06': {
        'vendor': 'UBER',
        'price': '54.40'
    },
    '2017-12-12': {
        'vendor': 'AMAZON.COM',
        'price': '120.64'
    },
    '2017-12-14': {
        'vendor': 'NETFLIX',
        'price': '9.99'
    },
    '2017-12-16': {
        'vendor': 'KAPNOS TAVERNA',
        'price': '98.39'
    },
}

'''
sum = 0.0
for (date1, balance), (date2, payment) in zip(balence_history.items(), payment_history.items()):
    sum += ((balance - payment)/balance)

print(sum/12)
'''