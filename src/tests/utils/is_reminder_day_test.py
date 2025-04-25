import datetime
from src.utils.utils import is_reminder_day


def test_is_reminder_day():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    assert is_reminder_day(today.strftime("%d/%m/%Y")) is True
    assert not is_reminder_day("22/04/2025")

