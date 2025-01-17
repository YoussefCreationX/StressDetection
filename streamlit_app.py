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
with st.expander('Data visualizationj'):
   st.scatter_chart(data=df, x='EDA',y='TEMP',color='danger_level')
# Data Preparations 
with st.sidebar: 
  st.header('Input features')
  acc_x = st.slider('acc_x (m/s²)',-35,30)
