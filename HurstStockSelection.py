import numpy as np
import pandas as pd

# interpretation of return value
# hurst < 0.5 - input_ts is mean reverting
# hurst = 0.5 - input_ts is effectively random/geometric brownian motion
# hurst > 0.5 - input_ts is trending

def hurst(input_ts, lags_to_test = 150):
    tau = []
    lags = range(2, lags_to_test)
    #  Step through the different lags  
    for lag in lags:  
        #  produce price difference with lag  
        pp = np.subtract(input_ts[lag:].reset_index(drop=True), input_ts[:-lag].reset_index(drop=True)) 
        #  Calculate the variance of the difference vector  
        tau.append(np.sqrt(np.std(pp)))  
    #  linear fit to double-log graph (gives power)  
    m = np.polyfit(np.log10(lags), np.log10(tau), 1)  
    # calculate hurst  
    hurst = m[0]*2
    return hurst

def make_HurstScoresCSV():
    stocklist = pd.read_table('stocklist.txt', names = ['A'])
    f = open("HurstScores.csv", "w+")
    for stockname in stocklist['A']:
        df_all = pd.read_csv("stock_data/"+stockname+".csv", names=('Dates', 'stockVWAP', 'futureVWAP', 'bidPrice', 'askPrice', 'total_value', 'total_size'))
        df_train = df_all[:60000]
        df_train_resampled_10min = df_train[df_train.index%10 == 0]
        df_train_resampled_10min.reset_index(drop = True)   
        df = df_train_resampled_10min[:5999]
        hurst_score = hurst(df['stockVWAP'])
        print(stockname.ljust(10) + " : " + f'{hurst_score:6.4f}')
        f.write(stockname+","+str(hurst_score))
        f.write('\n')  
    f.close()
    
def make_HurstSelectedStocksCSV(HurstThreshold=0.5):
    # HurstThreshold at 0.5 gives all mean reverting stocks
    # HurstThreshold at 0.4 gives all 'safely' mean reverting stocks
    SelectedStocks = []
    SelectedScore = []
    df = pd.read_csv('HurstScores.csv', names=('StockName', 'HS'))
    stocks = df['StockName']
    scores = df['HS']
    j = 0
    while j < len(scores) :
        if(scores[j] < HurstThreshold) :
            SelectedStocks.append(stocks[j])
            SelectedScore.append(scores[j])
        j += 1
    df2 = pd.DataFrame(columns= ['StockName', 'HurstScore'])
    df2['StockName'] = SelectedStocks
    df2['HurstScore'] = SelectedScore
    print(df2)
    df2.head()
    df2.to_csv("HurstSelectedStocks.csv")