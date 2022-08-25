import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import webbrowser

st.set_page_config(page_title="AI World", page_icon=":bar_chart:", layout="wide")

from IPL_Analysis import IPL_Analysis

selected_option = option_menu(None, ["Home", "Movie Recommendation", "IPL Analysis", 'House Price Prediction',
                                     'Whatsapp Chat Analyzer', 'Laptop Price Prediction' ,'Book Recommendation' , 'Data Science Blogs'],
    icons=['house',"film",  'bar-chart-line' , 'house-door-fill' , 'chat' , 'laptop' , 'book','book-half'],
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected_option == 'Home':

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return  None
        return r.json()


    col1, col2 = st.columns(2)
    with col1:
        st.title('Welcome to the World of AI')
    with col2:
        lottie_hello = load_lottieurl('https://assets10.lottiefiles.com/private_files/lf30_jyxnt8gq.json')
        st_lottie(lottie_hello, height = 200 , key = 'hello')

    lottie_ai = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_zrqthn6o.json')
    st_lottie(lottie_ai, height = 300 , key = 'coding')

    st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
    link = '[GitHub](http://github.com)'
    st.markdown(link, unsafe_allow_html=True)

    col1, col2  = st.columns(2)
    with col1:
        st.header('Movie Recommendation')
        st.markdown("[![Foo](https://cdn-images-1.medium.com/max/1200/1*LkpzdDsOk5rlVXrihGzKVw.png)](https://movie-recmd-system.herokuapp.com/)")
    with col2:
        st.header('IPL Win probability predictor')
        st.markdown("[![Foo](https://cdn-images-1.medium.com/max/1200/1*tCSSyaWVr0STmTEPIB9-VQ.png)](https://ipl-win-probability-ml-model.herokuapp.com/)")
    col1, col2 = st.columns(2)
    with col1:
        st.header('IPL Win probability predictor')
        st.markdown("[![Foo](https://cdn-images-1.medium.com/max/1200/1*2T4A_TlWshqmE71HPlfrMQ.png)](https://ipl-win-probability-ml-model.herokuapp.com/)")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style, unsafe_allow_html=True)