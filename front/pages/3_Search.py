import streamlit as st
import urllib3
from scripts.functions import *
import json
from time import sleep


st.write("<h3>Find what you are looking for!</h3>", unsafe_allow_html=True)
item = st.text_input('', placeholder="eg: iphone 14 pro max")          
submitted = st.button('Search')
if submitted and len(item) != 0:
    data = search_products(item)
    #with open("front/pages/test2.json", 'r') as js:
    #    data = json.load(js)
    create_cache(data)
    st.success("Success")
        
#-------------
#with open("front/pages/test.json", 'r') as js:
#     data = json.load(js)
details_button_state = False
last_number = 0 
#--------------

def show_data():
    total = len(data) 
    per_pag = total // 2
    st.write("Total items:", total)

    pag1, pag2 = st.tabs(["pag1", "pag2"])

    with pag1:
        for i in range(0, per_pag):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                item_id = data[i]['product_id']
                st.write(data[i]['title'])
                st.write("Price $(ars):", data[i]['price'])
                st.write("Quantity:",data[i]["available_quantity"])
                st.write("Id:", item_id)
                st.write("Seller Nickname:", data[i]['seller_nickname'])
                st.image(data[i]['thumbnail'], width=90)
            with col2:
                fav_button = st.button("add to favorites", key= item_id, use_container_width=True)
                if fav_button:
                    pass
                        
                details_button = st.button("more details", key= item_id + str(i), use_container_width=True)
                if details_button:
                    details_button_state = True

            global last_number 
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



if submitted:
    show_data()

data = read_cache()


if len(data) != 0:
   data = read_cache()
   show_data()
   delete_cache()



















