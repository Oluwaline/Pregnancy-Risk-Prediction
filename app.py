import streamlit as st
import pickle
import numpy as np
import pandas as pd
import time

# Load the models
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

decision_tree_model = load_model('decision_tree_model.pkl')
random_forest_model = load_model('random_forest_model.pkl')
xgboost_model = load_model('xgboost_model.pkl')

# Risk level mapping
risk_level_mapping = {0: "low risk", 1: "mid risk", 2: "high risk"}

# Streamlit app
st.set_page_config(page_title="Pregnancy Risk Prediction", page_icon="🤰", layout="wide")

# Sidebar for model selection
st.sidebar.image("img.png", use_column_width=False, width=200)

st.sidebar.markdown("## About")
st.sidebar.info("This app predicts the risk level of pregnant women using three machine learning models: Random Forest, Decision Tree, and XGBoost.")

st.sidebar.markdown("## Contact")
st.sidebar.info("For more information, visit [GitHub](https://github.com/Oluwaline)")

# Main content
st.title("Pregnancy Risk Prediction 🤰")
st.markdown("---")


st.header("Select Model")
model_selection = st.selectbox("Choose a model", ["Decision Tree", "Random Forest", "XGBoost"])

# Input features
st.header("Input Features")

# Create columns
col1, spacer, col2 = st.columns([1, 0.5, 1])

with col1:
    age = st.number_input("**Age**", value=26, min_value=10, max_value=70, step=1)
    SystolicBP = st.slider("**Systolic Blood Pressure (mmHg):**", value=120, min_value=70, max_value=160, step=1)
    DiastolicBP = st.slider("**Diastolic Blood Pressure (mmHg):**", value=80, min_value=49, max_value=100, step=1)

with col2:
    BS = st.slider("**Blood Sugar (mmol/L):**", value=7.5, min_value=6.0, max_value=19.0, step=0.1)
    BodyTemp = st.slider("**Body Temperature (°F):**", value=98.0, min_value=98.0, max_value=103.0, step=0.1)
    HeartRate = st.slider("**Heart Rate (bpm):**", value=76, min_value=7, max_value=90, step=1)

# Predict button
if st.button("Check Status"):
    with st.spinner('Predicting...'):
        # Simulate a delay
        time.sleep(2)
        
        # Prepare input data
        input_data = pd.DataFrame({
            'Age': [age],
            'SystolicBP': [SystolicBP],
            'DiastolicBP': [DiastolicBP],
            'BS': [BS],
            'BodyTemp': [BodyTemp],
            'HeartRate': [HeartRate]
        })

        # Select the model
        if model_selection == "Decision Tree":
            model = decision_tree_model
        elif model_selection == "Random Forest":
            model = random_forest_model
        elif model_selection == "XGBoost":
            model = xgboost_model

        # Make prediction
        prediction = model.predict(input_data)
        risk_level = risk_level_mapping[prediction[0]]

        # Display the result
        st.success(f"The predicted risk level is: {risk_level}")

# Footer 
st.markdown("---") 
st.markdown("© 2024 Algorithms and Data Structure Class. All rights reserved.")
