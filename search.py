from serpapi import search


import pandas as pd
import streamlit as st

def search_entity(df, column, prompt_template):
    api_key = st.secrets["SERPAPI_API_KEY"]
    results = []
    for entity in df[column]:
        prompt = prompt_template.replace("{entity}", entity)
        search = GoogleSearch({"q": prompt, "api_key": api_key})
        search_results = search.get_dict().get("organic_results", [])
        results.append({'Entity': entity, 'SearchResults': search_results})
    return pd.DataFrame(results)
