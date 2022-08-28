import numpy as np
import pandas as pd

def make_Profits1D_csv(HurstThreshold=0.5):
    SelectedStocks = []
    df = pd.read_csv('HurstScores.csv', names=('StockName', 'HS'))
    stocks = df['StockName']
    scores = df['HS']
    for j in range(len(stocks)):
        if(scores[j] < HurstThreshold):
            SelectedStocks.append(stocks[j])
    print("Number of stocks in consideration: " + str(len(SelectedStocks)))
    print("--------------------------------------")
    df_out = pd.DataFrame()
    for StockName in SelectedStocks:
        df_all = pd.read_csv("stock_data/"+ StockName +".csv", names=('Dates', 'stockVWAP', 'futureVWAP', 'bidPrice', 'askPrice', 'total_value', 'total_size'))
        df_train = df_all[:60000]
        df_5min_train = df_train[df_train.index%5 == 0]
        df_5min_train.reset_index(drop=True, inplace=True) 
        df = df_5min_train
        data = np.array([])
        for i in range(224):
            data = np.append(data, df.loc[i,"stockVWAP"])
        for i in range(224, 12000):
            # Rolling Average of past 3 days from Day 3 last value to Day 160 last value
            data = np.append(data, np.mean(df.loc[i-224:i+1,"stockVWAP"])) 
        df_mean = pd.DataFrame(data)
        df["stockVWAP1DMean"] = df_mean
        df["stockVWAP1DDeviation"] = 0
        for j in df.index:
            df["PriceSpread"] = df.loc[j,"askPrice"] - df.loc[j,"bidPrice"]
            df.loc[j,"stockVWAP1DDeviation"] = df.loc[j,"stockVWAP"]-df.loc[j,"stockVWAP1DMean"]-df.loc[j,"PriceSpread"]-0.20 
            # 0.20 is the brokerage amount
        df = df.drop(columns=["Dates","futureVWAP","bidPrice","askPrice","total_value","total_size"])
        NTrades = 0    
        profit = 0
        for j in df.index:
            if df.loc[j, "stockVWAP1DDeviation"] > 0:
                NTrades = NTrades + 1
                profit = profit + df.loc[j, "stockVWAP1DDeviation"]
        if NTrades > 0:
            dev_mean = profit/NTrades
        else:
            dev_mean = 0
        s = pd.Series([StockName, dev_mean, NTrades, profit, "1d" ], index= ['StockName', 'avg_profit', 'NTrades', 'total_profit', 'timeseries'])
        df_out = df_out.append(s, ignore_index = True)
        print(StockName.ljust(10) + " : " + f'{dev_mean:6.3f}' + " : " + f'{NTrades:5.0f}' + " : " + f'{profit:9.2f}')
    reposition_columns = ['StockName', 'avg_profit', 'NTrades', 'total_profit', 'timeseries']
    df_out = df_out.reindex(columns = reposition_columns)
    df_out.to_csv("Profits1D.csv")

