from src.utils.utils import get_phone_number, is_debug_mode
from unittest import mock
import os

import datetime
from src.utils.utils import is_reminder_day


def test_is_debug_mode():
    with mock.patch.dict(os.environ, {"DEBUG_MODE": "false"}):
        assert is_debug_mode() is False

    with mock.patch.dict(os.environ, {"DEBUG_MODE": "true"}):
        assert is_debug_mode() is True


def test_is_reminder_day():
    today = datetime.datetime.now() + datetime.timedelta(days=1)
    assert is_reminder_day(today.strftime("%d/%m/%Y")) is True
    assert not is_reminder_day("22/04/2025")


def test_get_phone_number():
    assert (
        get_phone_number(["25/04/2025", "9:00", "John Doe", "1234567890"])
        == "1234567890"
    )
    assert (
        get_phone_number(["25/04/2025", "9:00", "John Doe", "123456 7890"])
        == "1234567890"
    )
    assert (
        not get_phone_number(["25/04/2025", "9:00", "John Doe", "1234567890"])
        == "3333333333"
    )
