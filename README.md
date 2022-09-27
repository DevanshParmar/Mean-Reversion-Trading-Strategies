# Mean-Reversion-Trading-Strategies

Mean Reversion Trading is the theory which suggests that prices, returns, or various economic indicators tend to move to the historical average or mean over time. This theory has led to many trading strategies which involve the purchase or sale of a financial instrument whose recent performance has greatly differed from their historical average without any apparent reason.

In this project, we used financial concepts of Hurst Values, stockVWAP, basics of meanreversion theory and machine learning concepts of ARIMA modelling (Auto Regressive Integrated Moving Average) to build an algo-trading strategy on top-25 performing stocks.

## 1. Problem Statement
Identify mean-reverting stocks by calculating their Hurst values, calculate the mean value and deviations using StockVWAP and price spread. Use ARIMA modelling to predict the future value of stock. Building a mean-reversion strategy which involves buying when the predicted value falls below mean value - deviation and selling when predicted value rises above mean value + deviation.

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
We used minute-wise data containing StockVWAP (Stock Volume-Weighted Average Price), bid price and ask price of 111 stocks spanning energy, IT, financials, healthcare, telecommunications and other sectors of the Indian market for the entire year of 2017. Stock traded for 375 minutes each day from 9:15-3:30 and for 160 days throughout the year. So, we have 60,000 data points to backtest our model and predict future stock price.

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

##### <p align="center"> Var(𝛕) = 〈|log(t+𝛕)-log(t)<sup>2</sup>〉</p>
