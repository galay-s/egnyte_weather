import unittest
import pandas as pd

from weather import remove_asterisk, get_day

# """
# We will test just our part of code. We will not test pandas library.
# """


class TestFunctions(unittest.TestCase):

    def test_remove_asterisk_case_1(self):
        self.assertEqual(remove_asterisk('1*'), 1.0)

    def test_remove_asterisk_case_2(self):
        self.assertEqual(remove_asterisk('2.2*'), 2.2)

    def test_remove_asterisk_case_3(self):
        self.assertEqual(remove_asterisk('*3.3*'), 3.3)

    def test_get_day_case_1(self):
        df = pd.DataFrame(
            {'MxT': [9, 5, 5, 5],
             'MnT': [9, 9, 9, 9]},
            index=[1, 2, 3, 4]  # days
        )
        self.assertEqual(get_day(df), 1)

    def test_get_day_case_2(self):
        df = pd.DataFrame(
            {'MxT': [5, 5, 8, 5],
             'MnT': [9, 9, 9, 9]},
            index=[1, 2, 3, 4]  # days
        )
        self.assertEqual(get_day(df), 3)

    def test_get_day_case_3(self):
        df = pd.DataFrame(
            {'MxT': [9, 9, 9, 9],
             'MnT': [5, 9, 5, 5]},
            index=[1, 2, 3, 4]  # days
        )
        self.assertEqual(get_day(df), 2)


if __name__ == '__main__':
    unittest.main()
