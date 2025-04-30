# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 18:52:45 2025

@author: HONNAPPA M S
"""
import pickle
import streamlit as st
import numpy as np

 # load the saved model

load_model=pickle.load(open('C:/Users/HONNAPPA M S/Desktop/Wine Quality Prediction/wine_trained_data2.sav','rb'))

 # create function for prediction
def prediction_function(input):
     
     # chaning the input_data  to numpy array
     input_data_asarray=np.asarray(input)

    # reshape the array as we are predictive for one instance
     input_data_reshape=input_data_asarray.reshape(1,-1)

     predict=load_model.predict(input_data_reshape)
     print(predict)

     if predict[0]==0:
         return 'Good Quality Wine'
     else:
         return 'Bad Quality Wine'

def main():
     
     # creating title
     st.title('Wine Quality Prediction Using ML')
     
 
     
     #getting the input from user
     
     col1,col2=st.columns(2)
     with col1:
         
         fixed_acidity=st.text_input('Enter the Fixed Acidity Value')
     with col2:
         
         volatile_acidity=st.text_input('Enter the Volatile Acitidy Value')
         
     with col1:
         citric_acid=st.text_input('Enter the Citic Acid Value')
     with col2:
         residual_sugar=st.text_input('Enter the Residual Sugar Value' )
     with col1:
         chlorides=st.text_input('Enter the Chlorides Values')
     with col2:
         free_sulfur_dioxide=st.text_input('Enter the Free Sulfur Dioxide Value')
     with col1:
         total_sulfur_dioxide=st.text_input('Enter the Total Sulfur Dioxide Value')
     with col2:
         density=st.text_input('Enter the Density Value')
     with col1:
         pH=st.text_input('Enter the PH Value')
     with col2:
         sulphates=st.text_input('Enter the Sulphate Value')
     with col1:
         alcohol=st.text_input('Enter the Alcohol Value' )
         
     
     # code for prediction
     diagnosis=''
     
     # create the button for prediction
     if st.button('Wine Quality Result'):
         diagnosis=prediction_function([fixed_acidity, volatile_acidity, citric_acid, residual_sugar,chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                                       pH, sulphates, alcohol])
     st.success(diagnosis)
if __name__=='__main__':
     main()

