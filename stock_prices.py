#!/usr/bin/env python3

prices = [1,2,3,4,9,1]
buy = []
sell = []

#print(prices)

def stock_tracker():
    i=0
    while i < len(prices):
        #determine if we are buying or selling
        if len(buy) == len(sell):
            #required for last list item
            if i+1 == len(prices):
                i += 1
            #buy
            elif prices[i] < prices[i+1]:
                buy.append(prices[i])
            else:
                i += 1
        else:
            #required for last list item
            if i+1 == len(prices):
                sell.append(prices[i])
                i += 1
            #sell
            elif prices[i] > prices[i+1]:
                sell.append(prices[i])
            else:
                i += 1
    #empty list return 0 else return profit
    if not prices:
        print(0)
    else:
        print(sum(sell)-sum(buy))


stock_tracker()


#print(sell, buy)



