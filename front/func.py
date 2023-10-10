import streamlit as st
from func_api import *
import json
import pandas as pd
import numpy as np
from random import randint
import streamlit.components.v1 as components

#Functions related to the flow and work areas of the webapp

def login():
    with st.form("Login"):
        st.write("<h3>Log in</h3>", unsafe_allow_html=True)
        #username = st.text_input("UserName")
        #password = st.text_input("Password", type="password")
        my_token = st.text_input("Bearer Token", type="password")
        submitted = st.form_submit_button('Login')
        #submitted2 = st.form_submit_button("Register")  
    if len(my_token) != 0 and submitted:
       st.success("Log in completed", icon="✅")
       st.write("Token ended in:", my_token[-4:])
       global user
       user = get_user(my_token)
    elif len(my_token) == 0 and submitted:
       st.error('Empy field', icon="🚨")


def metrics():
    st.title("Metrics")
    cat_dic_var = {"Accesorios para Vehículos": "MLA5725", "Agro": "MLA1512", "Alimentos y Bebidas": "MLA1403",
                   "Animales y Mascotas": "MLA1071", "Antigüedades y Colecciones": "MLA1367",
                   "Arte, Librería y Mercería": "MLA1368", "Autos, Motos y Otros": "MLA1743",
                   "Bebés": "MLA1384", "Belleza y Cuidado Personal": "MLA1246",
                   "Cámaras y Accesorios": "MLA1039", "Celulares y Teléfonos": "MLA1051",
                   "Computación": "MLA1648", "Consolas y Videojuegos": "MLA1144",
                   "Construcción": "MLA1500", "Deportes y Fitness": "MLA1276",
                   "Electrodomésticos y Aires Ac.": "MLA5726", "Electrónica, Audio y Video": "MLA1000",
                   "Entradas para Eventos": "MLA2547", "Herramientas": "MLA407134",
                   "Hogar, Muebles y Jardín": "MLA1574", "Industrias y Oficinas": "MLA1499",
                   "Inmuebles": "MLA1459", "Instrumentos Musicales": "MLA1182",
                   "Joyas y Relojes": "MLA3937", "Juegos y Juguetes": "MLA1132",
                   "Libros, Revistas y Comics": "MLA3025", "Música, Películas y Series": "MLA1168",
                   "Ropa y Accesorios": "MLA1430", "Salud y Equipamiento Médico": "MLA409431",
                   "Servicios": "MLA1540", "Souvenirs, Cotillón y Fiestas": "MLA9304",
                   "Otras categorías": "MLA1953"}
    
    options = st.selectbox("Categories",cat_dic_var.keys())
    col1, col2 = st.columns([0.8, 0.2])
    nuevo_dict = {v: k for k, v in cat_dic_var.items()}
    
    #with col2:
    #    st.metric(label="Dolar Blue", value="900$", delta="30%")
    #    df = pd.DataFrame( {"Productos mas buscados":["iphone 14", "rxt 3080", "muñeco de milei", "auriculares sony wh 1000 xm4"]}, index=[1,2,3,4])
    #    st.table(df)
    st.divider()
    st.write("Category in Tendency")
    data = get_category_table().json()
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("categorias")["cant_items"], use_container_width=True, color="#ffaa0088", width=800, height=600)
    
    st.divider()
    st.write("AvgPricePerCategory")
    data2 = get_avgPricePerCategory()
    df2 = pd.DataFrame(data2)
    #st.write(df2)
    #st.write(df2['categoria'].unique())
    genre = st.radio(
    "What Category?",
    df2['categoria'].unique()) 
    if genre:
        df2b = df2[df2['categoria']==genre]
        st.line_chart(df2b.set_index("fecha")["precio_promedio"], use_container_width=True, color='#00f900')

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

def my_products():
    pass


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


def more_details(item_id, title, price, quantity, seller_nickname, img, item_word):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write(title)
        st.write("Price $(ars):", price)
        st.write("Quantity:", quantity)
        st.write("Id:", item_id)
        st.write("Seller Nickname:", seller_nickname)
        st.image(img, width=90)
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.line_chart(chart_data)
    with col2:
        st.button("add to favorites", key="fav", use_container_width=True,
                    )
        back = st.button("Go to Products List", key="back",on_click=show_data, args=([item_word]), use_container_width=True)


#This function gets a word to be search and displays the results in a list
def show_data(item):
    data = search_products(item)
    #data = data_read()
    last_number = 0
    total = len(data) 
    per_pag = total // 2
    st.write("Total items:", total)
    #st.write(item)
    pag1, pag2 = st.tabs(["pag1", "pag2"])
    with pag1:
        for i in range(0, per_pag):
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
                st.write("Price $(ars):", price)
                st.write("Quantity:", quantity)
                st.write("Id:", item_id)
                st.write("Seller Nickname:", seller_nickname)
                st.image(img, width=90)
            with col2:
                st.button("Add to Favorites", key= item_id + str(randint(0,3000)), on_click=addFavorite ,args=([item_id]),use_container_width=True,
                          )
                st.button("More Details", key= item_id + str(randint(0,250)), use_container_width=True,
                          on_click=more_details, 
                          args=(item_id, title, price, quantity, seller_nickname, img, item)) 
                st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)
                st.metric(label="Average Price", value="null$", delta="1%")   
            last_number = i
            st.divider()
        st.write("max item:",last_number +1)
    with pag2:
        for i in range(last_number, total):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                item_id = data[i]['product_id']
                title = data[i]['title']
                price = data[i]['price']
                quantity = data[i]["available_quantity"]
                seller_nickname = data[i]['seller_nickname']
                img = data[i]['thumbnail']
                permalink = data[i]['permalink']
                st.write(f"<h4>{title}</h4>", unsafe_allow_html=True)
                st.write("Price $(ars):", price)
                st.write("Quantity:", quantity)
                st.write("Id:", item_id)
                st.write("Seller Nickname:", seller_nickname)
                st.image(img, width=90)
            with col2:
                st.button("Add to Favorites", key= item_id + str(randint(3500, 4000)), on_click=addFavorite,use_container_width=True)       
                st.button("More Details", key= item_id + str(randint(500,550)) + permalink, use_container_width=True,
                          on_click=more_details, 
                          args=(item_id, title, price, quantity, seller_nickname, img, item))
                st.link_button("Go to MercadoLibre", permalink, use_container_width=True)
                st.metric(label="Average Price", value="null$", delta="1%")
            last_number = i
            st.divider()
        st.write("max item:",last_number +1)


def get_categories():
    with open("front/categories.json", 'r') as js:
        data = json.load(js)
    return data