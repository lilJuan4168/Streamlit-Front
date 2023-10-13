import streamlit as st
from func_api import get_user, send_registration
import json

st.sidebar.image("img/bocanblack.webp")


with st.form("Login"):
        st.title("Login")
        username = st.text_input("UserName")
        password = st.text_input("Password", type="password")
        submitted2 = st.form_submit_button("Login")
with st.form("Register"):
        st.title("Register")
        my_token = st.text_input("Bearer Token")
        refresh_token = st.text_input("Refresh Token")
        my_password = st.text_input("Password", type="password")
        submitted = st.form_submit_button('Register')  
if len(my_token) != 0 and submitted:
    st.success("Registration Completed", icon="✅")
    #st.write("Token ended in:", my_token[-4:])
    st.info('Remember your NICKNAME and PASSWORD to login!', icon="ℹ️")
    global user
    user = get_user(my_token)
    st.title(f"Hello! {user['first_name']} {user['last_name']}")
    st.write("Nickname:",user['nickname'])
    st.write("Email:",user['email'])
    st.write("Transactions Completed:",user['seller_reputation']['transactions']['completed'])
    st.write("Points:", user['points'])
    st.link_button("MercadoLibre Profile", user['permalink'])
    state = send_registration(user['id'], user['nickname'], 
                              user['first_name'], user['email'], 
                              my_password, my_token, 
                              refresh_token, user['phone']['number'])
    st.write(state)
elif len(my_token) == 0 and submitted:
    st.error('Empy field', icon="🚨")

elif len(my_token) != 0 and submitted2:
      pass
elif len(my_token) == 0 and submitted2:
    st.error('Empy field', icon="🚨")