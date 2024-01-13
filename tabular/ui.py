import streamlit as st
import requests

# Define UI layout
st.title('Diabetes Prediction')
age = st.number_input('age')
gender = st.number_input('gender')
bmi = st.number_input('BMI')
hypertension = st.number_input('hypertension')
hd = st.number_input('heart disease')
sh = st.number_input('smoking history')
hl = st.number_input('HbA1c level')
bgl = st.number_input('blood glucose level')
ip1 = st.number_input('ip1')
ip2 = st.number_input('ip2')

if st.button('Predict'):
    # Sending a request to our Flask API
    response = requests.post('http://localhost:5000/predict', json={
        'age': age,
        'gender': gender,
        'bmi': bmi,
        'hypertension': hypertension,
        'hd': hd,
        'sh': sh,
        "hl": hl,
        "bgl": bgl,
        "ip1": ip1,
        "ip2": ip2
    })
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f'Predicted value: {prediction}')
    else:
        st.error('Error in prediction')

