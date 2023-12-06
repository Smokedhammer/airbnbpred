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


data ="Optimization terminated successfully (Exit mode 0) Current function value: 0.14186434517999363 Iterations: 186 Function evaluations: 187 Gradient evaluations: 186 Logit Regression Results Dep. Variable: Superhost No. Observations: 40155 Model: Logit Df Residuals: 40144 Method: MLE Df Model: 10 Date: Tue, 05 Dec 2023 Pseudo R-squ.: 0.7883 Time: 15:42:28 Log-Likelihood: -5676.7 converged: True LL-Null: -26817. Covariance Type: nonrobust LLR p-value: 0.000 Coefficients: const: -1.7599 (std err: 0.209, z: -8.429, P>|z|: 0.000, [0.025-0.975]: [-2.169, -1.351]) hostResponseAverage_pastYear: 0.6660 (std err: 0.036, z: 18.681, P>|z|: 0.000, [0.025-0.975]: [0.596, 0.736]) tract_superhosts_ratio: 1.0328 (std err: 0.033, z: 31.446, P>|z|: 0.000, [0.025-0.975]: [0.968, 1.097]) prev_rating_ave_pastYear: 2.2915 (std err: 0.087, z: 26.376, P>|z|: 0.000, [0.025-0.975]: [2.121, 2.462]) superhost_change_gain_superhost: 5.4226 (std err: 0.686, z: 7.899, P>|z|: 0.000, [0.025-0.975]: [4.077, 6.768])  num_5_star_Rev_pastYear: 2.3450 (std err: 0.090, z: 26.195, P>|z|: 0.000, [0.025-0.975]: [2.170, 2.520]) rating_ave_pastYear: 1.8790 (std err: 0.089, z: 21.041, P>|z|: 0.000, [0.025-0.975]: [1.704, 2.054]) prev_numCancel_pastYear: -1.5190 (std err: 0.062, z: -24.521, P>|z|: 0.000, [0.025-0.975]: [-1.640, -1.398]) numCancel_pastYear: -1.1112 (std err: 0.060, z: -18.660, P>|z|: 0.000, [0.025-0.975]: [-1.228, -0.994]) Number of Reviews: 0.0782 (std err: 0.030, z: 2.600, P>|z|: 0.009, [0.025-0.975]: [0.019, 0.137]) prev_num_5_star_Rev_pastYear: 1.7979 (std err: 0.079, z: 22.623, P>|z|: 0.000, [0.025-0.975]: [1.642, 1.954]) Possibly complete quasi-separation: A fraction 0.23 of observations can be perfectly predicted. This might indicate that there is complete quasi-separation. In this case, some parameters will not be identified."


def bug_fixer(text_input):
  response = openai.ChatCompletion.create(
  model="text-davinci-003",
  messages=[
      {"role": "user", "content": "Tell the following in a way that is explainable to clients, dont talk technical. Based on only the following: answer the following"+data+"Tell the user the how much it matters and implications of the answer as well"+fixed}
            
   ]
)
  return response['choices'][0]['message']['content']


# Now we create the frontend code and all


logo = Image.open('logo.png')


st.sidebar.image(logo)

st.sidebar.markdown("# Welcome to the python AI assistant")

#st.sidebar.markdown(link, unsafe_allow_html=True)

image = Image.open('frontend.png')


st.image(image,caption='Powered by ChatGPT')

st.title("Welcome to the airbnb prediction tool tool powered by the latest AI technology.")


fixed=st.text_area("Enter your question")
st.write(bug_fixer(fixed))
    

st.write("----------------------------------------------------------")
st.write("                                                          ")
st.write("                                                          ")

st.subheader("Help support this free tool by giving us feedback!")


    # embed streamlit docs in a streamlit app
    
components.html("""<iframe src="https://docs.google.com/forms/d/e/1FAIpQLScuE8Vf20u03K3PKym99G45asg1UXPJkPs89-17nKMiq2JqCA/viewform?embedded=true" width="350" height="843" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>""",height=850,width=350)




    
    