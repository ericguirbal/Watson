"""Utility functions for the unit tests."""

import datetime
import os
from io import StringIO
from unittest import mock

import py

TEST_FIXTURE_DIR = (
    py.path.local(os.path.dirname(os.path.realpath(__file__))) / "resources"
)


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
