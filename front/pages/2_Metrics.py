import streamlit as st
from func_api import get_category_table, get_avgPricePerCategory, dolar_price, get_highlights, get_trends
from func import read_categories
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.image("img/bocanblack.webp")

st.title("Metrics")
    
#options = st.selectbox("Categories",cat_dic_var.keys())
tab1, tab2, tab3 = st.tabs(["Website Metrics", "MercadoLibre Metrics", "External Metrics"])
#nuevo_dict = {v: k for k, v in cat_dic_var.items()}
    
with tab3:

    dolar = dolar_price(20)
    delta = round(((dolar['blue'][0] - dolar['blue'][1])/dolar['blue'][1]) * 100)
    st.metric(label="Dolar Blue", value=str(dolar['blue'][0])+"$", delta=str(delta)+"%"+"/24hs")
    
    data = pd.DataFrame(dolar)
    #st.write(data)  
    st.line_chart(data.set_index("date"))


    mostSearched = pd.DataFrame( {"Productos mas buscados":["iphone 14", "rxt 3080", "muñeco de milei", "auriculares sony wh 1000 xm4"]}, index=[1,2,3,4])
    st.table(mostSearched)
    st.divider()

with tab1:
    st.write("Category in Tendency")
    data = get_category_table()
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("categorias")["cant_items"], use_container_width=True, color="#ffaa0088", width=600, height=600)
    
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

with tab2:
    categories = read_categories()
    
    selected = st.selectbox("Seleccione una categoría", list(categories.keys()))

    # Define el número de tarjetas por fila
    
    # Definir CSS personalizado
    css_code = f"""
    <style>
        .card-container {{
            display: flex;
            background-color: #F3EFEF;
            border-radius: 10px;
            padding: 10px;
            margin: 10px;
        }}
        .card-image {{
            width: 100px;
            height: auto;
            margin-right: 10px;
        }}
        .card-details {{
            flex-grow: 1;
            padding: 10px;
        }}
        .price {{
            font-size: 18px;
        }}
    </style>
    """
    if st.button("Consultar más vendidos"):
        data = get_highlights(categories[selected])
        st.markdown(css_code, unsafe_allow_html=True)

        # Iterar sobre los datos y crear las tarjetas horizontales
        for i, item in enumerate(data):
            st.write("----")

            col1 = st.columns(2)
            with col1[0]:
                try:
                    st.image(item['thumbnails'][0], width=100)
                except KeyError:
                    st.image(item['thumbnail'], width=100)
            with col1[1]:
                try:
                    st.subheader(item['name'])
                except KeyError:
                    st.subheader(item['title'])
                
                st.write(f"${item.get('price', 'Precio no disponible')}", key=f"price_{i}", class_="price")
                
                if 'condition' in item:
                    if item['condition'] == 'new':
                        st.write("Nuevo")

                st.link_button("Go to MercadoLibre",item['permalink'],use_container_width=True)
    
    if st.button("Consultar tendencias en búsqueda"):
        #Que más crecieron en la semana
        category_trends = get_trends(categories[selected])
        for category in category_trends:
            try:
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    keyword = category['keyword']
                    url = category['url']
                    st.write(f"<h4>{keyword}</h4>", unsafe_allow_html=True)                    
                with col2:
                    st.link_button("Buscar en MercadoLibre",url,use_container_width=True)   
                st.divider()
            except Exception as e:
                st.write(str(e)) 
        #st.write(category_trends)