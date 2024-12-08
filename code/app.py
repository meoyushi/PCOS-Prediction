import streamlit as st
import numpy as np
import joblib

# Load the trained model
# Replace 'pcos_model.pkl' with your actual model file
model = joblib.load("path/to/PCOS_LogisReg.pkl")


st.title("PCOS Prediction App")
st.markdown("### Enter patient details to predict the likelihood of PCOS:")

# Input Fields
age = st.number_input("Age (years)", min_value=0, step=1)
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, step=0.1, format="%.1f")
cycle_length = st.number_input("Cycle Length (days)", min_value=0, step=1)
follicle_count = st.number_input("Follicle Count", min_value=0, step=1)
amh = st.number_input("AMH (Anti-Müllerian Hormone) Level (ng/mL)", min_value=0.0, step=0.1, format="%.2f")
testosterone = st.number_input("Testosterone Level (ng/dL)", min_value=0.0, step=0.1, format="%.2f")
insulin = st.number_input("Fasting Insulin (µIU/mL)", min_value=0.0, step=0.1, format="%.2f")
glucose = st.number_input("Fasting Glucose Level (mg/dL)", min_value=0.0, step=0.1, format="%.2f")
irregular_cycles = st.radio("Irregular Menstrual Cycles?", options=["Yes", "No"])
hirsutism = st.radio("Hirsutism (Excess Hair Growth)?", options=["Yes", "No"])
acne = st.radio("Acne?", options=["Yes", "No"])
obesity = st.radio("Obesity?", options=["Yes", "No"])

# Map categorical inputs to numerical values (if needed)
irregular_cycles = 1 if irregular_cycles == "Yes" else 0
hirsutism = 1 if hirsutism == "Yes" else 0
acne = 1 if acne == "Yes" else 0
obesity = 1 if obesity == "Yes" else 0

# Create an input array for prediction
input_data = np.array([
    age, bmi, cycle_length, follicle_count, amh, testosterone, insulin, glucose,
    irregular_cycles, hirsutism, acne, obesity
]).reshape(1, -1)

# Prediction button
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)[0]
        result = "Positive for PCOS" if prediction == 1 else "Negative for PCOS"
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
