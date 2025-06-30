import joblib
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = joblib.load('C:/Users/DELL/Desktop/ML Projects/Multiple Disease App/models/diabetes_model.sav')
heart_model = joblib.load('models/heart_disease_model.sav')
parkinson_model = joblib.load('models/parkinson_disease_model.sav')