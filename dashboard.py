
import streamlit as st
import pandas as pd

st.title('Intelligent Weather Forecasting Dashboard')
uploaded=st.file_uploader('Upload Weather CSV')

if uploaded:
    df=pd.read_csv(uploaded)
    st.dataframe(df.head())
    st.line_chart(df.select_dtypes(include='number'))
