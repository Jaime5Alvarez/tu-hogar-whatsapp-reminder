import os
import dotenv

dotenv.load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME = os.getenv("RANGE_NAME")
AUTH_FILE = os.getenv("AUTH_FILE") or ""
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
DEBUG_MODE = os.getenv("DEBUG_MODE")


for i in ["SPREADSHEET_ID", "RANGE_NAME", "AUTH_FILE", "RESEND_API_KEY", "DEBUG_MODE"]:
    if not os.getenv(i):
        raise ValueError(f"{i} is not set")
