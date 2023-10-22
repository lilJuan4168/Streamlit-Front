import streamlit as st
import json
from func_api import get_favorites, get_user_cached, folders, addFavorite
from func import more_details
from random import randint
from time import sleep


st.title("My Saved")
user = get_user_cached()
user_id = user['credentials']['user_id']

with st.form("Create a Folder"):
    fname = st.text_input("Folder Name")
    send = st.form_submit_button("Create Folder")
if send:
    x = folders(user_id=user_id, action="create", fname=fname, item_id="none")
    msg = x['message']
    if msg:
       st.toast(x)
       st.success("Completed")
    else:
        st.warning(f"Error: {msg}")

myfolders = folders(user_id=user['credentials']['user_id'], action="list")
with st.expander("Delete a Folder", expanded=True):
    options = st.multiselect("Select", options=[x for x in myfolders['message'] if x != "favorite"])
    if st.button("Delete Selected"):
        for item in options:
            folders(user_id, "delete", item)
            st.toast(f"{item} Deleted...")
        st.success("Completed")
        sleep(2)
        st.rerun()

st.divider()

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
                    item_id = data[i]['body']["id"]
                    title = data[i]['body']["title"]
                    price = data[i]['body']["price"]
                    quantity = data[i]['body']["available_quantity"]
                    #seller_nickname = data[i]['body']["seller_nickname"]
                    seller_id = data[i]['body']["seller_id"]
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
                    st.button("More Details", key= item_id, use_container_width=True,
                             on_click=more_details, args=(item_id, title, price, quantity, seller_id, img))
                    st.link_button("Go to MercadoLibre",permalink ,use_container_width=True)
                    st.button("Delete from Favorites", key= item_id + str(i), on_click=folders ,args=(user['credentials']['user_id'],"delete_item","favorite", item_id),use_container_width=True)   
                last_number = i
                st.divider()
            except Exception as e:
                st.write(str(e))
        st.write("max item:",last_number +1)
           
for folderName in myfolders['message']:
    if folderName != "favorite":
        with st.expander(folderName):
            try:
                user = get_user_cached()
                data = get_favorites(user['credentials']['user_id'], folderName)
                st.write(data)
            except Exception as e:
               st.warning(str(e))   

#x = st.button("cache")
#if x:
#    with open("front/json/user.json", "r") as js:
#        data = json.load(js)
#    st.write(data)