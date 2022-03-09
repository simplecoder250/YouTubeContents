from nsepy import get_history
import datetime
from datetime import date


#OBjective of this video
    # -> Determine the pivot point( up / down ) of the stock
    # Rule
        # previous close < close < next close
        # Count the candles flowing in the up direction for bottom pivot
        # Count the candles flowing the the down direction for up pivot




nifty50Stocks = ['TATAMOTORS','HEROMOTOCO','UPL','BAJAJFINSERV','ADANIPORTS','DIVISLAB','IOC','INDUSINDBNK','BAJFINANCE',
                 'ICICIBANK','GRASIM','TATASTEEL','INFY','M&M','BPCL','ULTRACEMECO','WIPRO','SHREECEM','TCS','TATACONSUM',
                 'ONGC','AXISBANK','HDFC','SBIN','HCLTECH','COALINDIA','KOTAKBANK','HDFCBANK','ITC','HINDALCO','LT',
                 'HDFCLIFE','JSWSTEEL','ASIANPAINT','HINDUNILVR','RELIANCE','BHARTIARTL','CIPLA','POWERGRID','TITAN',
                 'EICHERMOT','MARUTI','SBILIFE','DRREDDY','NTPC','BAJAJ-AUTO','NESTLELIND','SUNPHARMA','BRITANNIA']

for name in nifty50Stocks :
    data = get_history(symbol=name, start=date(2015,2 ,1),end=date(2022, 1, 1))
    for ind in range(len(data)-2):
        # pivot_left > pivot and pivot < pivot_right
        if ind > 2 :
            check_left_condition = data['Low'][ind - 2] > data['Low'][ind] and data['Low'][ind - 1] > data['Low'][ind]
            check_right_condition = data['Low'][ind + 2] > data['Low'][ind] and data['Low'][ind + 1] > data['Low'][ind]
            # print('if its a pivot or not-->',check_left_condition and check_right_condition)
            if check_left_condition and check_right_condition :
                print('name',name,'and pivot candle low price->',data['Low'][ind])














