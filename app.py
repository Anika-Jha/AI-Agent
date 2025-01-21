#main
#import necessary libraries
import streamlit as st
import pandas as pd
from search import search_entity
from llm import extract_information
from sheets import connect_google_sheet
from utils import load_csv, download_data
import os
api_key = os.getenv("SERPAPI_API_KEY")
st.title("AI Agent Dashboard")

# File upload options
uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
json_keyfile = st.file_uploader("Upload Google Sheets JSON Key", type=['json'])
sheet_url = st.text_input("Enter Google Sheet URL")

# Load data
df = load_csv(uploaded_file) if uploaded_file else None
if json_keyfile and sheet_url:
    df = connect_google_sheet(json_keyfile, sheet_url)

if df is not None:
    st.write("Data Preview:")
    st.dataframe(df)

    column = st.selectbox("Select the Primary Column", df.columns)
    prompt_template = st.text_input("Enter your search prompt (use {entity} as a placeholder)")

    if st.button("Run Search"):
        search_results_df = search_entity(df, column, prompt_template)
        extracted_info_df = extract_information(search_results_df, prompt_template)
        st.dataframe(extracted_info_df)

        # Download option
        download_data(extracted_info_df, "extracted_info.csv")
else:
    st.warning("Please upload a CSV file or connect a Google Sheet.")
