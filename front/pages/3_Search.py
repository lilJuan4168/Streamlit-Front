import streamlit as st
import urllib3
from functions.search_products import search_products
import json

with st.form(key='my_search'):
        st.write("<h3>Find what you are looking for!</h3>", unsafe_allow_html=True)
        item = st.text_input('', placeholder="iphone 14 pro max")
        submitted = st.form_submit_button('Search')
        if submitted:
            #results = search_products("APP_USR-3750359463586153-093013-74f30a003501175650feeb53496be82f-142830670", "item")
            st.success("complete") 

#total = results['paging']['total']
#per_tag = total // 4

with open("front/pages/test.json", 'r') as js:
     data = json.load(js)

total = data['paging']['total']    


if submitted:
    st.write("Total items:", total)

    pag1, pag2, pag3, pag4, pag5, pag6 = st.tabs(["pag1", "pag2", "pag3", "pag4", "pag5", "pag6"])

    with pag1:
        st.write(data['results'][0]['title'])
        st.write(data['results'][0]['price'])
        st.image(data['results'][0]['thumbnail'])

        st.divider()

        st.write(data['results'][1]['title'])
        st.write(data['results'][1]['price'])
        st.image(data['results'][1]['thumbnail'])
            