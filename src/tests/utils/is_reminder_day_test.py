from src.utils.utils import is_reminder_day


def test_is_reminder_day():
    assert is_reminder_day("25/04/2025") is True
    assert not is_reminder_day("25/04/2025")
    assert not is_reminder_day("25/04/2025")
