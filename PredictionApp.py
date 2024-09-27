import streamlit as st 
import joblib
import numpy as np

st.title("Salary Prediction App")
#
st.divider()

st.write("With this Prediction Application, you can get Projections for the salaries of the company employees")

years = st.number_input("Please Enter Total Experience",value = 1 , step = 1, min_value= 0)
jobrate = st.number_input("Please Enter Job Rate",value= 3.5, step= 0.5, min_value= 0.0)

X = [years, jobrate]

model = joblib.load("linear_Salary.pkl")

st.divider()

predict= st.button("for salary prediction Press the button ")

st.divider()
if predict:
    st.balloons()
    X1 = np.array([X])
    prediction = model.predict(X1)[0]
    st.write(f"Salary Cound be {prediction:,.2f}")