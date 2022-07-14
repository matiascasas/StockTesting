import ta
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


def indicators(df):

    df['%K'] = ta.momentum.stoch(df.High, df.Low, df.Close, window=14, smooth_window=3)
    df['%D'] = df['%K'].rolling(3).mean()  # %D es la media movil de %K
    df['rsi'] = ta.momentum.rsi(df.Close, window=14)

    df['macd'] = ta.trend.macd_diff(df.Close)
    adx_class = ta.trend.ADXIndicator(high=df['High'],  # no se le puede cambiar el suavizado!
                                      low=df['Low'],
                                      close=df['Close'],
                                      window=14,
                                      fillna=False)
    df['adx'] = adx_class.adx()
    df['adx_neg'] = adx_class.adx_neg()
    df['adx_pos'] = adx_class.adx_pos()

    df['atr'] = ta.volatility.AverageTrueRange(high=df['High'],  # no se le puede cambiar el suavizado!
                                                low=df['Low'],
                                                close=df['Close'],
                                                window=14,
                                                fillna=False).average_true_range()

    df['vwap'] = ta.volume.VolumeWeightedAveragePrice(high=df['High'],
                                                       low=df['Low'],
                                                       close=df['Close'],
                                                       volume=df['Volume'],
                                                       window=14,
                                                       fillna=False).volume_weighted_average_price()

    df = df.drop(df.index[range(15)])  # Eliminamos las 15 primeras filas
    df.dropna(inplace=True)
    print(df)
    return df

def decide_filled_gap(df):

    # https://www.investopedia.com/articles/trading/05/playinggaps.asp

    df['Buy'] = 0
    df['Sell'] = 0

    delta = 2    # para rango de reconocimiento de gap
    delta_2 = 1   # para rango de bajada del precio despues del gap
    delta_3 = 8  # para rango de subida del precio despues del gap ANTES que baje

    i = 2
    while i < len(df):

        if (df.Close[i-1] + delta) < df.Open[i]:
            j = i

            while j < (len(df)-1) and df.Close[j] > (df.Close[i-1] + delta_2):
                if df.Close[j] > (df.Close[i-1] + delta_3):
                    break
                j = j + 1

            if df.Close[j] <= (df.Close[i-1] + delta_2):
                df.Buy[j] = 1

            i = j

        elif (df.Close[i-1] - delta) > df.Open[i]:
            j = i

            while j < (len(df)-1) and df.Close[j] < (df.Close[i - 1] - delta_2):
                if df.Close[j] < (df.Close[i - 1] + delta_3):
                    break
                j = j + 1

            if df.Close[j] >= (df.Close[i - 1] - delta_2):
                df.Sell[j] = 1

            i = j

        i = i + 1

    return df

# def decide_breakaway_gap(df):
#
#     # https://dotnettutorials.net/lesson/gap-trading-strategy/#:~:text=Why%20the%20breakaway%20gap%20occur%3F
#
#     df['Buy'] = 0
#     df['Sell'] = 0


def decide_turtle_1(df):

    df['Buy'] = 0
    df['Sell'] = 0

    n = 20

    for i in range(n + 1, len(df)):
        if df.Close[i] > df.High[i - n:i].max():
            df.Buy[i] = 1
        elif df.Close[i] < df.Low[i - n:i].min():
            df.Sell[i] = 1

    return df

def decide_turtle_2(df):

    df['Buy'] = 0
    df['Sell'] = 0

    n = 55

    for i in range(n + 1, len(df)):
        if df.Close[i] > df.High[i - n:i].max():
            df.Buy[i] = 1
        elif df.Close[i] < df.Low[i - n:i].min():
            df.Sell[i] = 1

    return df

def decide_macd(df):

    df['Buy'] = 0
    df['Sell'] = 0

    delta = 0.1

    for i in range(2, len(df)):
        if df.macd[i-1] <= delta < df.macd[i]:
            df.Buy[i] = 1
        if df.macd[i - 1] >= -delta > df.macd[i]:
            df.Sell[i] = 1
    return df
