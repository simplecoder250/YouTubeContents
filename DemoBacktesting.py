import pandas as pd
import time
from utils import PositionSizing as ps
from utils import Move as mv
watchlist = ['HDFC']
import time


# Initialization of values
totalFund = 100000
traded_count = 0
entry_price = 0
exit_price = 0
trade_target = 0
trade_sl = 0
traded = False
trade_long = False
trade_short = False
trade_qty = 1
trade_pnlBooked = False
trade_exit_time = None
trade_entry_time = None
trade_slhit = False
pnl = 0
total_pnl = 0


# Taking the past values of stocks
read_stock = pd.read_csv('/Users/vivekpatel/PycharmProjects/30MinsBreakout/5 minute/HDFC.csv')
high = 0
low = 11110000
trade_open_high = 0
trade_open_low = 0
percentageMove = 0

# Iterating the values of stock
for index,row in read_stock.iterrows():

    if row['date'][11:16] == "09:15":
        high = 0
        low = 11110000
        trade_open_high = 0
        trade_open_low = 11100000
        entry_price = 0
        exit_price = 0
        trade_target = 0
        trade_sl = 0
        traded = False
        trade_long = False
        trade_short = False
        trade_qty = 1
        trade_pnlBooked = False
        trade_exit_time = None
        trade_entry_time = None
        trade_slhit = False
        pnl = 0

    if row['date'][11:16] >= "09:15" and row['date'][11:16] <= "10:15":
        # Saving the high and low within the 1 hour to calculate the range
        if trade_open_high < row['high']:
            trade_open_high = row['high']
        if trade_open_low > row['low']:
            trade_open_low = row['low']

    if row['date'][11:16] >= "09:30" and row['date'][11:16] <= "15:15":

        if traded is True and trade_pnlBooked is False:  # We have entered the market

            if row['date'][11:16] is not "15:15":  # current time is not 3 pm 15 minutes
                if trade_long is True:

                    if row['close'] >= trade_target:   # Target reached
                        trade_exit_time = row['date']
                        exit_price = row['close']
                        pnl = (exit_price - entry_price) * trade_qty
                        trade_pnlBooked = True
                        total_pnl = total_pnl + pnl
                        print('pnl is-->', pnl)
                        print('Total pnl is-->', total_pnl)

                    if row['close'] < trade_sl:        # Stop loss hit
                        trade_exit_time = row['date']
                        exit_price = row['close']
                        pnl = (exit_price - entry_price) * trade_qty
                        trade_pnlBooked = True
                        total_pnl = total_pnl + pnl
                        print('pnl is-->', pnl)
                        print('Total pnl is-->', total_pnl)

                if trade_short is True:

                    if row['close'] <= trade_target:     # Target reached
                        trade_exit_time = row['date']
                        exit_price = row['close']
                        pnl = (entry_price - exit_price) * trade_qty
                        trade_pnlBooked = True
                        total_pnl = total_pnl + pnl
                        print('pnl is-->', pnl)
                        print('Total pnl is-->', total_pnl)

                    if row['close'] > trade_sl:
                        trade_exit_time = row['date']
                        exit_price = row['close']
                        pnl = (entry_price - exit_price) * trade_qty
                        trade_pnlBooked = True
                        total_pnl = total_pnl + pnl

                        print('pnl is-->', pnl)
                        print('Total pnl is-->', total_pnl)

            if row['date'][11:16] is "15:15":
                print('Exit while market close')
                trade_exit_time = row['date']
                exit_price = row['close']
                trade_pnlBooked = True
                if trade_long is True:
                    pnl = (exit_price - entry_price) * trade_qty
                    total_pnl = total_pnl + pnl
                    print('Total pnl is-->', total_pnl)

                if trade_short is True:
                    pnl = (entry_price - exit_price) * trade_qty
                    total_pnl = total_pnl + pnl
                    print('Total pnl is-->', total_pnl)

        if traded is False:   # We havent entered the market
            if row['close'] >= trade_open_high:  # Breakout occured upward
                trade_long = True
                traded = True

                entry_price = trade_open_high + 1
                trade_qty = ps.total_quantity(250000, int(trade_open_high - trade_open_low), row['close'], 1)
                traded_count = traded_count + 1
                range = int(trade_open_high - trade_open_low)
                trade_entry_time = row['date']
                trade_target = trade_open_high + int(trade_open_high/100)
                trade_sl = trade_open_high - int(row['close'] / 500)

            elif row['close'] < trade_open_low:  # Breakout occured downward
                trade_short = True
                traded = True
                entry_price = trade_open_low - 1
                range = int(trade_open_high - trade_open_low)
                trade_qty = ps.total_quantity(250000, int(trade_open_high - trade_open_low), row['close'], 1)
                traded_count = traded_count + 1
                trade_entry_time = row['date']
                trade_target = trade_open_low - int(trade_open_high/100)
                trade_sl = trade_open_low + int(row['close'] / 500)

    if row['date'][11:16] >= "09:15" and row['date'][11:16] <= "15:25":
        if high < row['high']:
            high = row['high']
        if low > row['low']:
            low = row['low']


print('Total Number of Trades',traded_count)












