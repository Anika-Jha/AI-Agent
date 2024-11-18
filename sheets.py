from google.oauth2 import service_account
from gspread import authorize
import pandas as pd

def connect_google_sheet(json_keyfile, sheet_url):
    credentials = service_account.Credentials.from_service_account_info(json_keyfile)
    client = authorize(credentials)
    sheet = client.open_by_url(sheet_url).sheet1
    return pd.DataFrame(sheet.get_all_records())
