# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 12:05:20 2025

@author: Manav
"""

import pickle
import streamlit as st

# Load models
placement_model = pickle.load(open("D:\placement\placement_data.sav", 'rb'))

# Streamlit app title
st.title("Student Placement Prediction App")

st.markdown(
    """
    ### Predict whether a student will be placed or not based on their academic and personal details.
    """
)

# Input fields
gender = st.selectbox("Gender:", ["Male", "Female"])
ssc_p = st.slider("SSC Percentage (10th Grade):", min_value=0.0, max_value=100.0, value=75.0)
ssc_b = st.selectbox("SSC Board:", ["Central", "Others"])
hsc_p = st.slider("HSC Percentage (12th Grade):", min_value=0.0, max_value=100.0, value=70.0)
hsc_b = st.selectbox("HSC Board:", ["Central", "Others"])
hsc_s = st.selectbox("HSC Stream:", ["Commerce", "Science", "Arts"])
degree_p = st.slider("Degree Percentage:", min_value=0.0, max_value=100.0, value=60.0)
degree_t = st.selectbox("Degree Type:", ["Sci&Tech", "Comm&Mgmt", "Others"])
workex = st.selectbox("Work Experience:", ["Yes", "No"])
etest_p = st.slider("Employability Test Percentage:", min_value=0.0, max_value=100.0, value=50.0)
specialisation = st.selectbox("MBA Specialization:", ["Mkt&HR", "Mkt&Fin"])
mba_p = st.slider("MBA Percentage:", min_value=0.0, max_value=100.0, value=65.0)

# Adding missing columns
salary = st.number_input("Expected Salary (if any, else leave as 0):", min_value=0.0, value=0.0)
status = st.selectbox("Placement Status (For Training Only):", ["Placed", "Not Placed"])

# Encode categorical inputs to match model expectations

gender_encoded = 1 if gender == "Male" else 0
ssc_b_encoded = 1 if ssc_b == "Central" else 0
hsc_b_encoded = 1 if hsc_b == "Central" else 0
hsc_s_encoded = {"Commerce": 0, "Science": 1, "Arts": 2}[hsc_s]
degree_t_encoded = {"Sci&Tech": 0, "Comm&Mgmt": 1, "Others": 2}[degree_t]
workex_encoded = 1 if workex == "Yes" else 0
specialisation_encoded = 1 if specialisation == "Mkt&Fin" else 0
status_encoded = 1 if status == "Placed" else 0

placement_model_prediction = placement_model.predict([[
gender_encoded, ssc_p, ssc_b_encoded, hsc_p, hsc_b_encoded,
hsc_s_encoded, degree_p, degree_t_encoded, workex_encoded,
etest_p, specialisation_encoded, mba_p, salary, status_encoded
]])

# Prediction
if st.button("Predict Placement Status"):
    try:
        st.success(placement_model_prediction)
    except Exception as e:
        st.error(f"Error during prediction: {e}")

st.markdown(
    """
    *Note:* This prediction is based on historical data and may not guarantee outcomes.
    """
)