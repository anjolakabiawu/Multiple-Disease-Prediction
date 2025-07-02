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

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age of the Person', placeholder="e.g. 30")

    with col2:
        Sex = st.text_input('Gender of the Person', placeholder="0 for female, 1 for male")

    with col3:
        Cp = st.text_input('Type of Chest pain', placeholder="0-3")
    
    with col1:
        Trestbps = st.text_input('Resting blood pressure', placeholder="e.g. 120")
    
    with col2:
        Chol = st.text_input('Serum Cholestoral', placeholder="e.g. 200")

    with col3:
        Fbs = st.text_input('Fasting Blood Sugar', placeholder="e.g. 1.5")

    with col1:
        Restecg = st.text_input('resting electrocardiographic', placeholder="0-2")
    
    with col2:
        Thalach = st.text_input('Maximum heart rate achieved', placeholder="e.g. 130")

    with col3:
        Exang = st.text_input('exercise induced', placeholder="0 for no, 1 for yes")

    with col1:
        Oldpeak = st.text_input('ST depression induced by exercise relative to rest', placeholder="e.g. 1.5")

    with col2:
        Slope = st.text_input('the slope of the peak exercise ST segment', placeholder="0-2")

    with col3:
        Ca = st.text_input('Number of major vessels ', placeholder="0-3")

    with col1:
        Thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', placeholder="0-2")
    
    # Prediction
    heart_diagnosis = ''

    # Creating the button for the prediction
    if st.button('Heart Disease Results'):
        input_data = [[float(Age), float(Sex), float(Cp), float(Trestbps), float(Chol),
                float(Fbs), float(Restecg), float(Thalach), float(Exang),
                float(Oldpeak), float(Slope), float(Ca), float(Thal)]]
        heart_pred = heart_model.predict(input_data)

        if heart_pred[0] == 1:
            heart_diagnosis = 'The person has a heart disease'
        else:
            heart_diagnosis = 'The person does not have a heart disease'

    st.success(heart_diagnosis)


if (selected == 'Parkinsons Prediction'):

    # page title
    st.title('Parkinsons Disease Prediction')

    st.write("Please enter the following details to predict Parkinsons Disease:")

    MDVP_Fo_Hz = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_Fhi_Hz = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_Flo_Hz = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_Jitter_perc = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_Jitter_Abs = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_RAP = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_PPQ = st.text_input('Age of the Person', placeholder="e.g. 30")
    Jitter_DDP = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_Shimmer = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_Shimmer_dB = st.text_input('Age of the Person', placeholder="e.g. 30")
    Shimmer_APQ3 = st.text_input('Age of the Person', placeholder="e.g. 30")
    Shimmer_APQ5 = st.text_input('Age of the Person', placeholder="e.g. 30")
    MDVP_APQ = st.text_input('Age of the Person', placeholder="e.g. 30")
    Shimmer_DDA = st.text_input('Age of the Person', placeholder="e.g. 30")
    NHR = st.text_input('Age of the Person', placeholder="e.g. 30")
    HNR = st.text_input('Age of the Person', placeholder="e.g. 30")
    RPDE = st.text_input('Age of the Person', placeholder="e.g. 30")
    DFA = st.text_input('Age of the Person', placeholder="e.g. 30")
    spread1 = st.text_input('Age of the Person', placeholder="e.g. 30")
    spread2 = st.text_input('Age of the Person', placeholder="e.g. 30")
    D2 = st.text_input('Age of the Person', placeholder="e.g. 30")
    PPE = st.text_input('Age of the Person', placeholder="e.g. 30")