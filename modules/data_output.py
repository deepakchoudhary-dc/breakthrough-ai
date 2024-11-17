import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import GOOGLE_SERVICE_ACCOUNT_FILE

def save_to_csv(data, filename="output.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def update_google_sheet(sheet_id, range_name, values):
    creds = service_account.Credentials.from_service_account_file(GOOGLE_SERVICE_ACCOUNT_FILE)
    service = build('sheets', 'v4', credentials=creds)
    body = {'values': values}
    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id, range=range_name,
        valueInputOption="RAW", body=body).execute()
    return result
