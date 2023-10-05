import urllib3
import streamlit as st
import json

http = urllib3.PoolManager()

@st.cache_data
def search_products(word:str):
    #headers = {
    #"Authorization": f"Bearer {token}"
    #}
    new_word = word.strip().replace(" ","%")
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/search?product_name={new_word}")
    return json.load(items)

def favorite_product_selection(user_id:str, item_id:str, location_id:str):
    response = http.request("POST")
    return response.json()

def mores_details():
    st.write('hello')


def create_cache(data):
    with open("front/pages/cache.json", 'w') as cache:
        json.dump(data, cache)

def read_cache():
    with open("front/pages/cache.json", 'r') as js:
        data = json.load(js)
    return data

def delete_cache():
    empty = []
    with open("front/pages/cache.json", 'w') as cache:
        json.dump(empty, cache)
