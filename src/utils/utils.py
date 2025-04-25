from datetime import datetime, timedelta
import os


def is_reminder_day(date_str: str):
    target_date = datetime.now() + timedelta(days=1)
    return date_str == target_date.strftime("%d/%m/%Y")


def get_phone_number(row: list[str]) -> str:
    return row[3].replace(" ", "")


def is_debug_mode():
    return os.getenv("DEBUG_MODE") == "true"
