import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Parameter Definitions

# So    :   initial stock price
# dt    :   time increment -> a day in our case
# T     :   length of the prediction time horizon(how many time points to predict, same unit with dt(days))
# N     :   number of time points in the prediction time horizon -> T/dt
# t     :   array for time points in the prediction time horizon [1, 2, 3, .. , N]
# mu    :   mean of historical daily returns
# sigma :   standard deviation of historical daily returns
# b     :   array for brownian increments
# W     :   array for brownian path

tickers = ['MSFT', 'AAPL', 'GOOG']
prices = yf.download(
	tickers,
	start="2010-01-01",
	end="2025-01-01",
	auto_adjust=False,
	progress=False,
).reset_index(drop=False)

price_col = "Adj Close" if "Adj Close" in prices.columns else "Close"
prices = prices[["Date", price_col]]

plt.figure(figsize=(10, 6))
plt.plot(prices["Date"], prices[price_col])
plt.title(f"{', '.join(tickers)} (2010-2025)")
plt.xlabel("Date")
plt.ylabel(f"{price_col} Price")
plt.grid()
plt.show()
print(prices.head())