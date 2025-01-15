# Importing required libraries
import pandas as pd  # pandas is used for handling data frames 
import streamlit as st 

# Function to load a CSV file into a pandas DataFrame
def load_csv(uploaded_file):
    # Reads the uploaded CSV file and returns it as a DataFrame
    return pd.read_csv(uploaded_file)

# Function to enable downloading of the processed DataFrame as CSV
def download_data(df, filename):
    # Converts the DataFrame to CSV format (without including the index as the first column)
    csv = df.to_csv(index=False)
    
    # Creates a download button in the Streamlit interface to download the CSV file
    # The file will be named 'filename' and will be downloadable in CSV format
    st.download_button(label="Download CSV", data=csv, file_name=filename, mime='text/csv')

