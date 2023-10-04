import streamlit as st
import urllib3
from functions.search_products import search_products
import json


with st.form(key='my_search'):
        st.write("<h3>Find what you are looking for!</h3>", unsafe_allow_html=True)
        item = st.text_input('', placeholder="iphone 14 pro max")
        submitted = st.form_submit_button('Search')
        if submitted and len(item) != 0:
            data = search_products("APP_USR-3750359463586153-100300-850be7d19f6faf69fd9ef64a06f1f1d7-142830670", item)
            st.success("Ok") 

#-------------
#with open("front/pages/test.json", 'r') as js:
#     data = json.load(js)
last_number = 0 
#--------------



if submitted:
    total = len(data) 
    per_pag = total // 3
    st.write("Total items:", total)

    pag1, pag2, pag3, pag4, pag5, pag6 = st.tabs(["pag1", "pag2", "pag3", "pag4", "pag5", "pag6"])

    with pag1:
        for i in range(0, per_pag):
            st.write(data[i]['title'])
            st.write("Price $(ars):", data[i]['price'])
            st.write("Quantity:",data[i]["available_quantity"])
            st.write("Id:",data[i]['product_id'])
            st.write("Seller Nickname:", data[i]['seller_nickname'])
            st.image(data[i]['thumbnail'], width=90)
            last_number = i
            st.divider()
        st.write("max item:",last_number)

    with pag2:
        for i in range(last_number, 2 * per_pag):
            st.write(data[i]['title'])
            st.write("Price $(ars):", data[i]['price'])
            st.write("quantity:",data[i]["available_quantity"])
            st.write("id:",data[i]['product_id'])
            st.image(data[i]['thumbnail'], width=90)
            last_number = i
            st.divider()
        st.write("max item:",last_number)

    with pag3:
        for i in range(last_number, (3 * per_pag) - 10):
            st.write(data[i]['title'])
            st.write("Price $(ars):", data[i]['price'])
            st.write("quantity:",data[i]["available_quantity"])
            st.write("id:",data[i]['product_id'])
            st.image(data[i]['thumbnail'], width=90)
            last_number = i
            st.divider()
        st.write("max item:",last_number)
 

  