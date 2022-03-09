from nsepy import get_history
from datetime import date
import pandas as pd

# Objective of this video :
# To check the direction of movement of the stock next day which gave more than 3% of movement in a day
# if stock move more than 3%
    # check the direction of stock

nifty50Stocks = ['TATAMOTORS','HEROMOTOCO','UPL','BAJAJFINSERV','ADANIPORTS','DIVISLAB','IOC','INDUSINDBNK','BAJFINANCE',
                 'ICICIBANK','GRASIM','TATASTEEL','INFY','M&M','BPCL','ULTRACEMECO','WIPRO','SHREECEM','TCS','TATACONSUM',
                 'ONGC','AXISBANK','HDFC','SBIN','HCLTECH','COALINDIA','KOTAKBANK','HDFCBANK','ITC','HINDALCO','LT',
                 'HDFCLIFE','JSWSTEEL','ASIANPAINT','HINDUNILVR','RELIANCE','BHARTIARTL','CIPLA','POWERGRID','TITAN',
                 'EICHERMOT','MARUTI','SBILIFE','DRREDDY','NTPC','BAJAJ-AUTO','NESTLELIND','SUNPHARMA','BRITANNIA']

highestMove = 0
stockWithHighestMove = None
for name in nifty50Stocks :
    data = get_history(symbol=name, start=date(2015, 1, 1),
                       end=date(2022, 2, 1))
  #  print(data.columns)
    flag_up = False
    flag_down = False
    followed_movement = 0
    not_followed_movement = 0
    for ind in range(len(data)-1) :
        open_price = data['Open'][ind]
        low_price = data['Low'][ind]
        high_price = data['High'][ind]
        close_price = data['Close'][ind]

        percentageofMove = ((high_price - low_price) / high_price )*100

        if percentageofMove > 3 :
            open_price_nextday = data['Open'][ind + 1]
            close_price_nextday = data['Close'][ind + 1]
            if open_price > close_price :
                flag_up = True
                if open_price_nextday > close_price_nextday :
                    followed_movement = followed_movement + 1
                else :
                    not_followed_movement = not_followed_movement + 1


            if open_price < close_price :
                flag_down = True
                if open_price_nextday < close_price_nextday :
                    followed_movement = followed_movement + 1
                else :
                    not_followed_movement = not_followed_movement + 1
    print(followed_movement,'followed movement',name)
    print(not_followed_movement,'not followed movement',name)












