# -*- coding: utf-8 -*-


import streamlit as st
import os
import openai
import PIL
from PIL import Image
import pandas as pd 
import streamlit.components.v1 as components
import streamlit_analytics


st.set_page_config(page_title="PocketNinja", page_icon="🤖")

### Tracking code ###


with streamlit_analytics.track():
    st.write(" ")
    
    
########################


openai.api_key = "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"

hide_streamlit_style = """
            <style>
            
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)    


# Now we create the frontend menu code and all


logo = Image.open('logo.png')

st.sidebar.image(logo)

st.sidebar.markdown("# Welcome to the python AI assistant")


link = '[Support Us](https://www.buymeacoffee.com/Pocketninja)'
st.sidebar.markdown(link, unsafe_allow_html=True)



# Frontend Code

image = Image.open('frontend.png')

st.image(image,caption='Powered by ChatGPT')

st.title("Welcome to the python assistant toolkit powered by the latest AI technology.")

st.header("Navigate using the Menu on the left hand side to select the tool that you need!")

#maybe include a vid here
    
