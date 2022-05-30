
#!/usr/bin/env/ python3


import unittest
import primenumbers2
from mock import patch


class TestPrimeNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=('string', ' ',  '0', '1', '-9','50'))
    def test_input_value_error(self, value):
        self.assertEqual(primenumbers2.get_user_input(), 50)

    def test_primenumbers(self):
        self.assertEqual(primenumbers2.check_numbers(2),[2])
        self.assertEqual(primenumbers2.check_numbers(3),[2, 3])
        self.assertEqual(primenumbers2.check_numbers(19),[2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(primenumbers2.check_numbers(50),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

if __name__ == "__main__":
    unittest.main()

