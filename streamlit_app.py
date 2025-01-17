import streamlit as st
import pandas as pd 
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
