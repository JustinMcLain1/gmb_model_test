import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

prices = yf.download(
	"GOOGL",
	start="2010-01-01",
	end="2017-01-01",
	auto_adjust=False,
	progress=False,
).reset_index(drop=False)

price_col = "Adj Close" if "Adj Close" in prices.columns else "Close"
prices = prices[["Date", price_col]]

plt.figure(figsize=(10, 6))
plt.plot(prices["Date"], prices[price_col])
plt.title("Google Stock Price (2010-2016)")
plt.xlabel("Date")
plt.ylabel(f"{price_col} Price")
plt.grid()
plt.show()