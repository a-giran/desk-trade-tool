import pandas as pd

# Sample trade data
trade_data = {
    "Trade ID": [1, 2, 3, 4],
    "Date": ["2025-04-01", "2025-04-03", "2025-04-04", "2025-04-05"],
    "Asset": ["AAPL", "TLT", "SPY", "BTC"],
    "Direction": ["Buy", "Sell", "Buy", "Buy"],
    "Quantity": [100, 50, 200, 1],
    "Entry Price": [165.00, 110.50, 412.00, 65000],
    "Current Price": [170.00, 108.00, 420.00, 67000]
}

df_trades = pd.DataFrame(trade_data)
df_trades["Date"] = pd.to_datetime(df_trades["Date"])
df_trades["PnL"] = (df_trades["Current Price"] - df_trades["Entry Price"]) * df_trades["Quantity"]
df_trades["Exposure"] = df_trades["Current Price"] * df_trades["Quantity"]

summary = {
    "Total PnL": df_trades["PnL"].sum(),
    "Total Exposure": df_trades["Exposure"].sum(),
    "Number of Trades": df_trades.shape[0],
    "Net Long Exposure": df_trades[df_trades["Direction"] == "Buy"]["Exposure"].sum(),
    "Net Short Exposure": df_trades[df_trades["Direction"] == "Sell"]["Exposure"].sum()
}
#blah
df_summary = pd.DataFrame(list(summary.items()), columns=["Metric", "Value"])
df_trades.to_csv("trade_blotter.csv", index=False)
df_summary.to_csv("summary.csv", index=False)

print("Trade data and summary saved.")