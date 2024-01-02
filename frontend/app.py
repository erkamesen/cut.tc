import streamlit as st
import hydralit_components as hc
import requests
import json

st.set_page_config(layout="wide")
menu_data = [
        {'icon': "📊", 'label':"Dashboard"},
        {'icon': "✍️", 'label':"Register",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
        {'icon': "👨‍💻", 'label':"Login"},
        {'icon': "👋", 'label':"Logout"},
]
over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme)

custom_html = """
<div class="banner">
    <img src="https://img.freepik.com/premium-photo/wide-banner-with-many-random-square-hexagons-charcoal-dark-black-color_105589-1820.jpg" alt="Banner Image">
</div>
<style>
    .banner {
        width: 160%;
        height: 200px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""
# Display the custom HTML
st.components.v1.html(custom_html)


#get the id of the menu item clicked
st.info(f"{menu_id=}")

if menu_id == "Copy":
    st.success("oldu")
st.header("FRONTEND")




resp = requests.get("http://127.0.0.1:8000/api/base-url/")
st.json(resp.json())



with st.form("POST FORM"):
    base_url = st.text_input(":red[BASE URL]")
    code = st.text_input("CODE")
    password = st.text_input(placeholder="Password", type="password", label="Password")
    if st.form_submit_button("Submit"):
        st.success("test")
        requests.post("http://127.0.0.1:8000/api/base-url/", data={"base_url":base_url,"short_code":code})
    
