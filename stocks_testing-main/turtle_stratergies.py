from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import signals


def turtle1_stratergy(cash, sym, k_stop_loss, k_target, str_time, end_time, buy_position=False, sell_position=False):

    i = 0
    j = 0
    n = 10
    compras = 0
    ventas = 0
    buy_price = 0
    sell_price = 0
    suma = 0
    venta_positiva = 0
    venta_negativa = 0
    compra_positiva = 0
    compra_negativa = 0
    exit_buy = False
    exit_sell = False

    df = data.DataReader(sym, 'yahoo', str_time, end_time)

    if isinstance(df, pd.DataFrame):

        df = signals.indicators(df)
        df = signals.decide_turtle_1(df)

        # Plots
        # fig, ax = plt.subplots(2)
        # fig.suptitle('Estrategia TURTLE 1: ' + sym + ' desde: ' + str_time + ' hasta: ' + end_time)
        # fig.tight_layout()
        #
        # x_axe = df.index
        # y_axe = np.ones(len(df.index))
        #
        # ax[0].set_title('Precio de cierre')
        # ax[0].grid(linestyle='dotted')
        # ax[0].plot(df.index, df['Close'])
        #
        # ax[1].set_title('ATR')
        # ax[1].grid(linestyle='dotted')
        # ax[1].plot(df['atr'], "r-")
        # ax[1].plot(x_axe, np.multiply(y_axe, 0))

        while i <= (len(df)-2):

            if df.Buy.iloc[i]:  # abre posicion y compra

                # ax[0].annotate('Compra', (df.index[i], df.Close.iloc[i]),
                #             arrowprops = dict(facecolor='blue', shrink=0.05))

                buy_price = df.Close.iloc[i]
                compras = compras + 1
                buy_position = True
                target = df.Close[i] + df.atr[i-2] * k_target   #el target no es dinamico!
                stop_loss = df.Close[i] - df.atr[i-2] * k_stop_loss
                j = i
                start_index = i

            elif df.Sell.iloc[i]:

                # ax[0].annotate('Venta', (df.index[i], df.Close.iloc[i]),
                #                arrowprops=dict(facecolor='blue', shrink=0.05))

                sell_price = df.Close.iloc[i]
                ventas = ventas + 1
                sell_position = True
                target = df.Close[i] - df.atr[i] * k_target   #el target no es dinamico!
                stop_loss = df.Close[j] + df.atr[j] * k_stop_loss
                j = i
                start_index = i

            else:
                i = i + 1

            while (buy_position or sell_position) and j <= (len(df)-2):

                j = j + 1
                i = j

                # agrego que si no rompe al alza en 10 ticks, salga
                if buy_position and (j-start_index > 5) and (df.Close[j] < buy_price + df.atr[j-5]):
                    print ("entre: ")
                    print(j-i)
                    exit_buy = True

                if sell_position and (j-start_index > 5) and (df.Close[j] > sell_price - df.atr[j-5]):
                    exit_sell = True

                if buy_position and ((df.Close[j] <= stop_loss)\
                        or (df.Close[j] <= df.Low[j-n:j].min())\
                        or (df.Close[j] >= target)\
                        or exit_buy):

                    dif = (df.Close[j] - buy_price) / buy_price * cash
                    if dif > 0:
                        venta_positiva = venta_positiva + 1
                        suma = suma + dif

                        # ax[0].annotate('Venta', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='green', shrink=0.05))
                    else:
                        venta_negativa = venta_negativa + 1
                        suma = suma + dif

                        # ax[0].annotate('Venta', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='red', shrink=0.05))

                    buy_position = False
                    exit_buy = False
                    break

                if sell_position and ((df.Close[j] >= stop_loss)\
                        or df.Close[j] >= df.High[j-n:j].max()\
                        or (df.Close[j] <= target)\
                        or exit_sell):

                    dif = (sell_price - df.Close[j]) / sell_price * cash
                    if dif > 0:
                        compra_positiva = compra_positiva + 1
                        suma = suma + dif

                        # ax[0].annotate('Compra', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='green', shrink=0.05))
                    else:
                        compra_negativa = compra_negativa + 1
                        suma = suma + dif

                        # ax[0].annotate('Compra', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='red', shrink=0.05))

                    sell_position = False
                    exit_sell = False
                    break


        print('Numero de compras: ' + str(compras) + '\n')
        print('Numero de ventas Positivas: ' + str(venta_positiva) + '\n')
        print('Numero de ventas Negativas: ' + str(venta_negativa) + '\n')
        print('Numero de compras Positivas: ' + str(compra_positiva) + '\n')
        print('Numero de compras Negativas: ' + str(compra_negativa) + '\n')
        print('Saldo total: ' + str(suma) + '\n')
        # plt.show()

        return suma


