import streamlit as st


with st.form("Login"):
    st.write("<h3>Log in</h3>", unsafe_allow_html=True)
    my_token = st.text_input("Bearer Token", type="password")
    submitted = st.form_submit_button('Log in')
    
if len(my_token) != 0 and submitted:
    st.success("Log in completed", icon="✅")
    st.write("Token ended in:", my_token[-4:])
elif len(my_token) == 0 and submitted:
    st.error('Empy field', icon="🚨")