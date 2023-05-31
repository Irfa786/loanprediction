import numpy as np
import pickle
import streamlit as st
import pandas as pd


# loading the saved model
loaded_model = pickle.load(open('LoanStatusApproval.pkl', 'rb'))


# creating a function for Prediction

def loan_status_prediction(loanstatus):
    loan=pd.DataFrame(loanstatus,index=[1], columns=["Gender","Married",	"Dependents",	"Education",	"Self_Employed",\
                                                     	"ApplicantIncome",	"CoapplicantIncome",	"LoanAmount",	"Loan_Amount_Term",	"Credit_History",	"Property_Area"
])
    loan.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)
    prediction = loaded_model.predict(loan)
    print(prediction)

    if (prediction[0] == 0):
      return 'Loan cannot be approved'
    else:
      return 'Loan approved'
  
    
  
def main():
    
    
    # giving a title
    st.title('Loan Status Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Gender= st.radio('Gender',('Male','Female'))
    Married = st.radio('Married',('Yes','No'))
    Dependents = st.text_input("Dependents")
    Education= st.radio('Education',('Graduate','Not a Graduate'))
    Self_Employed= st.radio('Self Employed',('Yes','No'))
    ApplicantIncome = st.text_input('Applicant Income')
    CoapplicantIncome = st.text_input('Co Applicant Income')
    LoanAmount= st.text_input('Loan Amount')
    Loan_Amount_Term= st.text_input('Loan_Amount_Term')
    Credit_History= st.text_input('Credit_History')
    Property_Area= st.radio('Property_area',('Urban','Semiurban','Rural'))
    
    
    
    # code for Prediction
    loanstatus = ''
    
    # creating a button for Prediction
    
    if st.button('Loan Status'):
        loanstatus = loan_status_prediction([[Gender,Married,int(Dependents),Education,Self_Employed,float(ApplicantIncome),float(CoapplicantIncome),float(LoanAmount),float(Loan_Amount_Term),int(Credit_History),Property_Area]])
        st.success(loanstatus)
    
        
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  
