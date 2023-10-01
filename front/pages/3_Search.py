import streamlit as st
import urllib3
from functions.search_products import search_products

with st.form(key='my_search'):
        st.write("<h3>Find what you are looking for!</h3>", unsafe_allow_html=True)
        item = st.text_input('', placeholder="iphone 14 pro max")
        submitted = st.form_submit_button('Search')
        if submitted:
            results = search_products("APP_USR-3750359463586153-093013-74f30a003501175650feeb53496be82f-142830670", "item")
            st.write("complete") 

total = results['paging']['total']
per_tag = total // 4

if submitted:
    st.write("Total items:", total)

    pag1, pag2, pag3, pag4, pag5, pag6 = st.tabs(["pag1", "pag2", "pag3", "pag4", "pag5", "pag6"])

    with pag1:
        cnt1, cnt2, cnt3 = st.container()
        with cnt1:
            item1= results['results'][0]
            
    with pag2:
        st.write("hola1")