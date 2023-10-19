import streamlit as st
from func_api import send_registration, get_user_cached, login
import json

st.sidebar.image("img/bocanblack.webp")

st.title("login")
with st.expander("Your products are waiting for you..."):
    with st.form("Login"):
        username = st.text_input("UserName")
        password = st.text_input("Password", type="password")
        submitted2 = st.form_submit_button("Login")
    if username and submitted2 and password:
        try:
           login(username, password)
           user = get_user_cached()
           st.success("Login Completed User:", user['credentials']['nickname'])
        except Exception as e:
            st.warning(str(e))
    elif submitted2 and (len(username) == 0 or len(password) == 0):
        st.warning("There is an EMPTY FIELD")


st.title("Register")
with st.expander("join us for more functionality..."):
    with st.form("Register"):
        client_id =  st.text_input("Client ID")
        client_secret = st.text_input("Client Secret")
        my_token = st.text_input("Bearer Token")
        refresh_token = st.text_input("Refresh Token")
        my_password = st.text_input("Password", type="password")
        submitted = st.form_submit_button('Register')  
    if submitted and my_token and refresh_token and my_password and client_id and client_secret:
        st.success("Registration Completed, Remember your NICKNAME and PASSWORD to login!", icon="✅")
        user = send_registration(my_password, my_token, refresh_token)
        try:
           st.title(f"Hello!", user["ml_data"]["name"])
           st.write("Nickname:",user["ml_data"]['nickname'])
           st.write("Email:",user["ml_data"]["email"])
        #st.link_button("MercadoLibre Profile", user["ml_data"]['permalink'])
        except Exception as e:
            st.write("User Not Found", str(e))
    elif submitted and (len(my_token) == 0 or len(refresh_token) == 0 or len(my_password) == 0 or len(client_id) == 0 or len(client_secret) == 0):
        st.warning("There is an EMPTY FIELD")
