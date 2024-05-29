import streamlit as st

def app():
    st.write("## About our website")
    st.write("SMF is a website used to predict and forecast trends and price for a given stock just by entering its ticker symbol. Our system has various features like Buy/Sell signals which can someone make informed decisions. The News service gives latest Top 10 news about the given STOCK. The Details service provides all the fundamentals info about the stock which can be used by investor to get to know the company")

    
    

    st.write("## Some Stock Market Terminologies")
    st.write("""
    <ul>
        <li><strong>Ticker Symbol:</strong> The unique symbol used to identify a particular stock on a stock exchange.</li>
        <li><strong>High:</strong> The highest price at which a stock traded during a specific period, typically a day.</li>
        <li><strong>Low:</strong> The lowest price at which a stock traded during a specific period, typically a day.</li>
        <li><strong>Moving Average:</strong> A calculated average of a specified number of previous prices, often used to smooth out short-term fluctuations and identify trends.</li>
        <li><strong>Volume:</strong> The total number of shares of a stock traded during a specific period, typically a day.</li>
        <li><strong>Market Cap (Market Capitalization):</strong> The total value of a company's outstanding shares, calculated by multiplying the current stock price by the total number of outstanding shares.</li>
        <li><strong>Dividend:</strong> A distribution of a portion of a company's earnings to its shareholders, typically paid quarterly.</li>
        <li><strong>P/E Ratio (Price-to-Earnings Ratio):</strong> A measure of a company's current share price relative to its per-share earnings. It indicates how much investors are willing to pay per dollar of earnings.</li>
        <li><strong>Beta:</strong> A measure of a stock's volatility in relation to the overall market. A beta greater than 1 indicates higher volatility, while a beta less than 1 indicates lower volatility.</li>
        <li><strong>EPS (Earnings Per Share):</strong> The portion of a company's profit allocated to each outstanding share of common stock, calculated by dividing the company's net income by the total number of outstanding shares.</li>
        <li><strong>Dividend Yield:</strong> A financial ratio that indicates the annual dividend income per share relative to the stock's market price, expressed as a percentage.</li>
        <li><strong>52-Week High/Low:</strong> The highest and lowest prices at which a stock has traded over the past 52 weeks (1 year).</li>
        <li><strong>Trading Volume:</strong> The number of shares of a security that were traded during a given period of time.</li>
        <li><strong>Volatility:</strong> A statistical measure of the dispersion of returns for a given security or market index. It indicates the degree of variation of a trading price series over time.</li>
    </ul>
    """, unsafe_allow_html=True)
   
