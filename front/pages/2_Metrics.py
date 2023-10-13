import streamlit as st
from func_api import get_category_table, get_avgPricePerCategory, dolar_price
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
    st.line_chart(data.set_index("fechas"))


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
    st.write("In development")
    st.snow()

