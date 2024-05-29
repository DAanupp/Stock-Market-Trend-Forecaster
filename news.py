import streamlit as st
from stocknews import StockNews

def app():
    # st.subheader('News')
    st.write("##### Stay updated on the latest news and developments related to a selected stock.")
    ticker_symbols = ["TCS.NS", "GOOG", "AAPL", "TSLA" ,"SBIN.NS","GAIL.NS"]

    selected_symbol = st.selectbox('Select a ticker symbol:', ticker_symbols, index=0)
    custom_symbol = st.text_input('Or enter a custom ticker symbol:')

    ticker= [custom_symbol if custom_symbol else selected_symbol]
    if ticker:
        # sn = StockNews(ticker,save_news=False)
        # df = sn.read_rss()
        # st.write(df)
        st.header(f'News of {ticker}')
        sn = StockNews(ticker, save_news=False)
        df_news = sn.read_rss()
        for i in range(10):
            st.subheader (f'News {i+1}')
            st.write(df_news['published'][i])
            st.write(df_news['title'][i])
            st.write(df_news['summary'][i])
            title_sentiment = df_news['sentiment_title'][i]
            st.write(f'Title sentiment {title_sentiment}')
            news_sentiment = df_news['sentiment_summary'][i]
            st.write(f'News Sentiment {news_sentiment}')

        
# def appt():
#     st.header(f'News of {ticker}')
#     sn = StockNews(ticker, save_news=False)
#     df_news = sn.read_rss()
#     for i in range(10):
#         st.subheader (f'News {i+1}')
#         st.write(df_news['published'][i])
#         st.write(df_news['title'][i])
#         st.write(df_news['summary'][i])
#         title_sentiment = df_news['sentiment_title'][i]
#         st.write(f'Title sentiment {title_sentiment}')
#         news_sentiment = df_news['sentiment_summary'][i]
#         st.write(f'News Sentiment {news_sentiment}')
