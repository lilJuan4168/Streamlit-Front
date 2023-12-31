import streamlit as st
import json
import streamlit.components.v1 as components
from time import sleep

st.title("My Products")


option = st.selectbox("Options", ["My Inventory", "Publish a Product", "My Competitors"])
if option == "Publish a Product":
    with st.form(key="publish", clear_on_submit= True):
        st.write("Create a Post")
        title = st.text_input("Title")
        category = st.text_input("Category")
        price = st.number_input("Price", placeholder="$ars")
        condition = st.selectbox("Condition",["new", "secondHand"])
        description = st.text_input("Description")
        images = st.file_uploader("Image") 
        submit = st.form_submit_button("Submit")
    if submit:
       st.write("ok")    
if option == "My Inventory":
    st.write("Total:", "0")
    pag1, pag2, pag3 = st.tabs(["pag1", "pag2", "pag3"])
    
#with st.spinner('In Development...'):
#    sleep(12)
#    st.snow()
