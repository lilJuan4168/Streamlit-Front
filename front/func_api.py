import urllib3
import streamlit as st
import json
from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["argon2", "des_crypt"], deprecated="auto")

#Functions related to API requests

http = urllib3.PoolManager()


def search_products(word:str, pag):
    #headers = {
    #"Authorization": f"Bearer {token}"
    #}
    user = get_user_cached()
    token = user['credentials']['access_token']
    new_word = word.replace(" ", "%20")
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/searchFunction?product_name={new_word}&access_token={token}&pag={pag}")
    return items.json()

def addFavorite(item_id:str):
    user = get_user_cached()
    dic = {
        "user_id": str(user['credentials']['user_id']),
        "token": user['credentials']['access_token'],
        "item_id": item_id,
        "location": "favorite"
    }
    headers = {'Content-Type': 'application/json'}
    response = http.request("POST", f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/search/addFavoritesToRDS", headers=headers, body=json.dumps(dic))
    return True

def data_read():
    with open("front/json/cache.json", 'r') as js:
        data = json.load(js)
    return data

def get_highlights(category):
    high = http.request("GET",f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/highlightFunction?category={category}")
    return high.json()

def get_trends(category):
    user = get_user_cached()
    token = user['credentials']['access_token']
    #token = "APP_USR-167625776650646-101913-31020790c54b89d2ed09c606ed6d2cff-241473590"
    headers = {
    "Authorization": f"Bearer {token}"
    }
    trends = http.request("GET",f"https://api.mercadolibre.com/trends/MLA/{category}",headers=headers)
    return trends.json()

def get_categories():
    categories = http.request("GET",f"https://api.mercadolibre.com/sites/MLA/categories")
    return categories.json()

def get_favorites(user_id, location):
    headers = {'Content-Type': 'application/json'}
    dic = {"user_id":user_id, "location":location}
    favorites = http.request("GET", f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/favoritesSearch",headers=headers ,body=json.dumps(dic))
    return favorites.json()

def get_my_products():
    my_products = 1
    return my_products


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

def send_registration(password, access_token, refresh_token, client_id, client_secret):
    hashed_pass = hash_password(password)
    data = {
        "password": hashed_pass,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    send = http.request("POST", url="https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/newUser", 
                        headers={'Content-Type': 'application/json'}, 
                        body=json.dumps(data, indent=4)).json()
    return send

def login(user_name, password):
    data = {
        "nickname": user_name,
        "password": password
        }
    send = http.request("POST", url="https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/login", 
                        headers={'Content-Type': 'application/json'}, 
                        body=json.dumps(data, indent=4)).json()
    with open("front/json/user.json", "w") as usr:
        json.dump(send, usr, indent=4)
    return send

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)

def mercado_track_historic(item_id):
    result = http.request("GET", f"https://mercadotrack.com/_next/data/toSzs6S9f71DST-8OKqHf/articulos/{item_id}.json")
    return result.json()


def get_user_cached():
    with open("front/json/user.json", "r") as js:
        user = json.load(js)
        return user
    
def get_password_hash(plain_pasword:str):
    return pwd_context.hash(plain_pasword)

def hash_password(password):
    # Genera una sal (puedes almacenar esto de forma segura)
    salt = "mi_sal_secreta".encode()
    # Combina la contraseña con la sal y luego hashea usando SHA-256
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    return hashed_password

def folders(user_id:str, action:str, fname:str="optional", item_id:str="optional2"):
    headers = {'Content-Type': 'application/json'}
    body = {
            "user_id": user_id,
            "action": action,
            "fname": fname,
            "item_id": item_id
        }
    cfolder = http.request("POST", f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/favorites/folder", body=json.dumps(body), headers=headers)
    return cfolder.json()

def get_available_quantity(permalink:str):
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/availableQuantity?permalink={permalink}")
    return items.json()