"""Utility functions for the unit tests."""

import datetime
from io import StringIO
from pathlib import PurePath
from unittest import mock

TEST_FIXTURE_DIR = PurePath(__file__).parent / "resources"


def mock_datetime(dt, dt_module):
    class DateTimeMeta(type):
        @classmethod
        def __instancecheck__(cls, obj):
            return isinstance(obj, datetime.datetime)

    class BaseMockedDateTime(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return dt.replace(tzinfo=tz)

        @classmethod
        def utcnow(cls):
            return dt

        @classmethod
        def today(cls):
            return dt

    mocked_datetime = DateTimeMeta("datetime", (BaseMockedDateTime,), {})

    return mock.patch.object(dt_module, "datetime", mocked_datetime)


def mock_read(content):
    return lambda self, name: self._read(StringIO(content), name)
