import urllib3
import streamlit as st
import json

#Functions related to API requests

http = urllib3.PoolManager()


def search_products(word:str):
    #headers = {
    #"Authorization": f"Bearer {token}"
    #}
    new_word = word.replace(" ", "%20")
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/searchFunction?product_name={new_word}").json()
    #with open("front/json/cache.json", "w") as js:
    #    json.dump(items, js, indent=4)
    return items

def addFavorite(item_id:str):
    user_id = "x"
    location_id = "y"
    dic = {
        "user_id": user_id,
        "item_id": item_id,
        "location": location_id
    }
    headers = {'Content-Type': 'application/json'}
    response = http.request("POST", "", headers=headers, body=json.dumps(dic))
    return True

def data_read():
    with open("front/json/cache.json", 'r') as js:
        data = json.load(js)
    return data

def get_highlights():
    high = http.request("GET","")
    return high

def get_favorites():
    favorites = http.request("GET", "")

def get_my_products():
    my_products = 1
    return my_products


def get_user(token):
    headers = {
    "Authorization": f"Bearer {token}"
    }
    user = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/login/{token}", headers=headers).json()
    
    x = {"token": token,
         }
    with open("front/json/user.json", "w") as usr:
        json.dump(user, usr, indent=4)
    return user

@st.cache_data
def get_category_table():
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/metrics/dashboards")
    return items.json()

@st.cache_data
def get_avgPricePerCategory():
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/metrics/avgPricePerCategory")
    return items.json()

def dolar_price(days:str = 0):
    dolar = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/metrics/dolarPrice/{days}")
    return dolar.json()

def send_registration(user_id, nickname, name, email, password, access_token, refresh_token, contact):
    data = {
        "user_id": str(user_id),
        "nickname": nickname,
        "name":name,
        "email":email,
        "password": password,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "contact":contact
    }

    send = http.request("POST", url="https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/newUser", 
                        headers={'Content-Type': 'application/json'}, 
                        body=json.dumps(data, indent=4))
    return send