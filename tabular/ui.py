import streamlit as st
import requests

# Define UI layout
st.title('Iris data Prediction')
SL = st.number_input('sepal length')
SW = st.number_input('sepal width')
PL = st.number_input('petal length')
PW = st.number_input('petal width')


if st.button('Predict'):
    # Sending a request to our Flask API
    response = requests.post('http://localhost:5000/predict', json={
        'SL': SL,
        'SW': SW,
        'PL': PL,
        'PW': PW,
        # ... (other features)
    })
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f'Predicted value: {prediction}')
    else:
        st.error('Error in prediction')

