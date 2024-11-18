# AI-Agent 
The AI Agent Dashboard is a powerful tool that automates data retrieval using web searches and advanced language models. It enables users to extract specific information for entities listed in CSV files or Google Sheets. By leveraging APIs like SerpAPI for web searches and OpenAI's GPT for data extraction, the dashboard provides a seamless experience for gathering insights from the web.

Key Features

File Upload & Google Sheets Integration: Upload CSV files or connect Google Sheets to fetch data.
Dynamic Search Queries: Input custom prompts to perform web searches for each entity.
Automated Information Extraction: Use GPT-4 to extract relevant details from search results.
User-Friendly Dashboard: Intuitive interface built with Streamlit for ease of use.
Downloadable Results: Export extracted data as a CSV file.

Tech Stack

Programming Language: Python
Framework: Streamlit
APIs:
OpenAI GPT
SerpAPI
Google Sheets API
Libraries: pandas, gspread, google-auth, openai, serpapi

Setup Instructions

 1.Clone the Repository
   git clone https://github.com/yourusername/AI-Agent-Project.git
   cd AI-Agent-Project
2.Create a Virtual Environment
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install Dependencies
  pip install -r requirements.txt
4.Configure API Keys
  Create a .streamlit directory (if it doesn't exist) and add your API keys in .streamlit/secrets.toml:
  mkdir .streamlit
  nano .streamlit/secrets.toml
  Add the following content to secrets.toml:
  OPENAI_API_KEY = "your_openai_api_key"
  SERPAPI_API_KEY = "your_serpapi_api_key"
  For Google Sheets, upload your service account JSON key file, and reference it in app.py as needed.
5.Run the Application
  streamlit run app.py
  Open your browser and navigate to http://localhost:8501.

Usage Guide

1. Upload Data
Upload a CSV file or connect to a Google Sheet using the provided interface.
2. Select Column & Input Prompt
Choose the primary column containing entities (e.g., company names).
Enter a custom prompt using {entity} as a placeholder (e.g., "Find the contact email for {entity}").
3. Perform Web Search & Extract Information
Click on the "Run Search" button.
The AI Agent will use SerpAPI for web search and GPT-4 for information extraction.
4. View & Download Results
The extracted information will be displayed in a table format.
Use the "Download CSV" button to save the results.
API Configuration

1. OpenAI GPT API
Sign up at OpenAI to get your API key.

2. SerpAPI
Sign up at SerpAPI to obtain your API key.

3. Google Sheets API
Go to the Google Developers Console.
Create a new project and enable the Google Sheets API.
Create a service account and download the JSON key file.

Future Enhancements

Advanced NLP Analysis:Integrate SpaCy or NLTK for entity recognition and text summarization.

Batch Processing:Implement asynchronous processing to handle larger datasets efficiently.

Multi-Model Support:Allow users to choose between multiple LLMs (e.g., GPT-4, Claude).

Improved Error Handling:Add detailed error messages and retry mechanisms for failed API calls.

Enhanced UI/UX:Add more interactive widgets like sliders, checkboxes, and charts for better data visualization.

Authentication & User Management:Implement user authentication for personalized dashboards and data storage.

Data Caching:Use caching mechanisms like Redis to store frequent search results and reduce API costs.

Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

Steps to Contribute:
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Open a pull request.

Acknowledgments

Special thanks to OpenAI for the GPT model.
Thanks to SerpAPI for the web search capabilities.
Inspired by the need for efficient, automated data extraction in real-world applications.
