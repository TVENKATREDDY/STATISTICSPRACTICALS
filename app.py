import streamlit as st
import pickle
import numpy as np

model=pickle.load(open(r'C:\Users\91807\VSCodeProjects\linear_regression_model.pkl','rb'))

#Set title
st.title("Salary Prediction App")

#Add a Brief Description
st.write("This App predicts the salary based on the years of experience of employee")

#Add input widget to user to enter years of experience
years_experience=st.number_input("Enter Years of Experience:",min_value=0.0,max_value=50.0,value=15.0,step=0.5)

#hen the button clicked
if st.button("Predict Salary"):
    expereince_input=np.array([[years_experience]])
    prediction=model.predict(expereince_input)
    
    #Display Result
    st.success(f"The Predicted Salary for {years_experience} years of experience is: ${prediction[0]:,.2f}")
    
    #Display info about the result
    
st.write("the model is trained with using dataset of salaries and years of experience. built by Vemkat Reddy")