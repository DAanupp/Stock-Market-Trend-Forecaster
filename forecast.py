import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

def app():
    st.write("##### View predicted future performance of a selected stock.")
    # List of ticker symbols for suggestions
    ticker_symbols = ["TCS.NS", "GOOG", "AAPL", "TSLA"]

    st.write("#### Select a ticker:")
    selected_stock = st.selectbox('', ticker_symbols, index=0)

    custom_stock = st.text_input('### Or enter a custom ticker symbol:')

    selected_stock = custom_stock if custom_stock else selected_stock

    n_years = st.slider('Years of prediction:', 1, 4)
    period = n_years * 365

    st.success("###  " + str(yf.Ticker(selected_stock).info.get('longName', 'N/A')))

    @st.cache_data
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    if selected_stock:
        data_load_state = st.text('Downloading data.....')
        data = load_data(selected_stock)
        data_load_state.text('Downloaded succesfully !!')
        st.subheader('Raw data')
        st.write(data)

        
        def plot_raw_data():
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
            fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
            fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
            st.plotly_chart(fig)

        plot_raw_data()

        
        df_train = data[['Date','Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        
        st.subheader('Forecasted data')
        st.write(forecast.tail())
        
        st.subheader(f'Forecast Trend for {n_years} years')

        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

        st.write("Forecast components")
        fig2 = m.plot_components(forecast)
        st.write(fig2)
    else:
        st.warning('Please enter a valid ticker symbol.')

