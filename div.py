from time import time
import yfinance as yf
from yfinance.ticker import Ticker 
from datetime import time
import numpy

agnc = yf.Ticker("AGNC")



dividend = float(agnc.info['dividendRate'])


question = float(input("How many shares of AGNC do you own? "))

print(question)

add = (question + dividend)

print(add)

