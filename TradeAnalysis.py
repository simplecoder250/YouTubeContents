import pandas as pd

TCSData = pd.read_csv('TCS.csv')
print(TCSData.head(5))
print(TCSData.columns)
maximumLossDays = 0
count = 0
MaxLossIndex = 0
date = 0


# Maximum consecutive value of loss days.
for i in range(len(TCSData)) :
    if TCSData.iloc[i,6] < 0 :
        count = count + 1;
    if TCSData.iloc[i,6] > 0:
        if count > maximumLossDays :
            maximumProfitDays = count
            print(count)
            MaxLossIndex = i
            print(TCSData.loc[i,"entry_time"])
        count = 0

print("Maximum loss days->",maximumLossDays)


# Maximum consecutive value of profitable days.

maximumProfitDays = 0
MaxProfitIndex = 0
for i in range(len(TCSData)) :
    if TCSData.iloc[i,6] > 0 :
        count = count + 1;
    if TCSData.iloc[i,6] < 0:
        if count > maximumProfitDays :
            maximumProfitDays = count
            print(count)
            MaxProfitIndex = i
            print(TCSData.loc[i,"entry_time"])
            print('\n')
        count = 0

print("Maximum profit days->",maximumProfitDays)


# Calculate the max loss and profit return in a day in ( % )

maxProfitPerecentage = 0
maxLossPercentage = 0
for i in range(len(TCSData)):
    if  TCSData.loc[i,"percentageReturn"] > 0 :
        if maxProfitPerecentage < TCSData.loc[i,"percentageReturn"] :
            maxProfitPerecentage = TCSData.loc[i,"percentageReturn"]

    if TCSData.loc[i, "percentageReturn"] < 0:
        if maxLossPercentage > TCSData.loc[i, "percentageReturn"]:
            maxLossPerecentage = TCSData.loc[i, "percentageReturn"]

print("Maximum profit percentage :",maxProfitPerecentage)
print("Minimum loss percentage :",maxLossPerecentage)