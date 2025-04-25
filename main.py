from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os
from src.config.constants import AUTH_FILE, RANGE_NAME, SPREADSHEET_ID
from src.utils.utils import get_phone_number, is_reminder_day, send_email

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), AUTH_FILE)


def main():
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"Error: The file {CREDENTIALS_FILE} does not exist.")
        return send_email(f"Error: The file {CREDENTIALS_FILE} does not exist.")

    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        )
        # number_of_rows = len(result.get("values", []))
        # headers = result.get("values", [])[0]
        rows = result.get("values", [])[1:]

        for row in rows:
            if is_reminder_day(row[0]):
                phone_number = get_phone_number(row)
                print(phone_number)

    except Exception as err:
        print(f"Error trying to get data from the sheet: {err}")
        return send_email(f"Error trying to get data from the sheet: {err}")


if __name__ == "__main__":
    main()
