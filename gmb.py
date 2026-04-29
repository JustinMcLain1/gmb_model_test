import pandas as pd
import numpy as np
import quandl
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

prices = quandl.get("WIKI/GOOGL", start_date="2010-01-01", end_date="2016-12-31").reset_index(drop=False)[["Date", "Adj. Close"]]

plt.figure(figsize=(10, 6))
plt.plot(prices["Date"], prices["Adj. Close"])
plt.title("Google Stock Price (2010-2016)")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.grid()
plt.show()