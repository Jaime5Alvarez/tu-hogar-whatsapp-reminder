from datetime import datetime

from src.config.constants import DEBUG_MODE


def is_reminder_day(date_str: str):
    target_date = datetime.now().strftime("%d/%m/%Y")
    return date_str == target_date


def get_phone_number(row: list[str]) -> str:
    return row[3].replace(" ", "")


def is_debug_mode():
    return DEBUG_MODE == "true"


def send_email(message: str):
    if not is_debug_mode():
        print(message)
