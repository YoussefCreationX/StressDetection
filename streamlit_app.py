import streamlit as st
import pandas as pd 
import joblib
import numpy as np 
st.title('Stress Detection APP')
st.info('This is a stress detection app based on physiological data and machine learning model')

with st.expander('Physiological dataset used from a smartwatch'):
  st.write('**Raw data**')
  df = pd.read_csv('LeftDataSetA2Fin.csv')
  df

  st.write('**X**')
  X = df.drop('danger_level',axis=1)
  X 

  st.write('**y**')
  y = df.danger_level
  y
with st.expander('Data visualization'):
   st.scatter_chart(data=df, x='EDA',y='TEMP',color='danger_level')
# Data Preparations 
# ACC_x,ACC_y,ACC_z,BVP,EDA,TEMP,HR,IBI_intervals,danger_level
with st.sidebar: 
  st.header('Input features')
  acc_x = st.slider('acc_x (m/s²)',-60,60)
  acc_y = st.slider('acc_y (m/s²)',-60,60)
  acc_z = st.slider('acc_z (m/s²)',-60,60)
  BVP = st.slider('BVP ()',0,10)
  EDA = st.slider('EDA (mS)',0,1)
  TEMP = st.slider('TEMP (c°)',15,40)
  HR = st.slider('HR ()',70,120)
  IBI_intervals = st.slider('IBI_intervals ()',0,1)
  # Machine learning training 
  # Upload the model 
  model = joblib.load('tree.joblib')
  data = {"features":[acc_x,acc_y,acc_z,BVP,EDA,TEMP,HR,IBI_intervals]}
def predict(data:dict):
# Extract feature values from the input dictionary
  features = list(data.values())
        
# Convert the input data to a 2D NumPy array
  features = np.array(features).reshape(1, -1)
        
# Make a prediction
  prediction = model.predict(features)
        
# Interpret the prediction
  if prediction[0] == 1:
      message = "You are Safe"
  elif prediction[0] == 0:
      message = "You are stressed but with a lower rate!"
  else:
      message = "You are under high danger! If you need help, tell me!"
 # Return the result as a dictionary
  return {'Danger type is': message}
  
# Display predicted species 
st.subheader('Predicted Species')
prediction = predict(data)
st.success(prediction.values())
prediction
   
  


