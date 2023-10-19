import streamlit as st
import json
import streamlit.components.v1 as components

st.title("My Products")
st.sidebar.image("img/bocanblack.webp")

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
    components.html("""
                     
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
  {
  "symbols": [
    [
      "Apple",
      "AAPL|1D"
    ],
    [
      "Google",
      "GOOGL|1D"
    ],
    [
      "Microsoft",
      "MSFT|1D"
    ]
  ],
  "chartOnly": false,
  "width": 1000,
  "height": 500,
  "locale": "en",
  "colorTheme": "dark",
  "autosize": false,
  "showVolume": false,
  "showMA": false,
  "hideDateRanges": false,
  "hideMarketStatus": false,
  "hideSymbolLogo": false,
  "scalePosition": "right",
  "scaleMode": "Normal",
  "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
  "fontSize": "10",
  "noTimeScale": false,
  "valuesTracking": "1",
  "changeMode": "price-and-percent",
  "chartType": "area",
  "maLineColor": "#2962FF",
  "maLineWidth": 1,
  "maLength": 9,
  "lineWidth": 2,
  "lineType": 0,
  "dateRanges": [
    "1d|1",
    "1m|30",
    "3m|60",
    "12m|1D",
    "60m|1W",
    "all|1M"
  ]
}
  </script>
</div>
<!-- TradingView Widget END -->
 
""", width=600, height=600, scrolling=True)
    
if option == "My Competitors":
    #with open("front/json/user.json", 'r') as js:
    #    data = json.load(js)
    st.write("In development")
