import streamlit as st

from streamlit_option_menu import option_menu

import forecast , news , signals , details , info

# st.title('Stock Trend Forecaster App')

# stocks = ('GOOG', 'AAPL', 'MSFT', 'GME','TSLA')
# selected_stock = st.text_input('Enter a ticker ( TCS.NS , GOOG , AAPL , TSLA ):')

st.title('Stock Trend Forecaster App')


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:        
            app = option_menu(
                menu_title=' SMF ',
                options=['Forecast','Buy\Sell','Details','News','About'],
                icons=['graph-up-arrow','arrow-down-up','list-task','newspaper','info-circle','info-circle-fill'],
                menu_icon='bar-chart-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Forecast":
            forecast.app()   
        if app == "Details":
            details.app()        
        if app == 'News':
            news.app()
        if app == 'Buy\Sell':
            signals.app()
        if app == 'About':
            info.app()    
             
          
             
    run()
