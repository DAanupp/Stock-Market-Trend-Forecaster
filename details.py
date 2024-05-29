import streamlit as st
import yfinance as yf

def app():
    ticker_symbols = ["TCS.NS", "GOOG", "AAPL", "TSLA"]
    st.write("##### Access fundamental information about a selected stock.")

    selected_symbol = st.selectbox('Select a ticker symbol:', ticker_symbols, index=0)
    custom_symbol = st.text_input('Or enter a custom ticker symbol:')

    ticker_symbol = custom_symbol if custom_symbol else selected_symbol

    if ticker_symbol:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info

        
        st.subheader('Basic Information')
        basic_info_columns = st.columns(2) 
        with basic_info_columns[0]:
            st.write("Name:", info.get('longName', 'N/A'), font_size="80px")
            st.write("Exchange:", info.get('exchange', 'N/A'), font_size="80px")
        with basic_info_columns[1]:
            st.write("Sector:", info.get('sector', 'N/A'), font_size="20px")
            st.write("Industry:", info.get('industry', 'N/A'), font_size="20px")

        
        st.subheader('Summary')
        st.info("Market Cap: " + str(info.get('marketCap', 'N/A')))
        st.success("PE Ratio (TTM): " + str(info.get('forwardPE', 'N/A')))
        st.warning("Dividend Yield: " + str(info.get('dividendYield', 'N/A')))
        st.error("52 Week High: " + str(info.get('fiftyTwoWeekHigh', 'N/A')))
        st.error("52 Week Low: " + str(info.get('fiftyTwoWeekLow', 'N/A')))


        st.subheader('Additional Information')
        st.write("Website:", info.get('website', 'N/A'))
        st.write("Business Summary:", info.get('longBusinessSummary', 'N/A'))


