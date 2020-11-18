import unittest

from lib import OpeningHoursHelper
from freezegun import freeze_time


# This is the spec!
class OpenHoursHelperTestCase(unittest.TestCase):

    @freeze_time("2020-11-15T08:30")
    def test_opening_hours_on_sunday_morning(self):
        helper = OpeningHoursHelper()
        is_open = helper.is_it_open_now()

        self.assertTrue(is_open)

# add the following tests
# test it's closed before 8 on sunday
# test it's closed after 16 on sunday
# test it's closed every hour in non workdays
# test tuesday behavior

if __name__ == '__main__':
    unittest.main()
