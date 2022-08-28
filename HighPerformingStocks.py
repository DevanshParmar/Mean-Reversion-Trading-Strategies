import numpy as np
import pandas as pd

def HighPerformingStocks(csv_path, ap_qlimit=0.7, Nt_qlimit=0.7, tp_qlimit=0.7):
    # csv_path - path of the csv on which to operate
    # ap_qlimit - quantile limit for average profit
    # Nt_qlimit - quantile limit for total favourable number of trades
    # tp_qlimit - quantile limit for total profit
    # qlimit are generally kept at 0.6, i.e. stocks in top 40% in all categories
    
    df = pd.read_csv(csv_path)
    df_out = df[(df['avg_profit']>df['avg_profit'].quantile(ap_qlimit)) &
                (df['NTrades']>df['NTrades'].quantile(Nt_qlimit)) &
                (df['total_profit']>df['total_profit'].quantile(tp_qlimit))]
    df_out = df_out.reset_index().drop(["index","Unnamed: 0"], axis =1)
    return df_out

def make_TopStocksCSV(df, topN):
    df = df.sort_values(["total_profit"], ascending= False)
    df = df.reset_index(drop = True)
    df = df.drop_duplicates(subset=['StockName'], keep='first').reset_index(drop = True)
    df = df[:topN]
    topN = len(df)
    print(df)
    Name = "Top" + str(topN) + "Stocks.csv"
    df.to_csv(Name)
    