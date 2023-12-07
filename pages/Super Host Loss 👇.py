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


data= """                                        Logit Regression Results                                 \n===========================================================================================\nDep. Variable:     superhost_change_lose_superhost   No. Observations:                55808\nModel:                                       Logit   Df Residuals:                    55788\nMethod:                                        MLE   Df Model:                           19\nDate:                             Thu, 07 Dec 2023   Pseudo R-squ.:                  0.1823\nTime:                                     15:08:00   Log-Likelihood:                -7918.5\nconverged:                                    True   LL-Null:                       -9684.0\nCovariance Type:                         nonrobust   LLR p-value:                     0.000\n=====================================================================================================\n                                        coef    std err          z      P>|z|      [0.025      0.975]\n-----------------------------------------------------------------------------------------------------\nconst                                -4.4170      0.063    -70.196      0.000      -4.540      -4.294\nprev_numCancel_pastYear              -2.5219      0.098    -25.609      0.000      -2.715      -2.329\nprev_numReviews_pastYear              0.9206      0.055     16.671      0.000       0.812       1.029\nprev_rating_ave_pastYear              1.1947      0.045     26.558      0.000       1.106       1.283\nhostResponseNumber_pastYear           0.1681      0.050      3.384      0.001       0.071       0.265\nsuperhost_period_all                  0.1396      0.026      5.473      0.000       0.090       0.190\nrevenue                              -0.0726      0.022     -3.375      0.001      -0.115      -0.030\nprev_hostResponseAverage_pastYear     0.1579      0.030      5.333      0.000       0.100       0.216\nnumCancel_pastYear                    0.7532      0.026     28.906      0.000       0.702       0.804\nprev_numReserv_pastYear               0.0422      0.054      0.777      0.437      -0.064       0.149\nprev_scrapes_in_period               -0.0295      0.045     -0.652      0.514      -0.118       0.059\nProperty Type_Serviced apartment      0.0270      0.021      1.283      0.199      -0.014       0.068\ntract_superhosts_ratio               -0.6263      0.039    -16.077      0.000      -0.703      -0.550\nprev_Number of Reviews                0.2072      0.036      5.688      0.000       0.136       0.279\nnumReviews_pastYear                  -0.5765      0.046    -12.400      0.000      -0.668      -0.485\nnumReserv_pastYear                   -0.0143      0.057     -0.252      0.801      -0.126       0.097\nscrapes_in_period                     0.1136      0.041      2.773      0.006       0.033       0.194\ntract_superhosts                      0.1737      0.034      5.072      0.000       0.107       0.241\nprev_hostResponseNumber_pastYear     -0.1501      0.039     -3.860      0.000      -0.226      -0.074\nrating_ave_pastYear                  -0.7674      0.034    -22.579      0.000      -0.834      -0.701\n====================================================================================================='

"""

#def bug_fixer(text_input):
#  response = openai.Completion.create(
#  engine="text-davinci-003",
#  messages=[
#      {"role": "user", "content": "Tell the following in a way that is explainable to clients, dont talk technical. Based on only the following: answer the following"+data+"Tell the user the how much it matters and implications of the answer as well"+fixed}
#            
#   ]
#  
#)

import openai

import openai

import openai

def bug_fixer(data, fixed, api_key):
    try:
        # Set the API key
        openai.api_key = api_key

        # Create the messages for the chat completion
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": data + " Knowing the data, answer the following question to the user in a realistic, simple way. Use the data to support the answers. " + fixed + " Apply this formulas to the coefficient to interpret in %s round((math.exp(coef*0.01) -1) * 100 , 3). Interpret the coefficients properly and answer the users properly. Tell the user how much it matters and the implications of the answer as well. If the question is not relevant to context, tell them it's not a relevant question."}
        ]

        # Call the OpenAI API using the chat completions endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Return the latest response in the conversation
        return response.choices[0].message['content'].strip()
    except Exception as e:
        # Handle any errors that occur during the API call
        return f"An error occurred: {str(e)}"


# Now we create the frontend code and all


logo = Image.open('logo.png')


st.sidebar.image(logo)

st.sidebar.markdown("# Welcome to the AirBnb Prediction Software")

#st.sidebar.markdown(link, unsafe_allow_html=True)

image = Image.open('frontend.png')


st.image(image,caption='Powered by ChatGPT')

st.title("This page determines whether you will lose your status.")


fixed=st.text_area("Enter your question")

if st.button('Submit'):
    st.write(bug_fixer(fixed=fixed,data=data,api_key=openai.api_key))



    

st.write("----------------------------------------------------------")
st.write("                                                          ")
st.write("                                                          ")


    # embed streamlit docs in a streamlit app
    
    
    