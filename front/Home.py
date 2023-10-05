import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Mercado Track remastered",
    page_icon="Ⓜ",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "track app for mercado libre"
    }
)

#title
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
    st.image('http://mercadolabs.net/images/snaps/680-n-market-1.png', use_column_width= True)
    st.write("<h2>Crea y Modifica Publicaciones</h2>", unsafe_allow_html=True)
    st.image('http://mercadolabs.net/images/snaps/580-n-new-listing-2.png', use_column_width=True)

