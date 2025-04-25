from src.utils.utils import is_debug_mode
from unittest import mock
import os

def test_is_debug_mode():
    with mock.patch.dict(os.environ, {"DEBUG_MODE": "false"}):
        assert is_debug_mode() is False

    with mock.patch.dict(os.environ, {"DEBUG_MODE": "true"}):
        assert is_debug_mode() is True


