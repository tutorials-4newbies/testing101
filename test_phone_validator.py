import unittest

from lib import CellPhoneValidator


class PhoneValidatorTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_phone_validator_regular_number(self):
        value = "0546734469"
        result = CellPhoneValidator(value).is_valid()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
