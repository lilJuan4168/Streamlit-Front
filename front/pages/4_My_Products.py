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

if option == "My Competitors":
    #with open("front/json/user.json", 'r') as js:
    #    data = json.load(js)
    components.html(""" 
<!DOCTYPE html>
<html>
<head>
    <title>Gráfico de TradingView</title>
    
    <!-- Agregar enlace a la biblioteca lightweight-charts -->
    <script src="ruta-a-lightweight-charts.min.js"></script>
</head>
<body>
    <div id="container" style="width: 100%; height: 500px;"></div>

    <script>
        const chartOptions = {
            layout: {
                textColor: 'black',
                background: {
                    type: 'solid',
                    color: 'white'
                }
            }
        };

        const chart = LightweightCharts.createChart(document.getElementById('container'), chartOptions);

        const areaSeries = chart.addAreaSeries({
            lineColor: '#2962FF',
            topColor: '#2962FF',
            bottomColor: 'rgba(41, 98, 255, 0.28)',
        });

        areaSeries.setData([
            { time: '2018-12-22', value: 32.51 },
            { time: '2018-12-23', value: 31.11 },
            // ... Otros datos ...
        ]);

        const candlestickSeries = chart.addCandlestickSeries({
            upColor: '#26a69a',
            downColor: '#ef5350',
            borderVisible: false,
            wickUpColor: '#26a69a',
            wickDownColor: '#ef5350',
        });

        candlestickSeries.setData([
            { time: '2018-12-22', open: 75.16, high: 82.84, low: 36.16, close: 45.72 },
            { time: '2018-12-23', open: 45.12, high: 53.90, low: 45.12, close: 48.09 },
            // ... Otros datos ...
        ]);

        chart.timeScale().fitContent();
    </script>
</body>
</html>
               
 """, width=600, height=600, scrolling=True)
