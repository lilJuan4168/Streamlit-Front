import streamlit as st
from func_api import *
import json
import pandas as pd
import numpy as np
from random import randint
from datetime import datetime


#Functions related to the flow and work areas of the webapp


def read_categories():
    # Abrir json
    file = open('front/json/categories.json')
    # Devolver diccionario
    category_dict = json.load(file)
    file.close()
    return category_dict

def about_us():
    st.write("<h1 align='center'>Mercado Track Remastered 📈</h1>", unsafe_allow_html=True)
    st.divider()
    st.write("""Lorem ipsum dolor sit amet consectetur adipiscing elit egestas elementum praesent velit,
          curabitur interdum mi consequat litora tortor curae eros fringilla quisque. 
         Malesuada ornare luctus faucibus dignissim laoreet lacus hendrerit, dictumst eget magnis cum purus diam porttitor, 
         neque at posuere accumsan venenatis nascetur. Pretium duis sagittis condimentum mus dapibus venenatis, 
         penatibus sed tempus lacinia nascetur, primis congue ridiculus tristique arcu.""")
    col1, col2, col3 = st.columns([0.2,0.6,0.2])
    with col2:
       st.write("<h2>Analisis de Mercado</h2>", unsafe_allow_html=True)
       st.image('img/mlabs.png', use_column_width= True)
       st.write("<h2>Crea y Modifica Publicaciones</h2>", unsafe_allow_html=True)
       st.image('img/mertrack.webp', use_column_width=True)


def more_details(item_id, title, price, quantity, seller_nickname, img, item_word=None, avg_price="optional", historic=[], permalink = None):
    col1, col2 = st.columns([0.8, 0.2])
    dolar = dolar_price(20)
    dol = pd.DataFrame(dolar)
    hist = pd.DataFrame(historic)
    with col1:
        try:
            st.write(title)
            st.write("Price $(ars):", price)
            st.write("Id:", item_id)
            st.write("Seller Nickname:", seller_nickname)
            update_quantity = get_available_quantity(permalink)["stock"]
            st.write("Quantity:", update_quantity)
            st.image(img, width=90)
        
            dolar = dolar_price(20)
            delta = round(((dolar['blue'][0] - dolar['blue'][1])/dolar['blue'][1]) * 100)
            st.metric(label="Dolar Blue", value=str(dolar['blue'][0])+"$", delta=str(delta)+"%"+"/24hs")
            #merged = dol.merge(hist, how="outer", on="date")
            #merged['priceUSD'] = merged['price']/merged['blue']
            st.write("Historic Price")  
            st.line_chart(hist[['date', 'price']].set_index("date"), color=["#11f708"])
            st.divider()
            st.write("Historic Dolar")  
            st.line_chart(dol.set_index("date"), color=["#260be6", "#e40a0d"])
        except Exception as e:
            st.warning("Not Historic Data")
            st.write("Historic Dolar")  
            st.line_chart(dol.set_index("date"), color=["#260be6", "#e40a0d"])

    with col2:
        st.button("add to favorites", key="fav", use_container_width=True,
                    )
        back = st.button("Go to Products List", key="back",on_click=show_data, args=([item_word]), use_container_width=True)
        try:
           st.metric(label="Average Price", value=round(sum(avg_price)/25,2), delta="1%")
        except:
            pass
        
