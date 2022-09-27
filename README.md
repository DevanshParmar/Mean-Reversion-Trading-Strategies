# Mean-Reversion-Trading-Strategies

Mean Reversion Trading is the theory which suggests that prices, returns, or various economic indicators tend to move to the historical average or mean over time. This theory has led to many trading strategies which involve the purchase or sale of a financial instrument whose recent performance has greatly differed from their historical average without any apparent reason.

In this project, we used financial concepts of Hurst Values, stockVWAP, basics of mean reversion theory to identify and suggest an algo-trading strategy on top-10 performing stocks.

## 1. Problem Statement
Identify mean-reverting stocks by calculating their Hurst values, calculate the mean value and deviations using StockVWAP and price spread. Building a mean-reversion strategy which involves buying when the predicted value falls below mean value - deviation and selling when predicted value rises above mean value + deviation.

## 2.  Requisites and Dataset
### 2.1.  Capital Asset Pricing Model (CAPM)
The Capital Asset Pricing Model (CAPM) describes the relationship between systematic risk and expected return for assets, particularly stocks. CAPM is widely used throughout finance for pricing risky securities and generating expected returns for assets given the risk of those assets and cost of capital. The formula for calculating the expected return of an asset given its risk is as follows:

##### <p align="center"> ER<sub>i</sub> = R<sub>f</sub> + β<sub>i</sub>(ER<sub>m</sub> - R<sub>f</sub>) </p>

Here,
ER<sub>i</sub> = Expected return of investment <br/>
R<sub>f</sub> = Risk-free rate <br/>
β<sub>i</sub> = Beta of the investment <br/>
ER<sub>m</sub> = Expected return of market <br/>
ER<sub>m</sub> - R<sub>f</sub> = Market risk premium

The risk-free rate in the CAPM formula accounts for the time value of money. The other components of the CAPM formula account for the investor taking on additional risk. The ultimate goal of the CAPM formula is to evaluate whether a stock is fairly valued when its risk and the time value of money are compared to its expected return.

### 2.2. Concepts of Algorithmic Trading
Algorithmic trading uses a computer program that follows a defined set of instructions (an algorithm) to place a trade. The algorithms are based on timing, price, quantity, or any mathematical model. Apart from profit opportunities for the trader, algo-trading renders markets more liquid and trading more systematic by ruling out the impact of human emotions and manual errors on trading activities. Also, Algo-Trading can be backtested using available historical and real-time data to check for its viability. Some frequent algo-trading strategies are:
1. Trend Trading
2. Arbitrage Opportunities
3. Mean Reversion Trading
4. Index Fund Rebalancing
5. Volume-Weighted Average Price (VWAP)
6. Time-Weighted Average Price

### 2.3. Dataset
We used minute-wise data containing StockVWAP (Stock Volume-Weighted Average Price), bid price and ask price of 110 stocks spanning energy, IT, financials, healthcare, telecommunications and other sectors of the Indian market for the entire year of 2017. Stock traded for 375 minutes each day from 9:15-3:30 and for 240 days throughout the year. So, we have 90,000 data points to work on.

## 3. Mean Reversion Trading Strategies (MRTS)
### 3.1. Hurst Exponent Calculation for checking stationarity of a time series
#### 3.1.1. Time Series
In simple language, time series is a sequence of observations in a certain period of time. Recording changes in various things such as temperature in a specific city, or as we make use of it, stock prices in regular intervals over a large period of time is a time series. We use a time series as initial data for our analysis and to experiment on to predict whether our models and strategies are profitable or not. A time series of stock prices tell us a lot about how the stock has performed in different time intervals in the past and how it may perform in the future. Through the years, extensive analysis of time series by using sophisticated statistical tools have told traders a lot about a stock’s traits and behaviours. Through time, the trend of the graph has given rise to the concept of stationarity

#### 3.1.2. Stationarity
A time series is defined to be stationary if its joint probability distribution is mostly invariant under translations in time or space. In particular, and of key importance for traders, the mean and variance of the process do not change over time or space and they each do not follow a trend.

