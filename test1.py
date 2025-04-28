import streamlit as st
import pandas as pd 
import numpy as np
import yfinance as yf

st.title('Stock Market Analysis !!')

start_date=st.date_input('Start_Date',pd.to_datetime('2020-01-01'))

end_date=st.date_input('End_Date',pd.to_datetime('2020-01-01'))


symbol=st.text_input('Enter the stock ticker symbol')

ticker_data=yf.Ticker(symbol)
ticker_df=ticker_data.history(period='1d',start=start_date,end=end_date)

st.dataframe(ticker_df)

st.write('## Closing Price Chart')
st.line_chart(ticker_df['Close'])