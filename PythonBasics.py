

# Python Basics used in Algorithmic Trading


#Variables

# x = 5
# y = "ITC"
# z = "NSE : TATAMOTOR is a multibagger stock"
#
# print(x)
# print(y)
# print(z)


# var = 2.2
# print(var)
#
# var_cast = int(var)  # data_type(variable_name)
# print(var_cast)


# Python Strings

# strings = "ABCDE FG H I "
# strings2 = 'VALUABLE STOCK'
# print(strings2)
#
#
# last_element = strings2[-1]
# first_element = strings[0]
#
# print(last_element)
# print(first_element)


stocks = "NSE :TATAMOTORS"

# tata_motors = stocks[5:]
# print(tata_motors)


# in

# if "BATA" in stocks :
#     print("TATA")
# else :
#     print("NOT AVAILABLE")


# if "BATA" not in stocks :
#     print("NOT AVAILABLE")
# else:
#     print("AVAILABLE")


# stock_length = len(stocks)
# print(stock_length)


# Python Booleans
# rsi = 90
# rsi_indicator = rsi > 30 and rsi < 80
#
# print(rsi_indicator)



# Python Lists


myListOFStocks = ['NSE:ITC',34,2.2,"IGL"]

# print(myListOFStocks)


first = myListOFStocks[1]
# print(first)


myTradableStocks = ['ITC','RELIANCE','TATAMOTORS','IGL','HDFC','HDFCBANK']

stocks_filter = myTradableStocks[:4]
# print('stocks filter',stocks_filter)

# for stocks in myTradableStocks :
#     if stocks is "ITC":
#         print("ITC")
#     if stocks is "RELIANCE" :
#         print("RELAICNE")


# for i in range(len(myTradableStocks)) :
#
#    if "TATAMOTORS" in myTradableStocks[i] :
#        print("trade",myTradableStocks[i])
#
#
# myTradableStocks.sort()
# print(myTradableStocks)



# Dictionaries

#
# stock_name = {'STOCK1' : {'name':'TATAMOTORS','buy_price':490,'sell_price':500,'tradeType':'Long' },
#          'STOCK2' : {'name':'TATAMOTORS','buy_price':410,'sell_price':500,'tradeType':'Long' },
#          'STOCK3' : {'name':'TATAMOTORS','buy_price':390,'sell_price':500,'tradeType':'Long' }}
#
#
# for stock in stock_name :
#     print(stock_name[stock]['name'])



# Python if else conditions


# x = 10
#
# if x > 5 :
#     print('x is greater than 5')
# else :
#     print('x is less than 5')
#

x = 1
if x > 4 :
    print(4)
elif x > 5:
    print(5)
elif x > 10:
    print(10)

elif x  > 15:
    print(15)

else :
    print('nothing')
















