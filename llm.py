# Importing the necessary modules
import openai
import streamlit as st
import pandas as pd
import os
api_key = os.getenv("SERPAPI_API_KEY")
# Ensure that the secrets are correctly accessed
if "OPENAI_API_KEY" not in st.secrets:
    st.error("OPENAI_API_KEY not found in secrets.")
else:
    openai.api_key = st.secrets["OPENAI_API_KEY"]

def extract_information(search_results_df):
    extracted_data = []
    for _, row in search_results_df.iterrows():
        prompt = f"Extract information for {row['Entity']} from: {row['SearchResults']}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            extracted_info = response['choices'][0]['message']['content']
            extracted_data.append({'Entity': row['Entity'], 'ExtractedInfo': extracted_info})
        except Exception as e:
            st.error(f"Error processing {row['Entity']}: {e}")
            extracted_data.append({'Entity': row['Entity'], 'ExtractedInfo': None})  # Append None or an error message

    return pd.DataFrame(extracted_data)

# Example usage
if __name__ == "__main__":
    # Example DataFrame creation for testing
    data = {
        'Entity': ['Entity1', 'Entity2'],
        'SearchResults': ['Some search results for entity 1', 'Some search results for entity 2']
    }
    search_results_df = pd.DataFrame(data)

   
    result_df = extract_information(search_results_df)
    st.write(result_df)
