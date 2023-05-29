# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:53:29 2023

@author: ozgur
"""

import yfinance as yf
import pandas as pd


def name_fix(stk): # Arrange this name function for yourself, this is for BIST only
    if stk.startswith("."):
        stk = stk.replace(".","")
        stk = stk + ".IS"
    
    return stk
        
existingdata = pd.read_csv("data.csv")
new_data = dict()
new_df = pd.DataFrame()
ema14 = []
sma55 = []
sma200 = []
vsma20 = []
vsma5 = []
vol = []
for stock in existingdata["Symbol"]:
    print(stock)
    data = yf.Ticker(name_fix(stock)).history(period = "2y")
    ema = data["Close"].ewm(span= 14, adjust = False, min_periods = 14, ignore_na = True).mean()[-1]
    sma1 = data["Close"].rolling(window = 55).mean()[-1]
    sma2= data["Close"].rolling(window = 200).mean()[-1]
    ema14.append(ema)
    sma55.append(sma1)
    sma200.append(sma2)
    vsma1 = data["Volume"].rolling(window = 20).mean()[-1]
    vsma2= data["Volume"].rolling(window = 5).mean()[-1]
    volume = data["Volume"].rolling(window = 1).mean()[-1]
    vsma20.append(vsma1)
    vsma5.append(vsma2)
    vol.append(volume)

existingdata["ema14"] = ema14
existingdata["ma55"] = sma55
existingdata["ma200"] = sma200
existingdata["vsma20"] = vsma20
existingdata["vsma5"] = vsma5
existingdata["volume"] = vol

existingdata.to_csv("data.csv",  index = False)
