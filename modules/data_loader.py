import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import GOOGLE_SERVICE_ACCOUNT_FILE

def load_csv_data(file_obj):
    return pd.read_csv(file_obj)

def load_google_sheet_data(sheet_id, range_name):
    creds = service_account.Credentials.from_service_account_file(GOOGLE_SERVICE_ACCOUNT_FILE)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
    return result.get('values', [])
