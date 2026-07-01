
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = yf.download('RNMBY', period='5y')
print(data.head())

data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()

data['Signal'] = (data['SMA50'] > data['SMA200']).astype(int)
print(data[['Close', 'SMA50', 'SMA200', 'Signal']].tail())

plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='RNMBY Price', alpha=0.5)
plt.plot(data['SMA50'], label='SMA50', alpha=0.8)
plt.plot(data['SMA200'], label='SMA200', alpha=0.8)
plt.title('Momentum Analysis: SMA50 vs SMA200')
plt.legend()
plt.show()

/tmp/ipykernel_3651/193217642.py:7: FutureWarning: YF.download() has changed argument auto_adjust default to True
  data = yf.download('RNMBY', period='5y')
[*********************100%***********************]  1 of 1 completed
Price           Close       High        Low       Open Volume
Ticker          RNMBY      RNMBY      RNMBY      RNMBY  RNMBY
Date                                                         
2021-07-01  18.962473  18.962473  18.962473  18.962473    600
2021-07-02  18.661633  18.661633  18.661633  18.661633    300
2021-07-06  18.163364  18.445405  17.956536  18.426602   1200
2021-07-07  17.909527  18.059948  17.862521  17.980037   6900
2021-07-08  18.172762  18.172762  17.627485  17.627485   6100
Price            Close       SMA50      SMA200 Signal
Ticker           RNMBY                               
Date                                                 
2026-06-23  266.299988  296.617657  368.543813      0
2026-06-24  214.240005  293.925596  367.595236      0
2026-06-25  214.050003  291.259424  366.589746      0
2026-06-26  215.679993  288.520555  365.610220      0
2026-06-29  222.179993  285.983533  364.595107      0

