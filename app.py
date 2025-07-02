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
                            icons = ['activity', 'heart', 'person'],
                            default_index = 0)
    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction')

    st.write("Please enter the following details to predict Diabetes:")

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder="e.g. 2")

    with col2:
        Glucose = st.text_input('Glucose level', placeholder="e.g. 120")

    with col3:
        BloodPressure = st.text_input('Blood Pressure value', placeholder="e.g. 70")

    with col1:
        SkinThickness = st.text_input('Skin Thickness value', placeholder="e.g. 20")
    
    with col2:
        Insulin = st.text_input('Insulin Level', placeholder="e.g. 80")
    
    with col3:
        BMI = st.text_input('BMI value', placeholder="e.g. 25.3")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value', placeholder="e.g. 0.5")
    
    with col2:
        Age = st.text_input('Age of the Person', placeholder="e.g. 30")

    # Prediction
    diab_diagnosis = ''

    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diagnosis = diabetes_model.predict(input_data)

        if (diagnosis[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'
    
    st.success(diab_diagnosis)


if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction')

    st.write("Please enter the following details to predict Heart Disease:")

    Age = st.text_input('Age of the Person', placeholder="e.g. 30")
    Sex = st.text_input('Gender of the Person', placeholder="0 for female, 1 for male")
    Cp = st.text_input('Type of Chest pain', placeholder="e.g. 30")
    Trestbps = st.text_input('Resting blood pressure', placeholder="e.g. 30")
    Chol = st.text_input('Serum Cholestoral', placeholder="e.g. 30")
    Fbs = st.text_input('Fasting Blood Sugar', placeholder="e.g. 30")
    Restecg = st.text_input('resting electrocardiographic', placeholder="e.g. 30")
    Thalach = st.text_input('Age of the Person', placeholder="e.g. 30")
    Exang = st.text_input('exercise induced', placeholder="0 for no, 1 for yes")
    Oldpeak = st.text_input('ST depression induced by exercise relative to rest', placeholder="e.g. 30")
    Slope = st.text_input('the slope of the peak exercise ST segment', placeholder="e.g. 30")
    Ca = st.text_input('Age of the Person', placeholder="e.g. 30")
    Thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', placeholder="e.g. 30")


if (selected == 'Parkinsons Prediction'):

    # page title
    st.title('Parkinsons Disease Prediction')