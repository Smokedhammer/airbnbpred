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


 
data =  """
OLS Regression Results
Dep. Variable: Rating Overall   R-squared: 0.631
Model: OLS   Adj. R-squared: 0.631
Method: Least Squares   F-statistic: 1052.
Date: Thu, 07 Dec 2023   Prob (F-statistic): 0.00
Time: 20:17:35   Log-Likelihood: -1.3228e+05
No. Observations: 53540   AIC: 2.647e+05
Df Residuals: 53452   BIC: 2.655e+05
Df Model: 87
Covariance Type: nonrobust

coef std err t P>|t| [0.025 0.975]
prev_scrapes_in_period -0.0056 0.001 -6.903 0.000 -0.007 -0.004
superhost_change_gain_superhost -0.1307 0.048 -2.752 0.006 -0.224 -0.038
rating_ave_pastYear 6.2724 0.244 25.722 0.000 5.794 6.750
numReviews_pastYear -0.0222 0.004 -5.594 0.000 -0.030 -0.014
numCancel_pastYear -0.0929 0.034 -2.722 0.006 -0.160 -0.026
num_5_star_Rev_pastYear 0.0318 0.005 6.297 0.000 0.022 0.042
prop_5_StarReviews_pastYear -4.0972 0.352 -11.626 0.000 -4.788 -3.406
prev_rating_ave_pastYear -2.2333 0.271 -8.244 0.000 -2.764 -1.702
prev_numReviews_pastYear 0.0133 0.004 3.095 0.002 0.005 0.022
prev_numCancel_pastYear 0.0773 0.038 2.023 0.043 0.002 0.152
prev_num_5_star_Rev_pastYear -0.0202 0.005 -3.700 0.000 -0.031 -0.010
prev_prop_5_StarReviews_pastYear 3.3929 0.379 8.945 0.000 2.649 4.136
numReservedDays_pastYear 0.0007 0.000 2.669 0.008 0.000 0.001
numReserv_pastYear -0.0025 0.001 -2.678 0.007 -0.004 -0.001
prev_numReservedDays_pastYear -0.0007 0.000 -2.354 0.019 -0.001 -0.000
prev_numReserv_pastYear 0.0025 0.001 2.331 0.020 0.000 0.005
hostResponseAverage_pastYear 0.0083 0.003 3.298 0.001 0.003 0.013
available_days_aveListedPrice 0.0008 0.000 2.802 0.005 0.000 0.001
booked_days 0.0077 0.001 6.101 0.000 0.005 0.010
prev_available_days -0.0012 0.000 -5.348 0.000 -0.002 -0.001
Max Guests -0.0419 0.007 -5.764 0.000 -0.056 -0.028
Minimum Stay 0.0039 0.002 2.495 0.013 0.001 0.007
Number of Photos 0.0100 0.001 7.461 0.000 0.007 0.013
Longitude -2.2132 0.664 -3.331 0.001 -3.515 -0.911
Pets Allowed -0.1447 0.035 -4.148 0.000 -0.213 -0.076
Instantbook Enabled -0.0959 0.035 -2.719 0.007 -0.165 -0.027
prev_Instantbook Enabled -0.1051 0.037 -2.865 0.004 -0.177 -0.033
Number of Reviews -0.0064 0.001 -4.794 0.000 -0.009 -0.004
prev_Number of Reviews 0.0070 0.001 4.872 0.000 0.004 0.010
prev_Rating Overall 0.7337 0.004 181.736 0.000 0.726 0.742
occupancy_rate -0.3934 0.152 -2.582 0.010 -0.692 -0.095
census_tract -1.165e-08 3.43e-09 -3.399 0.001 -1.84e-08 -4.93e-09
tract_asian_perc -0.0065 0.003 -2.375 0.018 -0.012 -0.001
zip_hispanic_or_latino_anyrace_percent 0.1021 0.023 4.421 0.000 0.057 0.147
zip_white_nothispanic_percent 0.1048 0.024 4.441 0.000 0.059 0.151
zip_black_nothispanic_percent 0.1047 0.024 4.447 0.000 0.059 0.151
zip_asian_nothispanic_percent 0.0974 0.024 3.990 0.000 0.050 0.145
tract_unique_prices 0.0065 0.002 2.796 0.005 0.002 0.011
prev_available_days_aveListedPrice_tractQuartile 0.0494 0.014 3.538 0.000 0.022 0.077
tract_superhosts -0.0114 0.004 -2.840 0.005 -0.019 -0.004
tract_superhosts_ratio 0.3115 0.095 3.279 0.001 0.125 0.498
revenue_period_city -8.911e-09 2.57e-09 -3.463 0.001 -1.4e-08 -3.87e-09
booked_days_period_tract -0.0002 9.74e-05 -2.164 0.030 -0.000 -1.98e-05
revenue_period_tract 1.688e-06 5.16e-07 3.269 0.001 6.76e-07 2.7e-06
time_to_date_mean 0.0018 0.001 2.915 0.004 0.001 0.003
prev_time_to_date_mean 0.0013 0.001 2.204 0.028 0.000 0.003
Period Category 0.0152 0.003 4.461 0.000 0.009 0.022
Property Type_Cabin -3.1844 1.439 -2.213 0.027 -6.005 -0.364
Property Type_Condominium 0.1010 0.036 2.787 0.005 0.030 0.172
Property Type_Dorm 3.0060 1.282 2.344 0.019 0.492 5.520
Property Type_Entire Floor -12.5861 2.867 -4.390 0.000 -18.205 -6.967
Property Type_Entire apartment -0.2126 0.108 -1.976 0.048 -0.424 -0.002
Property Type_Entire place 2.7349 1.282 2.133 0.033 0.221 5.248
Property Type_Other -2.6113 0.443 -5.889 0.000 -3.480 -1.742
Property Type_Place 1.7710 0.828 2.138 0.033 0.147 3.395
Property Type_Private room -1.2680 0.438 -2.894 0.004 -2.127 -0.409
Property Type_Private room in house -0.5952 0.255 -2.337 0.019 -1.094 -0.096
Property Type_Room in aparthotel -1.5136 0.590 -2.567 0.010 -2.669 -0.358
Property Type_Shared room 1.6484 0.813 2.026 0.043 0.054 3.243
Zipcode_60604 -2.1415 0.609 -3.517 0.000 -3.335 -0.948
Zipcode_60606 0.8290 0.338 2.451 0.014 0.166 1.492
Zipcode_60610 -0.4619 0.080 -5.806 0.000 -0.618 -0.306
Zipcode_60612 -0.2968 0.088 -3.374 0.001 -0.469 -0.124
Zipcode_60613 0.2182 0.066 3.329 0.001 0.090 0.347
Zipcode_60621 0.7853 0.234 3.358 0.001 0.327 1.244
Zipcode_60624 -0.9539 0.196 -4.865 0.000 -1.338 -0.570
Zipcode_60625 0.2622 0.087 3.027 0.002 0.092 0.432
Zipcode_60634 -0.3960 0.161 -2.457 0.014 -0.712 -0.080
Zipcode_60637 -0.2498 0.103 -2.421 0.015 -0.452 -0.048
Zipcode_60641 -0.2683 0.117 -2.296 0.022 -0.497 -0.039
Zipcode_60644 -1.2176 0.229 -5.325 0.000 -1.666 -0.769
Zipcode_60649 -0.6727 0.160 -4.208 0.000 -0.986 -0.359
Zipcode_60654 0.2763 0.118 2.342 0.019 0.045 0.507
Neighborhood_Armour Square 5.7884 1.659 3.489 0.000 2.537 9.040
Neighborhood_Back of the Yards -1.6226 0.249 -6.526 0.000 -2.110 -1.135
Neighborhood_Belmont Cragin -0.8433 0.212 -3.985 0.000 -1.258 -0.428
Neighborhood_Calumet Heights 1.0896 0.438 2.485 0.013 0.230 1.949
Neighborhood_Chatham -2.3621 0.471 -5.018 0.000 -3.285 -1.439
Neighborhood_Edgewater 0.2211 0.073 3.028 0.002 0.078 0.364
Neighborhood_Englewood -1.1960 0.269 -4.451 0.000 -1.723 -0.669
Neighborhood_Irving Park 0.3437 0.086 4.000 0.000 0.175 0.512
Neighborhood_Lincoln Park -0.1789 0.069 -2.605 0.009 -0.313 -0.044
Neighborhood_Little Village -0.7302 0.147 -4.978 0.000 -1.018 -0.443
Neighborhood_McKinley Park -0.5034 0.216 -2.335 0.020 -0.926 -0.081
Neighborhood_Pilsen -0.1836 0.090 -2.032 0.042 -0.361 -0.007
Neighborhood_River North -12.1884 1.657 -7.357 0.000 -15.435 -8.941
Neighborhood_Roseland -1.5062 0.591 -2.549 0.011 -2.664 -0.348
Neighborhood_West Ridge 0.3384 0.142 2.385 0.017 0.060 0.616

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

def bug_fixer(data, fixed, api_key):
    try:
        # Set the API key
        openai.api_key = api_key

        # Create the message
        prompt_message = data+ "Knowing the data, answer the following question to the user in a realistic,simple way.Use the data to support the answers " + fixed + "Tell the user how much it matters and the implications of the answer as well. If the question is not relevant to context tell them its not a relevant question " 
        
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

st.title("This page determines how you can increase your rating.")


fixed=st.text_area(" Enter your question")

if st.button('Submit'):
    st.write(bug_fixer(fixed=fixed,data=data,api_key=openai.api_key))



    

st.write("----------------------------------------------------------")
st.write("                                                          ")
st.write("                                                          ")


    # embed streamlit docs in a streamlit app
    
    
    