def make_Profits5D_csv(HurstThreshold=0.5):
    SelectedStocks = []
    df = pd.read_csv('HurstScores.csv', names=('StockName', 'HS'))
    stocks = df['StockName']
    scores = df['HS']
    for j in range(len(stocks)):
        if(scores[j] < HurstThreshold):
            SelectedStocks.append(stocks[j])
    print("Number of stocks in consideration: " + str(len(SelectedStocks)))
    print("--------------------------------------")
    df_out = pd.DataFrame()
    for StockName in SelectedStocks:
        df_all = pd.read_csv("stock_data/"+StockName+".csv", names=('Dates', 'stockVWAP', 'futureVWAP', 'bidPrice', 'askPrice', 'total_value', 'total_size'))
        df_train=df_all[:60000]
        df_10min_train = df_train[df_train.index%10==0]
        df_10min_train.reset_index(drop=True, inplace=True)  
        df = df_10min_train
        data = np.array([])
        for i in range(562):
            data = np.append(data, df.loc[i,"stockVWAP"])
        for i in range(562, 6000):
            # Rolling Average of past 15 days from Day 15 last value to Day 160 last value
            data = np.append(data, np.mean(df.loc[i-562:i+1,"stockVWAP"]))
        df_mean = pd.DataFrame(data)
        df["stockVWAP5DMean"] = df_mean
        df["stockVWAP5DDeviation"] = 0 
        for j in df.index:
            df["PriceSpread"] = df.loc[j,"askPrice"] - df.loc[j,"bidPrice"]
            df.loc[j,"stockVWAP5DDeviation"] = df.loc[j,"stockVWAP"]-df.loc[j,"stockVWAP5DMean"]-df.loc[j,"PriceSpread"]-0.20 
            # 0.20 is the brokerage amount
        df = df.drop(columns=["Dates","futureVWAP","bidPrice","askPrice","total_value","total_size"])
        NTrades = 0
        profit = 0
        for j in df.index:
            if df.loc[j, "stockVWAP5DDeviation"] > 0:
                NTrades = NTrades + 1
                profit = profit + df.loc[j, "stockVWAP5DDeviation"]
        if NTrades > 0:
            dev_mean = profit/NTrades
        else:
            dev_mean = 0
        s = pd.Series([StockName, dev_mean, NTrades, profit, "5d" ], index= ['StockName', 'avg_profit', 'NTrades', 'total_profit', 'timeseries'])
        df_out = df_out.append(s, ignore_index = True)
        print(StockName.ljust(10) + " : " + f'{dev_mean:6.3f}' + " : " + f'{NTrades:5.0f}' + " : " + f'{profit:9.2f}')
    reposition_columns = ['StockName', 'avg_profit', 'NTrades', 'total_profit', 'timeseries']
    df_out = df_out.reindex(columns = reposition_columns)
    df_out.to_csv("Profits5D.csv")
    
def make_Profits14D_csv(HurstThreshold=0.5):
    SelectedStocks = []
    df = pd.read_csv('HurstScores.csv', names=('StockName', 'HS'))
    stocks = df['StockName']
    scores = df['HS']
    for j in range(len(stocks)):
        if(scores[j] < HurstThreshold):
            SelectedStocks.append(stocks[j])
    print("Number of stocks in consideration: " + str(len(SelectedStocks)))
    print("--------------------------------------")
    df_out = pd.DataFrame()
    for StockName in SelectedStocks:
        df_all = pd.read_csv("stock_data/"+StockName+".csv", names=('Dates', 'stockVWAP', 'futureVWAP', 'bidPrice', 'askPrice', 'total_value', 'total_size'))
        df_train=df_all[:60000]
        df_60min_train = df_train[df_train.index%60==0]
        df_60min_train.reset_index(drop=True, inplace=True)  
        df = df_60min_train
        data = np.array([])
        for i in range(262):
            data = np.append(data, df.loc[i,"stockVWAP"])
        for i in range(262, 6000):
            # Rolling Average of past 42 days from Day 42 last value to Day 160 last value
            data = np.append(data, np.mean(df.loc[i-562:i+1,"stockVWAP"]))
        df_mean = pd.DataFrame(data)
        df["stockVWAP14DMean"] = df_mean
        df["stockVWAP14DDeviation"] = 0
        for j in df.index:
            df["PriceSpread"] = df.loc[j,"askPrice"] - df.loc[j,"bidPrice"]
            df.loc[j,"stockVWAP14DDeviation"] = df.loc[j,"stockVWAP"]-df.loc[j,"stockVWAP14DMean"]-df.loc[j,"PriceSpread"]-0.20 
            # 0.20 is the brokerage amount
        df = df.drop(columns=["Dates","futureVWAP","bidPrice","askPrice","total_value","total_size"])
        NTrades = 0
        profit = 0
        for j in df.index:
            if df.loc[j, "stockVWAP14DDeviation"] > 0:
                NTrades = NTrades + 1
                profit = profit + df.loc[j, "stockVWAP14DDeviation"]
        if NTrades > 0:
            dev_mean = profit/NTrades
        else:
            dev_mean = 0
        s = pd.Series([StockName, dev_mean, NTrades, profit, "14d" ], index= ['StockName', 'avg_profit', 'NTrades', 'total_profit', 'timeseries'])
        df_out = df_out.append(s, ignore_index = True)
        print(StockName.ljust(10) + " : " + f'{dev_mean:7.3f}' + " : " + f'{NTrades:5.0f}' + " : " + f'{profit:9.2f}')
    reposition_columns = ['StockName', 'avg_profit', 'NTrades', 'total_profit', 'timeseries']
    df_out = df_out.reindex(columns = reposition_columns)
    df_out.to_csv("Profits14D.csv")