
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


bitcoin = pd.read_csv('BTC-EUR.csv')
print(bitcoin.head())
bitcoin['Close'].plot(figsize=(9, 6))
plt.show()