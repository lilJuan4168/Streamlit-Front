import streamlit as st
import json
from func_api import get_favorites, get_user_cached, folders, addFavorite
from func import more_details
from random import randint

st.title("My Saved")
user = get_user_cached()
if st.button("Create Folder"):
    with st.form("folder"):
        fname = st.text_input("Folder Name")
        fdesc = st.text_area("Description")
        st.form_submit_button("Create Folder", on_click=folders, args=(user['credentials']['user_id'], fname, "create"))

if st.button("Delete Folder"):
    folders = folders(user_id=user['credentials']['user_id'], action="list")
    st.write("will continue")
    
with st.expander("My Favorites"):
    user = get_user_cached()
    data = get_favorites(user['credentials']['user_id'], "favorite")
    avg_price = []
    last_number = 0
    total = len(data) 
    per_pag = total // 2
    st.write("Total items:", total)
    pag1, pag2 = st.tabs(["pag1", "pag2"])
    with pag1:
        for i in range(0, total):
            try:
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    #item_id = data[i]['body']["product_id"]
                    title = data[i]['body']["title"]
                    price = data[i]['body']["price"]
                    #quantity = data[i]['body']["available_quantity"]
                    #seller_nickname = data[i]['body']["seller_nickname"]
                    img = data[i]['body']['thumbnail']
                    permalink = data[i]['body']['permalink']
                    st.write(f"<h4>{title}</h4>", unsafe_allow_html=True)
                    st.write("Price $(ars):", float(price))
                    #st.write("Quantity:", int(quantity))
                    #st.write("Id:", item_id)
                    #st.write("Seller Nickname:", seller_nickname)
                    st.image(img, width=90)
                    avg_price.append(float(price))
                with col2:
                    #st.button("Add to Favorites", key= item_id + str(randint(0,3000)), on_click=addFavorite ,args=([item_id]),use_container_width=True) 
                    #st.button("More Details", key= item_id + str(randint(0,250)), use_container_width=True,
                    #         on_click=more_details, args=(item_id, title, price, quantity, seller_nickname, img, "", avg_price)) 
                    st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)   
                last_number = i
                st.divider()
            except Exception as e:
                st.write(str(e))
        st.write("max item:",last_number +1)
           
   

x = st.button("cache")
if x:
    with open("front/json/user.json", "r") as js:
        data = json.load(js)
    st.write(data)