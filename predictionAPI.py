import csv
import random
import math
import operator
import sys
import argparse
import json


# Capital One Hackathon 1/11/2018


# hard coded cost prediction based on last 3 months of stock growth information
def findCostMarketInvestment(cost, timeReference, determinantFundData, balance, interest, payment):
    data = []
    days = int(timeReference)

    beforeInterest = getInterest(balance, interest, payment)
    afterInterest = getInterest(balance+cost, interest, payment)
    netInterest = afterInterest-beforeInterest
    with open(determinantFundData, 'r',encoding="utf8") as listing_file:

        csv_reader = csv.reader(listing_file)
        # creating list 
        for line in csv_reader:
            stockPrice = line[1]
            date = line[0]
            data.append([stockPrice,date])

        dataRecent = data[1:days]
        # print(dataRecent)
        

        percentGrowth  = (float(dataRecent[0][0]) - float(dataRecent[len(dataRecent) -1][0])) / float(dataRecent[len(dataRecent) -1][0])
        print("percent growth: " + str(percentGrowth))

        print("Cost of the item based on 70 day percent growth of " + determinantFundData +" index fund")
        # print((float(cost) * percentGrowth) + cost )
    

    return {
    "realCost": round((float(cost) * percentGrowth) + cost + netInterest,2),
    "interest": round(netInterest,2),
    "investmentReturn": round((float(cost) * percentGrowth),2)}
    

# Determining cost of good based off of interest rate of credit card
def getInterest(balance, interest, payment):
    total = 0;
    while(balance>0):
        balance=balance-payment
        if (balance<=payment): 
            balance=0
        balance= balance + balance*(interest/100/12)
        total += balance*(interest/100/12)
       
    return round(total,2)

def getDate(date):
    # date: 2017-01-01
    #print(date)
    year = int(date[2:4])
    #print(year)
    month = int(date[5:7])
    #print(month)
    day = int(date[8:])
    #print(day)
   
    return [year, month, day]


def getDatefromStock(date):
    #print(date)
    month = date[:2]
    monthLength=2
    #print(month)
    if (month[1]=='/'):
        month=month[0]
        monthLength=1
    #print(month)
    month=int(month)
    
    day = date[monthLength+1:monthLength+3]
    dayLength=2
    #print(day)
    if (day[1]=='/'):
        day = day[0]
        dayLength=1
    #print(day)
    day = int(day)

    year = int(date[(monthLength+dayLength+2):])

    return [year, month, day]


def actualRealCost(itemCost, purchaseDate, currentDate, stockData, balance, interest, payment):
    purchaseDate = getDate(purchaseDate)
    #print(purchaseDate)
    curDate = getDate(currentDate) #SUBJECT TO CHANGE
    #print(curDate)

    beforeStockPrice=0
    afterStockPrice=0
    counter=0;
    with open(stockData, 'r', encoding="utf8") as listing_file:
        csv_reader = csv.reader(listing_file)
        for line in csv_reader:
            if (line[0]=='date'): continue
            stockDate = getDatefromStock(line[0])
            #print(stockDate)
            if (stockDate[0]>=purchaseDate[0] and stockDate[1]>=purchaseDate[1] and stockDate[2]>=purchaseDate[2]):
                beforeStockPrice = float(line[1])
                if (afterStockPrice==0):
                    for line in csv_reader:
                        afterStockPrice=float(line[1])
                        break
            if (stockDate[0]>=curDate[0] and stockDate[1]>=curDate[1] and stockDate[2]>=curDate[2]):
                afterStockPrice = float(line[1])

    rate = (afterStockPrice-beforeStockPrice)/beforeStockPrice

    beforeInterest = getInterest(balance, interest, payment)
    afterInterest = getInterest(balance+itemCost, interest, payment)

    netInterest= afterInterest-beforeInterest

    return {    
    "realCost": round(rate*itemCost+itemCost+netInterest ,2), 
    "interest":round(netInterest,2),
    "investmentReturn":round(rate*itemCost,2)}
# handler for findCostMarketInvestment
def findCostMarketInvestment_handler(event, context):
    # TODO implement
    print(json.dumps(event))
    body = json.loads(event['body'])
    response = { "statusCode": 200, 
    "isBase64Encoded": False,
    "headers": {},
    "body": json.dumps({ "opportunityCost": findCostMarketInvestment(float(body['cost']),float(body['timeReference']),body['determinantFundData'],
        float(body['balance']), float(body['interest']), float(body['payment']) ) }) }
    return response
   # handler for actualRealCost
def actualRealCost_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    response = { "statusCode": 200, 
    "isBase64Encoded": False,
    "headers": {},
    "body": json.dumps({ "opportunityCost": actualRealCost(float(body['itemCost']),body['purchaseDate'],body['currentDate'], body['stockData'], float(body['balance']), float(body['interest']), float(body['payment']))}) }
    return response   
