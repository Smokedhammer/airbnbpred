import streamlit as st
import os
import openai
import PIL
from PIL import Image
import pandas as pd 
import streamlit.components.v1 as components
import streamlit_analytics


st.set_page_config(page_title="Airbnb Prediction", page_icon="🤖")

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




# Get user input for the question


# Prepare your question

# Use the `openai.Completion.create` function to get a response from the model


#def bug_fixer(text_input):
#  response = openai.Completion.create(
#  engine="text-davinci-003",
#  messages=[
#      {"role": "user", "content": "Tell the following in a way that is explainable to clients, dont talk technical. Based on only the following: answer the following"+data+"Tell the user the how much it matters and implications of the answer as well"+fixed}
#            
#   ]
#  
#)

logo = Image.open('logo.png')


st.sidebar.image(logo)

#st.sidebar.markdown(link, unsafe_allow_html=True)

image = Image.open('frontend.png')


st.image(image,caption='Powered by ChatGPT')

st.title("Welcome to the AirBnb Prediction Software. Click the tabs on the left to get started")

    

st.write("----------------------------------------------------------")
st.write("                                                          ")
st.write("                                                          ")


    # embed streamlit docs in a streamlit app
    
    
    