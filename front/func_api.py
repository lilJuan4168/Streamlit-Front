import urllib3
import streamlit as st
import json
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
import time

#Functions related to API requests

quicksightClient = boto3.client('quicksight',region_name='us-east-1')
sts = boto3.client('sts')

http = urllib3.PoolManager()

@st.cache_data
def search_products(word:str) -> dict:
    #headers = {
    #"Authorization": f"Bearer {token}"
    #}
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/searchFunction?product_name={word}").json()
    return items

def addFavorite(item_id:str):
    user_id = "x"
    location_id = "y"
    dic = {
        "user_id": user_id,
        "item_id": item_id,
        "location": location_id
    }
    headers = headers = {'Content-Type': 'application/json'}
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
    """headers = {
    "Authorization": f"Bearer {token}"
    }
    user = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/login/{token}", headers= headers).json()
    """
    x = {"user": token + str(datetime.now())}
    with open("front/json/user.json", "w") as usr:
        json.dump(x, usr)
    return x


def get_category_table():
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/metrics/dashboards")
    return items

def get_avgPricePerCategory():
    items = http.request("GET",url = f"https://8oh8gaouk4.execute-api.us-east-2.amazonaws.com/metrics/avgPricePerCategory")
    return items.json()