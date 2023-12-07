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


data = '                           Logit Regression Results                           \n==============================================================================\nDep. Variable:              Superhost   No. Observations:                55808\nModel:                          Logit   Df Residuals:                    55788\nMethod:                           MLE   Df Model:                           19\nDate:                Thu, 07 Dec 2023   Pseudo R-squ.:                  0.6312\nTime:                        15:06:50   Log-Likelihood:                -13586.\nconverged:                       True   LL-Null:                       -36840.\nCovariance Type:            nonrobust   LLR p-value:                     0.000\n=====================================================================================================\n                                        coef    std err          z      P>|z|      [0.025      0.975]\n-----------------------------------------------------------------------------------------------------\nconst                                -2.3016      0.027    -86.244      0.000      -2.354      -2.249\nprev_rating_ave_pastYear              0.4386      0.038     11.536      0.000       0.364       0.513\ntract_superhosts_ratio                1.0221      0.021     48.634      0.000       0.981       1.063\nMinimum Stay                          0.1321      0.017      7.948      0.000       0.100       0.165\nnumCancel_pastYear                   -2.2497      0.042    -53.191      0.000      -2.333      -2.167\ntract_total_pop                       0.0050      0.016      0.308      0.758      -0.027       0.037\nhostResponseAverage_pastYear          0.5592      0.038     14.534      0.000       0.484       0.635\nhostResponseNumber_pastYear           0.0498      0.023      2.135      0.033       0.004       0.096\nPeriod Category                      -0.2382      0.018    -13.076      0.000      -0.274      -0.202\nprev_num_5_star_Rev_pastYear         -0.1632      0.030     -5.505      0.000      -0.221      -0.105\nrating_ave_pastYear                   2.5570      0.049     52.688      0.000       2.462       2.652\nnumReservedDays_pastYear              0.3006      0.031      9.854      0.000       0.241       0.360\nprev_Number of Reviews                0.1940      0.027      7.136      0.000       0.141       0.247\nscrapes_in_period                    -0.0577      0.029     -2.000      0.045      -0.114      -0.001\nprev_scrapes_in_period               -0.1651      0.031     -5.300      0.000      -0.226      -0.104\nprev_numCancel_pastYear               0.0041      0.031      0.131      0.896      -0.057       0.065\nnum_5_star_Rev_pastYear               2.2578      0.039     57.495      0.000       2.181       2.335\nprev_hostResponseAverage_pastYear    -0.0477      0.032     -1.498      0.134      -0.110       0.015\nNumber of Reviews                     0.0640      0.026      2.435      0.015       0.012       0.116\nprev_numReserv_pastYear              -0.0187      0.022     -0.832      0.406      -0.063       0.025\n====================================================================================================='

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

def bug_fixer(data, fixed, api_key):
    try:
        # Set the API key
        openai.api_key = api_key

        # Create the message
        prompt_message = data+ "Knowing the data, answer the following question to the user in a realistic,simple way.Use the data to support the answers " + fixed + "It is in log log model, convert it to %s in the proper way. Tell the user how much it matters and the implications of the answer as well. If the question is not relevant to context tell them its not a relevant question " 
        
        # Call the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_message,
            max_tokens=450  # Adjust this value based on how long you want the response to be
        )
        # Return the text part of the response
        return response.choices[0].text.strip()
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

st.title("This page determines whether you will maintain your superhost status.")


fixed=st.text_area("Enter your question")

if st.button('Submit'):
    st.write(bug_fixer(fixed=fixed,data=data,api_key=openai.api_key))



    

st.write("----------------------------------------------------------")
st.write("                                                          ")
st.write("                                                          ")


    # embed streamlit docs in a streamlit app
    
    
    