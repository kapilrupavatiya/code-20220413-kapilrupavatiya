import unittest

from utility import *

class TestUser(unittest.TestCase):
    def test_bmi_calculator(self):
        # TODO write test cases to test end to end bmi calculator
        # Create json file for input
        # check output file corrsponding to input file
        # check summery file also
        pass

    def test_calculate_bmi_utility_method(self):
        """
        """
        height = 1.71
        weight = 96
        actual_bmi = calculate_bmi(height, weight)
        expected_bmi = round(96/1.71, 2)
        self.assertEqual(actual_bmi, expected_bmi)


    # TODO we can add proper test case for each and every utility method same as test_calculate_bmi_utility_method



if __name__ == '__main__':
    unittest.main()