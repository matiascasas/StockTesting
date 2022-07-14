import matplotlib.pyplot as plt

import macd_stratergies
import gap_stratergies
import turtle_stratergies


tech_symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "FB", "TSM", "NVDA", "UBER", "NET", "AMD", "INTC", "IBM", "ADI"]
energy_symbols = ["XOM", "CVX", "SHEL", "TTE", "COP", "EQNR", "BP", "PTR", "ENB", "PBR", "EOG", "SLB", "PXD", "OXY"]
finance_symbols = ["JPM", "BAC", "WFC", "MS", "HSBC", "SCHW", "AXP", "SPGI", "AMT", "GS", "HDB", "C", "BLK", "CB", "BX"]

start_date = '2021-01-01'
end_date = '2021-12-20'

pos_cash = []
neg_cash = []
suma_tech = 0
for symbol in tech_symbols:

    print("----------------" + symbol + "--------- --------")
    # gain = gap_stratergies.filled_gap_stratergy(cash=100, sym=symbol, k_stop_loss=0.2, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = turtle_stratergies.turtle1_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = macd_stratergies.macd_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = turtle_stratergies.turtle1_stratergy_LTLF(cash=100, sym=symbol, k_stop_loss=0.2, k_target=2, str_time=start_date,
    #                                                 end_time=end_date)
    gain = turtle_stratergies.turtle2_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
                                                end_time=end_date)

    suma_tech = suma_tech + gain

    if gain >= 0:
        pos_cash.append(gain)
        neg_cash.append(0)
    else:
        neg_cash.append(gain)
        pos_cash.append(0)

plt.figure(0)
plt.bar(range(len(pos_cash)), pos_cash, align='center',alpha=0.5, label="Ventas Positivas")
plt.bar(range(len(neg_cash)), neg_cash, align='center',alpha=0.5, label="Ventas Negativas")
plt.xticks(range(len(pos_cash)), tech_symbols, size='small')
plt.title("Tech symbols")
plt.legend(loc='upper right')


pos_cash = []
neg_cash = []
suma_energy = 0
for symbol in energy_symbols:

    print("----------------" + symbol + "-----------------")
    # gain = gap_stratergies.filled_gap_stratergy(cash=100, sym=symbol, k_stop_loss=0.2, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = turtle_stratergies.turtle1_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = macd_stratergies.macd_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = turtle_stratergies.turtle1_stratergy_LTLF(cash=100, sym=symbol, k_stop_loss=0.2, k_target=2, str_time=start_date,
    #                                                 end_time=end_date)
    gain = turtle_stratergies.turtle2_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
                                                end_time=end_date)
    suma_energy = suma_energy + gain

    if gain >= 0:
        pos_cash.append(gain)
        neg_cash.append(0)
    else:
        neg_cash.append(gain)
        pos_cash.append(0)

plt.figure(1)
plt.bar(range(len(pos_cash)), pos_cash, align='center',alpha=0.5, label="Ventas Positivas")
plt.bar(range(len(neg_cash)), neg_cash, align='center',alpha=0.5, label="Ventas Negativas")
plt.xticks(range(len(energy_symbols)), energy_symbols, size='small')
plt.title("Energy symbols")
plt.legend(loc='upper right')


pos_cash = []
neg_cash = []
suma_finance = 0
for symbol in finance_symbols:

    print("----------------" + symbol + "-----------------")
    # gain = gap_stratergies.filled_gap_stratergy(cash=100, sym=symbol, k_stop_loss=0.2, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = turtle_stratergies.turtle1_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = macd_stratergies.macd_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
    #                                             end_time=end_date)
    # gain = turtle_stratergies.turtle1_stratergy_LTLF(cash=100, sym=symbol, k_stop_loss=0.2, k_target=2, str_time=start_date,
    #                                                 end_time=end_date)
    gain = turtle_stratergies.turtle2_stratergy(cash=100, sym=symbol, k_stop_loss=1, k_target=2, str_time=start_date,
                                                end_time=end_date)
    suma_finance = suma_finance + gain

    if gain >= 0:
        pos_cash.append(gain)
        neg_cash.append(0)
    else:
        neg_cash.append(gain)
        pos_cash.append(0)

plt.figure(2)
plt.bar(range(len(pos_cash)), pos_cash, align='center',alpha=0.5, label="Ventas Positivas")
plt.bar(range(len(neg_cash)), neg_cash, align='center',alpha=0.5, label="Ventas Negativas")
plt.xticks(range(len(finance_symbols)), finance_symbols, size='small')
plt.title("Finance symbols")
plt.legend(loc='upper right')

print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
print("Saldo final TECH symbols: " + str(suma_tech))
print("Saldo final ENERGY symbols: " + str(suma_energy))
print("Saldo final FINANCE symbols: " + str(suma_finance))
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
plt.show()
