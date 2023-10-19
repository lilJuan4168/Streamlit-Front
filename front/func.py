import streamlit as st
from func_api import *
import json
import pandas as pd
import numpy as np
from random import randint
from datetime import datetime


#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Functions related to the flow and work areas of the webapp

def favorites():
    #st.write("in development")
    #st.snow()
    sidebar = st.sidebar
# Crear una carpeta en el panel lateral
    folder_name = sidebar.text_input("Nombre de la carpeta:")
# Verificar si se ha ingresado un nombre de carpeta
    if folder_name:
    # Agregar elementos a la carpeta
       item_name = st.text_input("Nombre del elemento:")
       if item_name:
          sidebar.markdown(f"- {folder_name}/{item_name}")


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


def more_details(item_id, title, price, quantity, seller_nickname, img, item_word, avg_price):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write(title)
        st.write("Price $(ars):", price)
        st.write("Quantity:", quantity)
        st.write("Id:", item_id)
        st.write("Seller Nickname:", seller_nickname)
        st.image(img, width=90)
        
        dolar = dolar_price(20)
        delta = round(((dolar['blue'][0] - dolar['blue'][1])/dolar['blue'][1]) * 100)
        st.metric(label="Dolar Blue", value=str(dolar['blue'][0])+"$", delta=str(delta)+"%"+"/24hs")
        data = pd.DataFrame(dolar)
        #st.write(data)  
        st.line_chart(data.set_index("fechas"))

    with col2:
        st.button("add to favorites", key="fav", use_container_width=True,
                    )
        back = st.button("Go to Products List", key="back",on_click=show_data, args=([item_word]), use_container_width=True)
        st.metric(label="Average Price", value=round(sum(avg_price)/25,2), delta="1%")

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


#This function gets a word to be search and displays the results in a list
def show_data(item):
    avg_price = []
    data = search_products(item)
    #data = data_read()
    last_number = 0
    total = len(data) 
    per_pag = total // 2
    st.write("Total items:", total)
    pag1, pag2 = st.tabs(["pag1", "pag2"])
    with pag1:
        for i in range(0, per_pag):
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
                    st.button("Add to Favorites", key= item_id + str(randint(0,3000)), on_click=addFavorite ,args=([item_id]),use_container_width=True) 
                    st.button("More Details", key= item_id + str(randint(0,250)), use_container_width=True,
                             on_click=more_details, args=(item_id, title, price, quantity, seller_nickname, img, item, avg_price)) 
                    st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)   
                last_number = i
                st.divider()
            except Exception as e:
                st.write(str(e))
        st.write("max item:",last_number +1)
    
    with pag2:
        for i in range(per_pag, total):
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
                    st.button("Add to Favorites", key= item_id + str(randint(0,3000)), on_click=addFavorite ,args=([item_id]),use_container_width=True) 
                    st.button("More Details", key= item_id + str(randint(0,250)), use_container_width=True,
                             on_click=more_details, args=(item_id, title, price, quantity, seller_nickname, img, item, avg_price)) 
                    st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)   
                last_number = i
                st.divider()
            except Exception as e:
                st.write(str(e))
        st.write("max item:",last_number +1)


def get_categories():
    with open("front/categories.json", 'r') as js:
        data = json.load(js)
    return data
