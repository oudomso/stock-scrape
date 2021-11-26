import yfinance as yf
import streamlit as st
import pandas as pd
import datetime as dt

st.write("""
### Simple stock price app

shown are the stock closing price and volume of stock


""")

user_input = st.text_input("Enter Ticker symbol")
tickerSymbol = user_input

tickerData = yf.Ticker(tickerSymbol)

currentdate = dt.date.today()

tickerDf = tickerData.history(period='1d', start="2000-1-1", end=currentdate)


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)