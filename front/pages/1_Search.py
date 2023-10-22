import streamlit as st
import streamlit.components.v1 as components
from func import *
from func_api import *


st.set_page_config(
    page_title="Mercado Track remastered",
    page_icon="Ⓜ",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "track app for mercado libre"
    }
)


st.title("Find what you are looking for!")
item = st.text_input('', placeholder="eg: iphone 14 pro max")          
submitted = st.button('Search', key="src0")
if len(item) != 0:
    show_data(item)
elif submitted and len(item) != 0:
    show_data(item)
elif submitted and len(item) == 0:
    st.warning("Empty Field")

