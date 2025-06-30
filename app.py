import joblib
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = joblib.load('C:/Users/DELL/Desktop/ML Projects/Multiple Disease App/models/diabetes_model.sav')
heart_model = joblib.load('models/heart_disease_model.sav')
parkinson_model = joblib.load('models/parkinson_disease_model.sav')

# Sideba for navigation

with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                            default_index = 0)
    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')


if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')


if (selected == 'Parkinsons Prediction'):

    # page title
    st.title('Parkinsons Disease Prediction using ML')