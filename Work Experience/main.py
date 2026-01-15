# librarires

import polars as pl
import plotly.graph_objects as go
import numpy as np
df = pl.read_csv("AMD.csv").reverse()

#plot amd stock price

graph = go.Figure(data=go.Scatter(x=df["Date"], y=df["Close/Last"].str.strip_chars("$").cast(pl.Float64), mode="markers", marker=dict(size=2)))
graph.update_layout(title= "AMD price", xaxis_title = "Date", yaxis_title = "Close Price")
graph.show()

print(df)

df = df.with_columns([
    (pl.col("Close/Last").str.strip_chars("$").cast(pl.Float64).pct_change(1)*100).alias("Change")
])
df = df.with_columns([
    (pl.col("Close/Last").str.strip_chars("$").cast(pl.Float64).diff(1)).alias("Value Change")
])

df = df.with_columns([
    (pl.col("Close/Last").str.strip_chars("$").cast(pl.Float64).pct_change(1).shift(1) * 100).alias("Prediction")
])

df = df.with_columns([
    (pl.col("Close/Last").str.strip_chars("$").cast(pl.Float64).pct_change(1).shift(-1) * 100).alias("Actual Returns")
])

df = df.with_columns([
    pl.when(pl.col("Change")>0)
    .then(1)
    .otherwise(-1)
    .alias("Signal")
])
print(df)

df = df.with_columns([
    pl.when(pl.col("Signal")==-1)
    .then(pl.lit("red"))
    .otherwise(pl.lit("green"))
    .alias("Color")
])
print(df)

graph1 = go.Figure(data=go.Scatter(x=df["Date"],y=df["Close/Last"].str.strip_chars("$").cast(pl.Float64), mode="markers", marker=dict(size=4, color=df["Color"].to_list())))
graph1.update_layout(title= "AMD signal prediction", xaxis_title = "Date", yaxis_title = "Close Price")
graph1.show()

print(df.filter(pl.col("Date").is_in(["03/13/2019", "03/11/2019","03/12/2019"])))


signals = df["Signal"].to_list()
price = df["Close/Last"].str.strip_chars("$").cast(pl.Float64)


prediction_list = [round(v,2) for v in df["Prediction"].to_list() if v is not None]
print(prediction_list)

actual_returns = [round(v,2) for v in df["Actual Returns"].to_list() if v is not None]
print(actual_returns)

min_len = min(len(prediction_list), len(actual_returns))
mse = np.mean((np.array(actual_returns[:min_len]) - np.array(prediction_list[:min_len]))**2)
print(mse)


graph2 = go.Figure(data=go.Scatter(x=actual_returns,y=prediction_list, mode="markers", marker=dict(size=4, )))#color=df["Color"].to_list())))
graph2.update_layout(title= "AMD price vs predicted", xaxis_title = "Actual", yaxis_title = "Predicted change")
graph2.show()


signals = df["Signal"].to_list()
price = df["Close/Last"].str.strip_chars("$").cast(pl.Float64)



df = df.with_columns([
    pl.col("Close/Last").str.strip_chars("$").cast(pl.Float64).rolling_mean(window_size=5).alias("moving_avg")
])


df = df.with_columns([
    pl.when(pl.col("moving_avg")>0)
    .then(1)
    .otherwise(-1)
    .alias("Signal of avg")
])

#prev_fast > prev_slow and curr_fast <= curr_slow → cross down (Sell)
#prev_fast < prev_slow and curr_fast >= curr_slow → cross up (Buy)

df = df.with_columns([
    (pl.col("Close/Last").str.strip_chars("$").cast(pl.Float64).rolling_mean(window_size=5).fill_null(0).alias("MA_fast"))
])

df = df.with_columns([
    (pl.col("Close/Last").str.strip_chars("$").cast(pl.Float64).rolling_mean(window_size=20).fill_null(0).alias("MA_slow"))
])

df = df.with_columns([
    (pl.when(pl.col("MA_fast") > pl.col("MA_slow")).then(1).otherwise(-1)).alias("MA_Signal")
])


df = df.with_columns([
    (pl.col("MA_fast").shift(1).fill_null(0).alias("fast_prev")), (pl.col("MA_slow").shift(1).fill_null(0).alias("slow_prev"))
])

