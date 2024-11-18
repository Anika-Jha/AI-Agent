import pandas as pd
import streamlit as st

def load_csv(uploaded_file):
    return pd.read_csv(uploaded_file)

def download_data(df, filename):
    csv = df.to_csv(index=False)
    st.download_button(label="Download CSV", data=csv, file_name=filename, mime='text/csv')
