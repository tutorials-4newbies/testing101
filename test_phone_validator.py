import unittest

from lib import CellPhoneValidator


# This is the spec!
class PhoneValidatorTestCase(unittest.TestCase):

    def test_phone_validator_regular_number(self):
        value = "0546734469"
        expected_true_result = CellPhoneValidator(value).is_valid()
        self.assertTrue(expected_true_result)

        false_value = "aaaaa"
        expected_false_result = CellPhoneValidator(false_value).is_valid()
        self.assertFalse(expected_false_result)

    def test_cell_phone_valid_prefix(self):
        value = "0554446666"
        expected_true_result = CellPhoneValidator(value).is_valid()
        self.assertTrue(expected_true_result)

        false_value = "0114446666"
        expected_false_result = CellPhoneValidator(false_value).is_valid()
        self.assertFalse(expected_false_result)

    def test_cell_phone_prefix_without_zero(self):
        pass

    def test_cell_phone_has_legal_number_of_numbers(self):
        pass

    def test_cell_phone_number_can_contain_spaces_and_dashes(self):
        pass


if __name__ == '__main__':
    unittest.main()
