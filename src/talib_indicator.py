import talib
import matplotlib.pyplot as plt
import pandas as pd

class talibIndicators:
    def __init__(self, df):
        self.df = df
        self. sma_20 = talib.SMA(df['Close'], timeperiod=20)
        self. ema_20 = talib.EMA(df['Close'], timeperiod=20)
        self. rsi = talib.RSI(df['Close'], timeperiod=14)
        self. macd, self.signal, self.hist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

        self. adx = talib.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)

        self.slowk, self.slowd = talib.STOCH(df['High'], df['Low'], df['Close'],fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

        self.upperBand, self.midleBand, self.lowerBand = talib.BBANDS(df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)

        self.atr = talib.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)

        self.obv = talib.OBV(df['Close'], df['Volume'])

        self.ad = talib.AD(df['High'], df['Low'], df['Close'], df['Volume'])


    def change_to_datetime(self, column= 'Date'):
        """To covert an object to datetime dtype
        takes data framw and column name to be converted """

        self.df[column] = pd.to_datetime(self.df[column])
        return self.df
    

    def assign_property(self):
        list=['SMA_20','ema', 'rsi','macd',"signal",
              'hist','adx','slowk',"slowd",'upperBand','middleBand','lowerBand','atr','obv','ad',]
        selfs =[self.sma_20,self.ema_20, self.rsi, self.macd, self.signal, self.signal, self.hist, 
                self.adx, self.slowk, self.slowd, self.upperBand,self.midleBand, self.lowerBand, self.atr, self.obv, self.ad]
        for i in range(len(list)):
            self.df[list[i]] = selfs[i]
        return self.df
    
    def filtered(self):
        self.df = self.df[self.df['Date'] >= '2000-01-01']
        self.df = self.df.set_index(self.df['Date'])
        return self.df


    def plot_stock_price_with_moving_average(self, titel="apple"):
        
        # Plot Close Price with SMA and EMA
        plt.figure(figsize=(14, 7))
        plt.plot(self.df['Close'], label='Close Price', color='blue')
        plt.plot(self.df['SMA_20'], label='SMA 20', color='green')
        plt.plot(self.df['ema'], label='EMA 20', color='red')
        plt.title(f"{titel}'s Stock Price with Moving Averages")
        plt.legend()
        plt.show()
        return plt

    def plot_relative_rsi(self, title="Apple"):
        # Plot RSI
        plt.figure(figsize=(14, 7))
        plt.plot(self.df['rsi'], label='RSI', color='purple')
        plt.axhline(70, color='red', linestyle='--', label='Overbought')
        plt.axhline(30, color='green', linestyle='--', label='Oversold')
        plt.title(f"{title}'s Relative Strength Index (RSI)")
        plt.legend()
        plt.show()
        return plt