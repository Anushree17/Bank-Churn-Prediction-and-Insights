import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)  


# Link external CSS
st.markdown("""
    <link rel="stylesheet" type="text/css" href="styles.css">
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown("<h1 class='stTitle'>🔮 Customer Behavior Prediction App</h1>", unsafe_allow_html=True)

st.markdown("<p class='stMarkdown'>Enter customer details below to predict outcomes based on key features.</p>", unsafe_allow_html=True)

# Container for inputs
st.markdown("<div class='container'>", unsafe_allow_html=True)


# User Inputs
gender = st.selectbox("Gender", ["Female", "Male"])
gender = 1.0 if gender == "Male" else 0.0  

num_products = st.selectbox("Number Of Products They Bought", [1, 2, 3])

is_active_member = st.selectbox("Is An Active Member?", ["No", "Yes"])
is_active_member = 1 if is_active_member == "Yes" else 0 

estimated_salary = st.number_input("Estimated Salary", min_value=0.0, max_value=1000000.0, value=50000.0)

complain = st.selectbox("Complain Registered?", ["No", "Yes"])
complain = 1 if complain == "Yes" else 0 

point_earned = st.number_input("Points Earned", min_value=100, max_value=1000, value=500)

age_group = st.selectbox("Which Age Group", ["Middle Age", "Young", "Senior"])
age_group = {"Middle Age": 0, "Young": 1, "Senior": 2}[age_group]

# Predict Button
if st.button("Predict Outcome"):
    input_data = np.array([[gender, num_products, is_active_member, estimated_salary, complain, point_earned, age_group]])
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.success("🎉 Hurray! We were able to retain the customer!")
    else:
        st.error("😢 Oh no! We lost the customer!")
