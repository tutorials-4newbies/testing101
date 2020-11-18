import datetime
import unittest

from lib import OpeningHoursHelper


# Can we do it cleaner? can we utilize Object oriented programming to get rid of this endless mocking?
class TimeProvider:
    def __init__(self):
        self.frozen_time = False

    def now(self):
        if not self.frozen_time:
            return datetime.datetime.now()

        else:
            return self.frozen_time

    def freeze_time(self, frozen_datetime: datetime.datetime):
        self.frozen_time = frozen_datetime

    def release_time(self):
        self.frozen_time = False


# This is the spec!
class OpenHoursHelperTestCase(unittest.TestCase):

    def test_opening_hours_on_sunday_morning(self):
        # Dependency injection

        time_provider = TimeProvider()
        time_provider.freeze_time(datetime.datetime(2020, 11, 15, 8, 30))
        helper = OpeningHoursHelper(time_provider)
        is_open = helper.is_it_open_now()

        self.assertTrue(is_open)

if __name__ == '__main__':
    unittest.main()
