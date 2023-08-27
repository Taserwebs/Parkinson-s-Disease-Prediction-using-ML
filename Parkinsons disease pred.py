# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:28:09 2023

@author: abish
"""

import streamlit as st
from streamlit_option_menu import option_menu

# set page config
st.set_page_config(page_title="Parkinson's Disease Prediction App", page_icon=":clipboard:", layout="wide", initial_sidebar_state="expanded", menu_items={"Get Help": "https://www.streamlit.io/"}, )

# rest of the code
import pickle
import pandas as pd

#loading the saved model
parkinsons_model = pickle.load(open('D:/desktop/Parkinsons disease prediction/saved model/parkinsons_model.sav','rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu('Minor Project -IV',
                           ['Home','Parkinsons Disease Prediction'],
                           icons = ['house','person'],
                           default_index= 0)


# Home Page
if selected == 'Home':
    st.title('Welcome to Parkinsons Disease Prediction App')
    st.write('This app predicts whether a person has Parkinsons Disease or not based on their health attributes')

# Parkinson's Prediction Page
elif selected == 'Parkinsons Disease Prediction':

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    # file upload
    st.header('Upload CSV file')
    file = st.file_uploader('Choose a CSV file', type='csv')
    if file is not None:
        df = pd.read_csv(file)

        # show uploaded data
        st.write('**Data uploaded:**')
        st.write(df)

        # select row
        st.header('Select a row to predict result')
        row_index = st.selectbox('Row', df.index)

        # code for prediction
        st.header('Prediction Result')
        if st.button("Predict"):
            parkinsons_prediction = parkinsons_model.predict([[
                df.at[row_index, 'MDVP:Fo(Hz)'],
                df.at[row_index, 'MDVP:Fhi(Hz)'],
                df.at[row_index, 'MDVP:Flo(Hz)'],
                df.at[row_index, 'MDVP:Jitter(%)'],
                df.at[row_index, 'MDVP:Jitter(Abs)'],
                df.at[row_index, 'MDVP:RAP'],
                df.at[row_index, 'MDVP:PPQ'],
                df.at[row_index, 'Jitter:DDP'],
                df.at[row_index, 'MDVP:Shimmer'],
                df.at[row_index, 'MDVP:Shimmer(dB)'],
                df.at[row_index, 'Shimmer:APQ3'],
                df.at[row_index, 'Shimmer:APQ5'],
                df.at[row_index, 'MDVP:APQ'],
                df.at[row_index, 'Shimmer:DDA'],
                df.at[row_index, 'NHR'],
                df.at[row_index, 'HNR'],
                df.at[row_index, 'RPDE'],
                df.at[row_index, 'DFA'],
                df.at[row_index, 'spread1'],
                df.at[row_index, 'spread2'],
                df.at[row_index, 'D2'],
                df.at[row_index, 'PPE']
            ]])

            # show predicted result
            if parkinsons_prediction[0] == 1:
                st.write(f"The person in row {row_index } has Parkinson's disease", font_size=20)
            else:
                st.write(f"The person in row {row_index } does not have Parkinson's disease", font_size=20)
    else:
        st.write('Please upload a CSV file to see prediction results')