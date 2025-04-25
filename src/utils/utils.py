from datetime import datetime, timedelta

from src.config.constants import DEBUG_MODE


def is_reminder_day(date_str: str):
    target_date = datetime.now() + timedelta(days=1)
    return date_str == target_date.strftime("%d/%m/%Y")


def get_phone_number(row: list[str]) -> str:
    return row[3].replace(" ", "")


def is_debug_mode():
    return DEBUG_MODE == "true"


def send_email(message: str):
    if not is_debug_mode():
        print(message)
