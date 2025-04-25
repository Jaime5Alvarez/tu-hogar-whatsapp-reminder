import os
from dotenv import load_dotenv

load_dotenv()

DEBUG_MODE = os.getenv("DEBUG_MODE") == "true"
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME = os.getenv("RANGE_NAME")
AUTH_FILE = os.getenv("AUTH_FILE") or ""

for i in ["SPREADSHEET_ID", "RANGE_NAME", "AUTH_FILE", "DEBUG_MODE"]:
    if not os.getenv(i):
        raise ValueError(f"{i} is not set")