def turtle1_stratergy_LTLF(cash, sym, k_stop_loss, k_target, str_time, end_time, buy_position=False, sell_position=False):

    i = 0
    j = 0
    n = 10
    compras = 0
    ventas = 0
    buy_price = 0
    sell_price = 0
    suma = 0
    venta_positiva = 0
    venta_negativa = 0
    compra_positiva = 0
    compra_negativa = 0
    exit_buy = False
    exit_sell = False
    ltlf_buy = False
    ltlf_sell = False

    df = data.DataReader(sym, 'yahoo', str_time, end_time)

    if isinstance(df, pd.DataFrame):

        df = signals.indicators(df)
        df = signals.decide_turtle_1(df)

        # Plots
        # fig, ax = plt.subplots(2)
        # fig.suptitle('Estrategia TURTLE 1: ' + sym + ' desde: ' + str_time + ' hasta: ' + end_time)
        # fig.tight_layout()
        #
        # x_axe = df.index
        # y_axe = np.ones(len(df.index))
        #
        # ax[0].set_title('Precio de cierre')
        # ax[0].grid(linestyle='dotted')
        # ax[0].plot(df.index, df['Close'])
        #
        # ax[1].set_title('ATR')
        # ax[1].grid(linestyle='dotted')
        # ax[1].plot(df['atr'], "r-")
        # ax[1].plot(x_axe, np.multiply(y_axe, 0))

        while i <= (len(df)-2):

            if df.Buy.iloc[i]:  # abre posicion y compra

                # ax[0].annotate('Compra', (df.index[i], df.Close.iloc[i]),
                #             arrowprops = dict(facecolor='blue', shrink=0.05))

                buy_price = df.Close.iloc[i]
                compras = compras + 1
                buy_position = True
                target = df.Close[i] + df.atr[i-2] * k_target   #el target no es dinamico!
                stop_loss = df.Close[i] - df.atr[i-2] * k_stop_loss
                j = i
                start_index = i

            elif df.Sell.iloc[i]:

                # ax[0].annotate('Venta', (df.index[i], df.Close.iloc[i]),
                #                arrowprops=dict(facecolor='blue', shrink=0.05))

                sell_price = df.Close.iloc[i]
                ventas = ventas + 1
                sell_position = True
                target = df.Close[i] - df.atr[i] * k_target   #el target no es dinamico!
                stop_loss = df.Close[j] + df.atr[j] * k_stop_loss
                j = i
                start_index = i

            else:
                i = i + 1

            while (buy_position or sell_position) and j <= (len(df)-2):

                j = j + 1
                i = j

                # agrego que si no rompe al alza en 10 ticks, salga
                if buy_position and (j-start_index > 5) and (df.Close[j] < buy_price + df.atr[j-5]):
                    print ("entre: ")
                    print(j-i)
                    exit_buy = True

                if sell_position and (j-start_index > 5) and (df.Close[j] > sell_price - df.atr[j-5]):
                    exit_sell = True

                if buy_position and ((df.Close[j] <= stop_loss)\
                        or (df.Close[j] <= df.Low[j-n:j].min())\
                        or (df.Close[j] >= target)\
                        or exit_buy):

                    dif = (df.Close[j] - buy_price) / buy_price * cash
                    if dif > 0 and not ltlf_buy:
                        venta_positiva = venta_positiva + 1
                        suma = suma + dif
                        ltlf_buy = True
                        # ax[0].annotate('Venta', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='green', shrink=0.05))
                    elif ltlf_buy:
                        ltlf_buy = False   #si la anterior fue exitosa, descansa 1

                    if dif < 0 and not ltlf_sell:
                        venta_negativa = venta_negativa + 1
                        suma = suma + dif
                        # ax[0].annotate('Venta', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='red', shrink=0.05))
                    elif ltlf_sell:
                        ltlf_sell = False  #si la anterior fue exitosa, descansa 1

                    buy_position = False
                    exit_buy = False
                    break

                if sell_position and ((df.Close[j] >= stop_loss)\
                        or df.Close[j] >= df.High[j-n:j].max()\
                        or (df.Close[j] <= target)\
                        or exit_sell):

                    dif = (sell_price - df.Close[j]) / sell_price * cash
                    if dif > 0:
                        compra_positiva = compra_positiva + 1
                        suma = suma + dif

                        # ax[0].annotate('Compra', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='green', shrink=0.05))
                    else:
                        compra_negativa = compra_negativa + 1
                        suma = suma + dif

                        # ax[0].annotate('Compra', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='red', shrink=0.05))

                    sell_position = False
                    exit_sell = False
                    break


        print('Numero de compras: ' + str(compras) + '\n')
        print('Numero de ventas Positivas: ' + str(venta_positiva) + '\n')
        print('Numero de ventas Negativas: ' + str(venta_negativa) + '\n')
        print('Numero de compras Positivas: ' + str(compra_positiva) + '\n')
        print('Numero de compras Negativas: ' + str(compra_negativa) + '\n')
        print('Saldo total: ' + str(suma) + '\n')
        # plt.show()

        return suma

