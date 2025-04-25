import os
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME = os.getenv("RANGE_NAME")
AUTH_FILE = os.getenv("AUTH_FILE") or ""

for i in ["SPREADSHEET_ID", "RANGE_NAME", "AUTH_FILE"]:
    if not os.getenv(i):
        raise ValueError(f"{i} is not set")
