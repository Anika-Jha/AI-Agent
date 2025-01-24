# Import necessary modules for authentication, Google Sheets API access, and data manipulation
from google.oauth2 import service_account  # For creating credentials using a service account JSON keyfile
from gspread import authorize  # For authorizing and accessing Google Sheets
import pandas as pd  # For working with data in a tabular format

# Define a function to connect to a Google Sheet and return its data as a Pandas DataFrame
def connect_google_sheet(json_keyfile, sheet_url):
    # Create credentials from the JSON keyfile of the service account
    credentials = service_account.Credentials.from_service_account_info(json_keyfile)
    
    # Authorize the client with the credentials to access the Google Sheets API
    client = authorize(credentials)
    
    # Open the Google Sheet using its URL and select the first worksheet (sheet1)
    sheet = client.open_by_url(sheet_url).sheet1
    
    # Retrieve all records from the worksheet and convert them into a Pandas DataFrame
    return pd.DataFrame(sheet.get_all_records())