![Examples-for-stationary-and-non-stationary-time-series](https://github.com/DevanshParmar/Mean-Reversion-Trading-Strategies/blob/main/images/Examples-for-stationary-and-non-stationary-time-series.png)

If a time series is stationary in nature, we observe that the probability distribution is invariant and hence a lot of factors somewhat constant remain in control and such a series is easier to work upon for statistical purposes. Hence, calculating the stationarity of the series is important. To calculate the stationarity of a time series, we have made use of the concept of Hurst Exponent.


#### 3.1.3. Hurst Exponent
Hurst Exponent aims to classify a time series into one of the following: mean reverting, random walking or trending. The idea behind it is to look at the variance of log prices to assess the rate of diffusive behavior. For a time lag 𝛕, the variance is given by:

<p align="center"> Var(𝛕) = 〈(log(t+𝛕) - log(t))<sup>2</sup>〉</p>

In case of random walking, or general brownian motion, we can conclude that the equation stated above directly depends on the time lag 𝛕:

<p align="center"> Var(𝛕) = 〈(log(t+𝛕) - log(t))<sup>2</sup>〉~ 𝛕</p>

Here, if autocorrelations exist (any sequential price movements possess non-zero correlation) this relation stated above does not stand. So to overcome this, we modify the 𝛕 variable to 𝛕<sup>2H</sup>. This exponent factor of ‘2H’ is twice of the Hurst Exponent, i.e. H.

<p align="center"> Var(𝛕) = 〈(log(t+𝛕) - log(t))<sup>2</sup>〉~ 𝛕<sup>2H</sup></p>

According to the Hurst Exponent we obtain, we conclude as following:
* H < 0.5 - Time series is mean reverting
* H = 0.5 - Time series is random walking or in General Brownian Motion
* H > 0.5 - Time series is trending

![Hurst Exponent and Mean Reversion](https://github.com/DevanshParmar/Mean-Reversion-Trading-Strategies/blob/main/images/Variable%20Hurst%20Exponent.png)

### 3.2. Theory of MRTS
Mean-reversion strategies work on the assumption that there is an underlying stable trend in the price of an asset and prices fluctuate randomly around this trend. Therefore, values deviating far from the trend will tend to reverse direction and revert back to the trend. That is, if the value is unusually high, we expect it to go back down and if it is unusually low, go back up.

### 3.3. Time period of MRTS strategy
We have taken 1 day, 5 day and 2 weeks as time periods for mean reversion trading strategy.

### 3.4. Calculation of profits from the mean reverting stocks:
We started with 110 stocks and calculated their Hurst Exponent. 93 stocks had a Hurst Exponent below 0.5; they were mean-reverting. Just to select only the "safely" mean-reverting profiles, we chose the stocks which had a Hurst Score below 0.45, then we made a list of these stocks and proceeded to our profit analysis step. Next, we refine our data points according to the time frames mentioned to improve computation time. After we have the final dataframes to operate upon, we begin computing our moving average data in a newly formed array. To calculate the moving average, we resorted to using three times the data points than we are calculating for to maintain a stable trend to compare data upon. Given below is the time intervals and the data points taken into consideration for the moving average.

* 1 Day - at a 5 minute interval - 75 data points - 225 taken for moving average
* 5 Day - at a 10 minute interval - 187.5 data points - 563 taken for moving average
* 14 Day - at a 1 hour interval - 87.5 data points - 263 taken for moving average

The first 75, 188 and 88 data points of ‘stock volume weighted average price’ (stockVWAP) go into the array as they are, for 1 day, 5 day and 14 day data respectively. The following data points are a moving average of the 75, 188 and the 88 data points preceding this position. Now, we calculate the deviation of each data point’s stockVWAP from the moving average taking the spread of ask and bid price, and brokerage into consideration. We take note of all instances when the deviation is positive and count these instances as the number of trades and the deviations for total profit and mean deviation. Further, we compile this data into a final data frame and also obtain a CSV file of the same. 

Now when it comes to selecting the top performing 10 stocks across timeframes, there is no fixed approach needed. One of the approaches we used was loading the 3 profits CSVs in a dataframes and adding the columns of total profit (Average profit per trade * number of trades) and timeframe (1d, 5d or 2w). We finally selected the stocks whose total profit, avg profit and number of trades were in the top 70% in all three categories, and in all 3 time periods. We then combined the three datasets into a single dataframe. Now, in the new dataframe, we arranged the datapoints in decreasing order of total profit, and selected the top 10 stocks in any of the time periods.

## 4. Conclusion
We have successfully identifed the top 10 best-performing stocks as per our MRT strategy.

## 5. Files and Functions - Legend
* stock_data - contains the stock data of the year 2017 for 110 stocks, each in 90,000 data points
* stocklist.txt - name-list of the 110 stocks in consideration
* HurstStockSelection.py - contains functions to compute and publish hurst scores for stocks
  * hurst() - calculates hurst score for a stock
  * make_HurstScoresCSV() - publishes ___HurstScores.csv___, i.e. a CSV file containing the hurst scores of all stocks 
  * make_HurstSelectedStocksCSV() - publishes ___HurstSelectedStocks.csv___, i.e. a CSV file containing the hurst scores of selected stocks
* MakeProfitsCSV.py - contains functions to publish a CSV file of profits for various time periods
  * make_Profits1D_csv() - publishes ___Profits1D.csv___
  * make_Profits5D_csv() - publishes ___Profits5D.csv___
  * make_Profits14D_csv() - publishes ___Profits14D.csv___
* HighPerformingStocks.py - contains functions to select and publish the stocks which are high performing
  * HighPerformingStocks() - selects top stocks according to the given parameters
  * make_TopStocksCSV() - publishes ___TopNStocks.csv___, where N can be any number, and here N=10
* MRTS.ipynb - displays all the processes of the project
