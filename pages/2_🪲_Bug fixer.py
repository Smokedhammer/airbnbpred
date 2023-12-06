import streamlit as st
import os
import openai
import PIL
from PIL import Image
import pandas as pd 
import streamlit.components.v1 as components
import streamlit_analytics


st.set_page_config(page_title="Bug Fixer", page_icon="🤖")

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


def bug_fixer(text_input):
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "user", "content": text_input+" Fix the bugs in this python code"}
            
   ]
)
  return response['choices'][0]['message']['content']


# Now we create the frontend code and all


logo = Image.open('logo.png')


st.sidebar.image(logo)

st.sidebar.markdown("# Welcome to the python AI assistant")

link = '[Support Us](https://www.buymeacoffee.com/Pocketninja)'
st.sidebar.markdown(link, unsafe_allow_html=True)

image = Image.open('frontend.png')


st.image(image,caption='Powered by ChatGPT')

st.title("Welcome to the bug fixing tool powered by the latest AI technology.")

st.subheader("Enter the python code that you have bugs with and get the correct code in response.")
    
fixed=st.text_area("CTRL + Enter to simplify. (Click anywhere on the app after typing for mobile users)")

st.write(bug_fixer(fixed))
    

st.write("----------------------------------------------------------")
st.write("                                                          ")
st.write("                                                          ")

st.subheader("Help support this free tool by giving us feedback!")


    # embed streamlit docs in a streamlit app
    
components.html("""<iframe src="https://docs.google.com/forms/d/e/1FAIpQLScuE8Vf20u03K3PKym99G45asg1UXPJkPs89-17nKMiq2JqCA/viewform?embedded=true" width="350" height="843" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>""",height=850,width=350)




    
    