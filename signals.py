import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from tabulate import tabulate
def app():
    def GoldenCrossoverSignal(symbol, data_point):
    
        data = yf.download(symbol, period="1y")

        data['20_SMA'] = data['Close'].rolling(window=20, min_periods=1).mean()
        data['50_SMA'] = data['Close'].rolling(window=50, min_periods=1).mean()
        data['Signal'] = np.where(data['20_SMA'] > data['50_SMA'], 1, 0)
        data['Position'] = data['Signal'].diff()

        st.write("### Stock Price and Moving Averages")
        st.line_chart(data[['Close', '20_SMA', '50_SMA']].iloc[-data_point:])

        
        fig, ax = plt.subplots(figsize=(20, 10))
        data.iloc[-data_point:]['Close'].plot(color='k', label='Close Price', ax=ax)
        data.iloc[-data_point:]['20_SMA'].plot(color='b', label='20-day SMA', ax=ax)
        data.iloc[-data_point:]['50_SMA'].plot(color='g', label='50-day SMA', ax=ax)
        ax.plot(data.iloc[-data_point:][data.iloc[-data_point:]['Position'] == 1].index,
                data.iloc[-data_point:]['20_SMA'][data.iloc[-data_point:]['Position'] == 1],
                '^', markersize=15, color='g', label='Buy')
        ax.plot(data.iloc[-data_point:][data.iloc[-data_point:]['Position'] == -1].index,
                data.iloc[-data_point:]['20_SMA'][data.iloc[-data_point:]['Position'] == -1],
                'v', markersize=15, color='r', label='Sell')
        ax.set_ylabel('Price in Rupees', fontsize=15)
        ax.set_xlabel('Date', fontsize=15)
        ax.set_title(symbol, fontsize=20)
        ax.legend()
        ax.grid()
        st.pyplot(fig)

        df_pos = data.iloc[-data_point:][(data.iloc[-data_point:]['Position'] == 1) | (data['Position'] == -1)].copy()
        df_pos['Position'] = df_pos['Position'].apply(lambda x: 'Buy' if x == 1 else 'Sell')

        st.write("### Buy/Sell Signals")
        st.table(df_pos[['Close', 'Position']])

    
    st.write("### Golden Crossover Signal ")
    
    
    ticker_symbols = ["TCS.NS", "GOOG", "AAPL", "TSLA" ,"SBIN.NS","GAIL.NS"]

    selected_symbol = st.selectbox(' Select a ticker symbol:', ticker_symbols, index=0)
    custom_symbol = st.text_input('Or enter a custom ticker symbol:')

    ticker= [custom_symbol if custom_symbol else selected_symbol]
    data_point = st.slider("Number of Data Points to Display", min_value=50, max_value=500, value=200, step=50)

    if st.button("Generate Signals"):
        if ticker:
            GoldenCrossoverSignal(ticker, data_point)
        else:
            st.warning("Please enter a stock symbol.")
    st.write("##### Get actionable insights for optimal buying or selling times of a stock.")
    