df = df.with_columns([
    (pl.when((pl.col("fast_prev") > pl.col("slow_prev")) & (pl.col("MA_fast") <= pl.col("MA_slow"))).then(1)
    .when((pl.col("fast_prev") < pl.col("slow_prev")) & (pl.col("MA_fast") >= pl.col("MA_slow"))).then(-1)
    .otherwise(0))
    .alias("crossover_signals")
])


print(df)

# functions to buy and sell

def buy(balance, stocks, price, amount, fee_percent=0.001):
  deduct = (price * amount * (1+fee_percent)) + 1
  if balance >= deduct:
    balance -= deduct
    stocks += amount
  return balance, stocks

def sell(balance, stocks, price, amount, fee_percent=0.001):
  if stocks >= amount:
    balance += price*amount
    stocks -= amount
    balance -= 1
  return balance, stocks


long_signals = df["Signal of avg"].shift(1).fill_null(0).to_list()
counter = 0
balance = 100000
stocks = 0
bought_for_long = 0
bought_for = 0
counter_long = 0
balance_arr = []
stock_arr = []
crossover_signals = df["crossover_signals"].to_list()

# strategy loop


for i in range(len(signals)):
    #buying stocks with 30% of our balance using the short term signals
    counter += signals[i]
    amount_to_buy = int((balance * 0.3) // price[i])
    to_sell = int(stocks*0.3)
    #buying stocks with 70% of our balance using the moving average signals
    counter_long += long_signals[i]
    amount_to_buy_long = int((balance * 0.7) // price[i])
    to_sell_long = int(stocks*0.5)

    if counter_long == -4: # this is equivalent to 20 cumulative signals of 0
      balance, stocks = buy(balance, stocks, price[i], amount_to_buy_long)
      bought_for_long = price[i]*amount_to_buy_long
      counter_long = 0
    elif counter_long == 1 and stocks >= to_sell and price[i] > bought_for_long:# this is equivalent to 5 cumulative signals of 5
      counter_long = 0
      balance, stocks = sell(balance, stocks, price[i], to_sell)

    if counter == -1: # this will buy immediately when the signal is 0. This
      bought_for = price[i]
      balance, stocks = buy(balance, stocks, price[i], amount_to_buy)
      counter = 0
    elif counter == 16 and stocks > 0 and price[i] > bought_for:
      balance, stocks = sell(balance, stocks, price[i], to_sell)
      counter = 0
    balance_arr.append(balance)
    stock_arr.append(stocks*price[i])
balance, stocks = sell(balance, stocks, price[-1], stocks)
print(balance)

initial_price = price[0]
final_price = price[-1]
buy_and_hold_return = (final_price - initial_price) / initial_price * 100
print(buy_and_hold_return)
nw = [balance_arr[i]+stock_arr[i] for i in range(len(balance_arr))]

# plot balance plus equity

graph2 = go.Figure(data=go.Scatter(x=df["Date"],y=nw, mode="markers", marker=dict(size=4, )))#color=df["Color"].to_list())))
graph2.update_layout(title= "Balance + Equity over time", xaxis_title = "Date", yaxis_title = "USD")
graph2.show()


balance = 100000
stocks = 0
balance_arr = []
stock_arr = []

# crossover

for i in range(len(crossover_signals)): # crossover strategy test
    #buying with 90% of balance if crossover signals to
    crossover_buy = int((balance*0.7)) // price[i]
    to_sell_cross = int(stocks*0.5)

    if crossover_signals[i] == -1:
      balance, stocks = buy(balance, stocks, price[i], crossover_buy)
      bought_for = price[i]
      counter = 0
    elif crossover_signals[i] == 1:
      balance, stocks = sell(balance,stocks, price[i], to_sell_cross)

    balance_arr.append(balance)
    stock_arr.append(stocks*price[i])
balance, stocks = sell(balance, stocks, price[-1], stocks)
nw = [balance_arr[i]+stock_arr[i] for i in range(len(balance_arr))]
print(balance)

graph3 = go.Figure(data=go.Scatter(x=df["Date"],y=nw, mode="markers", marker=dict(size=4, )))#color=df["Color"].to_list())))
graph3.update_layout(title= "Balance + Equity over time (with crossover)", xaxis_title = "Date", yaxis_title = "USD")
graph3.show()


def sharpe_ratio(eq: np.ndarray, rf: float = 0.0) -> float:
    rets = np.diff(eq) / eq[:-1]
    return np.sqrt(252) * (rets.mean() - rf) / rets.std() if rets.std() else 0.0

print(sharpe_ratio(np.array(nw), 0.00043))