def show_data2(item):
    avg_price = []
    data = search_products(item)
    with open("front/json/search_results.json", "w") as dt:
        json.dump(data, dt, indent=4)
    st.write(data)
    #data = data_read()
    last_number = 0
    total = len(data) 
    per_pag = total // 2
    st.write("Total items:", total)
    pag1, pag2 = st.tabs(["pag1", "pag2"])
    for product in data:
        col1, col2 = st.columns([0.8, 0.2])
        if last_number < per_pag:
            with pag1:
                with col1:
                    item_id = data["product_id"]
                    title = data["title"]
                    price = data["price"]
                    quantity = data["available_quantity"]
                    seller_nickname = data["seller_nickname"]
                    img = data['thumbnail']
                    permalink = data['permalink']
                    st.write(f"<h4>{title}</h4>", unsafe_allow_html=True)
                    st.write("Price $(ars):", price)
                    st.write("Quantity:", quantity)
                    st.write("Id:", item_id)
                    st.write("Seller Nickname:", seller_nickname)
                    st.image(img, width=90)
                    avg_price.append(float(price))
                with col2:
                    st.button("Add to Favorites", key= item_id + str(randint(0,3000)), on_click=addFavorite ,args=([item_id]),use_container_width=True,
                          )
                    st.button("More Details", key= item_id + str(randint(0,250)), use_container_width=True,
                          on_click=more_details, 
                          args=(item_id, title, price, quantity, seller_nickname, img, item, avg_price)) 
                    st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)
                    if st.button("Save to a Folder", use_container_width=True):
                        with st.form("save"):
                            fname = st.text_input("New Folder Name")
                            st.form_submit_button("submit")
            last_number += 1
            st.write(last_number)    
        else:
            with pag2:
                with col1:
                    item_id = data["product_id"]
                    title = data["title"]
                    price = data["price"]
                    quantity = data["available_quantity"]
                    seller_nickname = data["seller_nickname"]
                    img = data['thumbnail']
                    permalink = data['permalink']
                    st.write(f"<h4>{title}</h4>", unsafe_allow_html=True)
                    st.write("Price $(ars):", price)
                    st.write("Quantity:", quantity)
                    st.write("Id:", item_id)
                    st.write("Seller Nickname:", seller_nickname)
                    st.image(img, width=90)
                    avg_price.append(float(price))
                with col2:
                    st.button("Add to Favorites", key= item_id + str(randint(0,3000)), on_click=addFavorite ,args=([item_id]),use_container_width=True,
                          )
                    st.button("More Details", key= item_id + str(randint(0,250)), use_container_width=True,
                          on_click=more_details, 
                          args=(item_id, title, price, quantity, seller_nickname, img, item, avg_price)) 
                    st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)
                    if st.button("Save to a Folder", use_container_width=True):
                        with st.form("save"):
                            fname = st.text_input("New Folder Name")
                            st.form_submit_button("submit")

#This function gets a word to be search and displays the results in a list
def show_data(item):
    pag1, pag2 = st.tabs(["pag1", "pag2"])
    with pag1:
        avg_price = []
        data = search_products(item, "1")
        #data = data_read()
        last_number = 0 
        st.write("Total items:", 50)
        for i in range(0, 25):
            try:
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    item_id = data[i]["product_id"]
                    title = data[i]["title"]
                    price = data[i]["price"]
                    quantity = data[i]["available_quantity"]
                    seller_nickname = data[i]["seller_nickname"]
                    img = data[i]['thumbnail']
                    permalink = data[i]['permalink']
                    historic = data[i]['history']
                    st.write(f"<h4>{title}</h4>", unsafe_allow_html=True)
                    st.write("Price $(ars):", float(price))
                    st.write("Quantity:", int(quantity))
                    st.write("Id:", item_id)
                    st.write("Seller Nickname:", seller_nickname)
                    st.image(img, width=90)
                    avg_price.append(float(price))
                with col2:
                    st.button("Add to Favorites", key= item_id, on_click=addFavorite ,args=([item_id]),use_container_width=True) 
                    st.button("More Details", key= item_id + str(i), use_container_width=True,
                             on_click=more_details, args=(item_id, title, price, quantity, seller_nickname, img, item, avg_price, historic,permalink)) 
                    st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)
                    if st.button("Save to a Folder",key= seller_nickname + str(i), use_container_width=True):
                        with st.form("save"):
                            fname = st.text_input("New Folder Name")
                            st.form_submit_button("submit")   
                last_number = i
                st.divider()
            except Exception as e:
                pass
                #st.write(str(e))
        st.write("max item:",last_number +1)
    
    with pag2:
        avg_price = []
        data = search_products(item, "2")
        #data = data_read()
        last_number = 0 
        st.write("Total items:", 50)
        for i in range(0, 25):
            try:
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    item_id = data[i]["product_id"]
                    title = data[i]["title"]
                    price = data[i]["price"]
                    quantity = data[i]["available_quantity"]
                    seller_nickname = data[i]["seller_nickname"]
                    img = data[i]['thumbnail']
                    permalink = data[i]['permalink']
                    st.write(f"<h4>{title}</h4>", unsafe_allow_html=True)
                    st.write("Price $(ars):", float(price))
                    st.write("Quantity:", int(quantity))
                    st.write("Id:", item_id)
                    st.write("Seller Nickname:", seller_nickname)
                    st.image(img, width=90)
                    avg_price.append(float(price))
                with col2:
                    st.button("Add to Favorites", key= item_id, on_click=addFavorite ,args=([item_id]),use_container_width=True) 
                    st.button("More Details", key= item_id + str(i), use_container_width=True,
                             on_click=more_details, args=(item_id, title, price, quantity, seller_nickname, img, item, avg_price, historic)) 
                    st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)
                    if st.button("Save to a Folder", key=seller_nickname + str(i),use_container_width=True):
                        with st.form("save"):
                            fname = st.text_input("New Folder Name")
                            st.form_submit_button("submit")   
                last_number = i
                st.divider()
            except Exception as e:
                st.write(str(e))
        st.write("max item:",25)


def get_categories():
    with open("front/categories.json", 'r') as js:
        data = json.load(js)
    return data