def turtle2_stratergy(cash, sym, k_stop_loss, k_target, str_time, end_time, buy_position=False, sell_position=False):

    i = 0
    j = 0
    n_buy = 20
    n_sell = 10
    compras = 0
    ventas = 0
    buy_price = 0
    sell_price = 0
    suma = 0
    venta_positiva = 0
    venta_negativa = 0
    compra_positiva = 0
    compra_negativa = 0
    exit_buy = False
    exit_sell = False

    df = data.DataReader(sym, 'yahoo', str_time, end_time)

    if isinstance(df, pd.DataFrame):

        df = signals.indicators(df)
        df = signals.decide_turtle_1(df)

        # Plots
        # fig, ax = plt.subplots(2)
        # fig.suptitle('Estrategia TURTLE 1: ' + sym + ' desde: ' + str_time + ' hasta: ' + end_time)
        # fig.tight_layout()
        #
        # x_axe = df.index
        # y_axe = np.ones(len(df.index))
        #
        # ax[0].set_title('Precio de cierre')
        # ax[0].grid(linestyle='dotted')
        # ax[0].plot(df.index, df['Close'])
        #
        # ax[1].set_title('ATR')
        # ax[1].grid(linestyle='dotted')
        # ax[1].plot(df['atr'], "r-")
        # ax[1].plot(x_axe, np.multiply(y_axe, 0))

        while i <= (len(df)-2):

            if df.Buy.iloc[i]:  # abre posicion y compra

                # ax[0].annotate('Compra', (df.index[i], df.Close.iloc[i]),
                #             arrowprops = dict(facecolor='blue', shrink=0.05))

                buy_price = df.Close.iloc[i]
                compras = compras + 1
                buy_position = True
                target = df.Close[i] + df.atr[i-2] * k_target   #el target no es dinamico!
                stop_loss = df.Close[i] - df.atr[i-2] * k_stop_loss
                j = i
                start_index = i

            elif df.Sell.iloc[i]:

                # ax[0].annotate('Venta', (df.index[i], df.Close.iloc[i]),
                #                arrowprops=dict(facecolor='blue', shrink=0.05))

                sell_price = df.Close.iloc[i]
                ventas = ventas + 1
                sell_position = True
                target = df.Close[i] - df.atr[i] * k_target   #el target no es dinamico!
                stop_loss = df.Close[j] + df.atr[j] * k_stop_loss
                j = i
                start_index = i

            else:
                i = i + 1

            while (buy_position or sell_position) and j <= (len(df)-2):

                j = j + 1
                i = j

                # agrego que si no rompe al alza en 10 ticks, salga
                if buy_position and (j-start_index > 20) and (df.Close[j] < buy_price + df.atr[j-5]):
                    print ("entre: ")
                    print(j-i)
                    exit_buy = True

                if sell_position and (j-start_index > 20) and (df.Close[j] > sell_price - df.atr[j-5]):
                    exit_sell = True

                if buy_position and ((df.Close[j] <= stop_loss)\
                        or (df.Close[j] <= df.Low[j-n_buy:j].min())\
                        or (df.Close[j] >= target)\
                        or exit_buy):

                    dif = (df.Close[j] - buy_price) / buy_price * cash
                    if dif > 0:
                        venta_positiva = venta_positiva + 1
                        suma = suma + dif

                        # ax[0].annotate('Venta', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='green', shrink=0.05))
                    else:
                        venta_negativa = venta_negativa + 1
                        suma = suma + dif

                        # ax[0].annotate('Venta', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='red', shrink=0.05))

                    buy_position = False
                    exit_buy = False
                    break

                if sell_position and ((df.Close[j] >= stop_loss)\
                        or df.Close[j] >= df.High[j-n_sell:j].max()\
                        or (df.Close[j] <= target)\
                        or exit_sell):

                    dif = (sell_price - df.Close[j]) / sell_price * cash
                    if dif > 0:
                        compra_positiva = compra_positiva + 1
                        suma = suma + dif

                        # ax[0].annotate('Compra', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='green', shrink=0.05))
                    else:
                        compra_negativa = compra_negativa + 1
                        suma = suma + dif

                        # ax[0].annotate('Compra', (df.index[j], df.Close.iloc[j]),
                        #             arrowprops=dict(facecolor='red', shrink=0.05))

                    sell_position = False
                    exit_sell = False
                    break


        print('Numero de compras: ' + str(compras) + '\n')
        print('Numero de ventas Positivas: ' + str(venta_positiva) + '\n')
        print('Numero de ventas Negativas: ' + str(venta_negativa) + '\n')
        print('Numero de compras Positivas: ' + str(compra_positiva) + '\n')
        print('Numero de compras Negativas: ' + str(compra_negativa) + '\n')
        print('Saldo total: ' + str(suma) + '\n')
        # plt.show()

        return suma